# 📋 Návrh lokalizácie ETS2 & ATS – Review & Schvaľovanie

> [!IMPORTANT]
> **Inkrementálny proces schvaľovania (Human-in-the-Loop):**
> 1. **Schválenie:** Označ preklad ako schválený zaškrtnutím `- [x] Schválené`.
> 2. **Úprava prekladu:** Text prekladu je možné upraviť priamo v riadku `* **SK:** ...`.
> 3. **Zlúčenie schválených:** Spusti `python run_pipeline.py merge` — do finálneho XLIFF sa zapíšu **len zaškrtnuté položky** (`- [x]`).
> 4. **Ďalšie kolo review:** Spusti `python run_pipeline.py draft` — schválené položky sa odfiltrujú.

## 📊 Celkový progres schvaľovania

* **Celkový počet reťazcov v projekte:** 193
* **Schválené na zlúčenie / zlúčené:** 193 (100.0 %)
* **Zostáva na schválenie:** 0

### Prehľad podľa kapitol

| Kapitola | Rozsah | Spolu | Schválené | Zostáva na review | Stav |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 1. Coach Mode (Autobusy) – Rozhranie, Zákazky, Zastávky a Hlásenia | **1 – 150** | 150 | 150 | 0 | ✅ Kompletné (100 %) |
| 2. Coach Mode – Garáž, Prehliadač, Úrovne vodiča a Zručnosti | **151 – 246** | 96 | 43 | 53 | 🔄 Rozpracované (43/96) |
| 3. Príslušenstvo kabíny, Diely, Prevodovky a Motory | **247 – 338** | 92 | 0 | 92 | ⏳ Čaká na review |
| 4. Laky a Farby vozidiel (Paintjobs) | **339 – 426** | 88 | 0 | 88 | ⏳ Čaká na review |
| 5. ATS Pamätihodnosti a Vyhliadky (Nebraska, Iowa, Texas, Oklahoma) | **427 – 193** | 0 | 0 | 0 | ✅ Kompletné (100 %) |
| **Spolu** | **1 – 193** | **193** | **193** | **0** | **100.0 % hotovo** |

---

## 1. Coach Mode (Autobusy) – Rozhranie, Zákazky, Zastávky a Hlásenia

### [Položka 1] ID: `828674` | `bus_panel`
- [x] Schválené
* **EN:** Destination Panel
* **SK:** Cieľová tabuľa
* *Kontext:* Bus Destination Panel Locator | Group: Various accessory slots or accessory names.

### [Položka 2] ID: `828676` | `curtains`
- [x] Schválené
* **EN:** Curtains
* **SK:** Záclonky
* *Kontext:* Coach Passenger Curtains | Group: Various accessory slots or accessory names.

### [Položka 3] ID: `828678` | `f_intake`
- [x] Schválené
* **EN:** Front Mask
* **SK:** Predná maska
* *Kontext:* Coach Front Mask | Group: Various accessory slots or accessory names.

### [Položka 4] ID: `828686` | `r_panel`
- [x] Schválené
* **EN:** Rear Panel
* **SK:** Zadná tabuľa
* *Kontext:* Rear Panel | Group: Various accessory slots or accessory names.

### [Položka 5] ID: `828688` | `rv_mirror`
- [x] Schválené
* **EN:** Rearview Mirror
* **SK:** Spätné zrkadlo
* *Kontext:* Group: Various accessory slots or accessory names.

### [Položka 6] ID: `828690` | `warnsticker`
- [x] Schválené
* **EN:** Warning Sticker
* **SK:** Výstražná nálepka
* *Kontext:* Stickers area for buses | Group: Various accessory slots or accessory names.

### [Položka 7] ID: `827464` | `bus_job_t`
- [x] Schválené
* **EN:** QUICK JOB
* **SK:** RÝCHLE ZÁKAZKY
* *Kontext:* Title of the screen. Please keep in upper case where possible. | Group: Bus quick job selection screen. | During a bus quick job the player drives a company provided bus from start to destination.

### [Položka 8] ID: `827466` | `bus_job`
- [x] Schválené
* **EN:** Quick Job
* **SK:** Rýchle zákazky
* *Kontext:* Icon opening the quick job screen. There is limited space allowing for two lines of 7 'W' characters each. | Group: Bus quick job selection screen. | During a bus quick job the player drives a company provided bus from start to destination.

### [Položka 9] ID: `828696` | `bus_job_bus_overturned_text`
- [x] Schválené
* **EN:** You've overturned your coach and cannot continue.<br>You can load your previous position or abandon the job with a penalty of $MONEY$.
* **SK:** Prevrátil si svoj autobus a nemôžeš pokračovať.<br>Môžeš načítať predchádzajúcu pozíciu alebo zrušiť zákazku s pokutou $MONEY$.
* *Kontext:* Group: Bus quick job failure screen. | This screen is shown when player overturns bus during job.

### [Položka 10] ID: `828698` | `bus_job_extreme_acceleration_text`
- [x] Schválené
* **EN:** You've had a severe crash and cannot continue.<br>You can load your previous position or abandon the job with a penalty of $MONEY$.
* **SK:** Mal si ťažkú nehodu a nemôžeš pokračovať.<br>Môžeš načítať predchádzajúcu pozíciu alebo zrušiť zákazku s pokutou $MONEY$.
* *Kontext:* Group: Bus quick job failure screen. | This screen is shown when player overturns bus during job.

### [Položka 11] ID: `827666` | `equipment_provided_bus`
- [x] Schválené
* **EN:** Provided coach
* **SK:** Poskytnutý autobus
* *Kontext:* Group: Multiplayer.

### [Položka 12] ID: `827668` | `equipment_owned_bus`
- [x] Schválené
* **EN:** Owned coach
* **SK:** Vlastný autobus
* *Kontext:* Group: Multiplayer.

### [Položka 13] ID: `827672` | `mp_job_wrong_bus`
- [x] Schválené
* **EN:** You don’t have a compatible coach currently assigned.
* **SK:** Momentálne nemáš priradený kompatibilný autobus.
* *Kontext:* Group: Multiplayer.

### [Položka 14] ID: `827896` | `tight_schedule_desc_xp_bonus_total`
- [x] Schválené
* **EN:** <color value=@@clr_skill_desc_highlight@@>0-$XP_BONUS$% XP bonus</color> based on job type
* **SK:** <color value=@@clr_skill_desc_highlight@@>0-$XP_BONUS$% vyšší bonus k XP</color> na základe typu zákazky
* *Kontext:* Group: Bus skills.

### [Položka 15] ID: `827898` | `satisfaction_decrease_desc_new`
- [x] Schválené
* **EN:** New jobs with passengers whose <color value=@@clr_skill_desc_highlight@@>satisfaction decreases more quickly</color> available
* **SK:** Dostupné nové zákazky s cestujúcimi, ktorých <color value=@@clr_skill_desc_highlight@@>spokojnosť klesá rýchlejšie</color>.
* *Kontext:* Group: Bus skills.

### [Položka 16] ID: `827922` | `low_acceleration_desc_xp_bonus`
- [x] Schválené
* **EN:** <color value=@@clr_skill_desc_highlight@@>$XP_BONUS$% XP bonus</color> for new job types
* **SK:** <color value=@@clr_skill_desc_highlight@@>O $XP_BONUS$% vyšší bonus k XP</color> za nové typy zákaziek
* *Kontext:* Group: Bus skills.

### [Položka 17] ID: `827924` | `low_acceleration_desc_xp_bonus_total`
- [x] Schválené
* **EN:** <color value=@@clr_skill_desc_highlight@@>0-$XP_BONUS$% XP bonus</color> based on job type
* **SK:** <color value=@@clr_skill_desc_highlight@@>0-$XP_BONUS$% vyšší bonus k XP</color> na základe typu zákazky
* *Kontext:* Group: Bus skills.

### [Položka 18] ID: `828700` | `is_cut_thingvellir`
- [x] Schválené
* **EN:** Þingvellir National Park
* **SK:** Národný park Þingvellir
* *Kontext:* Google maps: https://maps.app.goo.gl/NLqnU4XAgKMEq2ei6 | Group: Names of viewpoint cutscenes

