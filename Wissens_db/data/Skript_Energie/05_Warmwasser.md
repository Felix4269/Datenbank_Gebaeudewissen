---
tags: [Energie, Heizwärmebedarf, Wärmegewinne, Gebäudetechnik]
skript: "Energieflüsse im Gebäude"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "5"
---

> ◀ [[04_Heizwaermebedarf|← Heizwärmebedarf]] · [[_Skript_Energie_MOC|↑ MOC]] · [[06_1_berechnung_energiebedarf|Berechnung des Energiebedarfs →]] ▶

---

# Energieflüsse im Gebäude – Kapitel 5: Wärmebedarf Warmwasser

## 5 Wärmebedarf Warmwasser
> 📖 Norm: [[_SIA_385-2_2025_MOC|SIA 385/2:2025 – Trinkwarmwasseranlagen]]  ·  [[Anhang_A_Warmwasserbedarf|Anhang A – Warmwasserbedarf & Wärmebedarf]]

### 5.1 Warmwasserbedarf
Mit heutigem Komfortanspruch, aufgrund des Wellnesstrends sowie steigender Hygienestandards
steigt der Warmwasserbedarf tendenziell an. Demgegenüber sinkt der Heizwärmebedarf infolge
besserer Wärmedämmung und Fenster sowie dank der Wärmerückgewinnung deutlich. Der
Warmwasserbedarf erlangt damit eine prozentual immer grössere Bedeutung. Betrug dieser
früher ca. 10 % des Wärmebedarfs, kann bei einem heutigen Gebäude der Anteil Wärmebedarf
für Warmwasser höher als der Heizwärmebedarf werden.
Die Tabelle 5 gibt Anhaltswerte über den Warmwasserbedarf (60 °C) in Liter pro Tag und/oder pro Bezugsgrösse (Person, Mahlzeit etc.) an. Bei Warmwasser mit weniger als 60 °C erhöht sich der Bedarf in Litern entsprechend. Diese Tabelle kann zur Dimensionierung von Neuanlagen genutzt werden. Um bei bestehenden Gebäuden den Warmwasserbedarf zu bewerten, können diese Werte ebenfalls verwendet werden.
In der neuen Norm betr. Trinkwarmwasser SIA 385/2, 2025 sind jeweils nur die fetten Minimalwerte aufgeführt.

![[tab5_normwerte_nutzwarmwasserbedarf_pro_bezugse.jpg]]
Tabelle 5: Normwerte Nutzwarmwasserbedarf pro Bezugseinheit V<sub>w,u</sub> in Liter pro Tag oder pro Bezugseinheit


### 5.2 Berechnung Wärmebedarf Warmwasser
Der Energiebedarf für Wassererwärmung berechnet sich gemäss Formel 4:
**Formel 4: Energiebedarf für Warmwasser**

$Q = m \cdot c_p \cdot \Delta T$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $Q$ | Wärme(energie) | kJ |
| $m$ | Masse des zu erwärmenden Wassers (1 l = 1 kg) | kg |
| $c_p$ | spez. Wärme Wasser (≈ 4,2 kJ/(kg·K)) | kJ/(kg·K) |
| $\Delta T$ | Temperaturdifferenz Kalt- zu Warmwasser | K |
Die Umrechnung von Kilojoule in Kilowattstunden erfolgt mit dem Faktor 3600: 1 kWh = 3600 kJ.
Wenn die Wärmeerzeuger-Leistung gesucht ist, muss mit der Zeit dividiert werden, in der eine
bestimmte Warmwassermenge erwärmt werden muss (Formel 5). Diese Zeit ist von der Grösse
des Speichers abhängig, der zur Verfügung steht. Die geringste Leistung wäre erforderlich, wenn
das Wasser über 24 h, d. h. ganztägig, erwärmt werden kann. Dazu wäre aber ein Speicher von
mehr als einem Tagesbedarf nötig, um Bedarfsschwankungen je nach Tag auszugleichen. Aus
diversen Gründen (Hygiene, Energie, Kosten, Platzbedarf) soll ein Speicher nur knapp einen
durchschnittlichen Tagesbedarf abdecken. Falls genügend Wärmeleistung zur Verfügung steht,
wird besser nur ein halber Tagesbedarf gespeichert. Die Aufheizzeit wird so festgelegt, dass ein
geleerter Speicher in 4 bis 8 Stunden wieder aufgewärmt werden kann. Aus hygienischen
Gründen ist die Erwärmung im Durchlaufverfahren (Frischwasser-Stationen oder innere WW-
Register) zu bevorzugen. Die nötige Wärmeleistung wird aus einem Heizwasserspeicher
bezogen. Die Legionellengefahr kann so deutlich reduziert werden.
**Formel 5: Umrechnung in Leistungsbedarf des Wassererwärmers**

