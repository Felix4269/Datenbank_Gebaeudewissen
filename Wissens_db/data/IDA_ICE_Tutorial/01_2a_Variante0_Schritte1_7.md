---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.2a"
titel: "Variante 0 Step-by-Step – Schritte 1–7 (Eingaben, Hülle, Klima)"
---

# Kap. 1.2a – Variante 0 Step-by-Step – Schritte 1–7 (Eingaben, Hülle, Klima)

> ◀ [[01_1_Modell_Grundsaetzliches|Kap. 1.1]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_2b_Variante0_Geometrie|Kap. 1.2b]] ▶

---

![[data/assets/IDA_ICE_Tutorial/fig_1_5.png]]
*Abbildung 1.5: Vorgabewerte*

![[data/assets/IDA_ICE_Tutorial/fig_1_6.png]]
*Abbildung 1.6: Wärmebrücken Einstellung*

![[data/assets/IDA_ICE_Tutorial/fig_1_7.png]]
*Abbildung 1.7: Infiltration nach SIA Merkblatt 2024 [1]*

![[data/assets/IDA_ICE_Tutorial/fig_1_8.png]]
*Abbildung 1.8: Globale Infiltration eingeben*
5. Lüftungsgerät
> 📖 Theorie: [[_Skript_Lueftung_MOC|Skript Lüftungstechnik]]  ·  [[03_2_mechanische_lueftung|Kap. 3.2 – Mechanische Lüftung]]  ·  [[05_3_waermerueckgewinnung|Kap. 5.3 – Wärmerückgewinnung]]

Das Gebäude an der Waffenplatzstrasse hat keine mechanische Lüftung. Ebenso sieht die SIA
2024 für Bestand“ Wohnhäuser keine solche vor. Die SIA 2024 gibt aber einen sogenannten hygienebedingten Aussenluftvolumenstrom bei Bestand“ vor. Dieser Volumenstrom ist
vermutlich eine Mischrechnung über Fensterlüften, Küchenabzug, Türen öffnen usw.
Um den hygienebedingten Volumenstrom zu simulieren, baut die Schweizer Lokalisierung“ eine mechanische Lüftung auch bei Bestand“ Gebäuden ein. Diese Lüftung ist aber
fiktiv und sollte in den Resultaten nicht als reale mechanische Lüftung erscheinen. Zusammen mit dem Equa Support haben wir bemerkt, dass die Bestand“ Vorlage der Schweizer
Lokalisierung“ in diesem Bereich einen Fehler aufweist. Die Vorlage sieht eine Lüftung mit

Wärmerückgewinnung vor, was nicht im Sinne der SIA 2024 ist. Im folgenden ist eine Anleitung, wie das Lüftungsgerät ersetzt werden muss, um den hygienebedingten Aussenluftvolumenstrom korrekt abzubilden. Das Vorgehen wurde in Zusammenarbeit mit dem Equa
Support erstellt.
Lüftungsgerät ersetzen: Im Tab Allgemein“ unter Zentrale Gebäudetechnik auf Erset-
zen...“ klicken und Lüftungsgerät“ anwählen. In der Liste SIA 180 - C.1 AHU“ wählen.
Siehe Abbildung 1.9.
Das neue Lüftungsgerät öffnen und auf Emeter Fans“ klicken. N IN“ auf 0 setzten. Siehe
Abbildung 1.10. Damit wird verhindert, dass der Stromverbrauch der Ventilatoren in den
Ergebnissen erscheint.
![[data/assets/IDA_ICE_Tutorial/fig_1_9.png]]
*Abbildung 1.9: Lüftungsgerät ersetzen*

![[data/assets/IDA_ICE_Tutorial/fig_1_10.png]]
*Abbildung 1.10: Energie Meter der Lüftung trennen*

6. Wärme- und Kälteerzeuger
Wir wollen das Heizungssystem vorerst simpel halten und ersetzen es deswegen durch eine
ESBO-Plant“.Siehe Abbildung1.11.Dannkönnenwirdiezentrale Heizungunddie Kühlung
löschen, da wir vorerst mit idealen lokalen Heizelementen in den Zonenvorlagen arbeiten werden. Das Löschen erfolgt wie in Abbildung 1.12 gezeigt.
![[data/assets/IDA_ICE_Tutorial/fig_1_11.png]]
*Abbildung 1.11: Ersetzen durch ESBO Plant*

![[data/assets/IDA_ICE_Tutorial/fig_1_12.png]]
*Abbildung 1.12: Löschen von zentralen Wärme- und Kälteerzeuger*

7. Verteilverluste
Die Verteilverluste des Heizsystems sind 5 % und können im Allgemein-Tab unter Energiebedarf und Verluste (”Extra energy and losses”) bei Heat to zones“ eingegeben werden (siehe
Fig. 1.13).
![[data/assets/IDA_ICE_Tutorial/fig_1_13.png]]
*Abbildung 1.13: Eingeben von Verteilverlusten*
8. Gebäudevolumen
Gebäudevolumen anhand PDF Pläne zeichnen. Danach, klick auf Dach zeichnen“ und die
Dach-Punkte gemäss Abbildung 1.15 zeichnen. Darauf achten, dass die Höhe der Dachpunkte
stimmt → Klick auf Schaltfläche Höhe festlegen“ oder direkt Eingabe in Tabelle links in
Spalte Z“.

![[data/assets/IDA_ICE_Tutorial/fig_1_14.png]]
*Abbildung 1.14: Gebäudevolumen zeichnen*

![[data/assets/IDA_ICE_Tutorial/fig_1_15.png]]
*Abbildung 1.15: Dach zeichnen*
9. Zonen
Das Modell kommt mit zwei Zonenvorlagen aus:
• 1.1 Wohnen MFH Bestand“ und
• 12.3 Treppenhaus Bestand“
Die beiden relevanten SIA2024 Raumdatenblätter für 1.1 Wohnen MFH“ und 12.3 Trep-
penhaus“ sind im Anhang ?? abgedruckt.
Die Daten aus den Datenblättern sind grundsätzlich in der Schweizer Lokalisierung“
eingepflegt. Die Einsicht in die Datenblätter ist daher nicht zwingend nötig um das Simulationsmodell aufzusetzen.
Laut Tabelle 1 im Merkblatt SIA 2024 [1], gilt die Gebäudekategorie 1.1 Wohnen MFH“
für die meisten Räume in einem Mehrfamilienhaus. Siehe Printscreen in Abbildung 1.16.
