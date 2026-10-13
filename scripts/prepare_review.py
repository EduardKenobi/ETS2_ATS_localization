#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/prepare_review.py
Generuje štruktúrovaný review dokument (Markdown) pre ETS2/ATS lokalizáciu.
Podporuje interaktívne checkboxy (- [ ] / - [x]) pre postupné (inkrementálne)
schvaľovanie a zlúčenie prekladov.
"""

import os
import sys
import csv
import json
import re
import argparse

sys.stdout.reconfigure(encoding='utf-8')

def clean_context_desc(raw_ctx):
    if not raw_ctx:
        return ""
    c = raw_ctx
    if c.startswith("[Key:"):
        c = c.split("]", 1)[1].strip() if "]" in c else c
    return c.replace("\n", " ").strip()

def parse_existing_review_md(md_path):
    """
    Rozparsuje existujúci review súbor a vráti stav kariet:
    - schválenie (- [x] vs - [ ])
    - upravený slovenský text (ak bol používateľom modifikovaný)
    - vlastné poznámky a komentáre používateľa
    """
    if not os.path.exists(md_path):
        return {}

    cards = {}
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cur_id = None
    cur_approved = False
    cur_sk = None
    cur_notes = []

    def commit_card():
        nonlocal cur_id, cur_approved, cur_sk, cur_notes
        if cur_id:
            cards[cur_id] = {
                "approved": cur_approved,
                "sk": cur_sk,
                "notes": cur_notes
            }
        cur_id = None
        cur_approved = False
        cur_sk = None
        cur_notes = []

    for line in lines:
        line_s = line.strip()

        # Detekcia novej karty
        if line_s.startswith("###"):
            commit_card()
            m_id = re.search(r"ID:\s*`?(\d+)`?", line_s)
            if m_id:
                cur_id = m_id.group(1)
            continue

        if not cur_id:
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
                cur_sk = sk_txt
            continue

        # Poznámky používateľa (riadky začínajúce '>' alebo komentáre mimo štandardných polí)
        if line_s.startswith(">") or line_s.startswith("* *Poznámka:*") or line_s.startswith("* *Komentár:*"):
            cur_notes.append(line_s)
        elif line_s.startswith("* ") and not any(line_s.startswith(p) for p in ["* **EN:**", "* **SK:**", "* *Kontext:*", "* 💡"]):
            cur_notes.append(line_s)

    commit_card()
    return cards

CHAPTER_DEFINITIONS = [
    "1. ETS2: Coach Mode (Autobusy – Zákazky, Hlásenia a Zručnosti)",
    "2. ETS2: Vyhliadky a Pamätihodnosti (Island)",
    "3. ETS2: Príslušenstvo, Diely, Prevodovky a Laky",
    "4. ATS: Vozidlá, Výbava a Nastavenia (RAM 1500)",
    "5. ATS: Pamätihodnosti a Vyhliadky (Viewpoints & POIs)",
]

def get_item_chapter(it):
    f = it.get('file', '')
    ctx = it.get('group_or_context', '')
    key = ctx.split(']')[0].replace('[Key: ', '').strip() if '[Key:' in ctx else ''
    
    if 'ats' in f:
        if any(w in ctx for w in ['TBs and POIs', 'Viewpoints', 'landmark', 'poi_']) or key.startswith('poi_') or key.startswith('la_cut_'):
            return "5. ATS: Pamätihodnosti a Vyhliadky (Viewpoints & POIs)"
        else:
            return "4. ATS: Vozidlá, Výbava a Nastavenia (RAM 1500)"
    else:
        # ETS2
        if any(w in ctx for w in ['cutscenes', 'landmarks', 'is_cut_', 'landmark_']) or key.startswith('is_cut_') or key.startswith('landmark_'):
            return "2. ETS2: Vyhliadky a Pamätihodnosti (Island)"
        elif any(w in ctx for w in ['Bus skills', 'Multiplayer', 'Bus quick job', 'bus_job', 'coach_job', 'satisfaction', 'tight_schedule', 'low_acceleration', 'equipment_provided_bus', 'equipment_owned_bus', 'mp_job_wrong_bus']):
            return "1. ETS2: Coach Mode (Autobusy – Zákazky, Hlásenia a Zručnosti)"
        else:
            return "3. ETS2: Príslušenstvo, Diely, Prevodovky a Laky"

def generate_review_file(untranslated_csv, translations_json, approved_json, output_md, include_all=False, reset=False):
    if not os.path.exists(untranslated_csv):
        print(f"CHYBA: Súbor {untranslated_csv} neexistuje! Najprv spusti extrakciu.")
        sys.exit(1)

    with open(untranslated_csv, "r", encoding="utf-8-sig") as f:
        items = list(csv.DictReader(f))

    total_count = len(items)

    sk_dict = {}
    if os.path.exists(translations_json):
        with open(translations_json, "r", encoding="utf-8") as f:
            sk_dict = json.load(f)

    # Načítanie už schválených a zlúčených položiek z JSON úložiska
    approved_store = {}
    if os.path.exists(approved_json) and not reset:
        with open(approved_json, "r", encoding="utf-8") as f:
            approved_store = json.load(f)

    # Ak existuje predchádzajúci review súbor, zachováme úpravy a komentáre
    existing_cards = parse_existing_review_md(output_md)

    # Dynamické zistenie aktívnych kapitol
    all_chapters = []
    for c in CHAPTER_DEFINITIONS:
        if any(get_item_chapter(it) == c for it in items):
            all_chapters.append(c)
    for it in items:
        ch = get_item_chapter(it)
        if ch not in all_chapters:
            all_chapters.append(ch)

    # Rozdelenie položiek na aktívne na review a už schválené
    active_items = []
    already_approved_items = []

    for idx, it in enumerate(items):
        item_no = idx + 1
        uid = it.get("id", "")
        
        is_merged = (uid in approved_store) and not reset
        
        if is_merged and not include_all:
            already_approved_items.append((item_no, it, approved_store[uid]))
        else:
            # Určenie SK prekladu (priorita: používateľská úprava v MD -> draft JSON -> prázdne)
            if uid in existing_cards and existing_cards[uid]["sk"]:
                sk_val = existing_cards[uid]["sk"]
            elif is_merged:
                sk_val = approved_store[uid]
            else:
                sk_val = sk_dict.get(uid, "")
            
            # Striktný zákaz en-dash/em-dash: nahrádzame výhradne za '-'
            sk_val = (sk_val or "").replace('\u2013', '-').replace('\u2014', '-')

            # Určenie stavu checkboxu
            if reset:
                is_checked = False
            elif is_merged:
                is_checked = True
            elif uid in existing_cards:
                is_checked = existing_cards[uid]["approved"]
            else:
                is_checked = False

            user_notes = existing_cards.get(uid, {}).get("notes", [])

            active_items.append({
                "item_no": item_no,
                "item": it,
                "sk": sk_val,
                "approved": is_checked,
                "chapter": get_item_chapter(it),
                "notes": user_notes
            })

    total_approved_cumulative = len(approved_store)
    active_count = len(active_items)

    md = []
    md.append("# 📋 Návrh lokalizácie ETS2 & ATS – Review & Schvaľovanie\n\n")
    md.append("> [!IMPORTANT]\n")
    md.append("> **Inkrementálny proces schvaľovania (Human-in-the-Loop):**\n")
    md.append("> 1. **Schválenie:** Označ preklad ako schválený zaškrtnutím `- [x] Schválené` (v Markdown náhľade kliknutím na checkbox, alebo v kóde prepísaním `[ ]` na `[x]`).\n")
    md.append("> 2. **Úprava prekladu:** Text prekladu môžeš upraviť priamo v riadku `* **SK:** ...`.\n")
    md.append("> 3. **Zlúčenie schválených:** Spusti `python run_pipeline.py merge` — do finálneho XLIFF sa zapíšu **len zaškrtnuté položky** (`- [x]`).\n")
    md.append("> 4. **Ďalšie kolo review:** Spusti `python run_pipeline.py draft` — schválené položky sa odfiltrujú a v review zostanú iba položky čakajúce na doriešenie.\n\n")

    # Štatistický panel
    md.append("## 📊 Celkový progres schvaľovania\n\n")
    percent_done = (total_approved_cumulative / total_count * 100) if total_count else 0
    md.append(f"* **Celkový počet reťazcov v projekte:** {total_count}\n")
    md.append(f"* **Schválené a zlúčené v XLIFF:** {total_approved_cumulative} ({percent_done:.1f} %)\n")
    md.append(f"* **Položiek v tomto review kole:** {active_count}\n\n")

    # Tabuľka kapitol
    md.append("### Prehľad podľa kapitol\n\n")
    md.append("| Kapitola | Spolu | Schválené v XLIFF | V tomto review | Stav |\n")
    md.append("| :--- | :---: | :---: | :---: | :---: |\n")

    for title in all_chapters:
        ch_items_total = sum(1 for it in items if get_item_chapter(it) == title)
        ch_merged = sum(1 for (no, it, _) in already_approved_items if get_item_chapter(it) == title)
        ch_active = sum(1 for it in active_items if it.get("chapter") == title)

        if ch_active == 0 and ch_merged > 0:
            status_str = "✅ Kompletné (100 %)"
        elif ch_merged > 0:
            status_str = f"🔄 Rozpracované ({ch_merged}/{ch_items_total})"
        else:
            status_str = "⏳ Čaká na review"

        md.append(f"| {title} | **{ch_items_total}** | {ch_merged} | {ch_active} | {status_str} |\n")

    md.append(f"| **Spolu** | **{total_count}** | **{total_approved_cumulative}** | **{active_count}** | **{percent_done:.1f} % hotovo** |\n\n")
    md.append("---\n\n")

    if active_count == 0:
        md.append("## 🎉 Všetky preklady boli úspešne schválené a zlúčené!\n\n")
        md.append(f"Všetkých {total_count} reťazcov je pripravených vo finálnom súbore `data/output/SCS Trucks_sk_FINAL.xliff` na nahratie do platformy Crowdin.\n\n")
    else:
        # Generovanie položiek zoskupených podľa kapitol
        for title in all_chapters:
            chapter_items = [it for it in active_items if it.get("chapter") == title]
            md.append(f"## {title}\n\n")

            if not chapter_items:
                md.append("*✅ Všetky položky v tejto kapitole už boli schválené a zlúčené.* \n\n---\n\n")
                continue

            for entry in chapter_items:
                item_no = entry["item_no"]
                it = entry["item"]
                uid = it.get("id", "")
                ctx_raw = it.get("group_or_context", "")
                key = ctx_raw.split("]")[0].replace("[Key: ", "").strip() if "[Key:" in ctx_raw else ""
                en = it.get("source_en", "")
                sk = entry["sk"]
                ctx_clean = clean_context_desc(ctx_raw)
                checkbox_marker = "x" if entry["approved"] else " "

                md.append(f"### [Položka {item_no}] ID: `{uid}` | `{key}`\n")
                md.append(f"- [{checkbox_marker}] Schválené\n")
                md.append(f"* **EN:** {en}\n")
                md.append(f"* **SK:** {sk}\n")
                if ctx_clean:
                    md.append(f"* *Kontext:* {ctx_clean}\n")
                if entry["notes"]:
                    for note in entry["notes"]:
                        md.append(f"{note}\n")
                md.append("\n")

            md.append("---\n\n")

    # Voliteľný zbalený archív už schválených položiek
    if already_approved_items:
        md.append(f"<details>\n<summary><b>📦 Archív schválených a zlúčených položiek ({len(already_approved_items)})</b></summary>\n\n")
        md.append("| Položka | ID | Kľúč | Anglický originál | Slovenský preklad |\n")
        md.append("| :---: | :---: | :---: | :--- | :--- |\n")
        for item_no, it, sk_val in already_approved_items:
            uid = it.get("id", "")
            ctx_raw = it.get("group_or_context", "")
            key = ctx_raw.split("]")[0].replace("[Key: ", "").strip() if "[Key:" in ctx_raw else ""
            en_esc = it.get("source_en", "").replace("|", "\\|").replace("\n", " ")
            sk_esc = sk_val.replace("|", "\\|").replace("\n", " ")
            md.append(f"| {item_no} | `{uid}` | `{key}` | {en_esc} | {sk_esc} |\n")
        md.append("\n</details>\n\n")

    content_str = "".join(md)

    os.makedirs(os.path.dirname(output_md), exist_ok=True)
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(content_str)

    print(f"Review dokument vygenerovaný: {output_md}")
    print(f"  - Celkovo položiek v projekte: {total_count}")
    print(f"  - Už schválených v XLIFF:      {total_approved_cumulative}")
    print(f"  - Položiek v tomto review:     {active_count}")

def main():
    parser = argparse.ArgumentParser(description="Generátor review dokumentu.")
    parser.add_argument("--untranslated", default="data/temp/untranslated_strings.csv")
    parser.add_argument("--translations", default="data/temp/translations_complete.json")
    parser.add_argument("--approved", default="data/temp/approved_translations.json")
    parser.add_argument("--output", default="review/preklady_review.md")
    parser.add_argument("--all", action="store_true", help="Vygenerovať všetky položky vrátane už schválených.")
    parser.add_argument("--reset", action="store_true", help="Resetovať schválené úložisko a začať nanovo.")
    args = parser.parse_args()

    generate_review_file(
        untranslated_csv=args.untranslated,
        translations_json=args.translations,
        approved_json=args.approved,
        output_md=args.output,
        include_all=args.all,
        reset=args.reset
    )

if __name__ == "__main__":
    main()
