---
tags: [Norm, Beleuchtung, Elektrizität, SIA387-4, Gebäudetechnik, Licht, Energiebedarf]
normnummer: SN 565387/4:2023
gueltig_ab: "2023-08-01"
kapitel: "Kap. 3.4"
titel: "Berechnung – Jahresenergie im Stundenschritt (Methode 2)"
---
> ◀ [[03_3_Volllaststunden_Methode1|Kap. 3.3 Berechnung – Volllaststunden (Methode 1)]]  ·  [[_SIA_387-4_2023_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Anforderungen|Kap. 4 Anforderungen]] ▶

---

# Kap. 3.4 – Berechnung – Jahresenergie im Stundenschritt (Methode 2)

---

#### 3.4.1 Tageslichtstrom durch transparente Bauteile

Der Tageslichtstrom durch transparente Bauteile $\Phi_{dl}$ wird separat für direkte und diffuse Einstrahlung berechnet. Die Einstrahlungen werden gleichzeitig für die Berechnung der externen Wärmeeinträge benötigt und sind deshalb SIA 380/2 zu entnehmen.

$$\sum \Phi_{dl} = \sum_i A_{w,i} \cdot F_{F,i} \cdot 0{,}9 \cdot \left(I_{B,i} \cdot F_{dl,B} \cdot F_{s,B,i} \cdot \tau_{v,tot,B,i} + I_{D,i} \cdot F_{dl,D} \cdot F_{s,D,i} \cdot \tau_{v,tot,D,i}\right) \tag{11}$$

| Symbol | Bedeutung |
|---|---|
| $A_{w,i}$ | Fensterfläche des Bauteils $i$, in m² |
| $F_{F,i}$ | Verminderungsfaktor für den Rahmen für das Bauteil $i$ |
| $I_{B,i}$ | direkte Solarstrahlung auf der Fassade $i$, in W/m² |
| $F_{dl,B}$ | Tageslichtfaktor für Direktstrahlung: 125 lm/W |
| $F_{s,B,i}$ | Verschattungsfaktor für Direktstrahlung für das Bauteil $i$ (siehe [[03_4_Stundenschritt_Methode2|3.4.2]]) |
| $\tau_{v,tot,B,i}$ | gesamter Lichttransmissionsgrad für Direktstrahlung für das Bauteil $i$ (siehe [[03_4_Stundenschritt_Methode2|3.4.3.2]]) |
| $I_{D,i}$ | diffuse Solarstrahlung auf der Fassade $i$, in W/m² |
| $F_{dl,D}$ | Tageslichtfaktor für Diffusstrahlung: 115 lm/W |
| $F_{s,D,i}$ | Verschattungsfaktor für Diffusstrahlung für das Bauteil $i$ (siehe [[03_4_Stundenschritt_Methode2|3.4.2]]) |
| $\tau_{v,tot,D,i}$ | gesamter Lichttransmissionsgrad für Diffusstrahlung für das Bauteil $i$ (siehe [[03_4_Stundenschritt_Methode2|3.4.3.2]]) |

Bei Sonnenschutzvorrichtungen mit Umlenksystem (Kategorie 1 gemäss Tabelle 8) ist die Berechnung für die Teile mit und ohne Umlenkung separat vorzunehmen.

---

#### 3.4.2 Verschattungsfaktoren

Die Verschattungsfaktoren für Direkt- und Diffusstrahlung berechnen sich aus den Faktoren für Horizont, Überhang und Seitenblende:

$$F_{S,B} = F_{S1} \cdot F_{S2,B} \cdot F_{S3,B,l} \cdot F_{S3,B,r} \tag{12}$$

| Symbol | Bedeutung |
|---|---|
| $F_{S1}$ | Verschattungsfaktor Horizont (Topographie und andere Gebäude) |
| $F_{S2,B}$ | Verschattungsfaktor Überhang für direkte Strahlung |
| $F_{S3,B,l}$ | Verschattungsfaktor Seitenblende links für direkte Strahlung |
| $F_{S3,B,r}$ | Verschattungsfaktor Seitenblende rechts für direkte Strahlung |

