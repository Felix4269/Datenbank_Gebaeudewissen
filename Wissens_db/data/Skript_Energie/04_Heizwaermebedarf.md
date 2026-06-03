---
tags: [Energie, Heizwärmebedarf, Wärmegewinne, Gebäudetechnik]
skript: "Energieflüsse im Gebäude"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "4"
---

> ◀ [[03_3_waermespeicherung|← Wärmespeicherung]] · [[_Skript_Energie_MOC|↑ MOC]] · [[05_Warmwasser|Wärmebedarf Warmwasser →]] ▶

---

# Energieflüsse im Gebäude – Kapitel 4: Heizwärmebedarf

## 4 Heizwärmebedarf
### 4.1 Begriffe
Für das Verständnis und die Berechnung des Heizwärmebedarfes muss Klarheit über die Begriffe bestehen. Diese Begriffe hängen mit den Wärmeströmen im Gebäude zusammen und sind am einfachsten mit dem Energieflussdiagramm in Abbildung 11 zu erklären.

![[abb11_energieflussdiagramm_mit_warmestromen_gema.jpg]]
*Abbildung 11: Energieflussdiagramm mit Wärmeströmen gemäss SIA 380/1*

**Legende zu Abbildung 11:**

| Symbol | Beschreibung |
|---|---|
| 1 | Systemgrenze Heizwärmebedarf |
| 2 | Systemgrenze Wärmebedarf für Warmwasser |
| 3 | Systemgrenze Heiz- und Warmwassersystem |
| 4 | Systemgrenze Gebäude |
| $E_{F,El}$ | Elektrizitätsbedarf für Beleuchtung und Betriebseinrichtungen |
| $E_{F,hww}$ | Endenergiebedarf für Heizung und Warmwasser |

Ganz rechts sind die Gesamtwärmeverluste ($Q_{tot}$) abgebildet, die Wärmeverluste durch Transmission ($Q_T$) und die Lüftungswärmeverluste ($Q_V$). Darunter, separat ist der Wärmebedarf Warmwasser ($Q_{WW}$) gezeigt. Von oben sind die solaren Wärmegewinne ($Q_s$) und die Wärmegewinne der Personen ($Q_{iP}$) dargestellt. Zusammen mit den Wärmegewinnen der Elektrizität ($Q_{iE}$, von links) d.h. der Abwärme Geräte und Beleuchtung, ergeben sich die internen Wärmegewinne ($Q_i$). Ein Teil der internen und solaren Gewinne ($Q_g$) ist nicht nutzbar (geht in der Darstellung wieder nach oben), weil die Wärme zu Zeiten oder in Räumen anfällt, in denen gerade kein Wärmebedarf besteht. Übrig bleiben die genutzten Wärmegewinne $Q_{ug}$.

Der Wärmebedarf, der dem Gebäude (Systemgrenze 1 und 2) zugeführt werden muss, um den Wärmebedarf zu decken, ist der Heizwärmebedarf ($Q_h$), sowie der Wärmebedarf für Warmwasser ($Q_{WW}$), was den Gesamtwärmebedarf für Heizung und Warmwasser ($Q_{hww}$) ergibt.

In Systemgrenze 3 ist die Wärmeerzeugung dargestellt. Unvermeidlich ist, dass sowohl bei der Wärmeerzeugung, bei der Speicherung und der Verteilung von Warmwasser und Heizwärme Verluste auftreten. Diese werden als Wärmeverluste des Heiz- und Warmwassersystems bezeichnet ($Q_L$). Heute zunehmend wird für die Wärmeerzeugung auch Umgebungswärme oder Abwärme genutzt. Diese gewonnene Umweltwärme wird $Q_r$ genannt. Von links bleibt, was dem Gebäude an Endenergie (gekaufte Energie) zugeführt werden muss, der Energiebedarf für Heizung und Warmwasser $E_{F,hww}$.

