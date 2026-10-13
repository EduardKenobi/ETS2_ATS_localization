# AGENTS.md - Pokyny pre asistenta a vývojárov

Tento repozitár slúži na správu a automatizáciu slovenského prekladu hier **Euro Truck Simulator 2 (ETS2)** a **American Truck Simulator (ATS)** exportovaných z platformy Crowdin (formát XLIFF 1.2).

## Hlavné zásady a pravidlá

1. **Ľudská revízia pred zlúčením (Human-in-the-Loop):**
   * Žiadny nový preklad sa nesmie zapísať do `data/output/SCS Trucks_sk_FINAL.xliff` bez predchádzajúceho review používateľom.
   * Všetky návrhy prekladov sa najprv vygenerujú do `review/preklady_review.md`, kde ich používateľ skontroluje, prípadne okomentuje alebo upraví (či už priamo v editore alebo cez webové/mobilné rozhranie `python run_pipeline.py gui`).
   * Schválenie prebieha zaškrtnutím `- [x] Schválené` (resp. tlačidlom v GUI).
   * Príkaz `python run_pipeline.py merge` zapíše do finálneho XLIFF **iba zaškrtnuté položky** (`- [x]`) a uloží ich do kumulatívnej databázy `data/temp/approved_translations.json`.
   * Ďalšie kolo review sa pripraví príkazom `python run_pipeline.py draft`, ktorý automaticky odfiltruje už schválené položky a do review zaradí iba zostávajúce neschválené reťazce.

2. **Dôsledné dodržiavanie herných konvencií:**
   * **Zástupné premenné:** Nikdy neupravovať ani neprekladať premenné SCS engine (`$KEY$`, `$MONEY$`, `$PASSENGERS$`, `$DISTANCE$`, `$COUNT$`, `$BUS_NAME$`).
   * **Formátovacie značky:** Zachovávať tagy `<color value=...>`, `<br>`, `@@link@@`.
   * **XML bezpečnosť:** Pri zápise do `.xliff` musia byť entity správne escapované (`&lt;br&gt;`, `&amp;`), inak Crowdin export odmietne.
   * **Typografia a pomlčky:** NIKDY nepoužívať v prekladoch en-dash `–` (U+2013) ani em-dash `—` (U+2014). VŽDY používať výhradne štandardný ASCII spojovník `-` (U+002D). Herné fonty a engine nepodporujú znak `–` a spôsobujú chyby zobrazenia v hre.
   * **Ustálené herné a tuningové termíny:**
     * Značky pneumatík a marketingové série dielov ("Pulsar", "Radiant", "Monsieur Bibendum", "AERO TOP", "HYDRA") sa neprekladajú.
     * Typy doplnkov: "Roof Lamp Holder" -> "strešný nosník svetiel", "Bull Catcher" -> "ochranný rám", "Sideskirts" -> "bočné obloženie", "Dunnage Box" -> "odkladacia skrinka", "Toolbox" -> "Skrinka s náradím", "Flares" -> "obrysovky".
     * Nápravy a podvozok: "Sliding tandem" -> "posuvná náprava", "Midlift" -> "zdvíhacia stredná náprava", "Liftable" -> "zdvíhacia náprava".
     * Zhoda rodu pri materiáloch (Painted, Plastic, Matte, Chromed, Steel): rešpektovať rod podstatného mena (rám = lakovaný rám; clona = lakovaná clona; svetlo = lakované svetlo).
     * Špecifické SCS pojmy: "Stock" -> "Továrenský" / "Továrenská", "Heavy Duty" -> univerzálne "pre ťažkú prevádzku", "Smart Dash" -> "Smart palubná doska" ("Pokročilá smart palubná doska").
     * Svetlomety podľa kontextu: Route Adviser = "Stretávacie svetlá", tuning diely = "Predné svetlomety", nastavenie premávky = "Svetlomety okolitej dopravy".

3. **Orchestrácia cez `run_pipeline.py`:**
   * Pri práci so súbormi vždy preferuj použitie hlavného orchestrátora `run_pipeline.py`:
     * `python run_pipeline.py status` - prehľad rozpracovanosti a schválených položiek.
     * `python run_pipeline.py extract` - extrakcia z nového vstupného súboru (automaticky zálohuje a resetuje starý schválený stav, aby všetky nové položky začínali ako neschválené).
     * `python run_pipeline.py draft` - generovanie ďalšieho kola review s neschválenými položkami.
     * `python run_pipeline.py reset` - manuálne vynulovanie schválených položiek a vygenerovanie čistého review so všetkými položkami ako neschválené.
     * `python run_pipeline.py gui` - spustenie interaktívneho webového a mobilného review rozhrania.
     * `python run_pipeline.py merge` - zlúčenie schválených položiek do finálneho XML súboru.

4. **Webová a mobilná review aplikácia (`scripts/review_gui.py`):**
   * Server počúva na `0.0.0.0:8080`, čo umožňuje prístup nielen z lokálneho PC (`127.0.0.1`), ale aj z mobilu pripojeného na rovnakej Wi-Fi sieti (`http://<IP>:8080`).
   * Akékoľvek zmeny vykonané v GUI sa automaticky zapisujú priamo do `review/preklady_review.md` (Single Source of Truth), čím sa zachováva 100 % synchronizácia.
   * Komentáre a poznámky sa ukladajú vo formáte citácie `> Poznámka` pod príslušnou kartou položky.

5. **Projektová štruktúra:**
   * `data/input/`: Vstupné `.xliff` súbory z Crowdinu.
   * `data/output/`: Finálne pripravené súbory na upload do Crowdinu.
   * `data/glossaries/`: Rozdelené glosáre existujúcich prekladov (pod 500k slov).
   * `data/temp/`: Dočasné extrahované CSV, JSON súbory a stavová databáza `approved_translations.json`.
   * `review/`: Dokumenty pre kontrolu prekladov (`preklady_review.md`, `review_app.html`).
   * `scripts/`: Samostatné Python skripty (`extract.py`, `prepare_review.py`, `merge_to_xliff.py`, `review_gui.py`).
