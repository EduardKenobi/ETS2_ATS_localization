#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/extract.py
Pamäťovo efektívny extraktor XLIFF lokalizačných súborov pre ETS2 a ATS.
Extrahuje:
  1. Glossáre existujúcich slovenských prekladov (rozdelené podľa hier pod 500k slov).
  2. Zoznam nepreložených reťazcov s kontextom (state="needs-translation").
"""

import os
import sys
import csv
import argparse
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')
XML_NS = "{urn:oasis:names:tc:xliff:document:1.2}"

def clean_context(elem, resname, ns):
    """Extrahuje a vyčistí kontext zo značky <context-group><context>."""
    cg = elem.find(f"{ns}context-group")
    if cg is not None:
        ctx_elem = cg.find(f"{ns}context")
        if ctx_elem is not None and ctx_elem.text:
            text = ctx_elem.text.strip()
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            filtered = [
                l for l in lines
                if l != resname and not l.startswith(f"Id: {resname}") and not (l.startswith("Id: ") and l[4:].strip() == resname)
            ]
            if filtered:
                return " ".join(" | ".join(filtered).split())
    return resname

def find_input_xliff(input_path=None):
    if input_path and os.path.exists(input_path):
        return input_path
    
    # Skúsime štandardné umiestnenia
    candidates = [
        "data/input/SCS Trucks_sk.xliff",
        "SCS Trucks_sk.xliff"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
            
    # Vyhľadáme akýkoľvek .xliff v data/input
    if os.path.exists("data/input"):
        for f in os.listdir("data/input"):
            if f.endswith(".xliff"):
                return os.path.join("data/input", f)
                
    return None

import json
import time

def reset_approved_state(approved_store_path="data/temp/approved_translations.json", 
                         translations_path="data/temp/translations_complete.json",
                         keep_approved=False):
    """
    Pred novou extrakciou zálohuje a resetuje stav schválených položiek.
    Všetky texty prekladov uloží do translations_complete.json, aby slúžili
    ako drafty/pamäť prekladov, ale samotný schválený stav vynuluje na neschválený.
    """
    if keep_approved:
        print("ℹ️ Ponechávam existujúci stav schválených položiek (--keep-approved).")
        return

    if os.path.exists(approved_store_path):
        try:
            with open(approved_store_path, "r", encoding="utf-8") as f:
                old_approved = json.load(f)
        except Exception:
            old_approved = {}

        if old_approved:
            ts = time.strftime("%Y%m%d_%H%M%S")
            backup_dir = os.path.dirname(approved_store_path)
            backup_path = os.path.join(backup_dir, f"approved_translations_backup_{ts}.json")
            backup_latest = os.path.join(backup_dir, "approved_translations_backup.json")
            
            with open(backup_path, "w", encoding="utf-8") as f:
                json.dump(old_approved, f, ensure_ascii=False, indent=2)
            with open(backup_latest, "w", encoding="utf-8") as f:
                json.dump(old_approved, f, ensure_ascii=False, indent=2)

            # Zlúčenie starých schválených textov do translations_complete.json
            if translations_path:
                trans_dict = {}
                if os.path.exists(translations_path):
                    try:
                        with open(translations_path, "r", encoding="utf-8") as f:
                            trans_dict = json.load(f)
                    except Exception:
                        trans_dict = {}
                trans_dict.update(old_approved)
                os.makedirs(os.path.dirname(translations_path), exist_ok=True)
                with open(translations_path, "w", encoding="utf-8") as f:
                    json.dump(trans_dict, f, ensure_ascii=False, indent=2)

            # Reset schválených položiek pre nový export
            with open(approved_store_path, "w", encoding="utf-8") as f:
                json.dump({}, f, ensure_ascii=False, indent=2)

            print(f"ℹ️ Zistený nový export: Schválený stav bol resetovaný ({len(old_approved)} predchádzajúcich položiek zálohovaných).")
            print(f"   Všetky položky v novom exporte budú nastavené ako neschválené.")
            print(f"   Záloha schválených prekladov: '{backup_latest}'")

def run_extraction(input_file, glossaries_dir, output_untranslated, keep_approved=False):
    if not input_file or not os.path.exists(input_file):
        print(f"CHYBA: Vstupný XLIFF súbor nebol nájdený! ({input_file})")
        sys.exit(1)

    # Reset schváleného stavu pred parsovaním nového exportu
    reset_approved_state(keep_approved=keep_approved)

    os.makedirs(glossaries_dir, exist_ok=True)
    os.makedirs(os.path.dirname(output_untranslated), exist_ok=True)

    out_ets2 = os.path.join(glossaries_dir, "ets2_glossary.txt")
    out_ats = os.path.join(glossaries_dir, "ats_glossary.txt")

    print(f"Extrahuje sa súbor: '{input_file}'...")

    total_units = 0
    count_ets2 = 0
    count_ats = 0
    count_untranslated = 0
    count_skipped = 0

    seen_keys_ets2 = set()
    seen_keys_ats = set()
    current_file = "unknown"

    with open(out_ets2, "w", encoding="utf-8") as f_ets2, \
         open(out_ats, "w", encoding="utf-8") as f_ats, \
         open(output_untranslated, "w", newline="", encoding="utf-8-sig") as f_untrans:

        csv_writer = csv.writer(f_untrans, quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        csv_writer.writerow(["id", "file", "group_or_context", "source_en"])

        context = ET.iterparse(input_file, events=("start", "end"))
        context = iter(context)
        _, root = next(context)

        for event, elem in context:
            if event == "start":
                if elem.tag == f"{XML_NS}file":
                    current_file = elem.attrib.get("original", elem.attrib.get("id", "unknown"))
            elif event == "end" and elem.tag == f"{XML_NS}trans-unit":
                total_units += 1
                unit_id = elem.attrib.get("id", "")
                resname = elem.attrib.get("resname", "")

                source_elem = elem.find(f"{XML_NS}source")
                target_elem = elem.find(f"{XML_NS}target")

                source_text = source_elem.text if (source_elem is not None and source_elem.text) else ""
                target_text = target_elem.text if (target_elem is not None and target_elem.text) else ""

                state = target_elem.attrib.get("state") if target_elem is not None else None
                context_desc = clean_context(elem, resname, XML_NS)

                # Nepreložené
                if state == "needs-translation":
                    count_untranslated += 1
                    grp_ctx = f"[Key: {resname}] {context_desc}" if context_desc != resname else f"[Key: {resname}]"
                    csv_writer.writerow([unit_id, current_file, grp_ctx, source_text])

                # Preložené (s deduplikáciou vetvy trunk vs 1_61)
                elif state in ("final", "translated") and target_text.strip():
                    id_label = f"{resname} (#{unit_id})" if resname else unit_id
                    entry = (
                        f"[ID: {id_label}] | [Group/Context: {context_desc}] | [File: {current_file}]\n"
                        f"EN: {source_text}\n"
                        f"SK: {target_text}\n"
                        f"---\n"
                    )

                    if "ets2" in current_file or "extra_texts" in current_file:
                        if resname not in seen_keys_ets2:
                            seen_keys_ets2.add(resname)
                            f_ets2.write(entry)
                            count_ets2 += 1
                    elif "ats" in current_file:
                        if resname not in seen_keys_ats:
                            seen_keys_ats.add(resname)
                            f_ats.write(entry)
                            count_ats += 1
                else:
                    count_skipped += 1

                root.clear()

    print("\n" + "=" * 65)
    print("VÝSLEDKY EXTRAKCIE:")
    print("=" * 65)
    print(f"Celkovo spracovaných položiek:   {total_units}")
    print(f"Existujúce preklady ETS2:       {count_ets2} záznamov")
    print(f"Existujúce preklady ATS:        {count_ats} záznamov")
    print(f"Nepreložené stringy (na preklad): {count_untranslated}")
    print(f"Systémové / netranslatovateľné:  {count_skipped}")
    print("-" * 65)
    print(f"Glosár ETS2:         {out_ets2}")
    print(f"Glosár ATS:          {out_ats}")
    print(f"Nepreložené (CSV):   {output_untranslated}")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Extraktor lokalizácií SCS XLIFF.")
    parser.add_argument("--input", default=None, help="Cesta k vstupnému .xliff súboru.")
    parser.add_argument("--glossaries-dir", default="data/glossaries", help="Priečinok pre glosáre.")
    parser.add_argument("--output-untranslated", default="data/temp/untranslated_strings.csv", help="Výstupný CSV súbor s nepreloženými reťazcami.")
    parser.add_argument("--keep-approved", action="store_true", help="Ponechať existujúci stav schválených položiek bez resetu.")
    args = parser.parse_args()

    input_file = find_input_xliff(args.input)
    run_extraction(input_file, args.glossaries_dir, args.output_untranslated, keep_approved=args.keep_approved)

if __name__ == "__main__":
    main()