$P = \frac{Q}{t}$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $P$ | Wärmeleistung | kW |
| $Q$ | Wärme(energie) | kJ oder kWh |
| $t$ | Zeit(dauer) der Erwärmung (s, oder h wenn Q in kWh) | s oder h |
**Beispiel:**

Für ein 4-Familienhaus (je 3 Personen) werden pro Tag 500 l Warmwasser à 60 °C benötigt. Das
Wasser soll täglich innerhalb der Nachtabsenkung der Gas-Heizung (6 Stunden) aufgeheizt
werden. Es ist ein genügend grosser Speicher vorhanden. Wie gross wird der tägliche
Wärmebedarf, wie gross ist die erforderliche Leistung des Wassererwärmers?

Wärme-Energie pro Tag:

$Q = m \cdot c_p \cdot \Delta T = 500\,\text{kg} \times 4{,}2\,\text{kJ/(kg·K)} \times (60-10)\,\text{K} = 105\,000\,\text{kJ} = 29{,}17\,\text{kWh}$

$P = Q/t = 29{,}17\,\text{kWh} \,/\, 6\,\text{h} = 4{,}86\,\text{kW}$

### 5.3 Erwärmung Warmwasser
#### 5.3.1 Zentrale Warmwasserversorgung
Bei der zentralen Warmwasserversorgung ist pro Gebäude (ev. pro Gebäudegruppe) eine
Warmwassererwärmung vorhanden. Diese Anlagen brauchen eine relativ hohe Wärmeleistung
und die Speicher werden meist recht gross. Sie brauchen auch ein mehr oder weniger
umfangreiches Verteilnetz.
Die zentrale Wassererwärmung erfolgt fast immer mit dem Wärmeerzeuger der Heizung. Wie für
die Heizwärmeerzeugung soll ein umweltfreundlicher Energieträger genutzt werden (z. B.
Umweltwärme und «grüner» Strom bei Wärmepumpe, Fernwärme, ev. Holzpellets). Die Nutzung
von Strom zur direkten Wärmeerzeugung (Widerstandsheizung) ist aus energiepolitischen
Gründen bei Neubauten und System-Erneuerungen nicht zulässig.
Eine Wärmepumpe oder Fernwärme sind bestens geeignet für die ganzjährige Versorgung mit
Wärme für Warmwasser und Heizung. Da im Sommer insbesondere eine Luft/Wasser-
Wärmepumpe sehr effizient funktioniert und in Zukunft genügend PV-Strom zur Verfügung steht,
ist dies eine gute Lösung für das Warmwasser. Eine Kombination einer Wärmepumpe mit
thermischen Solarkollektoren ist aus ökologischen wie auch wirtschaftlichen Gründen sinnlos.
Auch bei Fernwärme steht im Sommer meist genügend regenerative Wärme zur Verfügung,
sodass auch hier eine Kombination mit thermischen Kollektoren keinen Sinn macht.
Früher wurde die zentrale Warmwassererwärmung häufig mit zwei Energieträger geplant: z. B.
mit Öl-, Gas- oder Stückholzkessel in der Heizperiode und direkt mit Strom im Sommer während
der Niedertarif-Zeit. Dazu ist ein elektrisches Heizregister im Warmwasserspeicher erforderlich.
Der Heizkessel konnte im Sommer ausgeschaltet werden, was dessen Bereitschaftsverluste
verringerte.
Heute soll ein elektrisches Heizregister nur als Redundanz bei Ausfall der Haupt-
Wärmeerzeugung dienen. Zukünftig könnte damit im Sommer Überschussstrom aus PV-Anlagen
genutzt werden, falls dies dannzumal mehr Sinn macht als die Abregelung der PV-Anlagen.
Sehr gut nutzbar für zentrale Warmwassererwärmung ist Abwärme (z. B. aus gewerblichen
Kälteanlagen oder von Serverräumen). Abwärme steht meist ganzjährig zur Verfügung und kann
mit einer Wärmepumpe effizient auf die erforderliche Temperatur gebracht werden,.
Auch ein BHKW kann als technisch geeigneter Wärmeerzeuger für Warmwasser (und ggf. die
Grundlast der Heizung) in grossen Bauten genutzt werden. Es können viele Betriebsstunden für
das BHKW erreicht werden, da das Warmwasser ganzjährig benötigt wird. Allerdings gilt dies aus
Gründen der Treibhausgas-Emissionsvermeidung nur dann, falls ein klimaneutraler Brennstoff für
das BHKW genutzt werden könnte (bspw. Biogas).
#### 5.3.2 Solare Warmwassererzeugung
Wo noch mit fossiler Energie Wärme erzeugt wird, könnte eine thermische Solaranlage helfen,
diese Ressourcen zu schonen. Viel nachhaltiger ist es, das Geld in den Ersatz der fossilen
Energieerzeugung zu investieren.
Nur in einem Gebäude mit einem Holzschnitzel-Kessel oder mit Stückholzheizung kann eine
thermische Solaranlage Sinn machen. Die Warmwassererwärmung stellt dann einen geeigneten

