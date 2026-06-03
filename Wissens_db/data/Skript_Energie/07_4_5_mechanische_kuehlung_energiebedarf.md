---
tags: [Energie, Heizwärmebedarf, Wärmegewinne, Gebäudetechnik]
skript: "Energieflüsse im Gebäude"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "7.4–7.5"
titel: "Mechanische Kühlung und Energiebedarf Kühlung/Lüftung"
---

> ◀ [[07_3_freie_kuehlung|← Freie Kühlung]] · [[_Skript_Energie_MOC|↑ MOC]] · [[08_Anhang|Anhang →]] ▶

---

# Energieflüsse im Gebäude – Kap. 7.4–7.5: Mechanische Kühlung und Energiebedarf

### 7.4 Mechanische Kühlung
> 📖 Vertiefung: [[03_2_mechanische_lueftung|Lüftung Kap. 3.2 – Mechanische Lüftung & Kühlung]]  ·  Simulation: [[_NEST_Sprint_MOC|NEST Sprint – Parameter cooling_capacity_offices (Run 002)]]

Um Kälte mit ganzjährig tiefen Temperaturen zu erzeugen, ist meistens eine Kältemaschine und
damit eine mechanische Kühlung erforderlich. Mit der mechanischen Kälteerzeugung besteht die
Möglichkeit, fast beliebig tiefe Temperaturen (bis ca. -50 °C) zu erreichen und die Leistung zu
steuern. Nachteilig ist der Energiebedarf für den Antrieb der Kältemaschine, im Allgemeinen
handelt es sich dabei um elektrischen Strom. Näheres siehe Skript Kältetechnik.
### 7.5 Energiebedarf Kühlung und Lüftung
#### Energiebedarf Kühlung
Infolge der Speichereffekte der Wärme sind manuelle Berechnungen des Kühlenergiebedarfs
schwierig. Um einigermassen genaue Resultate zu erhalten muss mit Simulationsprogrammen
gerechnet werden, die in Stundenschritten die Energieflüsse, Temperaturen und den
Kühlenergiebedarf rechnen.
Vereinfacht können die internen und externen Lasten in einem Raum überschlagsmässig
berechnet werden. Wie die internen Gewinne im Winter sind auch die internen Lasten im Sommer
bestehend aus der sensiblen Abwärme der Personen (ca. 80 W pro Person), die Abwärme der
Beleuchtung und der Abwärme der Geräte. Über den Tag gerechnet muss im Sommer etwa diese Energie auch wieder abgeführt werden. Bei der heutigen gut wärmegedämmten Bauweise ist der
"natürliche" Wärmeabfluss über Transmission und Fugenlüftung vernachlässigbar.
Die Kühlleistung ergibt sich aus der maximalen Leistung der aus den Räumen abzuführenden
Last, reduziert um einen Faktor für den Speichereffekt. Bei gut speichernden Räumen (massive
Bauweise) kann dabei angenommen werden, dass die Last entweder über 24 h abgeführt werden
kann oder sogar nur nachts über z. B. freie Kühlung.
Der genaue und für Planungen verbindliche Berechnungsgang ist in der SIA-Norm 382/2
Thermischer Energie- und Leistungsbedarf von klimatisierten Gebäuden (2011) zu finden.
#### Energiebedarf Lüftung
Für mechanisch belüftete Räume muss zusätzlich der Energiebedarf für die Lüftung berechnet
werden. Dieser rechnet sich aus zwei Komponenten: Aussenluftförderung und ggf.
Aussenluftkühlung und -entfeuchtung.
Der Energiebedarf für die Luftförderung berechnet sich aus der Leistung der Ventilatoren für
Zuluft und Abluft sowie der Betriebszeit. Solange eine Anlage nur im Ein-Ausbetrieb läuft, ist
diese Berechnung einfach. Heute werden, auch aus Energiespargründen, Lüftungsanlagen immer
mehr bedarfsabhängig mit variablem Volumenstrom gefahren. Die Berechnung des
Energiebedarfes für die Luftförderung bei solchen Anlagen ist nur mit einer stundenweisen
Berechnung möglich.
Der Leistungsbedarf eines Ventilators berechnet sich nach Formel 8:
**Formel 6: Leistung Ventilator**