### 4.2 Vorschriften zum Heizwärmebedarf
> 📖 Simulation: [[01_4a_Heizlast_Systemnachweis|IDA ICE Tutorial – Heizlastermittlung & Systemnachweis SIA 380/1]]

In den Baugesetzen der Kantone wird als Systemanforderung der maximale Heizwärmebedarf eines neuen Gebäudes limitiert (Tabelle 4). Die Berechnung des Heizwärmebedarfs für den Wärmedämmnachweis erfolgt bei Standardnutzung. Der Heizwärmebedarf bei Standardnutzung hängt nur von der Wärmedämmung, der Gebäudegeometrie und der passiven Solarenergienutzung ab. Für jeden Neubau, aber auch für Umbauten, muss dieser Wert berechnet werden. Dies wird üblicherweise vom Bauphysiker, ev. aber auch vom Heizungsplaner oder vom Architekten durchgeführt. Die Berechnung erfolgt dabei nach SIA 380/1.

Als Ausnahme kann bei kleinen Gebäuden oder bei Umbauten nur einzelner Bauteile ein Wärmedämmnachweis mit Einzelanforderung mit der Angabe der U-Werte der Einzelbauteile geführt werden. Diese U-Werte müssen die definierten Grenzwerte einhalten.

Mit den Mustervorschriften der Kantone im Energiebereich (MuKEn) wird eine Vereinheitlichung dieser Vorschriften in der Schweiz angestrebt. Die Kantone sind aber frei, welche Elemente der MuKEn sie wann einführen, ausser dem ersten Teil, welcher obligatorisch ist.

*Tabelle 4: Grenzwerte für den Heizwärmebedarf pro Jahr von Neubauten, Umbauten und Umnutzungen (bei 8,5 °C Jahresmitteltemperatur) nach MuKEn 2014*

| Gebäudekategorie | $Q_{h,li0}$ (kWh/m²) | $\Delta Q_{h,li}$ (kWh/m²) | P (W/m²) | Umbau $Q_{h,li}$ (kWh/m²) |
|---|---|---|---|---|
| I Wohnen MFH | 14 | 16 | 20 | 1,5 · $Q_{h,li,Neubau}$ |
| II Wohnen EFH | 16 | 16 | 25 | 1,5 · $Q_{h,li,Neubau}$ |
| III Verwaltung | 16 | 21 | 25 | 1,5 · $Q_{h,li,Neubau}$ |
| IV Schulen | 18 | 18 | 20 | 1,5 · $Q_{h,li,Neubau}$ |
| V Verkauf | 13 | 16 | – | 1,5 · $Q_{h,li,Neubau}$ |
| VI Restaurants | 24 | 19 | – | 1,5 · $Q_{h,li,Neubau}$ |
| VII Versammlungslokale | 24 | 19 | – | 1,5 · $Q_{h,li,Neubau}$ |
| VIII Spitäler | 20 | 20 | – | 1,5 · $Q_{h,li,Neubau}$ |
| IX Industrie | 15 | 18 | – | 1,5 · $Q_{h,li,Neubau}$ |
| X Lager | 15 | 18 | – | 1,5 · $Q_{h,li,Neubau}$ |
| XI Sportbauten | 19 | 18 | – | 1,5 · $Q_{h,li,Neubau}$ |
| XII Hallenbäder | 19 | 25 | – | 1,5 · $Q_{h,li,Neubau}$ |

Der zulässige Heizenergiebedarf ergibt sich aus der nachfolgenden Berechnung nach Formel 3. Er ist vom Verhältnis der gedämmten Gebäudehüllfläche zur Energiebezugsfläche abhängig.

**Formel 3: Berechnung max. zulässiger Heizenergiebedarf**

$$Q_{h,li} = Q_{h,li0} + \Delta Q_{h,li} \cdot \frac{A_{th}}{A_E} \quad [\text{kWh/m}^2]$$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $Q_{h,li}$ | Grenzwert für den Heizwärmebedarf (total) | kWh/m² |
| $Q_{h,li0}$ | Basiswert für den Heizwärmebedarf | kWh/m² |
| $\Delta Q_{h,li}$ | Steigungsfaktor für den Heizwärmebedarf | kWh/m² |
| $A_{th}$ / $A_E$ | Gebäudehüllzahl | – |