Abnehmer von Solarwärme dar. Im Sommer kann das Warmwasser solar erwärmt werden und die
Holzheizung muss nicht betrieben werden. Damit erspart man sich den Betrieb eines
Stückholzkessels im Teillastbereich mit tiefem Wirkungsgrad und etwas Brennholz. Oft besser
wird ein Wärmepumpenboiler installiert. Dieser kann das Warmwasser ganzjährig erwärmen.
Damit kann wesentlich mehr Brennholz gespart werden.
Kleine thermische Solaranlagen für EFH gibt es auf dem Markt als geprüfte und relativ
kostengünstige Komplett-Anlagen mit allen Komponenten. Für grössere Objekte ist es am
wirtschaftlichsten, das Wasser nur auf ca. 40 °C bis max. 50 °C vorzuwärmen, so dass der
Wirkungsgrad der Sonnenkollektoren hoch wird. Die Kollektoren werden so dimensioniert, dass
die anfallende Wärme im Sommer ganz genutzt werden kann. Die Anlage wir also auf den
Sommerfall dimensioniert. Theoretisch kann dann die Hälfte der jährlich benötigten Energie für
Warmwasser solar erzeugt werden. Solche Solaranlagen sind am kostengünstigsten, da es keine
überschüssige Wärme im Sommer gibt. Auch dann bleiben die Wärmeerzeugungskosten recht
hoch. Inzwischen ist es deutlich günstiger, eine Kilowattstunde Solarstrom zu erzeugen als eine
Kilowattstunde thermische Solarenergie.
![[abb16_solaranlage_deckungsgrad.png]]
*Abbildung 16: Einfaches Diagramm zur Bestimmung des nutzbaren solaren Wärmegewinns (Bild M. Hubbuch)*
Mit dem obigen Diagramm (Abbildung 16) kann vereinfacht gezeigt werden, wie gross der solare
Deckungsgrad für die Warmwassererwärmung wird. Wenn die Solaranlage so dimensioniert wird,
dass sie im Hochsommer gerade den ganzen Warmwasserbedarf decken kann, so wird etwa die
Hälfte des jährlichen Energiebedarfes solar gedeckt. Diese Solaranlage arbeitet am
wirtschaftlichsten, da keine nicht nutzbaren Überschüsse entstehen. Wenn die Solaranlage
doppelt so gross geplant wird, so steigt der solare Deckungsgrad auf 75 %, ein Viertel der
Wärme kann noch immer nicht genutzt werden. Da die Anlage ca. 2-mal teuer wird, aber nur 1,5-
mal so viel Energie genutzt werden kann, wird die nutzbare Energie spezifisch teurer. Ein solarer
Deckungsgrad von 100 % kann, wie das Diagramm zeigt, nicht erreicht werden. Ausnahme ist,
falls ein sehr grosser saisonaler Speicher vorhanden ist, der ca. 25 % der jährlichen solaren
Gewinne vom Sommer in den Winter speichern kann.
Für die Grobauslegung von thermischen Solaranlagen gibt es gratis verfügbare Rechner im
Internet. Eine präzisere Auslegung einer Solaranlage kann mit Computerprogrammen erfolgen,
z. B. mit Polysun. Diese basieren auf stündlichen Wetterdaten, welche heute für jeden Ort der
Welt verfügbar sind (z. B. Programm Meteonorm®).

---

> ◀ [[04_Heizwaermebedarf|← Heizwärmebedarf]] · [[_Skript_Energie_MOC|↑ MOC]] · [[06_1_berechnung_energiebedarf|Berechnung des Energiebedarfs →]] ▶

---




