---
name: ets2-ats-localization
description: "End-to-end workflow and knowledge base for ETS2 and ATS localization pipelines: extracting Crowdin XLIFF files, managing game glossaries, drafting contextual translations, human review, and merging back into valid XLIFF."
---

# ETS2 & ATS Localization Pipeline Skill

This skill defines the standardized end-to-end process for handling Euro Truck Simulator 2 and American Truck Simulator Slovak localization files exported from Crowdin.

## Workflow Overview

The localization lifecycle follows three distinct phases:

```
[Crowdin Export (.xliff)] 
       │
       ▼
 1. EXTRACTION (`python run_pipeline.py extract`)
       ├─► data/glossaries/ets2_glossary.txt (Translation memory)
       ├─► data/glossaries/ats_glossary.txt  (Translation memory)
       └─► data/temp/untranslated_strings.csv (Strings with state="needs-translation")
       │
       ▼
 2. REVIEW & DRAFTING (`python run_pipeline.py draft`)
       └─► review/preklady_review.md (Thematic review document with all strings)
           ▲
           └─► User edits / feedback / inline comments
       │
       ▼
 3. FINAL MERGE (`python run_pipeline.py merge`)
       └─► data/output/SCS Trucks_sk_FINAL.xliff (Updated XML ready for Crowdin)
```

## Directory Structure

* `data/input/`: Place the newly exported `.xliff` file from Crowdin here (e.g. `SCS Trucks_sk.xliff`).
* `data/glossaries/`: Auto-generated translation memory files split by game (`ets2_glossary.txt`, `ats_glossary.txt`), keeping file sizes under 400,000 words.
* `data/temp/`: Working files (`untranslated_strings.csv`, cached json).
* `review/preklady_review.md`: The central human review document. Divided into thematic chapters.
* `data/output/`: The merged, syntactically valid `.xliff` file (e.g. `SCS Trucks_sk_FINAL.xliff`) for Crowdin upload.
* `scripts/`: Modular processing scripts (`extract.py`, `prepare_review.py`, `merge_to_xliff.py`).
* `run_pipeline.py`: Master CLI orchestrator.

## Localization Rules for SCS Games

1. **Placeholders & Tags**:
   * NEVER translate or alter game engine variables: `$KEY$`, `$MONEY$`, `$PASSENGERS$`, `$DISTANCE$`, `$COUNT$`, `$BUS_NAME$`, `$PRICE$`.
   * Preserve color markup: `<color value=@@clr_skill_desc_highlight@@>...</color>`.
   * Preserve link tags: `@@bus_garage@@`.
   * XML entities: Ensure raw `<br>` tags in XML are escaped as `&lt;br&gt;`, and ampersands as `&amp;`.

2. **Terminology Consistency**:
   * **Coach**: "Autobus" / "Diaľkový autobus".
   * **Coach Dealer**: "Predajca autobusov".
   * **Quick Jobs**: "Rýchle zákazky".
   * **Contract Jobs**: "Zmluvné zákazky".
   * **Tourist Jobs**: "Turistické zákazky".
   * **Income / Job income**: "Príjem" / "Príjem zo zákazky".
   * **Departure / Arrival**: "Odchod" / "Príchod".
   * **Scheduled arrival / departure**: "Plánovaný príchod" / "Plánovaný odchod".
   * **On time**: "Načas" / "Včas".
   * **Medals**: Flawless ("Bezchybná"), Great ("Skvelá"), Reliable ("Spoľahlivá"), Average ("Priemerná"), Subpar ("Podpriemerná"), Poor ("Slabá"), Unprofessional ("Neprofesionálna").

3. **Character Limits**:
   * Inspect the context string in `untranslated_strings.csv` before drafting. If it specifies a character limit (e.g. "Must fit within 44 characters"), ensure the Slovak translation strictly respects it.

4. **Typography & Hyphens**:
   * NEVER use en-dash `–` (U+2013) or em-dash `—` (U+2014) in Slovak translations. ALWAYS use the standard ASCII hyphen `-` (U+002D). SCS engine fonts often do not support `–` and will render broken characters or missing squares in-game.