### [Položka 19] ID: `828702` | `is_cut_barthastran`
- [x] Schválené
* **EN:** Barðastrandarvegur
* **SK:** Barðastrandarvegur
* *Kontext:* Google maps: https://maps.app.goo.gl/EWGNbjLNkPh1x4R57 | Group: Names of viewpoint cutscenes

### [Položka 20] ID: `828704` | `is_cut_lagoon`
- [x] Schválené
* **EN:** Lagoon Spa
* **SK:** Kúpele Lagoon
* *Kontext:* Google maps: https://maps.app.goo.gl/GX5PTyWYZqH3r4XY8 | Group: Names of viewpoint cutscenes

### [Položka 21] ID: `828706` | `is_cut_selfoss`
- [x] Schválené
* **EN:** Selfoss
* **SK:** Selfoss
* *Kontext:* Google maps: https://maps.app.goo.gl/sBbYdt5EPeBMpTsE9 | Group: Names of viewpoint cutscenes

### [Položka 22] ID: `828708` | `is_cut_seljaland`
- [x] Schválené
* **EN:** Seljalandsfoss Waterfall
* **SK:** Vodopád Seljalandsfoss
* *Kontext:* Google maps: https://maps.app.goo.gl/5YGYHMu9mBBDnWyo9 | Group: Names of viewpoint cutscenes

### [Položka 23] ID: `828710` | `is_cut_geyser`
- [x] Schválené
* **EN:** Strokkur Geyser
* **SK:** Gejzír Strokkur
* *Kontext:* Google maps: https://maps.app.goo.gl/1Ri72WVFY19fPSud6 | Group: Names of viewpoint cutscenes

### [Položka 24] ID: `828712` | `is_cut_gullfoss`
- [x] Schválené
* **EN:** Gullfoss Waterfall
* **SK:** Vodopád Gullfoss
* *Kontext:* Google maps: https://maps.app.goo.gl/RCjELWsBtoWu3t439 | Group: Names of viewpoint cutscenes

### [Položka 25] ID: `828714` | `is_cut_joekul`
- [x] Schválené
* **EN:** Jökulsárlón
* **SK:** Jökulsárlón
* *Kontext:* Google maps: https://maps.app.goo.gl/JQ92AcC1PMmxhckY9 | Group: Names of viewpoint cutscenes

### [Položka 26] ID: `828716` | `is_cut_gothafoss`
- [x] Schválené
* **EN:** Goðafoss
* **SK:** Vodopád Goðafoss
* *Kontext:* Google maps: https://maps.app.goo.gl/M9u9bGwdw5GTLXH9A | Group: Names of viewpoint cutscenes

### [Položka 27] ID: `828718` | `is_cut_metal`
- [x] Schválené
* **EN:** Húsavík Metal Processing Plant
* **SK:** Kovospracujúci závod Húsavík
* *Kontext:* Google maps: https://maps.app.goo.gl/aYpppQHdJ3g66X2H8 | Group: Names of viewpoint cutscenes

### [Položka 28] ID: `828720` | `is_cut_canyon`
- [x] Schválené
* **EN:** Stuðlagil Canyon
* **SK:** Kaňon Stuðlagil
* *Kontext:* Google maps: https://maps.app.goo.gl/Tc7Ckk5XutyknVrN7 | Group: Names of viewpoint cutscenes

### [Položka 29] ID: `828722` | `landmark_kirkjufell`
- [x] Schválené
* **EN:** Kirkjufell
* **SK:** Kirkjufell
* *Kontext:* Group: Names of landmarks

### [Položka 30] ID: `828724` | `landmark_hvita`
- [x] Schválené
* **EN:** Hvítá Bridge
* **SK:** Most cez rieku Hvítá
* *Kontext:* Group: Names of landmarks

### [Položka 31] ID: `828726` | `landmark_reykjavikopera`
- [x] Schválené
* **EN:** Reykjavík Opera
* **SK:** Opera v Reykjavíku
* *Kontext:* Group: Names of landmarks

### [Položka 32] ID: `828728` | `landmark_reynisfjall`
- [x] Schválené
* **EN:** Reynisfjall
* **SK:** Reynisfjall
* *Kontext:* Group: Names of landmarks

### [Položka 33] ID: `828730` | `landmark_isfjord`
- [x] Schválené
* **EN:** Stöðvarfjörður Fjord
* **SK:** Fjord Stöðvarfjörður
* *Kontext:* Group: Names of landmarks

### [Položka 34] ID: `828732` | `landmark_hverir`
- [x] Schválené
* **EN:** Hverir
* **SK:** Hverir
* *Kontext:* Group: Names of landmarks

### [Položka 35] ID: `828734` | `landmark_ismemorial`
- [x] Schválené
* **EN:** Stephan G. Stephansson Memorial
* **SK:** Pamätník Stephana G. Stephanssona
* *Kontext:* Group: Names of landmarks

### [Položka 36] ID: `828736` | `landmark_ischurch`
- [x] Schválené
* **EN:** Ísafjörður Church
* **SK:** Kostol v Ísafjörðure
* *Kontext:* Group: Names of landmarks

### [Položka 37] ID: `828740` | `badge_standard_chromed`
- [x] Schválené
* **EN:** Standard, Chromed
* **SK:** Štandardný, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 38] ID: `828744` | `bus_panel_led_destination_display`
- [x] Schválené
* **EN:** LED Destination Display
* **SK:** LED cieľový displej
* *Kontext:* Group: Accessory Names

### [Položka 39] ID: `828746` | `bus_panel_standard_destination_display`
- [x] Schválené
* **EN:** Standard Destination Display
* **SK:** Štandardný cieľový displej
* *Kontext:* Group: Accessory Names

### [Položka 40] ID: `828504` | `busbody_hd_137m_6x2_4`
- [x] Schválené
* **EN:** HD 13.7m, 6x2*4
* **SK:** HD 13.7m, 6x2*4
* *Kontext:* Group: Accessory Names

### [Položka 41] ID: `828748` | `carpet_standard_beige`
- [x] Schválené
* **EN:** Standard, Beige
* **SK:** Štandardný, béžový
* *Kontext:* Group: Accessory Names

### [Položka 42] ID: `828750` | `carpet_standard_blue`
- [x] Schválené
* **EN:** Standard, Blue
* **SK:** Štandardný, modrý
* *Kontext:* Group: Accessory Names

### [Položka 43] ID: `828752` | `carpet_standard_brown`
- [x] Schválené
* **EN:** Standard, Brown
* **SK:** Štandardný, hnedý
* *Kontext:* Group: Accessory Names

### [Položka 44] ID: `828754` | `carpet_standard_gray`
- [x] Schválené
* **EN:** Standard, Gray
* **SK:** Štandardný, sivý
* *Kontext:* Group: Accessory Names

### [Položka 45] ID: `828756` | `carpet_standard_green`
- [x] Schválené
* **EN:** Standard, Green
* **SK:** Štandardný, zelený
* *Kontext:* Group: Accessory Names

### [Položka 46] ID: `828760` | `codrv_seat_standard_black`
- [x] Schválené
* **EN:** Standard Black
* **SK:** Štandardné, čierne
* *Kontext:* Group: Accessory Names

### [Položka 47] ID: `828762` | `codrv_seat_standard_black_crew_seat`
- [x] Schválené
* **EN:** Standard Black + Crew Seat
* **SK:** Štandardné, čierne + sedadlo posádky
* *Kontext:* Group: Accessory Names

### [Položka 48] ID: `828764` | `curtains_fabric_beige`
- [x] Schválené
* **EN:** Beige
* **SK:** Béžové
* *Kontext:* Group: Accessory Names

### [Položka 49] ID: `828766` | `curtains_fabric_black`
- [x] Schválené
* **EN:** Black
* **SK:** Čierne
* *Kontext:* Group: Accessory Names

