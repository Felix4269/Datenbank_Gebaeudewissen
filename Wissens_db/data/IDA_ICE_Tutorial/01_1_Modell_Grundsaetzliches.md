---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.1"
titel: "Modell Aufbau – Grundsätzliches"
---

# Kap. 1.1 – Modell Aufbau – Grundsätzliches

> ◀ [[00_Glossar_Konstanten|Vorwort]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_2a_Variante0_Schritte1_7|Kap. 1.2a]] ▶

---

Kapitel 1
Simulation Vorgehen
Für die Simulation wurden folgende Versionen verwendet:
• IDA Indoor Climate and Energy: Expert edition, Stand-alone
– Version: 4.8 SP2
– Datum: 2020-09-11
• Schweizer Lokalisierung: LOCAL-CH 4.8.0.2
### 1.1 Modell Aufbau - Grundsätzliches
Als Grundlage für das Zeichnen des Gebäudes dienen alte Pläne und aktuelle Fotos. Siehe
als Beispiel die Abbildungen 1.3 und 1.2. Ausserdem waren wir vor Ort um das Gebäude zu
inspizieren.
Aus diesen Eingabedaten entstand das Modell in Abbildung 1.1. Man sieht, dass das
Gebäude gegenüber dem Original vereinfacht wurde. Das oberste Geschoss ist von der Geometrie her identisch gezeichnet wie die anderen Geschosse.
Eine weitere Vereinfachung ist, dass im Modell alle Winkel zwischen Mauern rechtwinklig
gezeichnetsind.Im Originalistdie Ost-Seitedes Gebäudesleichtnach Nordenverdreht.Siehe
Plan vom EG in Abbildung 1.3.
Die grauen Flächen sind Verschattungen von Nachbargebäuden. Sie werden unter Punkt
11. Verschattung und Ausrichtung“ eingefügt.
Beim Erstellen eines Modells empfiehlt es sich es immer wieder zu speichern und eine
Simulation zu starten. Welche Simulation gestartet wird ist nicht relevant. Wichtig ist, dass
das mathematische Modell beim Starten der Simulation ohne Fehler kompiliert wird und die
Simulationstartet.Wenndie Simulationproblemlosgestartetist,kannsiewiederabgebrochen
werden.

![[data/assets/IDA_ICE_Tutorial/fig_1_1.png]]
*Abbildung 1.1: 3D-Modell Aussen*

![[data/assets/IDA_ICE_Tutorial/fig_1_2.png]]
*Abbildung 1.2: Foto Aussenfassade*

![[data/assets/IDA_ICE_Tutorial/fig_1_3.png]]
*Abbildung 1.3: Bauplan EG*
### 1.2 Modell Aufbau - Variante 0 - Step-by-Step
Im folgenden wird die Variante 0 (Siehe Tabelle ??) Schritt für Schritt aufgebaut. Variante
0 bedeutet der Ist-Zustand des Gebäudes inklusive Öl-Heizung und Radiatoren. Vorerst wird
das Gebäudemodell aber ohne Diese Heizungselemente erstellt. Stattdessen werden ideale
Heizelemente in die Zonen eingebaut, in denen im echten Gebäude Radiatoren vorhanden
sind. Später, im Kapitel 1.3.3, wird das Heizungssystem dimensioniert und schliesslich auch
simuliert.
1. Bestandsgebäude zeichnen
Als Ausgangspunkt dient ein Bestandsgebäude“ der Schweizer Lokalisierung“ [3]. Dieses
wird mit einem Klick auf das Symbol in Abbildung 1.4 initialisiert. (Im Rahmen von Effiwag werden keine neuen Gebäude untersucht. Daher zählen alle analysierten Gebäude zur
Kategorie Bestandsgebäude“).
> *Abbildung 1.4: Wählen Bestandsgebäude – im PDF nur als Vektorgrafik vorhanden*

2. Vorgabewerte
Im Tab Allgemein“ unter Vorgabewerte das Zonenmodell Vereinfacht“ wählen. Siehe Ab-
bildung 1.5. Die Bauteile wurden gemäss der Abbildung gewählt. Dabei sind gelb markierte
Bauteile solche die selbst zusammengestellt und nicht aus der SIA Datenbank gewählt sind.
Die Definitionen der eigenen Bauteile sind in Anhang ?? gezeigt.
3. Wärmebrücken
> 📖 Theorie: [[03_1_2_waermedurchgang_waermeleitung|Bauphysik Kap. 3.1–3.2 – Wärmefluss & Wärmeleitung]]

Eswurdegemeinsammit Lemonconsultentschieden,dass Wärmebrückenfürdie Gebäudemodelle
im Effiwagprojekt nicht simuliert werden. Siehe dazu Mail Konversation in Anhang ??. Entsprechendwirdunter Wärmebrückendie Optionobenrechts Wandvolumenerhalten“gewählt.
Siehe Abbildung 1.6. Es sollten dann alle Werte der Wärmebrücken auf 0 gesetzt sein, auch
die, die in der Abbildung nicht zu sehen sind (Symbolisiert mit dem gelben Pfeil nach unten).
4. Infiltration
> 📖 Theorie: [[02_1_schadstoffabfuhr_luftfuehrung|Lüftung Kap. 2.1 – Schadstoffabfuhr & hygienischer Luftwechsel]]  ·  [[05_3_4_lufterneuerung_radon|Bauphysik Kap. 5.3–5.4 – Lufterneuerung & Infiltration]]

Laut SIAMerkblatt2024[1],istder Aussenluft-Volumenstromdurch Infiltrationwieim Printscreen in Abbildung 1.7 definiert. Dabei ist 0.15m3/(m²h) = 0.04166L/(m²s).
Tipp: Volumenstrom Masseinheiten können mittels einer Maske umgerechnet werden.
Siehe Abbildung 1.24.
Da an der Waffenplatzstrasse die Fenster nach dem Jahr 2000 ersetzt wurden, haben wir
entschieden für die Infiltration, den Standard-Wert und nicht den Wert für Bestand für die
Infiltration zu verwenden. Ausgenommen ist das Dachgeschoss, da das Dach nur aus Ziegeln
auf einem Lattenrost besteht und deswegen im Dachgeschoss mit erheblicher Infiltration zu
rechnen ist. Ausserdem wird bei der Variante 1 auch im obersten bewohnten Stockwerk der
Wertfür Bestand“verwendet,weilder Bodenim Dachgeschossbei Variante1nichtgedämmt
ist und erfahrungsgemäss die Infiltration an solchen Stellen hoch ist. Siehe dazu die Email
Unterhaltungmit Lemonconsultim Anhang??.Dieglobale Infiltrationwirdwiein Abbildung
1.8 eingegeben. Bei Variante 1 wird später in den Zonen im obersten Geschoss die Infiltration
auf den Bestand Wert eingestellt. Mehr dazu unter Erstellen von Variante 1“ im Kapitel
1.3.2.
