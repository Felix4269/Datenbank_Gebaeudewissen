---
tags: [Norm, Beleuchtung, Elektrizität, SIA387-4, Gebäudetechnik, Licht, Energiebedarf]
normnummer: SN 565387/4:2023
gueltig_ab: "2023-08-01"
kapitel: "Kap. 3.3"
titel: "Berechnung – Volllaststunden (Methode 1)"
---
> ◀ [[03_2_Spezifische_Leistung|Kap. 3.2 Berechnung – Spezifische Leistung]]  ·  [[_SIA_387-4_2023_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_4_Stundenschritt_Methode2|Kap. 3.4 Berechnung – Stundenschritt (Methode 2)]] ▶

---

# Kap. 3.3 – Berechnung – Volllaststunden (Methode 1)

---

#### 3.3.1 Allgemein

Die vorliegende Norm beschreibt eine einfache Methode zur Ermittlung der Betriebszeiten von Beleuchtungsanlagen, die mit weniger Eingabe-Parametern auskommt als die europäische Norm SN EN 15193.

Die Volllaststunden für die Beleuchtung werden in zwei Schritten berechnet. In einem ersten Schritt werden unter Berücksichtigung des Typs der Beleuchtungssteuerung nach Tageslicht, der Sonnenschutzsteuerung und der baulichen Gegebenheiten die Volllaststunden für eine tägliche Nutzungszeit von 11 Stunden berechnet. In einem zweiten Schritt wird diese Zahl umgerechnet auf die Nutzungsstunden der effektiven Nutzung. Dabei werden auch die Reduktion der Volllaststunden durch die Beleuchtungssteuerung nach Präsenz sowie ein Gleichzeitigkeitsfaktor in Nutzungen mit sehr geringer Personenanwesenheit berücksichtigt.

---

#### 3.3.2 Volllaststunden pro Tag für eine Nutzungszeit von 11 Stunden

3.3.2.1 Die Volllaststunden pro Tag $t_{L,11}$ für eine Nutzungszeit von 11 Stunden sind gegeben durch:

$$t_{L,11} = \begin{cases} 0{,}5 \cdot (11\,\text{h} - t_{L,min}) \cdot \cos\!\left(\pi \cdot \dfrac{z_g}{z_{g0}}\right) + 0{,}5 \cdot (11\,\text{h} + t_{L,min}) & \text{für } z_g < z_{g0} \\ t_{L,min} & \text{für } z_g \geq z_{g0} \end{cases} \tag{5}$$

| Symbol | Bedeutung |
|---|---|
| $t_{L,min}$ | minimale Volllaststunden |
| $z_g$ | Glasflächenzahl (Verhältnis von Glas- zu Bodenfläche); bei Oberlichtern wird die doppelte Glasfläche eingesetzt |
| $z_{g0}$ | Wert der Glasflächenzahl, oberhalb welchem keine weitere Reduktion der Volllaststunden eintritt |

3.3.2.2 Der Wert von $z_{g0}$ ergibt sich aus:

$$z_{g0} = \max\left[0{,}175;\; 0{,}35 \cdot \left(0{,}375 + \frac{E_0}{800\,\text{lx}}\right)\right] \tag{6}$$

3.3.2.3 Der Wert von $t_{L,min}$ ergibt sich aus:

$$t_{L,min} = \min\left[11\,\text{h};\; 2\,\text{h} \cdot k_{ctr} \cdot k_{Re} \cdot k_T \cdot \max(k_{li};\, k_B) \cdot k_{sp} \cdot k_{sur}\right] \tag{7}$$

3.3.2.4 Der Korrekturfaktor Beleuchtungssteuerung nach Tageslicht $k_{ctr}$ beträgt:
$k_{ctr} = 1{,}0$ für Konstantlichtregelung mit LED-Lampen
$k_{ctr} = 1{,}1$ für Konstantlichtregelung mit Leuchtstofflampen
$k_{ctr} = 1{,}2$ – für automatische Ausschaltung und manuelle Einschaltung (halbautomatischer Betrieb)
– für automatische Ein/Aus-Schaltung (vollautomatischer Betrieb)
$k_{ctr} = 1{,}5$ für manuelle Schaltung mit zeitgesteuerter Ausschaltung
$k_{ctr} = 2{,}0$ für manuelle Schaltung