### [Položka 50] ID: `828768` | `curtains_fabric_blue`
- [x] Schválené
* **EN:** Blue
* **SK:** Modré
* *Kontext:* Group: Accessory Names

### [Položka 51] ID: `828770` | `curtains_fabric_brown`
- [x] Schválené
* **EN:** Brown
* **SK:** Hnedé
* *Kontext:* Group: Accessory Names

### [Položka 52] ID: `828772` | `curtains_fabric_gray`
- [x] Schválené
* **EN:** Gray
* **SK:** Sivé
* *Kontext:* Group: Accessory Names

### [Položka 53] ID: `828774` | `curtains_fabric_green`
- [x] Schválené
* **EN:** Green
* **SK:** Zelené
* *Kontext:* Group: Accessory Names

### [Položka 54] ID: `828776` | `curtains_fabric_orange`
- [x] Schválené
* **EN:** Orange
* **SK:** Oranžové
* *Kontext:* Group: Accessory Names

### [Položka 55] ID: `828778` | `curtains_fabric_red`
- [x] Schválené
* **EN:** Red
* **SK:** Červené
* *Kontext:* Group: Accessory Names

### [Položka 56] ID: `828780` | `curtains_fabric_yellow`
- [x] Schválené
* **EN:** Yellow
* **SK:** Žlté
* *Kontext:* Group: Accessory Names

### [Položka 57] ID: `828782` | `f_intake_bar_standard_chromed_glossy`
- [x] Schválené
* **EN:** Standard, Chromed & Glossy
* **SK:** Štandardná, chrómovaná a lesklá
* *Kontext:* Group: Accessory Names

### [Položka 58] ID: `828784` | `f_intake_standard_glossy`
- [x] Schválené
* **EN:** Standard Glossy
* **SK:** Štandardná, lesklá
* *Kontext:* Group: Accessory Names

### [Položka 59] ID: `828786` | `f_intake_standard_painted`
- [x] Schválené
* **EN:** Standard, Painted
* **SK:** Štandardná, lakovaná
* *Kontext:* Group: Accessory Names

### [Položka 60] ID: `828788` | `f_intake_standard_plastic`
- [x] Schválené
* **EN:** Standard, Plastic
* **SK:** Štandardná, plastová
* *Kontext:* Group: Accessory Names

### [Položka 61] ID: `828790` | `f_light_standard_led`
- [x] Schválené
* **EN:** Standard, LED
* **SK:** Štandardné, LED
* *Kontext:* Group: Accessory Names

### [Položka 62] ID: `828792` | `f_light_standard_xenon`
- [x] Schválené
* **EN:** Standard, Xenon
* **SK:** Štandardné, xenónové
* *Kontext:* Group: Accessory Names

### [Položka 63] ID: `828794` | `f_logo_standard_chromed`
- [x] Schválené
* **EN:** Standard, Chromed
* **SK:** Štandardné, chrómované
* *Kontext:* Group: Accessory Names

### [Položka 64] ID: `828796` | `f_wnd_frame_standard_glossy`
- [x] Schválené
* **EN:** Standard, Glossy
* **SK:** Štandardný, lesklý
* *Kontext:* Group: Accessory Names

### [Položka 65] ID: `828798` | `f_wnd_frame_standard_painted`
- [x] Schválené
* **EN:** Standard, Painted
* **SK:** Štandardný, lakovaný
* *Kontext:* Group: Accessory Names

### [Položka 66] ID: `828800` | `fcover_man_chromed`
- [x] Schválené
* **EN:** MAN, Chromed
* **SK:** MAN, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 67] ID: `828802` | `fcover_man_paintable`
- [x] Schválené
* **EN:** MAN, Paintable
* **SK:** MAN, lakovateľný
* *Kontext:* Group: Accessory Names

### [Položka 68] ID: `828804` | `fcover_scania_chromed`
- [x] Schválené
* **EN:** Scania, Chromed
* **SK:** Scania, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 69] ID: `828806` | `fcover_volvo_chromed`
- [x] Schválené
* **EN:** Volvo, Chromed
* **SK:** Volvo, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 70] ID: `828808` | `fcover_volvo_special_2026`
- [x] Schválené
* **EN:** Volvo Special 2026
* **SK:** Volvo Special 2026
* *Kontext:* Group: Accessory Names

### [Položka 71] ID: `828810` | `fcover_volvo_special_2026_paintable`
- [x] Schválené
* **EN:** Volvo Special 2026, Paintable
* **SK:** Volvo Special 2026, lakovateľný
* *Kontext:* Group: Accessory Names

### [Položka 72] ID: `828812` | `fhub_absolute_fury_black_edition`
- [x] Schválené
* **EN:** Absolute Fury, Black
* **SK:** Absolute Fury, čierny
* *Kontext:* Group: Accessory Names

### [Položka 73] ID: `828814` | `fhub_elite_rider`
- [x] Schválené
* **EN:** Elite Rider
* **SK:** Elite Rider
* *Kontext:* Group: Accessory Names

### [Položka 74] ID: `828816` | `fhub_night_star`
- [x] Schválené
* **EN:** Night Star
* **SK:** Night Star
* *Kontext:* Group: Accessory Names

### [Položka 75] ID: `828818` | `fhub_synergy`
- [x] Schválené
* **EN:** Synergy
* **SK:** Synergy
* *Kontext:* Group: Accessory Names

### [Položka 76] ID: `828820` | `fhub_titan`
- [x] Schválené
* **EN:** Titan
* **SK:** Titan
* *Kontext:* Group: Accessory Names

### [Položka 77] ID: `828822` | `fhub_titan_painted`
- [x] Schválené
* **EN:** Titan, Painted
* **SK:** Titan, lakovaný
* *Kontext:* Group: Accessory Names

### [Položka 78] ID: `828824` | `fnuts_scania`
- [x] Schválené
* **EN:** Scania
* **SK:** Scania
* *Kontext:* Group: Accessory Names

### [Položka 79] ID: `828826` | `intlight_bgr_blue`
- [x] Schválené
* **EN:** Blue
* **SK:** Modré
* *Kontext:* Group: Accessory Names

### [Položka 80] ID: `828828` | `intlight_bgr_green`
- [x] Schválené
* **EN:** Green
* **SK:** Zelené
* *Kontext:* Group: Accessory Names

### [Položka 81] ID: `828830` | `intlight_bgr_orange`
- [x] Schválené
* **EN:** Orange
* **SK:** Oranžové
* *Kontext:* Group: Accessory Names

### [Položka 82] ID: `828832` | `intlight_bgr_violet`
- [x] Schválené
* **EN:** Violet
* **SK:** Fialové
* *Kontext:* Group: Accessory Names

### [Položka 83] ID: `828834` | `intlight_bgr_warm`
- [x] Schválené
* **EN:** Warm
* **SK:** Teplé biele
* *Kontext:* Group: Accessory Names

### [Položka 84] ID: `828836` | `intlight_bgr_yellow`
- [x] Schválené
* **EN:** Yellow
* **SK:** Žlté
* *Kontext:* Group: Accessory Names

### [Položka 85] ID: `828838` | `mirror_camera_plastic`
- [x] Schválené
* **EN:** Camera, Plastic
* **SK:** Plastové s kamerou
* *Kontext:* Group: Accessory Names

### [Položka 86] ID: `828842` | `mirror_standard_fully_painted`
- [x] Schválené
* **EN:** Standard, Fully Painted
* **SK:** Štandardné, celolakované
* *Kontext:* Group: Accessory Names

### [Položka 87] ID: `828848` | `p_seats_fabric_black`
- [x] Schválené
* **EN:** Fabric, Black
* **SK:** Látkové, čierne
* *Kontext:* Group: Accessory Names

### [Položka 88] ID: `828850` | `p_seats_fabric_blue`
- [x] Schválené
* **EN:** Fabric, Blue
* **SK:** Látkové, modré
* *Kontext:* Group: Accessory Names