Der Steigungsfaktor ist dabei so gewählt, dass Gebäude mit viel Aussenflächenanteil (kleine und wenig kompakte Gebäude) besser wärmegedämmt werden müssen.

### 4.3 Energiebezugsfläche
Die Energiebezugsfläche $A_E$ oder EBF ist die Summe aller ober- und unterirdischen Geschossflächen $A_{NGF}$, die innerhalb der thermischen Gebäudehülle (innerhalb des Wärmedämmperimeters) liegen und für deren Nutzung ein Beheizen und/oder Klimatisieren notwendig ist. Zur EBF zählen die Hauptnutzflächen, sowie Verkehrsflächen, Sanitärräume, Abstellräume kleiner 10 m² und Garderoben, sofern diese innerhalb der thermischen Gebäudehülle liegen. Bei abgeschrägten Räumen zählen die Flächen mit einer lichten Raumhöhe von mehr als 1 m zur EBF (Abbildung 12).
Die Energiebezugsfläche wird brutto gerechnet, d. h. mit den Aussenmassen des Gebäudes resp. der Räume und inkl. aller Innenwände, Schächte usw. Anders gesagt, sind die beheizten Nettogeschossflächen und die zugehörigen Konstruktionsflächen zu addieren.

Falls nur die beheizte Nettogeschossfläche eines Gebäudes bekannt ist (z. B. die vermietete Fläche), dann kann näherungsweise mit einem Faktor 1,1 bei Geschäftsbauten und 1,15 bis 1,2 bei Wohnbauten in die Bruttogeschossfläche umgerechnet werden, je nach Wandstärken.

![[abb12_definition_ae.jpg]]
*Abbildung 12: Definition von $A_E$ (rot)*

### 4.4 Gebäudehüllfläche
Die thermische Gebäudehüllfläche $A_{th}$ ist die äussere wärmegedämmte Fläche eines Gebäudes. Die thermische Gebäudehüllfläche wird an der Aussenseite der Aussenbauteile entlang des Wärmedämmperimeters gemessen.

In Ausnahmefällen, wo vor der wärmegedämmten Fassadenwand eine mit mehr als 10 cm freiem Abstand hinterlüftete, nicht dämmende äussere Verkleidung angebracht ist, wird der nächsten innenliegenden Oberfläche entlang gemessen.

Bauteile gegen aussen (gegen Aussenluft) werden ungewichtet mitgerechnet. Bei Bauteilen gegen Erde wird ebenfalls an der Aussenseite der Bauteile gemessen, wobei eine dicke Erdüberdeckung bei Dächern bis zu 20 cm mit zum Dach gezählt wird. Flächen gegen unbeheizte Räume werden ebenfalls aussen erfasst.

Sowohl für Flächen gegen Erdreich wie auch für Flächen gegen unbeheizt sind Reduktionsfaktoren anzuwenden, die nach den Bestimmungen in SIA 380/1 zu berechnen sind. Diese Reduktionsfaktoren sollen den geringeren Wärmefluss als gegen aussen berücksichtigen, aufgrund der höheren Temperaturen des Erdreiches oder der unbeheizten Räume.

Trennflächen eines Gebäudes zu beheizten Räumen eines anderen Hauses (z. B. zu einem angebauten Haus) werden nicht mitgezählt, resp. hier gilt ein Reduktionsfaktor von Null.