5. **Brand Guidelines & Established Vehicle / Tuning Terminology**:
   * **Tire models & OEM branding**: Modely pneumatík (napr. "315/70 Goodyear Fuelmax S Gen2") ostávajú v pôvodnom znení.
   * **Tuning a marketingové série**: Špecifické doplnky a marketingové názvy (napr. "Pulsar", "Radiant", "Monsieur Bibendum", "AERO TOP", "CROSSBAR", "HYDRA") sa neprekladajú.
   * **Typy príslušenstva (Accessory types)**:
     * "Roof Lamp Holder" -> "strešný nosník svetiel"
     * "Bull Catcher" -> "ochranný rám"
     * "Light Bar" -> "svetelný nosník"
     * "Bull Bar" -> "ochranný nosník"
     * "Trim" -> "obloženie"
     * "Sideskirts" -> "bočné obloženie"
     * "Box" -> "skrinka"
     * "Dunnage Box" -> "odkladacia skrinka"
     * "Pipeguard" -> "chránič trubiek"
     * "Spare Tyre" -> "Rezerva"
     * "Toolbox" -> "Skrinka s náradím"
     * "Flares" -> "obrysovky" (napr. s obrysovkami, veľké obrysovky)
   * **Podvozok a nápravy (Chassis & axle)**:
     * "Sliding tandem" -> "posuvná náprava"
     * "Midlift" -> "zdvíhacia stredná náprava"
     * "Liftable" -> "zdvíhacia náprava" (napr. zdvíhací)
   * **Zhoda rodu pri materiáloch (Material adjectives)**: Prídavné mená (Painted, Plastic, Matte, Chromed, Steel) musia gramaticky ladiť s rodom podstatného mena:
     * Mužský rod (rám, nosník, kryt, deflektor): matný, lakovaný, plastový, chrómovaný, oceľový.
     * Stredný rod (svetlo - kontext `light_`, `r_light`): matné, lakované, plastové, chrómované, oceľové.
     * Ženský rod (lišta, clona - kontext `sunshld`, `sideskrt_bar`): matná, lakovaná, plastová, chrómovaná, oceľová.
   * **"Stock" ponuky / diely**: Prekladať ako "Továrenský" (továrenská, továrenské podľa rodu). Napr. "Stock Offers" -> "Továrenské ponuky".
   * **Úrovne výbavy (Trim levels)**: Exclusive, Elegance - zachovať alebo preložiť podľa glosára / kontextu.
   * **Smart Dash**: "Smart Dash" -> "Smart palubná doska", "Smart Dash Advanced" -> "Pokročilá smart palubná doska" (napr. "Smart Dash Advanced, Dark" -> "Pokročilá smart palubná doska, tmavá").
   * **Heavy Duty**: Univerzálne prekladať ako "pre ťažkú prevádzku" pre všetky doplnky a tuningové diely bez ohľadu na rod.
   * **Svetlomety a svetlá podľa kontextu**:
     * Route Adviser / palubka (`adv_hud_lgd_low_beam`): "Stretávacie svetlá"
     * Fyzické diely / sloty (`head_lights`, `f_light_chs`): "Predné svetlomety"
     * Nastavenia grafiky ("Traffic headlights"): "Svetlomety okolitej dopravy" (tooltip: "Povolí iným vozidlám v premávke vrhať svetlo zo svojich svetlometov.").

## Common CLI Commands

```bash
# Check current project status
python run_pipeline.py status

# Extract newly uploaded Crowdin file (automatically backs up and resets approved status)
python run_pipeline.py extract

# Generate or update review markdown document (filters already approved items)
python run_pipeline.py draft

# Generate complete review markdown document with all items
python run_pipeline.py draft --all

# Explicitly reset all approvals and regenerate review with all items unapproved
python run_pipeline.py reset

# Launch local web server & mobile reviewer app (Wi-Fi accessible on port 8080)
python run_pipeline.py gui

# Merge only approved translations (- [x]) from review/preklady_review.md into final XLIFF
python run_pipeline.py merge

# Merge all translations from review/preklady_review.md regardless of checkboxes
python run_pipeline.py merge --all
```

## Mobile & Web Review Application (`scripts/review_gui.py`)

* Start with: `python run_pipeline.py gui`
* PC access: `http://localhost:8080`
* Mobile Wi-Fi access: `http://<PC_LOCAL_IP>:8080` (device connected to the same local Wi-Fi)
* Features:
  * One-tap approve / unapprove toggles.
  * Instant auto-save to `review/preklady_review.md` (no manual save required).
  * Direct inline comments (`💬 Poznámka / Komentár`) saved as markdown quotes.
  * Real-time search and chapter filtering.
  * Bulk approve visible items button.
  * Direct merge to final XLIFF button.
* Shutdown: Press `Ctrl + C` in the host terminal window.

