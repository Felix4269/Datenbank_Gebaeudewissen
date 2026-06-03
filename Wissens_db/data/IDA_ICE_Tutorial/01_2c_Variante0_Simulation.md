---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.2c"
titel: "Variante 0 Step-by-Step – Simulation & Auswertung"
---

# Kap. 1.2c – Variante 0 Step-by-Step – Simulation & Auswertung

> ◀ [[01_2b_Variante0_Geometrie|Kap. 1.2b]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_2d_Kalibrieren|Kap. 1.2.1]] ▶

---

> 📖 Manual: [[03_3_1_zone_intro_solar|IDA ICE Manual Kap. 3.3–3.4 – Zonenmodell & Solar (Simulationsgrundlagen)]]  ·  Theorie: [[03_3_waermespeicherung|Skript Energie Kap. 3.3 – Wärmespeicherung & Thermische Masse]]

wird als Decke UG MitDaemm definiert. Der Teil des Bodens, der über der ungedämmten Zone steht, muss mittels eines Wandteils“ mit der Bauteilkonstruktion Decke UG OhneDaemm
definiert werden. Siehe dazu Abbildung 1.30.
Alle Decken der Zonen im OG3 müssen als Boden Estrich Gedaemmt definiert werden.
Dazu kann im Tab Allgemein“ in der Liste Flächen“ nach Verbunden mit“ sortiert werden.
Siehe Abbildungen 1.31 und 1.32
![[data/assets/IDA_ICE_Tutorial/fig_1_30.png]]
*Abbildung 1.30: Wandteil im Boden von Zone WoZi W OG0*
Tipp 2 Listen“:Umineiner Liste Daten in mehreren Zeilengleichzeitigzuändern,
wird zuerst ein Eintrag manuell geändert, z.B. mit Linksklick und Auswahl der Konstruktion“ in Abbildung 1.31. Danach mit Rechtsklick den Eintrag kopieren. Shift“ oder Ctrl“
gedrückt halten und immer mit Rechtsklick die Zellen anwählen, in denen der kopierte Eintrag eingefügt werden soll. Siehe Abbildung 1.32.
![[data/assets/IDA_ICE_Tutorial/fig_1_31.png]]
*Abbildung 1.31: Verändern mehrerer Zeilen in Liste*

![[data/assets/IDA_ICE_Tutorial/fig_1_32.png]]
*Abbildung 1.32: Verändern mehrerer Zeilen in Liste*
11. Verschattung und Ausrichtung
Im Tab Allgemein“ unter Verschattungen und Ausrichtung“ wird der Kompass so gedreht,
dass Norden nach links zeigt. Dies Entspricht der Darstellung auf den PDF Gebäudeplänen.
Mankannden Kompassmanuelldrehen,indemmanihnanklicktundmitder Mausdaskleine
Quadratimroten Pfeilbewegt.Umdie Ausrichtunggenaueinzustellen,kannmanden Winkel
unter Gliederung“ eingeben. Es wurden hier 270° eingegeben. Siehe Abbildung 1.34.
Die Nachbargebäude werden als vertikale Verschattungen eingezeichnet. Als Grundlage
für Ausrichtung und Verschattungen dient Google Maps. Die Verschattungen sind im Umgebungsplan sichtbar als violette Rechtecke, wie in Abbildung 1.33 dargestellt. Ausserdem sieht
man sie in der 3D Ansicht (Abbildungen 1.1 und 1.35).
Abbildung 1.35 zeigt ausserdem, wie Balkone als Verschattungsobjekte eingefügt werden.
Man findet sie in der Palette“ im Tab 3D“.
Tipp 3D-Ansicht“: Manchmal ist die 3D Ansicht übersichtlicher, wenn gewisse Elemente ausgeblendet werden. Rechtsklick auf den grünen Bereich in der 3D Ansicht und dann
auf Visuelle Filter“ klicken um beispielsweise Verschattungsobjekte auszublenden. Ausserdem kann mit klick auf Anzeigen...“ unten in der 3D Ansicht die Darstellung angepasst
werden. In der 3D Darstellung kann mit gedrücktem Mausrad der Plan verschoben werden.

![[data/assets/IDA_ICE_Tutorial/fig_1_33.png]]
*Abbildung 1.33: Verschattung*

![[data/assets/IDA_ICE_Tutorial/fig_1_34.png]]
*Abbildung 1.34: Ausrichtung*

![[data/assets/IDA_ICE_Tutorial/fig_1_35.png]]
*Abbildung 1.35: Verschattung Balkon*

12. Einstellungen Simulation
Grundsätzlichwirdder Jahresenergie Bedarfnach SIASimuliert,bei80%derinternen Lasten.
Dies Entspricht der Jahresgleichzeitigkeit“ für Wohnen MFH“ gemäss SIA 2024. Es werden
die Einstellungen gemacht wie in den Abbildungen 1.36 und 1.37 gezeigt.
![[data/assets/IDA_ICE_Tutorial/fig_1_36.png]]
*Abbildung 1.36: Einstellungen Simulation*

![[data/assets/IDA_ICE_Tutorial/fig_1_37.png]]
*Abbildung 1.37: SIA“ Tab Einstellungen*