### [Položka 89] ID: `828852` | `p_seats_fabric_diamond_brown`
- [x] Schválené
* **EN:** Fabric, Brown Diamonds
* **SK:** Látkové, hnedé diamantové vzory
* *Kontext:* Group: Accessory Names

### [Položka 90] ID: `828854` | `p_seats_fabric_diamond_red`
- [x] Schválené
* **EN:** Fabric, Red Diamonds
* **SK:** Látkové, červené diamantové vzory
* *Kontext:* Group: Accessory Names

### [Položka 91] ID: `828856` | `p_seats_fabric_gray_red`
- [x] Schválené
* **EN:** Fabric, Gray Red
* **SK:** Látkové, sivo-červené
* *Kontext:* Group: Accessory Names

### [Položka 92] ID: `828858` | `p_seats_fabric_green`
- [x] Schválené
* **EN:** Fabric, Green
* **SK:** Látkové, zelené
* *Kontext:* Group: Accessory Names

### [Položka 93] ID: `828860` | `p_seats_fabric_lines`
- [x] Schválené
* **EN:** Leather, Lines
* **SK:** Kožené, linky
* *Kontext:* Group: Accessory Names

### [Položka 94] ID: `828862` | `p_seats_fabric_orange_gray`
- [x] Schválené
* **EN:** Fabric, Orange Gray
* **SK:** Látkové, oranžovo-sivé
* *Kontext:* Group: Accessory Names

### [Položka 95] ID: `828864` | `p_seats_fabric_red`
- [x] Schválené
* **EN:** Fabric, Red
* **SK:** Látkové, červené
* *Kontext:* Group: Accessory Names

### [Položka 96] ID: `828866` | `p_seats_fabric_waves`
- [x] Schválené
* **EN:** Leather, Waves
* **SK:** Kožené, vlny
* *Kontext:* Group: Accessory Names

### [Položka 97] ID: `828868` | `p_seats_leather_black`
- [x] Schválené
* **EN:** Leather, Black
* **SK:** Kožené, čierne
* *Kontext:* Group: Accessory Names

### [Položka 98] ID: `828870` | `p_seats_leather_orange`
- [x] Schválené
* **EN:** Leather, Orange
* **SK:** Kožené, oranžové
* *Kontext:* Group: Accessory Names

### [Položka 99] ID: `828872` | `p_seats_leather_stripes_black`
- [x] Schválené
* **EN:** Leather, Black Stripes
* **SK:** Kožené, čierne pruhy
* *Kontext:* Group: Accessory Names

### [Položka 100] ID: `828874` | `r_logo_basic`
- [x] Schválené
* **EN:** Basic
* **SK:** Základné
* *Kontext:* Group: Accessory Names

### [Položka 101] ID: `828876` | `r_logo_standard`
- [x] Schválené
* **EN:** Standard
* **SK:** Štandardné
* *Kontext:* Group: Accessory Names

### [Položka 102] ID: `828878` | `r_logo_standard_chromed`
- [x] Schválené
* **EN:** Standard, Chromed
* **SK:** Štandardné, chrómované
* *Kontext:* Group: Accessory Names

### [Položka 103] ID: `828880` | `r_panel_standard_glossy`
- [x] Schválené
* **EN:** Standard, Black
* **SK:** Štandardný, čierny
* *Kontext:* Group: Accessory Names

### [Položka 104] ID: `828882` | `r_panel_standard_painted`
- [x] Schválené
* **EN:** Standard, Painted
* **SK:** Štandardný, lakovaný
* *Kontext:* Group: Accessory Names

### [Položka 105] ID: `828884` | `rcover_man_chromed`
- [x] Schválené
* **EN:** MAN, Chromed
* **SK:** MAN, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 106] ID: `828886` | `rcover_man_painted`
- [x] Schválené
* **EN:** MAN, Painted
* **SK:** MAN, lakovaný
* *Kontext:* Group: Accessory Names

### [Položka 107] ID: `828888` | `rcover_scania_chromed`
- [x] Schválené
* **EN:** Scania, Chromed
* **SK:** Scania, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 108] ID: `828890` | `rcover_volvo_chromed`
- [x] Schválené
* **EN:** Volvo, Chromed
* **SK:** Volvo, chrómovaný
* *Kontext:* Group: Accessory Names

### [Položka 109] ID: `828892` | `tank_2x205_l`
- [x] Schválené
* **EN:** 2x 205 l
* **SK:** 2x 205 l
* *Kontext:* Group: Accessory Names

### [Položka 110] ID: `828894` | `tank_3x205_l`
- [x] Schválené
* **EN:** 3x 205 l
* **SK:** 3x 205 l
* *Kontext:* Group: Accessory Names

### [Položka 111] ID: `828896` | `tank_4x205_l`
- [x] Schválené
* **EN:** 4x 205 l
* **SK:** 4x 205 l
* *Kontext:* Group: Accessory Names

### [Položka 112] ID: `828898` | `tank_525_l`
- [x] Schválené
* **EN:** 525 l
* **SK:** 525 l
* *Kontext:* Group: Accessory Names

### [Položka 113] ID: `828900` | `tank_525_l_185_l`
- [x] Schválené
* **EN:** 525 l + 185 l
* **SK:** 525 l + 185 l
* *Kontext:* Group: Accessory Names

### [Položka 114] ID: `828940` | `transmission_ishift_at2812d`
- [x] Schválené
* **EN:** I-Shift AT2812D
* **SK:** I-Shift AT2812D
* *Kontext:* Group: Accessory Names

### [Položka 115] ID: `828942` | `transmission_ishift_at2812d_r`
- [x] Schválené
* **EN:** I-Shift AT2812D R
* **SK:** I-Shift AT2812D R
* *Kontext:* Group: Accessory Names

### [Položka 116] ID: `828944` | `transmission_ishift_at2812g`
- [x] Schválené
* **EN:** I-Shift AT2812G
* **SK:** I-Shift AT2812G
* *Kontext:* Group: Accessory Names

### [Položka 117] ID: `828946` | `transmission_ishift_at2812g_r`
- [x] Schválené
* **EN:** I-Shift AT2812G R
* **SK:** I-Shift AT2812G R
* *Kontext:* Group: Accessory Names

### [Položka 118] ID: `828948` | `transmission_ishift_ato3512d`
- [x] Schválené
* **EN:** I-Shift ATO3512D
* **SK:** I-Shift ATO3512D
* *Kontext:* Group: Accessory Names

### [Položka 119] ID: `828950` | `transmission_ishift_ato3512d_r`
- [x] Schválené
* **EN:** I-Shift ATO3512D R
* **SK:** I-Shift ATO3512D R
* *Kontext:* Group: Accessory Names

### [Položka 120] ID: `828952` | `transmission_ishift_ato3512f`
- [x] Schválené
* **EN:** I-Shift ATO3512F
* **SK:** I-Shift ATO3512F
* *Kontext:* Group: Accessory Names

### [Položka 121] ID: `828954` | `transmission_ishift_ato3512f_aso_ulc`
- [x] Schválené
* **EN:** I-Shift ATO3512F + ASO-ULC
* **SK:** I-Shift ATO3512F + ASO-ULC
* *Kontext:* Group: Accessory Names

### [Položka 122] ID: `828956` | `transmission_ishift_ato3512f_r`
- [x] Schválené
* **EN:** I-Shift ATO3512F R
* **SK:** I-Shift ATO3512F R
* *Kontext:* Group: Accessory Names

### [Položka 123] ID: `828958` | `transmission_ishift_ato3512f_r_aso_ulc`
- [x] Schválené
* **EN:** I-Shift ATO3512F R + ASO-ULC
* **SK:** I-Shift ATO3512F R + ASO-ULC
* *Kontext:* Group: Accessory Names

### [Položka 124] ID: `828960` | `transmission_ishift_ato3812g`
- [x] Schválené
* **EN:** I-Shift ATO3812G
* **SK:** I-Shift ATO3812G
* *Kontext:* Group: Accessory Names