3.3.2.5 Der Korrekturfaktor Reflexionsgrad $k_{Re}$ beträgt:
$k_{Re} = 1{,}0$ für Standardkombination hell
$k_{Re} = 1{,}1$ für Standardkombination normal
$k_{Re} = 1{,}5$ für Standardkombination dunkel

3.3.2.6 Der Korrekturfaktor Transmissionsgrad $k_T$ beträgt:

$$k_T = \frac{0{,}7}{\tau_v}$$

$\tau_v$: Lichttransmissionsgrad der Verglasung (vgl. SN EN ISO 52022-1 und -3)

3.3.2.7 Der Korrekturfaktor Fenstersturz $k_{li}$ beträgt:

$$k_{li} = 0{,}8 + \frac{0{,}2\,\text{m}}{h_R - h_{li} - 1{,}8\,\text{m}} \tag{8}$$

$k_{li} = 1{,}8$ für $h_R - h_{li} < 2{,}0\,\text{m}$

| Symbol | Bedeutung |
|---|---|
| $h_R$ | Raumhöhe in m |
| $h_{li}$ | Höhe Fenstersturz in m |

3.3.2.8 Der Korrekturfaktor Balkon $k_B$ (Überhang) beträgt:

$$k_B = \frac{1}{1 - (0{,}25\,\text{m}^{-1} \cdot a_B)} \tag{9}$$

$k_B = 2{,}0$ für $a_B > 2{,}0\,\text{m}$

| Symbol | Bedeutung |
|---|---|
| $a_B$ | Balkontiefe in m |

3.3.2.9 Der Korrekturfaktor Sonnenschutz $k_{sp}$ ergibt sich durch Multiplikation der Teilfaktoren $k_{sp1}$ (Art des Sonnenschutzes) und $k_{sp2}$ (Typ der Sonnenschutzsteuerung): $k_{sp} = k_{sp1} \cdot k_{sp2}$.

Der Korrekturfaktor für die Art des Sonnenschutzes $k_{sp1}$ beträgt:
$k_{sp1} = 1{,}0$ helle Lamellen ($\rho$ mind. 70 %) oder lichtdurchlässiger Stoffbehang ($\tau$ mind. 25 %) mit Umlenksystem
$k_{sp1} = 1{,}1$ helle Lamellen ($\rho$ mind. 70 %) ohne Umlenksystem
$k_{sp1} = 1{,}2$ mittelhelle Lamellen ($\rho$ mind. 50 %) oder lichtdurchlässiger Stoffbehang ($\tau$ mind. 25 %)
$k_{sp1} = 1{,}3$ dunkle Lamellen oder wenig lichtdurchlässiger Stoffbehang ($\tau$ mind. 10 %)
$k_{sp1} = 1{,}4$ lichtundurchlässiger Stoffbehang

Der Korrekturfaktor für die Sonnenschutzsteuerung $k_{sp2}$ beträgt:
$k_{sp2} = 1{,}0$ motorbetrieben mit automatischer Steuerung und Lamellennachführung
$k_{sp2} = 1{,}1$ motorbetrieben mit automatischer Steuerung und Berücksichtigung der Verschattung; diese Funktion kann nur angewählt werden, wenn eine Verschattung vorliegt ($k_{sur} = 1{,}2$ oder $1{,}4$)
$k_{sp2} = 1{,}2$ motorbetrieben mit automatischer Steuerung
$k_{sp2} = 1{,}3$ motorbetrieben mit manueller Betätigung
$k_{sp2} = 1{,}4$ manuelle Betätigung

Wenn nachweislich kein Sonnenschutz notwendig ist, kann $k_{sp} = 1$ gesetzt werden.

3.3.2.10 Der Korrekturfaktor Horizontverschattung $k_{sur}$ beträgt:
$k_{sur} = 1{,}0$ Gebäudestandort mit freier Sicht, keine oder geringe Verschattung durch Umgebung
$k_{sur} = 1{,}2$ Gebäudestandort mit mittlerer Verschattung, Verbauungshöhenwinkel zwischen 15° und 35°
$k_{sur} = 1{,}4$ Gebäudestandort in der Stadt, grosse Verschattung durch Umgebung