$$F_{S,D} = F_{S2,D} \cdot F_{S3,D,l} \cdot F_{S3,D,r} \tag{13}$$

| Symbol | Bedeutung |
|---|---|
| $F_{S,D}$ | Verschattungsfaktor für diffuse Strahlung (Überhang) |
| $F_{S3,D,l}$ | Verschattungsfaktor Seitenblende links für diffuse Strahlung |
| $F_{S3,D,r}$ | Verschattungsfaktor Seitenblende rechts für diffuse Strahlung |

Sämtliche Teil-Verschattungsfaktoren werden auch für die Berechnung der externen Wärmeeinträge benötigt und sind der Berechnung nach SIA 380/2 zu entnehmen.

---

#### 3.4.3 Sonnenschutz

3.4.3.1 Der Sonnenschutz wird simultan mit der Berechnung der solaren Wärmeeinträge nach SIA 380/2 (sobald die totale Solarstrahlung $I_{G,i}$ auf der Fensterebene $i$ über den Grenzwert $I_{G,i,set}$ steigt) berücksichtigt.

3.4.3.2 Der gesamte Lichttransmissionsgrad $\tau_{v,tot}$ muss für jedes transparente Bauteil berechnet werden und hängt von der Qualität, dem Funktionstyp der Sonnenschutzsteuerung und vom Einstrahlwinkel ab.

$$\tau_{v,tot,B} = \frac{\tau_{v,G} \cdot \tau_{v,sp,B}}{1 - \rho_{v,G} \cdot \rho_{v,sp,B}} \cdot F_{sp,B,\beta} \cdot F_{sp,B,\delta} \tag{14}$$

| Symbol | Bedeutung |
|---|---|
| $\tau_{v,G}$ | Lichttransmissionsgrad der Verglasung |
| $\tau_{v,sp,B}$ | Lichttransmissionsgrad des Sonnenschutzes für direkte Strahlung |
| $\rho_{v,G}$ | Lichtreflexionsgrad der Verglasung |
| $\rho_{v,sp,B}$ | Lichtreflexionsgrad des Sonnenschutzes für direkte Strahlung |
| $F_{sp,B,\beta}$ | Korrekturfaktor des Lichttransmissionsgrades für direkte Strahlung für den Lamellwinkel |
| $F_{sp,B,\delta}$ | Korrekturfaktor des Lichttransmissionsgrades für direkte Strahlung für die Sonnenhöhe |

$$\tau_{v,tot,D} = \frac{\tau_{v,G} \cdot \tau_{v,sp,D}}{1 - \rho_{v,G} \cdot \rho_{v,sp,D}} \cdot F_{sp,D,\beta} \tag{15}$$

| Symbol | Bedeutung |
|---|---|
| $\tau_{v,sp,D}$ | Lichttransmissionsgrad des Sonnenschutzes für diffuse Strahlung |
| $\rho_{v,sp,D}$ | Lichtreflexionsgrad des Sonnenschutzes für diffuse Strahlung |
| $F_{sp,D,\beta}$ | Korrekturfaktor des Lichttransmissionsgrades für diffuse Strahlung für den Lamellen-Anstellwinkel |

3.4.3.3 Bei Stoffbehang sind $\tau_{v,sp,B}$ und $\tau_{v,sp,D}$ gleich $\tau_{v,sp}$.

3.4.3.4 Bei Stoffbehang und Sonnenschutzsteuerung Typ X = 1 oder 2 gemäss Tabelle 9 sind $F_{sp,B,\beta}$, $F_{sp,B,\delta}$ und $F_{sp,D,\beta} = 1$. Bei Typ X = 3 kann ein Ausstellen des Sonnenschutzes berücksichtigt werden und die Verschattungsfaktoren sind gemäss SN EN 14500 zu bestimmen.

3.4.3.5 Bei Lamellenstoren sind $\tau_{v,sp,B} = \tau_{v,B,45}$, $\rho_{v,sp,B} = \rho_{v,B,45}$ sowie $\tau_{v,sp,D} = \tau_{v,D,45}$ und $\rho_{v,sp,D} = \rho_{v,D,45}$ einzusetzen.