### [Položka 125] ID: `828962` | `transmission_ishift_ato3812g_aso_ulc`
- [x] Schválené
* **EN:** I-Shift ATO3812G + ASO-ULC
* **SK:** I-Shift ATO3812G + ASO-ULC
* *Kontext:* Group: Accessory Names

### [Položka 126] ID: `828964` | `transmission_ishift_ato3812g_r`
- [x] Schválené
* **EN:** I-Shift ATO3812G R
* **SK:** I-Shift ATO3812G R
* *Kontext:* Group: Accessory Names

### [Položka 127] ID: `828966` | `transmission_ishift_ato3812g_r_aso_ulc`
- [x] Schválené
* **EN:** I-Shift ATO3812G R + ASO-ULC
* **SK:** I-Shift ATO3812G R + ASO-ULC
* *Kontext:* Group: Accessory Names

### [Položka 128] ID: `828904` | `transmission_opticruise_grso_895`
- [x] Schválené
* **EN:** Opticruise GRSO 895
* **SK:** Opticruise GRSO 895
* *Kontext:* Group: Accessory Names

### [Položka 129] ID: `828906` | `transmission_opticruise_grso_895r`
- [x] Schválené
* **EN:** Opticruise GRSO 895R
* **SK:** Opticruise GRSO 895R
* *Kontext:* Group: Accessory Names

### [Položka 130] ID: `828908` | `transmission_zf_ecolife_2_r`
- [x] Schválené
* **EN:** ZF EcoLife 2 R
* **SK:** ZF EcoLife 2 R
* *Kontext:* Group: Accessory Names

### [Položka 131] ID: `828910` | `warnsticker_dead_angle_warning`
- [x] Schválené
* **EN:** Dead Angle Warning
* **SK:** Výstražná nálepka mŕtveho uhla
* *Kontext:* Group: Accessory Names

### [Položka 132] ID: `828558` | `bus_passengers_sound`
- [x] Schválené
* **EN:** Coach passengers
* **SK:** Zvuky cestujúcich v autobuse
* *Kontext:* Checkbox enabling the sounds of the passengers during bus jobs. | Group: Options/Audio | Screen used to configure audio related options.

### [Položka 133] ID: `828560` | `bus_passengers_sound_op_tooltip`
- [x] Schválené
* **EN:** Enables sounds of the passengers on board your coach.
* **SK:** Povolí zvuky cestujúcich na palube tvojho autobusu.
* *Kontext:* Group: Tooltips. | Group: Options/Audio | Screen used to configure audio related options.

### [Položka 134] ID: `33886` | `oversize_escort_crash_player_failure_dialog_text`
- [x] Schválené
* **EN:** You've damaged the escort vehicle.<br>You can load your previous position or cancel the delivery with a penalty of $MONEY$.
* **SK:** Poškodil si sprievodné vozidlo.<br>Môžeš načítať predchádzajúcu pozíciu alebo zrušiť prepravu s pokutou $MONEY$.
* *Kontext:* Text showed when player will hit the escort vehicle and oversized cargo delivery is over because of that. | Group: Strings related to special missions and the whole project of ovs.

### [Položka 135] ID: `828562` | `description_ram_1500_2025`
- [x] Schválené
* **EN:** The RAM 1500 hauls like a truck but drives like a car, pairing pickup strength with smooth and responsive steering.
* **SK:** RAM 1500 uvezie náklad ako nákladiak, no jazdí ako osobné auto, spája silu pick-upu s plynulým a citlivým riadením.
* *Kontext:* Group: Garage & Shop - car descriptions

### [Položka 136] ID: `828564` | `description_dodge_charger_1970`
- [x] Schválené
* **EN:** Bold, broad, and born for the spotlight, the Charger earned muscle-car legend status on the street and immortality on the silver screen.
* **SK:** Sebavedomý, robustný a stvorený pre žiaru reflektorov, Charger si na ulici vydobyl status legendy medzi muscle cars a na filmovom plátne nesmrteľnosť.
* *Kontext:* Group: Garage & Shop - car descriptions

### [Položka 137] ID: `828566` | `description_dodge_viper_gts_2002`
- [x] Schválené
* **EN:** Pure and raw to the core, the Viper punishes the heavy-footed without mercy, rewarding only the patient driver who treats its power with respect.
* **SK:** Číry a neotesaný až do špiku kostí, Viper neúprosne trestá ťažkú nohu na plyne a odmeňuje len trpezlivého vodiča, ktorý pristupuje k jeho výkonu s rešpektom.
* *Kontext:* Group: Garage & Shop - car descriptions

### [Položka 138] ID: `828568` | `description_dodge_challenger_srt_2023`
- [x] Schválené
* **EN:** Classic roots in a modern and powerful package, the Challenger keeps its timeless shape while riding with the ease of a contemporary car.
* **SK:** Klasické korene v modernom a výkonnom balení, Challenger si zachováva svoj nadčasový tvar, pričom ponúka pohodlnú jazdu moderného auta.
* *Kontext:* Group: Garage & Shop - car descriptions

### [Položka 139] ID: `828356` | `poi_ne1_01`
- [x] Schválené
* **EN:** Museum on the Fur Trade
* **SK:** Múzeum obchodu s kožušinami
* *Kontext:* Group: Nebraska TBs and POIs localization.

### [Položka 140] ID: `828376` | `poi_ne2_01`
- [x] Schválené
* **EN:** Museum on the Fur Trade
* **SK:** Múzeum obchodu s kožušinami
* *Kontext:* Group: Nebraska TBs and POIs localization.

### [Položka 141] ID: `828392` | `poi_ne2_04`
- [x] Schválené
* **EN:** Sentinels of the Prairie
* **SK:** Strážcovia prérie
* *Kontext:* Group: Nebraska TBs and POIs localization.

### [Položka 142] ID: `828570` | `tb_mo1`
- [x] Schválené
* **EN:** The Ozark Plateau
* **SK:** Plošina Ozark
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 143] ID: `828572` | `tb_mo1_desc`
- [x] Schválené
* **EN:** Forested hills, hidden caves and clear rivers: the Ozarks tell a story of people reshaping the land to fit their needs. A dam turned the Osage River into a sprawling lake, and beneath Springfield, humans took over where water left off, carving limestone into subterranean warehouses.
* **SK:** Zalesnené kopce, skryté jaskyne a priezračné rieky: pohorie Ozark rozpráva príbeh ľudí, ktorí pretvorili krajinu podľa svojich potrieb. Priehrada premenila rieku Osage na rozľahlé jazero a pod Springfieldom človek pokračoval tam, kde voda skončila, a vytesal do vápenca podzemné sklady.
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 144] ID: `828574` | `poi_mo1_01`
- [x] Schválené
* **EN:** Lake of the Ozarks
* **SK:** Jazero Ozarks
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 145] ID: `828576` | `poi_mo1_01_desc`
- [x] Schválené
* **EN:** Lake of the Ozarks winds through the hills for over 90 miles, with more shoreline than the coast of California. Built to generate power, it quickly became one of the Midwest's favorite getaways, and today its coves are lined with homes, marinas and resorts.
* **SK:** Jazero Ozarks sa kľukatí pomedzi kopce viac ako 90 míľ a jeho pobrežie je dlhšie než celé pobrežie Kalifornie. Pôvodne vzniklo na výrobu elektriny, no rýchlo sa stalo jedným z najobľúbenejších dovolenkových miest Stredozápadu a dnes sú jeho zátoky posiate domami, prístavmi a rekreačnými strediskami.
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 146] ID: `828578` | `poi_mo1_02`
- [x] Schválené
* **EN:** Bagnell Dam
* **SK:** Priehrada Bagnell
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 147] ID: `828580` | `poi_mo1_02_desc`
- [x] Schválené
* **EN:** Completed in 1931 after about two years of mostly hand labor, Bagnell Dam stretches nearly half a mile across the Osage River. It still generates electricity, but its real impact was economic, bringing jobs during the Great Depression and turning a quiet river valley into a vacation destination.
* **SK:** Priehrada Bagnell bola dokončená v roku 1931 po približne dvoch rokoch prevažne ručnej práce a cez rieku Osage sa tiahne takmer pol míle. Dodnes vyrába elektrinu, no jej skutočný význam bol hospodársky. Počas Veľkej hospodárskej krízy priniesla pracovné miesta a tiché riečne údolie premenila na dovolenkovú destináciu.
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 148] ID: `828582` | `poi_mo1_03`
- [x] Schválené
* **EN:** Rolla Stonehenge
* **SK:** Rolla Stonehenge
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 149] ID: `828584` | `poi_mo1_03_desc`
- [x] Schválené
* **EN:** Built by Rolla's engineering university to show off its waterjet technology, this half-scale Stonehenge was cut from 160 tons of granite in about a month. Dedicated on the 1984 summer solstice, it still works as a solar clock beside historic Route 66.
* **SK:** Túto zmenšenú polovičnú repliku Stonehenge postavila technická univerzita v Rolle, aby predviedla svoju technológiu rezania vodným lúčom. Zo 160 ton žuly ju vyrezali za približne mesiac. Odhalená bola počas letného slnovratu v roku 1984 a popri historickej Route 66 dodnes funguje ako slnečné hodiny.
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 150] ID: `828586` | `poi_mo1_04`
- [x] Schválené
* **EN:** Mark Twain National Forest
* **SK:** Národný les Marka Twaina
* *Kontext:* Group: Missouri TBs and POIs localization.

