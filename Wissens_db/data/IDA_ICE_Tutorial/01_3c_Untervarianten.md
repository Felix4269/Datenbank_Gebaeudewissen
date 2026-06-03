---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.3.3"
titel: "Untervarianten l, s, hl, hs, fl und fs"
---

# Kap. 1.3.3 – Untervarianten l, s, hl, hs, fl und fs

> ◀ [[01_3b_Basisvarianten|Kap. 1.3.2]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_4a_Heizlast_Systemnachweis|Kap. 1.4.1–2]] ▶

---

#### 1.3.3 Untervarianten l, s, hl, hs, fl und fs
Die Untervariantenunterscheidensichdurchunterschiedliche Wärmeerzeugerund Wärmeabgabesysteme.
Wie in Tabelle ?? gezeigt, steht l für Luft-Wasser Wärmepumpe, s steht für Sole-Wasser
Wärmepumpe, h für Niedertemperatur Radiatoren und f für Fussbodenheizung.
Bevordie Heizungssystemedimensioniertwerdenkönnen,musserstmitden Basisvarianten
mitidealen Heizelementendie Heizlastermitteltwerden.Die Resultateausder Heizlastsimulation können dann verwendet werden um die Untervarianten zu erstellen. Der nächste logische
Schritt in der Abfolge, vor der Erstellung der Untervarianten, ist entsprechend Kapitel 1.4.1.
Aus den Resultaten der Heizlastermittlung (Kapitel 1.4.1) folgen die Heizlasten pro Zone,
sowie die zu verwendenden Vor- und Rücklauftemperaturen. Die Resultate sind in Kapitel ??
zufinden.Entsprechendwerdendie Wärmeerzeugerund Wärmeabgabesystemedimensioniert.
Um beispielsweise die Untervariante Wpl77 simpl Var0l zu erstellen, öffnet man die Basisvariante Wpl77 simpl Var0 und fügt eine Wärmepumpe mit 25kW wie in Abbildung 1.50
gezeigt ein. Die Datei nun als Variante“ von Wpl77 simpl Var0 speichern. Wenn man das
Difference“ Skript bereits besitzt, kann man die Untervariante auch direkt durch Eingabe
des Skripts bei Difference“ (Abbildung 1.41) erzeugen.
1. Einfache Radiatoren (Untervarianten l und s)
Wenn von einem Radiator keine genauen Parameter vom Hersteller bekannt sind, kann er
durchein Vereinfachtes Modelldimensioniertwerden.Dortwoimechten Gebäude Radiatoren
vorhandensind,werdenauchim Modell Radiatorenindie Wändeeingebaut.Siehe Abbildung
1.47.
Abbildung 1.48 zeigt die Dimensionierung eines Radiators. Der Radiator wird anhand der
Heizlast der Zone, der Vorlauf- und Rücklauftemperatur sowie der Solltemperatur im Raum
dimensioniert. Ausserdem wird der Regler auf operative Temperatur eingestellt. Der N-Wert
wirdfürunbekannte,ältere Radiatorenauf1.28belassen.Fürneue Radiatorenkann1.3eingesetzt werden. Anhand der Eingaben, stellt sich der Massenstrom für den Nennbetriebspunkt
ein.
Die Dimensionierung in Abbildung 1.48 stammt aus den Resultaten für Bad Wohnung
Süd“ der Variante 1 in Kapitel ??. Die Lufttemperatur wird auf 21◦C eingestellt, da dies dem
Sollwert der SIA Zonenvorlage entspricht.

![[data/assets/IDA_ICE_Tutorial/fig_1_47.png]]
*Abbildung 1.47: Radiator in Wand einbauen*

![[data/assets/IDA_ICE_Tutorial/fig_1_48.png]]
*Abbildung 1.48: Einfacher Radiator Dimensionieren*
2. Niedertemperatur Radiatoren (Untervarianten hl und hs)
Im Unterschiedzudeneinfachen Radiatorenwirdhierder NExponent1.3gewählt.Ausserdem
wird die Vor- und Rücklauftemperatur entsprechend den Resultaten in Kapitel ?? angepasst.
3. Bodenheizung (Untervarianten fl und fs)
Abbildung 1.49 zeigt die dimensionierung der Bodenheizung in Bad Südwohnung“ Variante
1. Nachdem die Bodenheizung in den Boden eingefügt wurde (Boden öffnen, Palette, Heizen/Kühlen Bauteil“ auswählen), kann per Rechtsklick auf die Bodenheizung Öffnen mit /

Geometrie“ die Masse eingegeben werden. Die Masse wurden so eingegeben, dass die Bodenheizung zu allen Wänden 0.1m Abstand hat.
Die Leistung entspricht, wie bei den Radiatoren, der Heizlast aus den Resultaten. Der
Regler wurde auf PI belassen und Operative Temperatur wurde gewählt. Laut dem Equa
Support, sind 3-Wege Ventile in der Schweiz unüblich, weshalb 2-Wege Ventile ausgewählt
wurde. Die Einbautiefe beträgt nur 1cm um sicherzustellen, dass die Rohre innerhalb der
obersten Holzschicht zu liegen kommen und nicht in der darunterliegenden Luftschicht. Nach
Absprache mit Lemonconsult wurde der Wert für H-Wasser-Rohr-Rippe eher Hoch gewählt,
damit dieser nicht dominant wirkt.
![[data/assets/IDA_ICE_Tutorial/fig_1_49.png]]
*Abbildung 1.49: Dimensionierung Bodenheizung*
4. Luft-Wasser WP (Untervarianten l, hl und fl)
Wird eine LuWa-WP eingebaut, ist diese anhand der Heizlastermittlung des Gebäudes zu dimensionieren. Dabei wird die Leistung der WP aufgerundet. So wird in Variante 0l beispielsweise eine LuWa-WP mit 25kW eingebaut, denn die Heizlast des Gebäudes beträgt 24.6kW.
Genauso wird auch der Pufferspeicher anhand der Resultate dimensioniert. Für Variante 0
beispielsweise, ist der Speicher 2.2m3 gross. Siehe Abbildung 1.50.