### 4.5 Berechnung des Heizwärmebedarfes
Die normgerechte Berechnung des Heizwärmebedarfes erfolgt gemäss den Normen SIA 380/1, SIA 380/2 sowie SIA 384.201 (Normheizlast). Für diese Berechnungen sind EDV-Programme auf dem Markt verfügbar. Gebäude können berechnet werden. Sie berechnen die solaren Gewinne sowie die internen Gewinne ($Q_i$) von Personen und elektrischen Anwendungen mit Standardnutzungen oder mit projektspezifisch definierten Nutzungsdaten. Mit Nutzungsfaktoren wird der nutzbare Anteil abgeschätzt. Diese Programme sind oft auch zur Berechnung von bauphysikalischen Grössen, insbesondere des U-Wertes, nutzbar.

Damit die Programme für Nachweise gegenüber den Baubehörden verwendet werden können, müssen sie über eine Anerkennung des Bundesamtes für Energie verfügen. Im Allgemeinen können die nötigen Nachweisformulare direkt ausgedruckt werden. Mit denselben Programmen und Formularen können meist auch Nachweise zur Erlangung des Minergie®-Labels erzeugt werden, welche auch von Standardwerten ausgehen.

Für Optimierungsrechnungen in der Planung können die bestbekannten Nutzungsdaten eingegeben werden, oder es werden Sensitivitätsuntersuchungen mit verschiedenen Nutzungsdaten erstellt. Falls bestehende Gebäude nachgerechnet werden, werden die effektiv vorhandenen Nutzungen ermittelt und mit den Eingaben ins Programm abgebildet.

### 4.6 Deckung des Heizwärmebedarfes
Der Heizwärmebedarf $Q_h$ ist gemäss Energiediagramm (Abbildung 11) der nicht durch Gewinne gedeckte Anteil der Gesamtwärmeverluste. Je tiefer die Verluste durch Transmission sind, das heisst je besser die Wärmedämmung ist, desto tiefer wird der Heizwärmebedarf. Ebenso können die Wärmeverluste der Lüftung mit dichter Bauweise, keiner übermässigen natürlichen oder mechanischen Lüftung und mit Wärmerückgewinnung reduziert werden. Dadurch reduziert sich der Heizwärmebedarf weiter. Zusätzlich reduzieren auch die nutzbaren Wärmegewinne den Heizwärmebedarf. Die internen Gewinne hängen von der Nutzung ab. Die Gewinne von Personen sind wenig beeinflussbar. Die Gewinne von elektrischen Anwendungen sollten minimiert werden, um den Stromverbrauch im Gebäude zu minimieren. Nur die solaren Gewinne können und sollen positiv beeinflusst werden. Grosse Fenster nach Süden und wenig Beschattung sowie hohe g-Werte im Winter, verbunden mit genügend Speichermasse im Gebäudeinneren, tragen zu hohen solaren Gewinnen bei. Falls die Gesamtwärmeverluste ähnlich gross sind wie die Gewinne, dann wird der Heizwärmebedarf klein, im besten Fall sogar fast null. Selbst dann ist in den meisten Fällen noch eine Heizmöglichkeit der Räume notwendig, um bei fehlender Sonne oder bspw. nach einem Wochenende zu kühle Räume wieder aufheizen zu können.

Der Heizwärmebedarf fällt in Abhängigkeit der Witterung, insbesondere der Aussentemperatur, an. Ab 10 °C bis 16 °C Tagesmitteltemperatur besteht in der Praxis kein Heizbedarf mehr, je nach Wärmedämmung, Wärmespeicherfähigkeit und internen Gewinnen. Letztere decken dann den Wärmebedarf zur Aufrechterhaltung der geforderten Innentemperatur. Bei minimalen Aussentemperaturen und dann besonders am Morgen ist die maximale Heizleistung erforderlich. Bei Sonnenschein reduziert sich der Heizwärmebedarf um die passiven Solargewinne. In der Praxis ergibt sich damit ein sehr stark und teilweise rasch schwankender Heizwärmebedarf mit seltenen Spitzenwerten.

