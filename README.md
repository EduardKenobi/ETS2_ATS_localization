# 🚛 ETS2 & ATS Slovenská Lokalizácia - Automatizačný Pipeline

Tento projekt slúži na automatizované spracovanie, preklad a revíziu oficiálnych lokalizačných súborov pre hry **Euro Truck Simulator 2** a **American Truck Simulator** exportovaných z platformy **Crowdin** (formát XLIFF 1.2).

---

## ⚡ Rýchly prehľad celého procesu

```mermaid
flowchart TD
    A[1. Stiahnutie z Crowdinu<br>data/input/SCS Trucks_sk.xliff] --> B[2. Extrakcia<br>python run_pipeline.py extract]
    B --> C[Vytvorenie glosárov a nepreložených reťazcov]
    C --> D[3. Príprava Review<br>python run_pipeline.py draft]
    D --> E[review/preklady_review.md<br>alebo Mobilná / Web Aplikácia]
    E -->|Zaškrtnutie - [x] a poznámky| F[4. Inkrementálne zlúčenie<br>python run_pipeline.py merge]
    F --> G[5. Finálny XLIFF pre Crowdin<br>data/output/SCS Trucks_sk_FINAL.xliff]
    F -.->|Zostávajúce neschválené| D
```

---

## 📁 Projektová štruktúra

```text
ETS2_ATS_lokalizacia/
├── data/
│   ├── input/                # Vstupné .xliff súbory stiahnuté z Crowdinu
│   │   └── SCS Trucks_sk.xliff
│   ├── glossaries/           # Automaticky vytvorené glosáre existujúcich prekladov
│   │   ├── ets2_glossary.txt
│   │   └── ats_glossary.txt
│   ├── temp/                 # Dočasné pracovné a stavové súbory
│   │   ├── untranslated_strings.csv
│   │   ├── translations_complete.json
│   │   └── approved_translations.json   # Databáza schválených položiek
│   └── output/               # Výsledný súbor pripravený na upload do Crowdinu
│       └── SCS Trucks_sk_FINAL.xliff
├── review/
│   ├── preklady_review.md    # Hlavný dokument na kontrolu (Single Source of Truth)
│   └── review_app.html       # Webová šablóna pre rozhranie
├── scripts/
│   ├── extract.py            # Streamovacia pamäťovo efektívna extrakcia XLIFF
│   ├── prepare_review.py     # Generovanie review dokumentu s checkboxami
│   ├── merge_to_xliff.py     # Inkrementálne zlúčenie schválených prekladov (- [x])
│   └── review_gui.py         # Lokálny server a mobilná webová aplikácia
├── .agents/
│   └── skills/
│       └── ets2-ats-localization/
│           └── SKILL.md      # Skill znalostná báza pre AI asistenta
├── run_pipeline.py           # Hlavný orchestrátor (CLI rozhranie)
├── AGENTS.md                 # Pokyny a konvencie pre asistentov a vývojárov
└── README.md                 # Táto dokumentácia
```

---

## 📱 Webová & Mobilná Review Aplikácia (Obsluha)

Aplikácia umožňuje pohodlnú kontrolu a schvaľovanie takmer 500 reťazcov priamo z gauča na mobile (alebo v prehliadači na PC), s automatickým ukladaním zmien do projektových súborov.

### 1. Spustenie aplikácie
V termináli na počítači zadaj:
```bash
python run_pipeline.py gui
```
Konzola vypíše adresy na pripojenie:
* **Na PC:** `http://127.0.0.1:8080` (otvorí sa automaticky v prehliadači)
* **Na mobile:** `http://<IP_ADRESA_PC>:8080` (napr. `http://192.168.1.232:8080`)

> [!NOTE]
> Aby mobilná verzia fungovala, mobil a PC musia byť pripojené na **rovnakej domácej Wi-Fi sieti**.

### 2. Obsluha a funkcie aplikácie
* **Dotykové schvaľovanie položiek:**
  * Ťuknutím na tlačidlo **`◯ Schváliť`** sa položka označí ako **`✅ Schválené`** (zelená farba).
  * Opätovným ťuknutím sa schválenie zruší.
* **Automatické ukladanie na pozadí (Auto-Save):**
  * Akákoľvek zmena (zaškrtnutie, úprava prekladu, komentár) sa **do 350 ms automaticky zapíše na PC** do súboru `review/preklady_review.md`.
  * Nemusíš hľadať žiadne tlačidlo "Uložiť". V záhlaví svieti indikátor `🟢 Uložené na PC`.
* **Úprava slovenského prekladu:**
  * Text prekladu môžeš priamo prepísať v textovom poli každej položky.
* **Písanie komentárov a poznámok:**
  * Do žltého poľa `💬 Poznámka / Komentár:` môžeš napísať akúkoľvek pripomienku (napr. *„skontrolovať dĺžku v hre“*).
  * Komentár sa v `review/preklady_review.md` automaticky uloží ako citácia (`> komentár`).
* **Filtrovanie a vyhľadávanie:**
  * Filtruj podľa 5 kapitol alebo podľa stavu (*Iba na schválenie* / *Iba schválené*).
  * Fulltextové vyhľadávanie v reálnom čase podľa EN originálu, SK prekladu, ID alebo kľúča.
