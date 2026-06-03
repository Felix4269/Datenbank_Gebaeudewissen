---
tags: [Energie, Heizwärmebedarf, Wärmegewinne, Gebäudetechnik]
skript: "Energieflüsse im Gebäude"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "6.1"
titel: "Berechnung Energiebedarf Heizung und Warmwasser"
---

> ◀ [[05_Warmwasser|← Wärmebedarf Warmwasser]] · [[_Skript_Energie_MOC|↑ MOC]] · [[06_2_primaerenergie|Einfluss Primärenergiebedarf →]] ▶

---

# Energieflüsse im Gebäude – Kap. 6.1: Berechnung Energiebedarf Heizung und Warmwasser

## 6 Energiebedarf des Gebäudes
### 6.1 Berechnung Energiebedarf Heizung und Warmwasser
> 📖 Simulation: [[01_4b_Jahresenergiebedarf|IDA ICE Tutorial – Jahresenergiebedarf (SIA-Simulation)]]  ·  Norm WW: [[_SIA_385-2_2025_MOC|SIA 385/2:2025 – Warmwasserbedarf]]  ·  Norm Geothermie: [[_SIA_384-6_2021_MOC|SIA 384/6:2021 – Erdwärmesonden & Jahresarbeitszahl]]

Mit dem Heizwärmebedarf und dem Wärmebedarf Warmwasser ist bekannt, wie viel
Wärmeenergie die Wärmeerzeugungsanlage bereitstellen muss (Abbildung 17).

![[abb17_gesamtenergiebedarf_heizung_und_warmwasser.jpg]]
*Abbildung 17: Gesamtenergiebedarf Heizung und Warmwasser*

Der Energiebedarf für Heizung und Warmwasser ($E_{F,hww}$), der von aussen dem Gebäude zugeführt
werden muss, ergibt sich aus der Summe des Wärmebedarfes für Heizung und Warmwasser
($Q_{hww}$, Nutzenergie), ergänzt um die Verluste bei der Wärmeerzeugung, eventuell Speicherung
und Verteilung im Haus ($Q_L$), reduziert um die eventuell genutzte Umgebungsenergie ($Q_r$, aktive
Solarwärmenutzung, Photovoltaik oder Umgebungswärme der Aussenluft, von Oberflächenwasser
oder Geothermie).
Dieser Sachverhalt ist in der Abbildung 18 dargestellt.
Die Erzeugungsverluste $Q_{gen,ls}$ ergeben sich aus den Wirkungsgraden der Wärmeerzeugung resp.
aus der Jahresarbeitszahl gemäss den Anhaltswerten in Tabelle 6.
Daneben fallen Verluste bei der Speicherung an ($Q_{sto,ls}$). Diese Verluste sind im Allgemeinen klein.
Sie sind von der Art und Grösse der Speicher abhängig. Sie können vermieden werden, wenn
eine Speicherung weggelassen werden kann, bspw. bei einem modulierenden Wärmeerzeuger.

**Tabelle 6: Wirkungsgrade Wärmeerzeugung**

| Art der Wärmeerzeugung | Jahreswirkungsgrad resp. Jahresarbeitszahl (typische Bereiche) | Defaultwerte SIA Merkblatt 2031 |
|---|---|---|
| Öl-/Gaskessel herkömmlich | 65 bis 85 % (auf den Brennwert bezogen) | 80 % |
| Öl-/Gaskessel Brennwert | 85 bis 95 % (auf den Brennwert bezogen) | 85 % |
| Stückholzkessel, Holzofen, Cheminée mit Heizeinsatz | 60 bis 75 % (auf den Brennwert bezogen) | 65 % |
| Holzschnitzel- oder Pellets-Kessel | 65 bis 80 % (auf den Brennwert bezogen) | 70 % |
| Wärmepumpe Luft/Wasser | 2,5 bis 4,5 (Jahresarbeitszahl) | 2,8 |
| Wärmepumpe Sole oder Wasser/Wasser | 3,5 bis 5,5 (Jahresarbeitszahl) | 3,4 |
| Blockheizkraftwerk | 85 bis 90 % (Gesamtwirkungsgrad, ca. 30–40 % Strom, Rest Wärme) | – |
| Fernwärme | 93 bis 98 % (Wirkungsgrad beim Verbraucher, zus. Wärmeerzeugungs- und Verteilverluste) | 93 % |
| Elektro Direktheizung (El. Widerstandsheizung) | 90 bis 100 % | 93 % |
Weitere Verluste treten bei der Verteilung der Heizwärme und des Warmwassers im Gebäude auf
($Q_d$). Diese Verluste können gross werden, falls Verteilleitungen schlecht isoliert sind oder durch
unbeheizte Räume führen. Bei manchen älteren Gebäuden sind Verteilleitungen für Heizung und
Warmwasser in einer schlecht gedämmten Aussenwand geführt, was zu Wärmeverlusten nach
aussen führt. Bei neueren, gut wärmegedämmten Verwaltungsgebäuden wurde schon beobachtet,
dass mehr als die Hälfte der Wärme von den Verteilleitungen (und nicht von den dafür
vorgesehenen Heizkörpern) abgegeben wird.
Auch innerhalb der Räume können Verluste auftreten, falls Räume mehr als notwendig beheizt
werden. Dies kann durch schlechte raumweise Regulierbarkeit erfolgen oder durch nicht
gedämmte Verteilleitungen im Raum. Beim Warmwasser werden die Verteilleitungen oft
warmgehalten, um die Ausstosszeit zu verringern (mit elektr. Begleitheizungen oder mit einem
Zirkulationssystem). Dadurch können sehr grosse Verluste auftreten, die 20 bis 50 % der
genutzten Wärme ausmachen können. Aus diesen Gründen sind in den Mustervorschriften der
Kantone im Energiebereich (MuKEn) auch Module vorgesehen, die eine minimal notwendige
Dämmung von Heiz- und Warmwasser-Verteilleitungen vorschreiben.
Verteilverluste können mit dezentraler Wärmeerzeugung reduziert werden. Dies kann bspw.
einen kleinen Elektroboiler rechtfertigen, wo eine lange Warmwasser-Zuleitung wegfallen kann.

---

> ◀ [[05_Warmwasser|← Wärmebedarf Warmwasser]] · [[_Skript_Energie_MOC|↑ MOC]] · [[06_2_primaerenergie|Einfluss Primärenergiebedarf →]] ▶

---