Fast jedes Gebäude mit von Personen genutzten Räumen benötigt also ein Heizsystem, welches den Räumen individuell die noch nötige Heizwärme zuführen kann. Auch heutige, sehr gut gedämmte Gebäude oder selbst Nullheizenergiehäuser weisen zu gewissen Zeiten Räume auf, welche ohne weitere Wärmezufuhr zu kühl würden. Dies dann und dort, wo interne oder solare Gewinne fehlen, auch wenn diese Gewinne über die Heizperiode gesehen ausreichen würden, das Gebäude zu beheizen. In solchen Fällen kann man von einer Restwärme-Zufuhr sprechen, um diese Fälle von einer konventionellen, den ganzen Winter über in den meisten Räumen notwendigen Heizung zu unterscheiden.

Die Abbildung 13 und Abbildung 14 zeigen den aufgrund der Witterungsdaten für Kloten (Zürich) berechneten theoretischen Wärmebedarf unter Berücksichtigung von inneren und solaren Gewinnen und der Speicherfähigkeit des Gebäudes. (Berechnungen durch M. Hubbuch)

![[abb13_heizwaermebedarf_konventionell.png]]
*Abbildung 13: Theoretischer Heizwärmebedarf für ein konventionelles EFH mit wenig Speicherfähigkeit*

![[abb14_heizwaermebedarf_neu.png]]
*Abbildung 14: Theoretisch berechneter Heizwärmebedarf für ein neues EFH mit guter Speicherfähigkeit*


Die Speicherfähigkeit ist in der Praxis im Sommer wirksamer als hier vereinfacht berechnet, so dass z. B. ein neues, gut gedämmtes EFH im Sommer kaum je beheizt werden muss. Auch die Leistungsspitzen können in der Praxis etwas mehr gebrochen werden als hier berechnet. Trotz dieser Mängel in der Berechnung zeigen beide Abbildungen, was auch mit Messungen ermittelt werden kann: der Heizleistungsbedarf variiert sehr stark und rasch. Die Berechnungen erfolgten durch den Autor.

Um den Heizwärmebedarf den Anforderungen entsprechend jedem einzelnen Raum zuführen zu können, braucht es eine Wärmeerzeugungsanlage und eine Heizwärmeverteilung. Diese sind üblicherweise durch die Aussentemperatur gesteuert, mit Zeitprogramm für eine allfällige Nachtabsenkung.

Die Vorlauftemperatur wird in Abhängigkeit der Aussentemperatur geschoben, was mit der Heizkurve vorgegeben wird (Abbildung 15). Gut wärmegedämmte Gebäude und Gebäude mit Flächenheizungen benötigen wenig steile Heizkurven (max. 35 °C bei -10 °C aussen). Schlecht gedämmte Gebäude brauchen eine steilere Einstellung, was höhere Vorlauftemperaturen zur Folge hat (bis 60 °C bei -10 °C aussen). Eine Parallelverschiebung der Heizkurve hat generell höhere oder tiefere Raumtemperaturen zur Folge. In der Praxis sind Heizkurven oft zu hoch eingestellt. Dies hat einen unnötig hohen Heizenergiebedarf zur Folge.

Zusätzlich benötigt jeder Raum eine individuelle Steuerung der Wärmeabgabe. Am einfachsten und häufigsten erfolgt dies durch Thermostatventile pro Raum oder pro Heizkörper. Es kann auch ein von der Raumautomation oder selbst gesteuertes Motorventil vorhanden sein. Wichtig ist in jedem Fall eine raumweise und bedarfsabhängige Wärmeabgabe.

![[abb15_heizkurven_mit_unterschiedlicher_steigung_1.jpg]]
![[abb15_heizkurven_mit_unterschiedlicher_steigung_2.jpg]]
*Abbildung 15: Heizkurven mit unterschiedlicher Steigung (links) und Parallel-Verschiebung (rechts)*

---

> ◀ [[03_3_waermespeicherung|← Wärmespeicherung]] · [[_Skript_Energie_MOC|↑ MOC]] · [[05_Warmwasser|Wärmebedarf Warmwasser →]] ▶

---