---

## 2. Coach Mode – Garáž, Prehliadač, Úrovne vodiča a Zručnosti

### [Položka 151] ID: `828588` | `poi_mo1_04_desc`
- [x] Schválené
* **EN:** Named after Missouri writer Mark Twain, this forest grew back under federal protection once logging had stripped the hills bare by the 1920s. Today its 1.5 million acres of woods, rivers and hundreds of caves stretch across more counties than any other national forest in the US.
* **SK:** Tento les, pomenovaný po spisovateľovi z Missouri Markovi Twainovi, vyrástol nanovo pod federálnou ochranou po tom, čo ťažba dreva v 20. rokoch 20. storočia úplne odlesnila tunajšie kopce. Dnes sa jeho 1,5 milióna akrov lesov, riek a stoviek jaskýň rozprestiera naprieč viacerými okresmi než akýkoľvek iný národný les v USA.
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 152] ID: `828590` | `poi_mo1_05`
- [x] Schválené
* **EN:** Springfield Underground
* **SK:** Podzemie Springfield
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 153] ID: `828592` | `poi_mo1_05_desc`
- [x] Schválené
* **EN:** Beneath Springfield, hundreds of trucks drive into the tunnels of a former limestone mine every day. Its warehouses, about two-thirds the size of Vatican City, stay naturally cool all year, making them ideal for storing food.
* **SK:** Pod mestom Springfield vchádzajú stovky nákladných áut každý deň do tunelov bývalej vápencovej bane. Jej sklady, veľké približne ako dve tretiny Vatikánu, si celoročne udržiavajú prirodzený chlad, vďaka čomu sú ideálne na skladovanie potravín.
* *Kontext:* Group: Missouri TBs and POIs localization.

### [Položka 154] ID: `828594` | `tb_ks1`
- [x] Schválené
* **EN:** The High Plains
* **SK:** Náhorné plošiny High Plains
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 155] ID: `828596` | `tb_ks1_desc`
- [x] Schválené
* **EN:** Stagecoaches, cattle drives and cowboys once ruled the High Plains of western Kansas. When the railroad arrived, towns sprang up along the tracks and the prairie gave way to endless wheat fields and towering grain elevators. Today, wind turbines rise into a sky that seems to go on forever.
* **SK:** Dostavníky, honci dobytka a kovboji kedysi vládli náhorným plošinám High Plains v západnom Kansase. Po príchode železnice vyrástli pozdĺž tratí mestá a préria ustúpila nekonečným pšeničným poliam a mohutným obilným silám. Dnes sa k nekonečnej oblohe týčia veterné turbíny.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 156] ID: `828598` | `ks_cut_monument_rocks_desc`
- [x] Schválené
* **EN:** Some 80 million years ago, an inland sea covered Kansas. Today, its chalky seabed rises up to 70 feet above the prairie, rich in fossils of giant marine reptiles. These towers once guided stagecoaches heading west and became Kansas's first National Natural Landmark in 1968.
* **SK:** Pred približne 80 miliónmi rokov pokrývalo Kansas vnútrozemské more. Dnes sa jeho kriedové morské dno týči až 70 stôp nad prériou a ukrýva bohaté nálezy skamenelín obrovských morských plazov. Tieto skalné veže kedysi slúžili ako orientačný bod pre dostavníky smerujúce na západ a v roku 1968 sa stali prvou národnou prírodnou pamiatkou Kansasu.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 157] ID: `828600` | `ks_cut_mount_sunflower_desc`
- [x] Schválené
* **EN:** Mount Sunflower is the highest point in Kansas, yet you could easily drive past it. The land rises so gently that the summit barely stands out. It sits on a family ranch near the Colorado border, marked by a sunflower sculpture made of railroad spikes.
* **SK:** Hora Sunflower je najvyšším bodom Kansasu, no ľahko by ste ho minuli bez povšimnutia. Terén stúpa tak pozvoľna, že vrchol takmer vôbec nevyniká. Nachádza sa na rodinnom ranči neďaleko hraníc s Coloradom a označuje ho socha slnečnice vyrobená zo železničných klincov.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 158] ID: `828602` | `poi_ks1_01`
- [x] Schválené
* **EN:** Colby
* **SK:** Colby
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 159] ID: `828604` | `poi_ks1_01_desc`
- [x] Schválené
* **EN:** Since I-70 reached Colby in 1965, this farming town has been a welcome stop on the open prairie, living up to its nickname, the Oasis on the Plains. Its frontier and farming history is reflected in the Cooper Barn, the largest in Kansas, and the Prairie Museum, which chronicles High Plains life.
* **SK:** Odkedy diaľnica I-70 v roku 1965 dorazila do Colby, toto poľnohospodárske mestečko je vítanou zastávkou na otvorenej prérii a napĺňa svoju prezývku Oáza na rovinách. Jeho priekopnícku a farmársku históriu pripomína Cooper Barn, najväčšia stodola v Kansase a Múzeum prérie, ktoré zachytáva život na náhorných plošinách High Plains.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 160] ID: `828606` | `poi_ks1_02`
- [x] Schválené
* **EN:** Buffalo Dunes Wind Project
* **SK:** Veterný park Buffalo Dunes
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 161] ID: `828608` | `poi_ks1_02_desc`
- [x] Schválené
* **EN:** Where buffalo once roamed, 135 wind turbines now rise above the plains southwest of Garden City. Since 2013, the Buffalo Dunes Wind Project has turned the steady Kansas wind into enough electricity for about 65,000 homes, most of it bound for Alabama.
* **SK:** Tam, kde sa kedysi preháňali bizóny, sa dnes juhozápadne od Garden City týči nad rovinami 135 veterných turbín. Od roku 2013 premieňa veterný park Buffalo Dunes stály kansaský vietor na dostatok elektriny pre približne 65 000 domácností, z čoho väčšina smeruje do Alabamy.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 162] ID: `828610` | `poi_ks1_03`
- [x] Schválené
* **EN:** Dodge City Railway Station
* **SK:** Železničná stanica Dodge City
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 163] ID: `828612` | `poi_ks1_03_desc`
- [x] Schválené
* **EN:** Dodge City owes its Wild West fame to the railroad that brought cattle drives and cowboys to town. Built in 1898, its Santa Fe depot is the largest surviving one in Kansas. Still a working train station, it also houses a theater and stands on a street named after Old West lawman Wyatt Earp.
* **SK:** Mesto Dodge City vďačí za svoju slávu z čias Divokého západu železnici, ktorá doň priviedla honcov dobytka a kovbojov. Železničná stanica spoločnosti Santa Fe, postavená v roku 1898, je najväčšou dochovanou stanicou v Kansase. Dodnes slúži vlakom, ukrýva aj divadlo a stojí na ulici pomenovanej po legendárnom šerifovi Wyattovi Earpovi.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 164] ID: `828614` | `poi_ks1_04`
- [x] Schválené
* **EN:** Decatur County Fairgrounds
* **SK:** Výstavisko okresu Decatur
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 165] ID: `828616` | `poi_ks1_04_desc`
- [x] Schválené
* **EN:** On the High Plains, neighbors can live miles apart, and since the 1870s county fairs have given Kansas farm families a reason to gather. In Oberlin, the Decatur County Fairgrounds carry on that tradition with rides, games and local produce that draw folks in from across the county.
* **SK:** Na plošinách High Plains žijú susedia často na míle ďaleko od seba a už od 70. rokov 19. storočia dávali okresné jarmoky kansaským farmárskym rodinám dôvod stretnúť sa. V mestečku Oberlin udržiava výstavisko okresu Decatur túto tradíciu kolotočmi, hrami a miestnymi plodinami, ktoré lákajú ľudí z celého okresu.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 166] ID: `828618` | `poi_ks1_05`
- [x] Schválené
* **EN:** Hays
* **SK:** Hays
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 167] ID: `828620` | `poi_ks1_05_desc`
- [x] Schválené
* **EN:** From frontier fort to college town, Hays has kept its past close. Where Wild Bill Hickok once kept the peace, the largest city in northwestern Kansas now pairs a lively brick downtown with a museum whose most famous fossil shows a fish that swallowed another whole.
* **SK:** Od pohraničnej pevnosti po univerzitné mestečko si Hays uchováva svoju minulosť. Tam, kde kedysi dohliadal na poriadok Wild Bill Hickok, spája dnes najväčšie mesto severozápadného Kansasu rušné tehlové centrum s múzeom, ktorého najslávnejšia fosília zobrazuje rybu, ktorá prehltla inú rybu v celku.
* *Kontext:* Group: Kansas TBs and POIs localization.

