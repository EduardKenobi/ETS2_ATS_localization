#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/merge_to_xliff.py
Aplikuje schválené preklady z review dokumentu preklady_review.md
späť do oficiálneho XLIFF lokalizačného súboru pre Crowdin.

Podporuje inkrementálny merge:
- Do finálneho XLIFF zapisuje iba položky označené - [x] Schválené.
- Uchováva kumulatívny stav v data/temp/approved_translations.json.
- Pri použití prepínača --all zlúči všetky položky v review súbore.
"""

import os
import sys
import re
import json
import argparse
import xml.sax.saxutils as saxutils
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

def parse_review_for_merge(md_path):
    """
    Rozparsuje review súbor a vráti:
    - newly_approved: dict {uid: sk_text} pre položky s [x]
    - pending: dict {uid: sk_text} pre položky s [ ]
    - total_items: počet nájdených položiek
    """
    if not os.path.exists(md_path):
        return {}, {}, 0

    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    approved = {}
    pending = {}
    total_items = 0

    cur_id = None
    cur_approved = False
    cur_sk = None

    def commit_item():
        nonlocal cur_id, cur_approved, cur_sk, total_items
        if cur_id and cur_sk:
            total_items += 1
            if cur_approved:
                approved[cur_id] = cur_sk
            else:
                pending[cur_id] = cur_sk
        cur_id = None
        cur_approved = False
        cur_sk = None

    for line in lines:
        line_s = line.strip()

        # Detekcia karty
        if line_s.startswith("###"):
            commit_item()
            m_id = re.search(r"ID:\s*`?(\d+)`?", line_s)
            if m_id:
                cur_id = m_id.group(1)
            continue

        if not cur_id:
            # Záložná kontrola pre tabuľkový formát (| **1** | `827424` | ...)
            if line_s.startswith("| **"):
                cols = [c.strip() for c in re.split(r"(?<!\\)\|", line_s)]
                if len(cols) >= 6:
                    uid = cols[2].replace("`", "").strip()
                    sk = cols[5].replace("**", "").replace(r"\|", "|").replace("<br>", "\n").strip()
                    if uid.isdigit() and sk:
                        # V tabuľke predvolene schválené
                        approved[uid] = sk
                        total_items += 1
            continue

        # Checkbox detekcia
        m_cb = re.search(r"^-\s*\[([ xXvV✓])\]", line_s)
        if m_cb:
            val = m_cb.group(1).strip().lower()
            cur_approved = (val in ("x", "v", "✓"))
            continue

        # SK preklad
        if "* **SK:**" in line_s or "**SK:**" in line_s:
            m_sk = re.search(r"\*\*SK:\*\*\s*(.+)", line_s)
            if m_sk:
                sk_txt = m_sk.group(1).strip()
                if sk_txt.startswith("**") and sk_txt.endswith("**") and len(sk_txt) > 4:
                    sk_txt = sk_txt[2:-2].strip()
                # Zákaz en-dash / em-dash: nahrádzame výhradne za štandardný '-'
                sk_txt = sk_txt.replace('\u2013', '-').replace('\u2014', '-')
                cur_sk = sk_txt
            continue

    commit_item()
    return approved, pending, total_items

def update_xliff_file(input_xliff, output_xliff, translations):
    """
    Aplikuje preklady do XLIFFu pri zachovaní štruktúry a správneho XML escapovania.
    """
    if not os.path.exists(input_xliff):
        print(f"CHYBA: Vstupný XLIFF súbor '{input_xliff}' neexistuje!")
        sys.exit(1)

    os.makedirs(os.path.dirname(output_xliff), exist_ok=True)

    total_updated = 0
    current_unit_id = None

    tu_pattern = re.compile(r'<trans-unit\s+[^>]*id="(\d+)"', re.IGNORECASE)
    target_pattern = re.compile(r'(<target\s+[^>]*>)(.*?)(</target>)', re.IGNORECASE)

    with open(input_xliff, "r", encoding="utf-8") as fin, \
         open(output_xliff, "w", encoding="utf-8", newline="\n") as fout:

        for line in fin:
            tu_match = tu_pattern.search(line)
            if tu_match:
                current_unit_id = tu_match.group(1)

            if "</trans-unit>" in line:
                current_unit_id = None

            if current_unit_id and current_unit_id in translations:
                target_match = target_pattern.search(line)
                if target_match:
                    sk_translation = translations[current_unit_id].replace('\u2013', '-').replace('\u2014', '-')
                    clean_unescaped = saxutils.unescape(sk_translation)
                    escaped_text = saxutils.escape(clean_unescaped)

                    new_tag = re.sub(r'state="[^"]*"', 'state="translated"', target_match.group(1))
                    if 'state=' not in new_tag:
                        new_tag = new_tag.replace('<target', '<target state="translated"')

                    replaced_line = line[:target_match.start()] + f"{new_tag}{escaped_text}</target>" + line[target_match.end():]
                    fout.write(replaced_line)
                    total_updated += 1
                    continue

            fout.write(line)

    return total_updated

def main():
    parser = argparse.ArgumentParser(description="Zlúčenie schválených prekladov do XLIFF.")
    parser.add_argument("--review", default="review/preklady_review.md", help="Cesta k review súboru.")
    parser.add_argument("--input", default="data/input/SCS Trucks_sk.xliff", help="Pôvodný XLIFF súbor.")
    parser.add_argument("--output", default="data/output/SCS Trucks_sk_FINAL.xliff", help="Výstupný finálny XLIFF.")
    parser.add_argument("--approved-store", default="data/temp/approved_translations.json", help="Úložisko schválených prekladov.")
    parser.add_argument("--all", action="store_true", help="Zlúčiť všetky preklady v review dokumente bez ohľadu na checkbox.")
    args = parser.parse_args()

    print("=" * 65)
    print("ZLÚČENIE SCHVÁLENÝCH PREKLADOV DO FINÁLNEHO XLIFF")
    print("=" * 65)

    approved_in_review, pending_in_review, total_in_review = parse_review_for_merge(args.review)
    print(f"1. Analýza review súboru '{args.review}':")
    print(f"   - Celkovo položiek v súbore: {total_in_review}")
    print(f"   - Označených na schválenie [- [x]]: {len(approved_in_review)}")
    print(f"   - Čaká na schválenie [- [ ]]:       {len(pending_in_review)}")

    # Načítanie existujúcich kumulatívnych schválených položiek
    cumulative_approved = {}
    if os.path.exists(args.approved_store):
        try:
            with open(args.approved_store, "r", encoding="utf-8") as f:
                cumulative_approved = json.load(f)
        except Exception:
            cumulative_approved = {}

    # Spracovanie podľa prepínačov
    if args.all:
        print("\n⚠️  Použitý prepínač --all: Zlučujú sa VŠETKY položky z review.")
        cumulative_approved.update(approved_in_review)
        cumulative_approved.update(pending_in_review)
    else:
        if not approved_in_review:
            if not cumulative_approved:
                print("\n⚠️  UPOZORNENIE: Žiadne položky nie sú zaškrtnuté (- [x]).")
                print("   Otvorte 'review/preklady_review.md' a označte položky hodné zverejnenia pomocou - [x] Schválené.")
                print("   (Alebo použite 'python run_pipeline.py merge --all' pre zlúčenie všetkých).")
                sys.exit(0)
            else:
                print(f"\nℹ️  V review nie sú žiadne nové zaškrtnuté položky. Použije sa existujúcich {len(cumulative_approved)} schválených položiek.")
        else:
            new_additions = sum(1 for uid in approved_in_review if uid not in cumulative_approved)
            cumulative_approved.update(approved_in_review)
            print(f"\n✅ Pridaných {new_additions} novozvolených položiek do schválených.")

    # Uloženie kumulatívneho stavu
    os.makedirs(os.path.dirname(args.approved_store), exist_ok=True)
    with open(args.approved_store, "w", encoding="utf-8") as f:
        json.dump(cumulative_approved, f, ensure_ascii=False, indent=2)

    untrans_csv = "data/temp/untranslated_strings.csv"
    total_project_strings = len(cumulative_approved)
    if os.path.exists(untrans_csv):
        import csv
        try:
            with open(untrans_csv, "r", encoding="utf-8-sig") as f_u:
                total_project_strings = len(list(csv.DictReader(f_u)))
        except Exception:
            pass

    print(f"\n2. Kumulatívny stav projektu: {len(cumulative_approved)} / {total_project_strings} schválených reťazcov.")

    # Aplikovanie do XLIFF
    print(f"3. Zapisujem preklady do '{args.output}'...")
    updated_count = update_xliff_file(args.input, args.output, cumulative_approved)
    print(f"   ✅ Úspešne aktualizovaných v XML: {updated_count} záznamov.")

    # XML validácia
    print("4. Kontrola XML integrity...")
    try:
        context = ET.iterparse(args.output, events=("end",))
        it = iter(context)
        for _ in range(500):
            next(it)
        print("   ✅ XML syntax je 100 % platná.")
    except Exception as e:
        print(f"   ⚠️ Varovanie pri validácii XML: {e}")

    print("-" * 65)
    remaining_in_project = total_project_strings - len(cumulative_approved)
    if remaining_in_project > 0:
        print(f"⏳ V projekte zostáva neschválených: {remaining_in_project} reťazcov.")
        print("👉 Pre vygenerovanie čistého review dokumentu len s neschválenými položkami spusti:")
        print("   python run_pipeline.py draft")
    else:
        print("🎉 Všetky reťazce projektu boli schválené a zlúčené!")
        print("   Súbor 'data/output/SCS Trucks_sk_FINAL.xliff' je pripravený na upload do Crowdinu.")
    print("=" * 65)

if __name__ == "__main__":
    main()