| Symbol | Bedeutung |
|---|---|
| $\tau_{v,B,45}$ | Lichttransmissionsgrad des Sonnenschutzes für direkte Strahlung in Arbeitsstellung (45°) bei Sonnenhöhe 45° gemäss SN EN 14500 |
| $\rho_{v,B,45}$ | Lichtreflexionsgrad des Sonnenschutzes für direkte Strahlung in Arbeitsstellung (45°) bei Sonnenhöhe 45° gemäss SN EN 14500 |
| $\tau_{v,D,45}$ | Lichttransmissionsgrad des Sonnenschutzes für diffuse Strahlung in Arbeitsstellung (45°) bei Sonnenhöhe 45° gemäss SN EN 14500 |
| $\rho_{v,D,45}$ | Lichtreflexionsgrad des Sonnenschutzes für diffuse Strahlung in Arbeitsstellung (45°) bei Sonnenhöhe 45° gemäss SN EN 14500 |

Dazu sind Herstellerangaben zu verwenden. Falls keine näheren Angaben vorliegen, sind abhängig von der Art des Sonnenschutzes gemäss [[03_3_Volllaststunden_Methode1|3.3.2.9]] die Werte von Tabelle 8 einzusetzen.

**Tabelle 8** Werte für die Berechnung des Transmissionsgrades des Sonnenschutzes

| Kategorie | Art des Sonnenschutzes | Umlenksystem | $\rho_v$ Material | $\tau_v$ Material | $\rho_v$ Verglasung |
|---|---|---|---|---|---|
| 1 | Lamellen, Lamellenwinkel konstant 0° im Umlenkbereich | ja | 0,7 | 0 | – |
| 1 | Stoffbehang, nicht aktiv im Umlenkbereich | ja | 0,5 | 0,25 | – |
| 2 | Lamellen | – | 0,7 | 0 | 0,125 |
| 3 | Lamellen | – | 0,5 | 0 | – |
| 3 | Stoffbehang | – | 0,35 | 0,25 | – |
| 4 | Lamellen | – | 0,3 | 0 | – |
| 4 | Stoffbehang | – | 0,25 | 0,1 | – |
| 5 | Stoffbehang | – | 0,2 | 0,05 | – |

3.4.3.6 Die Korrekturfaktoren des Lichttransmissionsgrades für den Lamellen-Anstellwinkel sind:

$$F_{sp,B,\beta} = 1 - \frac{\beta - 45°}{45°} \tag{16}$$

$$F_{sp,D,\beta} = -1{,}1 \cdot 10^{-6} \cdot \beta^3 - 5 \cdot 10^{-5} \cdot \beta^2 + 1{,}2 \tag{17}$$

3.4.3.7 Der Lamellen-Anstellwinkel in (16) und (17) wird für die drei Funktionstypen der Sonnenschutzsteuerung gemäss Tabelle 9 berechnet.

**Tabelle 9** Berechnung des Lamellen-Anstellwinkels für die drei Funktionstypen der Sonnenschutzsteuerung

| Funktionstyp | Typ (SIA 411) | Beschrieb | Berechnung des Lamellen-Anstellwinkels |
|---|---|---|---|
| Motorbetrieben mit manueller Betätigung | X = 1 | Die Lamellen gehen in Arbeitsposition 45° und werden mehr geschlossen, wenn Direktstrahlung eindringen würde. Sie werden nicht mehr zurückgestellt, wenn sie mehr geschlossen sind. | $\beta = \max(45°;\; 90° - 2\delta_{s,n};\; \beta_{h-1})$ (18) — $\beta_{h-1}$: Lamellen-Anstellwinkel der vorangehenden Stunde |
| Motorbetrieben mit automatischer Steuerung (mit oder ohne Berücksichtigung der Verschattung) | X = 2 | Die Lamellen gehen in Arbeitsposition 45° und werden mehr geschlossen, wenn Direktstrahlung eindringen würde. | $\beta = \max(45°;\; 90° - 2\delta_{s,n})$ (19) |
| Motorbetrieben mit automatischer Steuerung und Lamellennachführung | X = 3 | Die Lamellen gehen in die optimale Position, so dass keine Direktstrahlung eindringt. | $\beta = \max[0°;\; \min(90°;\; 90° - 2\delta_{s,n})]$ (20) |