### [Položka 168] ID: `828622` | `tb_co1`
- [x] Schválené
* **EN:** The Western Slope
* **SK:** Západné svahy Colorada
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 169] ID: `828624` | `tb_co1_desc`
- [x] Schválené
* **EN:** West of the Continental Divide, the Rockies give way to towering peaks, deep canyons and red desert mesas. Silver and gold once drew miners into the San Juan Mountains, and the railroads and cliffside roads built to reach them still carry travelers through some of America's wildest terrain.
* **SK:** Západne od Kontinentálneho rozvodia ustupujú Skalnaté vrchy týčiacim sa štítom, hlbokým kaňonom a červeným púštnym stolovým horám. Striebro a zlato kedysi privábili baníkov do pohoria San Juan a železnice či útesové cesty postavené v tých časoch dodnes vedú cestovateľov jedným z najdivokejších terénov Ameriky.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 170] ID: `828626` | `poi_co1_01`
- [x] Schválené
* **EN:** Uncompahgre National Forest
* **SK:** Národný les Uncompahgre
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 171] ID: `828628` | `poi_co1_01_desc`
- [x] Schválené
* **EN:** From aspen-covered mesas to peaks over 14,000 feet, Uncompahgre National Forest spans nearly a million acres around Ouray and Telluride. The forest takes its name from the Ute people, whose word described the area's red, mineral-rich springs.
* **SK:** Od stolových hôr porastených osikami až po štíty prevyšujúce 14 000 stôp sa Národný les Uncompahgre rozprestiera na takmer milióne akrov v okolí Ouray a Telluride. Les nesie meno indiánskeho kmeňa Ute, ktorého slovo pôvodne opisovalo tunajšie červené pramene bohaté na minerály.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 172] ID: `828630` | `poi_co1_02`
- [x] Schválené
* **EN:** Ouray Historical Hotel
* **SK:** Historický hotel v Ouray
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 173] ID: `828632` | `poi_co1_02_desc`
- [x] Schválené
* **EN:** Built in 1886 at the height of Ouray's gold boom, this grand hotel was meant to impress wealthy mine investors. Its skylit rotunda, rosewood paneling and oak staircase once greeted royalty and presidents. After decades boarded up, it was restored and once again welcomes visitors to the San Juans.
* **SK:** Tento veľkolepý hotel, postavený v roku 1886 na vrchole zlatej horúčky v Ouray, mal zapôsobiť na bohatých banských investorov. Jeho presvetlená rotunda, obloženie z palisandrového dreva a dubové schodisko kedysi vítali kráľovské návštevy aj prezidentov. Po desaťročiach chátrania bol zrekonštruovaný a opäť víta návštevníkov pohoria San Juan.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 174] ID: `828634` | `co_cut_mil_desc`
- [x] Schválené
* **EN:** Built as a toll road for mining wagons in the 1880s, the Million Dollar Highway still clings to the cliffs of the Uncompahgre Gorge. Hairpin turns and sheer drops lead over Red Mountain Pass at 11,018 feet, earning it a reputation as one of America's most dangerous roads.
* **SK:** Cesta Million Dollar Highway, postavená v 80. rokoch 19. storočia ako spoplatnená trasa pre banské povozy, sa dodnes drží útesov rokliny Uncompahgre Gorge. Ostré zákruty a strmé zrázy vedú cez priesmyk Red Mountain Pass vo výške 11 018 stôp, vďaka čomu si vyslúžila povesť jednej z najnebezpečnejších ciest v Amerike.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 175] ID: `828636` | `poi_co1_03`
- [x] Schválené
* **EN:** Chimney Rock
* **SK:** Skalný útvar Chimney Rock
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 176] ID: `828638` | `poi_co1_03_desc`
- [x] Schválené
* **EN:** Chimney Rock towers over a ridge west of Pagosa Springs, where Ancestral Puebloans built more than 150 structures around 1,000 years ago. They were likely drawn by a rare sight: about every 18 years, the moon rises between Chimney Rock and its smaller neighbor, Companion Rock.
* **SK:** Skalný útvar Chimney Rock sa týči nad hrebeňom západne od Pagosa Springs, kde pred približne 1 000 rokmi postavili predkovia Pueblanov viac ako 150 stavieb. Pravdepodobne ich prilákal vzácny úkaz: približne každých 18 rokov vychádza mesiac presne medzi Chimney Rock a menšou susednou skalou Companion Rock.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 177] ID: `828640` | `poi_co1_04`
- [x] Schválené
* **EN:** Grand Valley
* **SK:** Údolie Grand Valley
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 178] ID: `828642` | `poi_co1_04_desc`
- [x] Schválené
* **EN:** The Grand Valley takes its name from the Grand River, as the upper Colorado River was known until 1921. Today, I-70 follows the river through orchards and vineyards, past the towering Book Cliffs and into Grand Junction, the largest city on the Western Slope.
* **SK:** Údolie Grand Valley je pomenované po rieke Grand River, ako sa horný tok rieky Colorado nazýval až do roku 1921. Dnes diaľnica I-70 sleduje rieku pomedzi sady a vinice popod mohutné útesy Book Cliffs až do Grand Junction, najväčšieho mesta oblasti Western Slope.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 179] ID: `828644` | `poi_co1_05`
- [x] Schválené
* **EN:** Durango
* **SK:** Durango
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 180] ID: `828646` | `poi_co1_05_desc`
- [x] Schválené
* **EN:** Durango was born with the railroad in 1880 and has never let go of it. Steam trains still climb the Animas Canyon to Silverton on a ledge barely wider than the tracks, while the historic downtown, framed by red cliffs and mountain peaks, keeps its Old West charm.
* **SK:** Mesto Durango vzniklo spolu so železnicou v roku 1880 a nikdy sa jej nevzdalo. Parné vlaky dodnes stúpajú kaňonom Animas do Silvertonu po rímse sotva širšej než samotné koľajnice, zatiaľ čo historické centrum lemované červenými útesmi a horskými štítmi si zachováva svoje čaro Divokého západu.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 181] ID: `828648` | `co_cut_wolf_desc`
- [x] Schválené
* **EN:** US 160 follows Wolf Creek Valley up into the San Juans, crossing the Continental Divide at 10,857 feet. Known for some of the heaviest snowfall in Colorado, the pass has tested drivers for over a century, and even inspired a 1975 trucker song about a runaway rig on its steep grades.
* **SK:** Cesta US 160 sleduje údolie Wolf Creek Valley nahor do pohoria San Juan a prekonáva Kontinentálne rozvodie vo výške 10 857 stôp. Priesmyk, známy jedným z najhustejších snežení v Colorade, preveruje vodičov už vyše storočia a v roku 1975 dokonca inšpiroval kamionistickú pieseň o neovládateľnom kamióne na jeho strmých klesaniach.
* *Kontext:* Group: Colorado TBs and POIs localization.

