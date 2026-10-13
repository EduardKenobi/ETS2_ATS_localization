#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_pipeline.py
Hlavný orchestrátor lokalizačného procesu pre ETS2 a ATS.

Príkazy:
  python run_pipeline.py status        - Zobrazí detailný stav projektu a inkrementálny progres
  python run_pipeline.py extract       - Rozparsuje vstupný .xliff, vytvorí glosáre a nepreložené stringy
  python run_pipeline.py draft         - Pripraví / aktualizuje review/preklady_review.md (len neschválené)
  python run_pipeline.py draft --all   - Pripraví review so všetkými položkami
  python run_pipeline.py merge         - Zapíše schválené preklady (- [x]) do finálneho XLIFF
  python run_pipeline.py merge --all   - Zapíše všetky preklady z review bez ohľadu na checkbox
  python run_pipeline.py all           - Spustí kompletný reťazec
"""

import os
import sys
import re
import json
import csv
import argparse
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

def run_command(script_name, args_list=None):
    script_path = os.path.join("scripts", script_name)
    if not os.path.exists(script_path):
        print(f"CHYBA: Skript '{script_path}' neexistuje!")
        return 1

    cmd = [sys.executable, script_path] + (args_list or [])
    return subprocess.call(cmd)

def print_status():
    print("=" * 65)
    print("STAV LOKALIZAČNÉHO PROJEKTU (ETS2 / ATS)")
    print("=" * 65)

    input_xliff = "data/input/SCS Trucks_sk.xliff"
    if not os.path.exists(input_xliff) and os.path.exists("SCS Trucks_sk.xliff"):
        input_xliff = "SCS Trucks_sk.xliff"

    has_input = os.path.exists(input_xliff)
    print(f"1. Vstupný XLIFF:          {'✅ Pripravený' if has_input else '❌ Chýba'} ({input_xliff})")

    untrans_csv = "data/temp/untranslated_strings.csv"
    untrans_count = 0
    if os.path.exists(untrans_csv):
        with open(untrans_csv, "r", encoding="utf-8-sig") as f:
            untrans_count = len(list(csv.DictReader(f)))
        print(f"2. Nepreložené stringy:    ✅ Extrahované ({untrans_count} reťazcov)")
    else:
        print(f"2. Nepreložené stringy:    ⏳ Nie sú extrahované (spusti: python run_pipeline.py extract)")

    # Kumulatívne schválené
    approved_store = "data/temp/approved_translations.json"
    approved_count = 0
    if os.path.exists(approved_store):
        try:
            with open(approved_store, "r", encoding="utf-8") as f:
                approved_count = len(json.load(f))
        except Exception:
            approved_count = 0

    review_md = "review/preklady_review.md"
    if os.path.exists(review_md):
        reviewed_cards = 0
        checked_cards = 0
        with open(review_md, "r", encoding="utf-8") as f:
            for line in f:
                ls = line.strip()
                if ls.startswith("### [Položka"):
                    reviewed_cards += 1
                elif ls.startswith("- [x]") or ls.startswith("- [X]"):
                    checked_cards += 1

        pct = (approved_count / untrans_count * 100) if untrans_count else 0
        print(f"3. Review dokument:        ✅ Pripravený ({reviewed_cards} položiek v review)")
        print(f"   ├─ Označené na merge:   {checked_cards} položiek [- [x]]")
        print(f"   ├─ Čaká na kontrolu:    {reviewed_cards - checked_cards} položiek [- [ ]]")
        print(f"   └─ Kumulatívne v XLIFF: {approved_count} / {untrans_count} položiek ({pct:.1f} %)")
    else:
        print(f"3. Review dokument:        ⏳ Chýba (spusti: python run_pipeline.py draft)")

    out_xliff = "data/output/SCS Trucks_sk_FINAL.xliff"
    has_out = os.path.exists(out_xliff)
    if has_out:
        print(f"4. Finálny súbor (Crowdin): ✅ Vygenerovaný ({approved_count} preložených)")
        print(f"   └─ Cesta: {out_xliff}")
    else:
        print(f"4. Finálny súbor (Crowdin): ⏳ Čaká na schválenie ({out_xliff})")

    print("-" * 65)
    print("Dostupné príkazy:")
    print("  python run_pipeline.py extract       -> Extrakcia z nového Crowdin exportu (automaticky resetuje schválenia)")
    print("  python run_pipeline.py draft         -> Vygenerovanie review pre neschválené položky")
    print("  python run_pipeline.py draft --all   -> Vygenerovanie review so všetkými položkami")
    print("  python run_pipeline.py draft --reset -> Vygenerovanie review s nastavením všetkých položiek na neschválené")
    print("  python run_pipeline.py reset         -> Vynulovanie schválených položiek a vygenerovanie čistého review")
    print("  python run_pipeline.py merge         -> Aplikovanie schválených položiek (- [x]) do finálneho XLIFF")
    print("  python run_pipeline.py merge --all   -> Zlúčenie všetkých položiek v review bez ohľadu na checkbox")
    print("  python run_pipeline.py gui           -> Spustenie interaktívneho webového klikacieho rozhrania")
    print("=" * 65)

def main():
    parser = argparse.ArgumentParser(description="Master CLI pre ETS2/ATS lokalizáciu.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "extract", "draft", "merge", "all", "gui", "review", "reset"], help="Príkaz na vykonanie.")
    parser.add_argument("extra_args", nargs=argparse.REMAINDER, help="Dodatočné argumenty pre podskripty.")
    args = parser.parse_args()

    if args.command == "status":
        print_status()
    elif args.command == "extract":
        sys.exit(run_command("extract.py", args.extra_args))
    elif args.command == "draft":
        sys.exit(run_command("prepare_review.py", args.extra_args))
    elif args.command == "reset":
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))
        import extract
        extract.reset_approved_state()
        print("\n>>> Generujem review dokument so všetkými položkami nastavenými na neschválené...")
        sys.exit(run_command("prepare_review.py", ["--reset"]))
    elif args.command == "merge":
        sys.exit(run_command("merge_to_xliff.py", args.extra_args))
    elif args.command in ("gui", "review"):
        sys.exit(run_command("review_gui.py", args.extra_args))
    elif args.command == "all":
        print(">>> Spúšťam extrakciu...")
        if run_command("extract.py") != 0: sys.exit(1)
        print("\n>>> Pripravujem review dokument...")
        if run_command("prepare_review.py") != 0: sys.exit(1)
        print("\n>>> Zlučujem schválené preklady...")
        if run_command("merge_to_xliff.py", ["--all"]) != 0: sys.exit(1)
        print("\n>>> Kompletný proces bol úspešne dokončený!")

if __name__ == "__main__":
    main()