3.4.3.8 Die orthogonale Sonnenhöhe $\delta_{s,n}$ ist:

$$\delta_{s,n} = \arctan\!\left(\frac{\tan \delta_s}{\cos \alpha_i}\right) \tag{21}$$

| Symbol | Bedeutung |
|---|---|
| $\delta_s$ | Sonnenhöhe |
| $\alpha_i$ | relatives Sonnenazimut gegenüber der Flächennormale |

3.4.3.9 Der Korrekturfaktor des Lichttransmissionsgrades für direkte Strahlung $F_{sp,B,\delta}$ für die Sonnenhöhe beträgt:

$$F_{sp,B,\delta} = 1 - 0{,}1 \cdot \frac{\delta_{s,n} - 45°}{20°} \tag{22}$$

---

#### 3.4.4 Beleuchtungsleistung

##### 3.4.4.1 Aktuelle stündliche Beleuchtungsleistung während der Einschaltdauer

Sie berechnet sich wie folgt:

$$P_{L,act} = p_L \cdot \left[A_{NGF,dl} \cdot F_{c,dl} + (A_{NGF} - A_{NGF,dl})\right] \cdot F_{c,Pr} \tag{23}$$

| Symbol | Bedeutung |
|---|---|
| $P_{L,act}$ | aktuelle stündliche Beleuchtungsleistung |
| $p_L$ | spezifische Leistung Beleuchtung, in W/m² |
| $A_{NGF,dl}$ | mit Tageslicht versorgte Nettogeschossfläche (siehe [[03_4_Stundenschritt_Methode2|3.4.4.3]]) |
| $F_{c,dl}$ | Faktor für Beleuchtungssteuerung nach Tageslicht (siehe [[03_4_Stundenschritt_Methode2|3.4.4.2]]) |
| $A_{NGF}$ | Nettogeschossfläche, in m² |
| $F_{c,Pr}$ | Faktor für Beleuchtungssteuerung nach Präsenz (siehe [[03_4_Stundenschritt_Methode2|3.4.4.4]]) |

In Raumbereichen, die ausserhalb der mit Tageslicht versorgten Nettogeschossfläche $A_{NGF,dl}$ liegen, bleiben somit die Leuchten eingeschaltet.

Die Einschaltdauer entspricht nutzungsspezifisch den Stunden mit $f_{P,h} > 0$ gemäss SIA 2024.

Wenn keine genaueren Angaben vorliegen, ist für die Raumbeleuchtung immer von automatischer Beleuchtungssteuerung nach Präsenz und Tageslicht auszugehen.

Die Akzentbeleuchtung ist während der Einschaltdauer immer eingeschaltet.

##### 3.4.4.2 Beleuchtungssteuerung nach Tageslicht

Die Faktoren für die Beleuchtungssteuerung nach Tageslicht werden gemäss Tabelle 10 bestimmt.

**Tabelle 10** Faktoren für Beleuchtungssteuerung nach Tageslicht

**Konstantlichtregelung mit LED-Lampen** (gemäss [[01_Begriffe_Definitionen|1.1.2.15]]):

$$F_{c,dl} = \max\!\left(1 - \frac{E_{dl}}{E_{vm}};\; 0\right) \tag{24}$$

**Manuelle Ein- und automatische Ausschaltung, für LED- und Leuchtstofflampen:**

$$F_{c,dl} = \begin{cases} 1 & \text{wenn } E_{dl} < (E_{vm} - \Delta E_{vm}) \\ 0 & \text{wenn } E_{dl} > E_{vm} \text{ und } F_{c,dl,h-1} = 1 \\ F_{c,dl,h-1} & \text{sonst} \end{cases} \tag{25}$$

**Konstantlichtregelung mit Leuchtstofflampen:**

$$F_{c,dl} = \max\!\left(1 - 0{,}8 \cdot \frac{E_{dl}}{E_{vm}};\; 0{,}2\right) \tag{26}$$

**Automatische Ein/Aus-Schaltung:**

$$F_{c,dl} = \begin{cases} 1 & \text{wenn } E_{dl} < E_{vm} \\ 0 & \text{sonst} \end{cases} \tag{27}$$