### [Položka 182] ID: `828650` | `tb_la1`
- [x] Schválené
* **EN:** The Cajun Country
* **SK:** Krajina Cajun Country
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 183] ID: `828652` | `tb_la1_desc`
- [x] Schválené
* **EN:** Explore the bayou country of south Louisiana, where the Mississippi winds past historic plantations and vast cypress swamps. Shaped by French, Creole and Cajun traditions, this land of water, music and spice stretches from Baton Rouge to New Orleans and the Gulf coast.
* **SK:** Preskúmajte močaristú krajinu južnej Louisiany, kde sa Mississippi kľukatí okolo historických plantáží a rozsiahlych cyprusových močiarov. Tento kraj vody, hudby a korenia, formovaný francúzskymi, kreolskými a cajunskými tradíciami, sa tiahne od Baton Rouge až po New Orleans a pobrežie Mexického zálivu.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 184] ID: `828654` | `poi_la1_01`
- [x] Schválené
* **EN:** Morganza Spillway
* **SK:** Priepust Morganza Spillway
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 185] ID: `828656` | `poi_la1_01_desc`
- [x] Schválené
* **EN:** The Morganza Spillway, completed in 1954, is a flood-control structure on the Mississippi River. Its 125 gated openings can divert part of the river's flow into the Atchafalaya Basin, protecting Baton Rouge and New Orleans from catastrophic floods.
* **SK:** Protipovodňový priepust Morganza Spillway, dokončený v roku 1954, je ochranná stavba na rieke Mississippi. Jeho 125 stavidlových otvorov dokáže odkloniť časť toku rieky do panvy Atchafalaya Basin a ochrániť tak mestá Baton Rouge a New Orleans pred katastrofálnymi záplavami.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 186] ID: `828658` | `landmark_la_capitols_desc`
- [x] Schválené
* **EN:** Completed in 1852, the Gothic Revival Old Louisiana State Capitol rises above the Mississippi like a medieval castle. Designed by James Dakin, it once housed the state government and today is home to the Museum of Political History, with a stained-glass dome inside.
* **SK:** Budova Old Louisiana State Capitol v neogotickom štýle, dokončená v roku 1852, sa týči nad riekou Mississippi ako stredoveký hrad. Navrhol ju James Dakin a kedysi v nej sídlila vláda štátu. Dnes v nej nájdete Múzeum politických dejín s kupolou z farebného skla.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 187] ID: `828660` | `la_cut_atchafalaya_desc`
- [x] Schválené
* **EN:** Interstate 10 crosses the Atchafalaya Basin on this 18-mile bridge, opened in 1973 and officially named the Louisiana Airborne Memorial Bridge. Raised above cypress swamps and bayous, it offers a rare view of one of America's largest wetlands.
* **SK:** Diaľnica Interstate 10 križuje panvu Atchafalaya Basin po tomto 18-míľovom moste, ktorý bol otvorený v roku 1973 a oficiálne nesie názov Louisiana Airborne Memorial Bridge. Most vyvýšený nad cyprusovými močiarmi a ramenami bayou ponúka nevšedný výhľad na jedny z najväčších mokradí v Amerike.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 188] ID: `828662` | `landmark_la_new_orleans_panorama_desc`
- [x] Schválené
* **EN:** New Orleans is defined by its position on the Mississippi, its French and Creole heritage and its music. Approaching on Interstate 10, the Caesars Superdome and the downtown towers rise above a port city famed as the birthplace of jazz, Mardi Gras and unique cuisine.
* **SK:** New Orleans definuje jeho poloha na rieke Mississippi, francúzske a kreolské dedičstvo a jeho hudba. Pri príchode po diaľnici Interstate 10 sa štadión Caesars Superdome a veže centra mesta týčia nad prístavným mestom presláveným ako kolíska džezu, osláv Mardi Gras a jedinečnej kuchyne.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 189] ID: `828664` | `poi_la1_02`
- [x] Schválené
* **EN:** Oak Alley Plantation
* **SK:** Plantáž Oak Alley
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 190] ID: `828666` | `poi_la1_02_desc`
- [x] Schválené
* **EN:** Built in 1839 for sugar planter Jacques Roman, Oak Alley Plantation is famous for its avenue of 28 live oaks, about 800 feet long, leading to a Greek Revival mansion.
* **SK:** Plantáž Oak Alley, postavená v roku 1839 pre pestovateľa cukrovej trstiny Jacquesa Romana, je známa svojou alejou 28 vždyzelených dubov viržínskych s dĺžkou približne 800 stôp, ktorá vedie k panskému sídlu v slohu gréckeho obrodenia.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 191] ID: `828668` | `la_cut_avery_island_desc`
- [x] Schválené
* **EN:** Avery Island, a salt dome rising above the Louisiana marshes, is where Edmund McIlhenny began making TABASCO sauce in 1868. The McIlhenny family still produces it here, aging pepper mash in oak barrels, and the island also holds Jungle Gardens and a bird sanctuary.
* **SK:** Ostrov Avery, soľný dóm týčiaci sa nad močiarmi Louisiany, je miestom, kde Edmund McIlhenny v roku 1868 začal vyrábať omáčku TABASCO. Rodina McIlhennyovcov ju tu vyrába dodnes, pričom paprikovú zmes necháva zrieť v dubových sudoch. Na ostrove sa nachádzajú aj záhrady Jungle Gardens a vtáčia rezervácia.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 192] ID: `828670` | `la_cut_houma_desc`
- [x] Schválené
* **EN:** Houma, seat of Terrebonne Parish, lies on Bayou Terrebonne in the heart of Louisiana's bayou country. Named after the Houma people, the city blends Cajun, French, Native and Creole traditions, and generations have made their living from shrimp, oysters and now offshore oil.
* **SK:** Houma, sídlo farnosti Terrebonne Parish, leží na ramene Bayou Terrebonne v srdci močaristého kraja Louisiany. Mesto pomenované po indiánskom kmeni Houma spája cajunské, francúzske, domorodé a kreolské tradície a celé generácie sa tu živili lovom kreviet, ustríc a v súčasnosti aj ťažbou ropy na mori.
* *Kontext:* Group: Louisiana TBs and POIs localization.

### [Položka 193] ID: `828672` | `la_cut_ponchatrain_bridge_desc`
- [x] Schválené
* **EN:** Stretching about 24 miles across Lake Pontchartrain, the Lake Pontchartrain Causeway consists of two parallel bridges, opened in 1956 and 1969. It holds the Guinness record for the longest continuous bridge over water and links Mandeville on the north shore with Metairie.
* **SK:** Most Lake Pontchartrain Causeway, tiahnuci sa približne 24 míľ cez jazero Lake Pontchartrain, pozostáva z dvoch paralelných mostov otvorených v rokoch 1956 a 1969. Drží Guinnessov rekord ako najdlhší súvislý most nad vodou a spája Mandeville na severnom brehu s mestom Metairie.
* *Kontext:* Group: Louisiana TBs and POIs localization.

---

## 3. Príslušenstvo kabíny, Diely, Prevodovky a Motory

---

## 4. Laky a Farby vozidiel (Paintjobs)

---

## 5. ATS Pamätihodnosti a Vyhliadky (Nebraska, Iowa, Texas, Oklahoma)

---