**Figur 2** Einflussfaktoren des Tageslichts auf die jährliche Volllaststundenzahl einer Beleuchtungsanlage

![[Figur_2_Einflussfaktoren.png]]

---

#### 3.3.3 Volllaststunden für allgemeine Nutzungszeiten mit Berücksichtigung der Beleuchtungssteuerung nach Präsenz und des Gleichzeitigkeitsfaktors für schwach belegte Nutzungen

3.3.3.1 Die Volllaststunden $t_L$ ergeben sich durch:

$$t_L = k_{Pr} \cdot \frac{t_{L,11} \cdot t_{ud}}{11\,\text{h}} + t_{un} \cdot d_P \cdot f_P \cdot k_{si} \tag{10}$$

| Symbol | Bedeutung |
|---|---|
| $k_{Pr}$ | Korrekturfaktor Beleuchtungssteuerung nach Präsenz |
| $t_{L,11}$ | Volllaststunden bei einer Nutzungszeit von 11 Stunden, in h/a |
| $t_{ud}$ | Nutzungsstunden Tag (7 h bis 18 h) |
| $t_{un}$ | Nutzungsstunden Nacht (18 h bis 7 h) |
| $d_P$ | Nutzungstage pro Jahr |
| $f_P$ | Jahresgleichzeitigkeit |
| $k_{si}$ | Korrekturfaktor Gleichzeitigkeit |

In SIA 2024 sind Standardannahmen für die Nutzungsstunden Tag und Nacht angegeben.

3.3.3.2 Beim Korrekturfaktor Beleuchtungssteuerung nach Präsenz wird zwischen Nutzungen mit dauernder Präsenz ($k_{Pr} = 1{,}0$), Nutzungen mit normaler Präsenz und Nutzungen mit sporadischer Präsenz unterschieden. Die Korrekturfaktoren hängen von drei Einflussgrössen ab (Funktionstyp, Nachlaufzeit, Grösse des Erfassungsbereichs).

3.3.3.3 Funktionstypen der Beleuchtungssteuerung nach Präsenz, siehe [[01_Begriffe_Definitionen|1.1.2.15]].

3.3.3.4 Nachlaufzeit des Präsenzmelders: Der Faktor ist umso kleiner (und damit die Einsparung grösser), je kürzer die Nachlaufzeit ist.

3.3.3.5 Der Korrekturfaktor $k_{Pr}$ für normale Präsenz hängt von Betriebsmodus und Nachlaufzeit ab.

**Tabelle 6** Korrekturfaktor Beleuchtungssteuerung nach Präsenz $k_{Pr}$

*Spalten 3–4: Normale Präsenz (NP) und dauernde Präsenz (DP); Spalten 5–6: Sporadische Präsenz (SP)*

| Funktionstyp | Nachlaufzeit Präsenzmelder | NP/DP manuell on, auto off | NP/DP auto on, auto off | SP manuell on, auto off | SP auto on, auto off |
|---|---|---|---|---|---|
| Vernetzte Sensor-Leuchten | Typisch 1 Minute | – | 0,4 | – | 0,2 |
| auto on-off oder manuell on / auto off | 1 Minute | 0,5 | 0,6 | 0,3 | 0,4 |
| auto on-off oder manuell on / auto off | 2 Minuten | 0,6 | 0,7 | 0,4 | 0,5 |
| auto on-off oder manuell on / auto off | 5 Minuten | 0,7 | 0,8 | 0,5 | 0,6 |
| Manuelles Schalten mit zeitgesteuertem Aus | – | 0,95 | – | 0,8 | – |
| Manuelles Schalten | – | 1 | – | – | – |

3.3.3.6 In Nutzungen mit sehr schwacher Personenfrequenz (z. B. Lager) oder mehreren, aber nicht gleichzeitig brennenden Leuchten (z. B. Betten- und Hotelzimmer) kommt ein zusätzlicher Gleichzeitigkeitsfaktor zur Anwendung, der die Volllaststundenzahl generell – auch ohne Einsatz von Präsenzmeldern – um 50 % reduziert. Die damit erreichten praxisnäheren Volllaststunden sollen falsche Gewichtungen dieser Räume in der energetischen Gesamtbetrachtung der Beleuchtung eines Gebäudes korrigieren.