**Manuelle Ein/Aus-Schaltung mit zusätzlicher zeitgesteuerter Ausschaltung:**

$$F_{c,dl} = \begin{cases} 1 & \text{wenn } E_{dl} < E_{vm} \\ 0 & \text{wenn } [E_{dl} > (E_{vm} + \Delta E_{vm}) \text{ und } F_{c,dl,h-1} = 1] \\ & \text{oder } [E_{dl} > E_{vm} \text{ und } h \in \{10, 13, 16, 19\}] \\ F_{c,dl,h-1} & \text{sonst} \end{cases} \tag{28}$$

**Manuelle Ein/Aus-Schaltung:**

$$F_{c,dl} = \begin{cases} 1 & \text{wenn } E_{dl} < E_{vm} \\ 0 & \text{wenn } E_{dl} > (E_{vm} + \Delta E_{vm}) \text{ und } F_{c,dl,h-1} = 1 \\ F_{c,dl,h-1} & \text{sonst} \end{cases} \tag{29}$$

Die Schalthysterese beträgt $\Delta E_{vm} = 0{,}5 \cdot E_{vm}$.

##### 3.4.4.3 Verfügbares Tageslicht

Die Tageslichtnutzung wird für die Fläche $A_{NGF,dl}$ entlang den mit Fenstern versehenen Fassaden berücksichtigt. Die mit Tageslicht versorgte Fläche entspricht der Raumlänge mal der mit Tageslicht versorgten Raumtiefe. Diese beträgt:
– bei Sonnenschutzvorrichtungen mit Umlenksystem (Kategorie 1 gemäss Tabelle 8) bis maximal zur dreifachen lichten Raumhöhe,
– bei allen übrigen Sonnenschutzvorrichtungen bis maximal zur zweifachen lichten Raumhöhe.

Unter Berücksichtigung des Raumwirkungsgrades $\eta_R$ wird aus dem Verhältnis von Tageslichtstrom $\Phi_{dl}$ zu $A_{NGF,dl}$ die durchschnittliche Tageslichtbeleuchtungsstärke $E_{dl}$ berechnet:

$$E_{dl} = \frac{\eta_R \cdot \Phi_{dl}}{A_{NGF,dl}} \cdot (1 - 0{,}55 \cdot h_{li}) \tag{30}$$

| Symbol | Bedeutung |
|---|---|
| $h_{li}$ | Sturzhöhe, in m |

Der Raumwirkungsgrad $\eta_R$ wird gemäss [[03_2_Spezifische_Leistung|3.2.5.5]] berechnet, wobei für die Berechnung des Raumindexes die effektive Raumtiefe und die Distanz zwischen Bewertungsebene und Decke, sowie für die Faktoren $f_1$ und $f_2$ je nach Standardkombination der Reflexionsgrade die Werte für die Lichtverteilcharakteristik «indirekt» gemäss Tabelle 5 einzusetzen sind.

##### 3.4.4.4 Beleuchtungssteuerung nach Präsenz

Der Faktor für die Beleuchtungssteuerung nach Präsenz $F_{c,Pr}$ wird wie folgt berechnet:

$$F_{c,Pr} = f_{P,m} \cdot f_{P,h} + (1 - f_{P,m} \cdot f_{P,h}) \cdot k_{Pr} \cdot k_{si} \tag{31}$$

| Symbol | Bedeutung |
|---|---|
| $f_{P,m}$ | monatlicher Präsenzfaktor für Personen gemäss SIA 2024 |
| $f_{P,h}$ | stündlicher Präsenzfaktor für Personen gemäss SIA 2024 |
| $k_{Pr}$ | Korrekturfaktor Präsenzmelder gemäss Tabelle 6 und Fussnote (*) zu Tabelle 7 |
| $k_{si}$ | Korrekturfaktor für Gleichzeitigkeit gemäss Tabelle 7 |

---

> ◀ [[03_3_Volllaststunden_Methode1|Kap. 3.3 Berechnung – Volllaststunden (Methode 1)]]  ·  [[_SIA_387-4_2023_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Anforderungen|Kap. 4 Anforderungen]] ▶

---