![[data/assets/IDA_ICE_Tutorial/fig_1_50.png]]
*Abbildung 1.50: Einfügen einer 25kW LuWa-WP und Pufferspeicher*
5. Varianten mit Öl-Heizung
Varianten mit Ölheizung werden analog zu Varianten mit LuWa-WP erzeugt. Es ist statt der
Ambient air to water heat pump“ der Generic topup heater“ zu wählen.
6. Sole-Wasser WP (Untervarianten s, hs und fs)
> 📖 Norm: [[_SIA_384-6_2021_MOC|SIA 384/6:2021 – Erdwärmesonden]]  ·  [[03_1_anforderungen_auslegung|Kap. 3.1 – Anforderungen Auslegung]]

Die SoWa-WP wird analog zur LuWa-WP dimensioniert. Es wird zusätzlich eine Erdsonde
mit Anzahl Sonden gemäss den Resultaten der Heizlastermittlung (Kapitel ??) eingefügt. Die
Bohrlochtiefe ist eine Angabe von Lemonconsult für den Standort Zürich. Das ESBO Modell
der SoWa-WP ist in Abbildung 1.51 dargestellt.

![[data/assets/IDA_ICE_Tutorial/fig_1_51.png]]
*Abbildung 1.51: Einfügen einer 25kW SoWa-WP und Pufferspeicher*
7. Heizkurve (Alle Untervarianten)
Die Heizkurve wird mittels doppelklick auf Distribution systems Heat“ (Unten im ESBO
Modell in Abbildung 1.50) geöffnet. Die Werte sind je nach Variante anzupassen anhand der
Vorlauftemperaturen von Lemonconsult in den Resultaten (Abbildung ??).
Für den Standort Zürich, wird die untere Temperaturgrenze auf −8◦C gesetzt. Das Beispiel in Abbildung 1.52 zeigt die Vorlauftemperatur von 61◦C, was der Variante 0 entspricht.
Des weiteren ist die Nachtabsenkung ausgeschaltet, und der AHU Sollwert“ auf 20◦C eingestellt. Dies verhindert, dass warmes Wasser für die Heizung der Lüftung bereitgestellt wird,
denninunserem Fallistsoeine Lufterwärmungnichtvorhanden.Der Eintragbei Temperaturabfall Raumauslegung“ sollte beim Verwenden von Radiatoren oder Bodenheizungen in den
Zonen, keinen Einfluss haben. Siehe dazu das ESBO Manual [5] bei Figure 49. Trotzdem wird
der Wert hier so gesetzt, dass die Rücklauftemperatur mit den Angaben von Lemonconsult
übereinstimmt.

![[data/assets/IDA_ICE_Tutorial/fig_1_52.png]]
*Abbildung 1.52: Vorlauftemperatur und Heizkurve*
### 1.4 Simulationen
#### 1.4.1 Heizlastermittlung
Die Basisvarianten 0,1,2 und 3 werden verwendet um mit den idealen Heizelementen die
Heizlast der einzelnen beheizten Zonen zu ermitteln. Die Summe aller Zonenheizlasten ist
die Heizlast des Gesamtgebäudes. Die Resultate der Simulation dienen Lemonconsult um
Vor- und Rücklauftemperaturen der unterschiedlichen Wärmeabgabesystemen in den Varianten zu bestimmen. Mit den Werten der Vor- und Rücklauftemperaturen können wir dann
in IDA ICE die Heizungssysteme (Untervarianten l, s, hl, hs, fl und fs) dimensionieren und schlussendlich Jahresenergie Bedarf von unterschiedlichen Wärmeabgabe- und
Wärmeerzeugersystemen simulieren.
Die Simulation zur Heizlastermittlung kann in IDA ICE aus dem SIA Tab gestartet werden. Mehr Informationen dazu im Handbuch der Schweizer Lokalisierung [3] (Kapitel 5.2
Heizlastermittlung (SIA 380/2:2022– 4.2)). Es wurde festgestellt, dass die Simulation beim
verwenden dieser Methode nicht lange genug einschwingt. In den Resultaten war die Lufttemperatur in unbeheizten Zonen zu Beginn unrealistisch hoch und sank kontinuierlich über die
Simulationsperiode (4 Tage im Januar).
Die Simulation wurde deshalb nicht aus dem SIA Tab gestartet. Es wurde die Simulation
aus dem Simulation Tab verwendet und gemäss den Abbildungen 1.53 und 1.54 eingestellt.
Die maximale Anzahl Perioden wurde auf 30 gesetzt. Dies garantiert ein genügend langes
Einschwingen bzw. einen stationären Zustand zu Beginn der Simulation.
Bei der Klimadatei wurde die SIA Datei der Auslegungsperiode für Gebäudeheizung des
entsprechenden Standortes gewählt. Eine Tabelle aller SIA Klimadateien ist in [3] (Kapitel
2.2.1 Spezielle Auslegungsperioden) verfügbar.
Wenn die Heizlast ermittelt wurde, kann im Tab Zusammenfassung“ nach Zonen sortiert
werden und die Resultate mittels klick auf Bericht“ exportiert werden. In der Spalte Lokale