* **Záložka „⚙️ Riadiace centrum & Pipeline“ (Novinka):**
  * Prepínač v záhlaví umožňuje prepnúť medzi kartami prekladov a **riadiacim centrom celého procesu**.
  * **Živý stav súborov:** Prehľadné karty zobrazujúce stav vstupného XLIFF (veľkosť, dátum), počty existujúcich záznamov v glosároch (ETS2 / ATS), nájdené nepreložené stringy a stav finálneho výstupu.
  * **Tlačidlá pre jednotlivé kroky:**
    * `⚡ Spustiť extrakciu` (Krok 1) - rozparsuje vstupný XLIFF a vytvorí glosáre.
    * `📋 Pripraviť Review` (Krok 2) - vygeneruje nové kolo review s voliteľným prepínačom `--all`.
    * `🔍 Prejsť na karty prekladov` (Krok 3) - prepne rovno do editačného zoznamu.
    * `🚀 Spustiť Merge do XLIFF` (Krok 4) - zlúči schválené položky do herného súboru.
  * **Konzolový výstup v reálnom čase:** Po kliknutí na krok sa priamo v rozhraní zobrazí výstup operácie z konzoly so všetkými detailmi a počtami.
* **Hromadné schvaľovanie:**
  * Tlačidlo **`✅ Všetko zobrazené`** v spodnej lište schváli všetky aktuálne vyfiltrované položky jedným klikom (napr. celú kapitolu).
* **Zlúčenie do herného súboru z mobilu:**
  * Tlačidlo **`🚀 Zlúčiť do XLIFF`** v spodnej lište priamo z mobilu spustí zlúčenie zaškrtnutých položiek do finálneho súboru.

### 3. Vypnutie servera
* V okne terminálu na PC stlač **`Ctrl + C`** (alebo jednoducho zatvor okno terminálu).

---

## ✍️ Alternatíva: Práca priamo v editore kódu (IDE)

Ak preferuješ pracovať priamo v editore bez webového rozhrania:
1. Otvor [**`review/preklady_review.md`**](review/preklady_review.md) v **textovom zobrazení kódu** (nie v náhľade Preview).
2. Schválenie vykonáš prepísaním `[ ]` na `[x]`:
   ```markdown
   ### [Položka 1] ID: `827424` | `front_left`
   - [x] Schválené
   * **EN:** Front Left
   * **SK:** Predné ľavé
   > Moja poznámka k prekladu
   ```
3. Preklad upravíš priamo v riadku `* **SK:** ...` a vlastné komentáre môžeš písať kamkoľvek pod kartu.

---

## 🔄 Inkrementálny proces schvaľovania (Viac-kolové review)

Pri takmer 500 položkách nie je potrebné schváliť všetko naraz:

1. **Čiastočné schválenie a zlúčenie:**
   * Schváľ prvých napr. 100 položiek (buď v GUI cez tlačidlá, alebo v MD cez `- [x]`).
   * Spusti v termináli:
     ```bash
     python run_pipeline.py merge
     ```
   * Do finálneho `SCS Trucks_sk_FINAL.xliff` sa zapíšu **iba zaškrtnuté položky**. Ostatné zostanú pripravené na preklad.
2. **Generovanie ďalšieho kola review:**
   * Spusti:
     ```bash
     python run_pipeline.py draft
     ```
   * Skript **automaticky odfiltruje už schválené a zlúčené položky**.
   * V súbore `review/preklady_review.md` (aj vo webovom GUI) zostanú **len položky, ktoré čakajú na schválenie**!
   * Tvoje poznámky a úpravy k neschváleným položkám zostanú zachované.

---

## 🚀 Postup krok za krokom (Nový Crowdin export)

### Krok 1: Uloženie exportu
* Stiahni z Crowdinu najnovší súbor XLIFF.
* Ulož ho do: `data/input/SCS Trucks_sk.xliff`.

### Krok 2: Extrakcia glosárov a nepreložených stringov
```bash
python run_pipeline.py extract
```

### Krok 3: Vygenerovanie review podkladov
```bash
python run_pipeline.py draft
```

### Krok 4: Kontrola a schválenie
Spusti webové rozhranie (alebo edituj Markdown priamo):
```bash
python run_pipeline.py gui
```
Označ položky ako schválené (`✅ Schválené`).

### Krok 5: Zlúčenie schválených položiek
```bash
python run_pipeline.py merge
```
Vygeneruje sa syntakticky validný: **`data/output/SCS Trucks_sk_FINAL.xliff`**.

### Krok 6: Nahratie do Crowdinu
1. V projekte na Crowdine otvor sekciu **Slovak (Slovenčina)**.
2. V ponuke klikni na **Upload Translations** (Nahrať preklady).
3. Vyber súbor `data/output/SCS Trucks_sk_FINAL.xliff`.
4. Crowdin automaticky spáruje ID a zaznamená preklady!

---

## 📌 Zoznam príkazov orchestrátora

| Príkaz | Popis |
| :--- | :--- |
| `python run_pipeline.py status` | Zobrazí prehľadný stav rozpracovanosti (schválené vs. čakajúce položky). |
| `python run_pipeline.py extract` | Pamäťovo efektívne rozparsuje vstupný XLIFF a vytvorí glosáre. |
| `python run_pipeline.py draft` | Pripraví review dokument iba so zostávajúcimi neschválenými položkami. |
| `python run_pipeline.py draft --all` | Pripraví kompletný review dokument so všetkými položkami (aj schválenými). |
| `python run_pipeline.py gui` | Spustí lokálny webový server s mobilným prístupom na pohodlné schvaľovanie. |
| `python run_pipeline.py merge` | Zlúči iba zaškrtnuté položky (`- [x]`) do finálneho herného XLIFF. |
| `python run_pipeline.py merge --all` | Núdzové zlúčenie všetkých položiek v review bez ohľadu na zaškrtnutie. |
| `python run_pipeline.py all` | Spustí kompletný automatizovaný reťazec (extrakcia, draft, merge). |