3.3.3.7 Die Korrekturfaktoren für Beleuchtungssteuerung nach Präsenz $k_{Pr}$ und Gleichzeitigkeit $k_{si}$ sind abhängig von der Nutzung.

**Tabelle 7** Standardnutzungen nach SIA 2024 mit Präsenzart und Gleichzeitigkeitsfaktor $k_{si}$

| Nr. | Raumnutzung | Dauernde Präsenz* | Normale Präsenz | Sporadische Präsenz | $k_{si}$ |
|---|---|---|---|---|---|
| 1.01 | Wohnen MFH | | x | | 0,5 |
| 1.02 | Wohnen EFH | | x | | 0,5 |
| 2.01 | Hotelzimmer | x | | | 0,5 |
| 2.02 | Empfang, Lobby | x | | | 1 |
| 3.01 | Einzel-, Gruppenbüro | | x | | 1 |
| 3.02 | Grossraumbüro | | x | | 1 |
| 3.03 | Sitzungszimmer | | x | | 1 |
| 3.04 | Schalterhalle, Empfang | x | | | 1 |
| 4.01 | Schulzimmer | | x | | 1 |
| 4.02 | Lehrerzimmer | | x | | 1 |
| 4.03 | Bibliothek | | x | | 1 |
| 4.04 | Hörsaal | | x | | 1 |
| 4.05 | Schulfachraum | | x | | 1 |
| 5.01 | Lebensmittelverkauf | x | | | 1 |
| 5.02 | Fachgeschäft | x | | | 1 |
| 5.03 | Verkauf Möbel, Bau, Garten | x | | | 1 |
| 6.01 | Restaurant | | x | | 1 |
| 6.02 | Selbstbedienungsrestaurant | | x | | 1 |
| 6.03 | Küche zu Restaurant | x | | | 1 |
| 6.04 | Küche zu SB-Restaurant | x | | | 1 |
| 7.01 | Vorstellungsraum | x | | | 1 |
| 7.02 | Mehrzweckhalle | x | | | 1 |
| 7.03 | Ausstellungshalle | x | | | 1 |
| 8.01 | Bettenzimmer | x | | | 0,5 |
| 8.02 | Stationszimmer | x | | | 1 |
| 8.03 | Behandlungsraum | x | | | 1 |
| 9.01 | Produktion (grobe Arbeit) | x | | | 1 |
| 9.02 | Produktion (feine Arbeit) | x | | | 1 |
| 9.03 | Laborraum | x | | | 1 |
| 10.01 | Lagerhalle | | x | | 1 |
| 11.01 | Turnhalle | | x | | 1 |
| 11.02 | Fitnessraum | | x | | 1 |
| 11.03 | Schwimmhalle | | x | | 1 |
| 12.01 | Verkehrsfläche | | | x | 0,5 |
| 12.02 | Verkehrsfläche (24 h) | | | x | 0,5 |
| 12.03 | Treppenhaus | | | x | 0,5 |
| 12.04 | Nebenraum | | | x | 0,5 |
| 12.05 | Küche, Teeküche | | | x | 0,5 |
| 12.06 | WC, Bad, Dusche | | | x | 0,5 |
| 12.07 | WC | | | x | 0,5 |
| 12.08 | Garderobe, Dusche | | | x | 0,5 |
| 12.09 | Parkhaus | | | x | 0,5 |
| 12.10 | Wasch- und Trockenraum | | | x | 0,5 |
| 12.11 | Kühlraum | | | x | 0,5 |
| 12.12 | Serverraum | x | | | 0,5 |

\* Dauernde Präsenz bedeutet insbesondere, dass der Einsatz von Präsenzmeldern in vielen Fällen nicht sinnvoll ist und deshalb im Rechenmodell von SIA 387/4 in den bezeichneten Nutzungen nicht vorgegeben ist. Für diese Raumnutzungen gilt somit $k_{Pr} = 1$.

---

> ◀ [[03_2_Spezifische_Leistung|Kap. 3.2 Berechnung – Spezifische Leistung]]  ·  [[_SIA_387-4_2023_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_4_Stundenschritt_Methode2|Kap. 3.4 Berechnung – Stundenschritt (Methode 2)]] ▶

---