$$P_V = \dot{V} \cdot \frac{\Delta p}{\eta}$$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $P_V$ | elektrische Leistung Ventilator | W |
| $\dot{V}$ | geförderter Luftvolumenstrom | m³/s |
| $\Delta p$ | Druckaufbau durch den Ventilator | Pa |
| $\eta$ | Wirkungsgrad des Ventilators | – |
Der Druckverlust ist dabei in zweiter Potenz vom Luftvolumenstrom abhängig, solange im
Luftkanalnetz keine Veränderungen wie z. B. Klappenstellungen erfolgen. Wenn
Klappenänderungen erfolgen oder Volumenstromregler vorhanden sind, wird die Festlegung des
nötigen Druckaufbaues sehr schwierig. Auch der Ventilator-Wirkungsgrad ist stark von der
Leistung und dem Druckaufbau abhängig, und muss somit ebenfalls je nach Verhältnissen neu
festgelegt werden.
Der Energiebedarf für die Aussenluftkühlung muss ebenfalls stundenweise mit den jeweiligen
Luftmengen, dem verlangten Zustand der Zuluft (Temperatur und Feuchte) und dem jeweiligen
Aussenluftzustand (Witterungsdaten) berechnet werden.
Der Leistungsbedarf für die Luftkühlung ohne Entfeuchtung kann dabei einfach nach der
Formel 9 berechnet werden (analog den Lüftungsverlusten, Formel 1).

**Formel 7: Abführbare Leistung mit Luftvolumenstrom, ohne Entfeuchtung**

$$P = \frac{\dot{V}}{3600} \cdot \Delta T \cdot c_p$$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $P$ | thermische Leistung (Kälte) | kW = kJ/s |
| $\dot{V}$ | Luftvolumenstrom | m³/h |
| $\Delta T$ | Temperaturdifferenz | K |
| $c_p$ | spez. Wärmekapazität | kJ/m³K (für Luft ca. 1,2 kJ/m³K) |
In der Praxis ist mit der Luftkühlung im Allgemeinen auch eine mehr oder weniger starke
Entfeuchtung verbunden. Dann muss noch die Energie für die Verflüssigung des Wasserdampfes
aufgebracht werden, weshalb die obige Formel 9 nicht mehr stimmt. Die Enthalpiedifferenz der
Luft über den Kühler muss einem h-x-Diagramm entnommen oder mit einem entsprechenden
Programm gerechnet werden. Aus der Enthalpiedifferenz kann dann mit der Luftmenge die
Leistung des Kühlers berechnet werden.
Die Entfeuchtung über den Kühler erfolgt, weil an der kalten Oberfläche des Kühlregisters
(Wärmetauscher) die Aussenluft teilweise kondensiert. Die Entfeuchtung ist umso stärker, je
tiefer die Kaltwassertemperatur im Kühler ist. Umgekehrt ist es also eine
Energiesparmassnahme, wenn mit hohen Kaltwassertemperaturen gekühlt wird, da dann weniger
Energie für die Entfeuchtung nötig ist. Zudem steigt die Effizienz der Kälteerzeugung bei
höheren Kaltwassertemperaturen und es kann eher freie Kühlung genutzt werden. Um auch so
genügend tiefe Zulufttemperaturen zu erreichen, sind genügend grosse Kühler erforderlich, was
ganz leicht zu höheren Druckverlusten und mehr Strombedarf für den Ventilator führt.
Noch mehr Energie ist nötig, falls bestimmte Werte der Zuluftfeuchte (resp. der Raumfeuchte)
eingehalten werden müssen. Dann muss mit tiefen Kaltwassertemperaturen die Aussenluft
entsprechend stark entfeuchtet werden, und kühlt dabei im Allgemeinen unter die Soll-Zuluft-
temperatur ab. Es ist anschliessend eine Nachwärmung auf die geforderte Zulufttemperatur
nötig. Bei schwülen Aussenbedingungen kann die Entfeuchtung mehr Kälteleistung erfordern als
die Aussenluftkühlung.

![[abb29_als_diskussionsgrundlage_zu_ebergeordneten.jpg]]
*Abbildung 29: Als Diskussionsgrundlage zu übergeordneten Problemen, seit Jahrzehnten aktuell!*

> Quelle: TOLES, © 2004 The Washington Post

---

> ◀ [[07_3_freie_kuehlung|← Freie Kühlung]] · [[_Skript_Energie_MOC|↑ MOC]] · [[08_Anhang|Anhang →]] ▶

---
