---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.4.1–2"
titel: "Heizlastermittlung & Systemnachweis SIA 380/1"
---

# Kap. 1.4.1–2 – Heizlastermittlung & Systemnachweis SIA 380/1

> ◀ [[01_3c_Untervarianten|Kap. 1.3.3]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_4b_Jahresenergiebedarf|Kap. 1.4.3]] ▶

---

Heizung“ ist die Heizlast der jeweiligen Zone zu finden. Siehe Abbildung 1.55. Das exportierte Excel Sheet kann an Lemonconsult zur Evaluation der Vor- und Rücklauftemperaturen
gesendet werden.
Lemonconsultschicktdanndie Temperaturenzurück.Fürdie Waffenplatzstrassesinddies
die Temperaturen in Abbildung ??.
![[data/assets/IDA_ICE_Tutorial/fig_1_53.png]]
*Abbildung 1.53: Einstellung Simulationsdaten Heizlast 1*

![[data/assets/IDA_ICE_Tutorial/fig_1_54.png]]
*Abbildung 1.54: Einstellung Simulationsdaten Heizlast 2*

![[data/assets/IDA_ICE_Tutorial/fig_1_55.png]]
*Abbildung 1.55: Resultate Heizlast*
#### 1.4.2 Systemnachweis nach SIA 380/1
> 📖 Theorie: [[04_Heizwaermebedarf|Skript Energie Kap. 4 – Heizwärmebedarf & Grenzwerte SIA 380/1]]

Die Eingabemaske für den SIA 380/ Systemnachweis ist im SIA“ Tab ganz unten. Sie wurde
gemäss Abbildung 1.56 ausgefüllt. Zonen die nicht beheizt sind, wurden entsprechend deklariert.
Um den Systemnachweis zu erfüllen, muss die Heizlast P unter dem Grenzwert von
20W/m² liegen. Um das zu erreichen, musste der effektiv thermisch wirksame Aussenluft-
Volumenstrom kleiner 0.6m3/(m²h) eingestellt werden.
![[data/assets/IDA_ICE_Tutorial/fig_1_56.png]]
*Abbildung 1.56: Eingabemaske SIA 380/1*
