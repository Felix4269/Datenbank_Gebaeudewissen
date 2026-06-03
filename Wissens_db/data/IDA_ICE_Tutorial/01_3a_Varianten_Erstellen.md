---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.3"
titel: "Varianten Erstellen – Grundlagen & Projektmanager"
---

# Kap. 1.3 – Varianten Erstellen – Grundlagen & Projektmanager

> ◀ [[01_2d_Kalibrieren|Kap. 1.2.1]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_3b_Basisvarianten|Kap. 1.3.2]] ▶

---

### 1.3 Varianten Erstellen
> 📖 Theorie: [[06_1_berechnung_energiebedarf|Skript Energie Kap. 6.1 – Berechnung Energiebedarf]]  ·  Manual: [[04_Getting_Started_Advanced|IDA ICE Manual Kap. 4 – Getting Started Advanced Level]]

Nachdemdie Variante0kalibriertwurde,könnendarausdie Gebäudehüllender Varianten1,2
und3gemässder Tabelle??erstelltwerden.Ausserdemdie Variante4fürden Systemnachweis
nach SIA 380/1. Das Vorgehen wird im folgenden erklärt.
#### 1.3.1 Projektmanager
Eine IDA ICE Datei kann über Datei / Speichern als Variante...“ gespeichert werden. Dabei
wird ein neues IDA ICE Projekt erstellt. Es können nun aus einer Datei mehrere Untervarianten erzeugt werden. Abbildung 1.41 zeigt die Variante 0“, die im Kapitel 1.2 Schritt für
Schritt erstellt wurde. Ausserdem die Untervariante 0Test, die vorerst identisch ist mit der
übergeordneten Variante0.Manerkenntdies,wennmanmit Rechtsklickdas Difference Skript
anschaut. Es ist leer.
Wenn wir nun Variante 0Test über den Projektmanager öffnen und etwas darin ändern,
dann erscheint dies im Difference Skript. Als Beisiel bauen wir einen Wassergeführten Radiator ins Wohnzimmer West im OG0 ein und löschen dort das ideale Heizelement. Ausserdem
bauenwireine30kW Luft-Wasser Wärmepumpeundeinen2m3 Pufferspeicherein.Siehe Abbildungen 1.43 und 1.44. Nach dem Abspeichern der Variante 0Test“ erscheint die Änderung
im Difference Skript, wie in Abbildung 1.42 ersichtlich.
Achtung:Nichtzuviele Parameterändernin Untervarianten.Immersehrbewusst Änderungen
machenunddannspeichernunddas Difference Skriptanalysieren.Eswirdschnellunübersichtlich
und Fehleranfällig wenn zu viel an den Varianten geändert wird.
Weitere Informationen zum Projektmanager (Auch Versionsmanager) findet man in der
IDA ICE Hilfe in der Index Suche mit dem Schlüsselwort Version“.
![[data/assets/IDA_ICE_Tutorial/fig_1_41.png]]
*Abbildung 1.41: Projektmanager IDA ICE*

![[data/assets/IDA_ICE_Tutorial/fig_1_42.png]]
*Abbildung 1.42: Difference“ Skript nach Verändern der Variante 0Test“*
![[data/assets/IDA_ICE_Tutorial/fig_1_43.png]]
*Abbildung 1.43: Verändern der Variante 0Test“*

![[data/assets/IDA_ICE_Tutorial/fig_1_44.png]]
*Abbildung 1.44: Verändern der Variante 0Test“*
1. Projektmanager Waffenplatzstrasse 77
Die Philosophie bei der Waffenplatzstrasse im Effiwag Projekt ist eine übergeordnete Variante pro Gebäudehülle zu erstellen. Das heisst die Varianten 0 bis 4 sind jeweils eigene
Überkategorien. Als Untervarianten werden die unterschiedlichen Heizungssysteme gespeichert gemäss Tabelle ??. Abbildung 1.45 zeigt den Projektmanager der Waffenplatzstrasse.
Die Namen der Varianten setzen sich zusammen aus Wpl77 für Waffenplatzstrasse 77, simpl
wegen der vereinfachten Geometrie des Gebäudes, Var XY für die Variantennummer X und das
Heizungssystem Y.
Im Unterschied zur Anleitung in diesem Dokument, wurde beim Projekt in Abbildung
1.45 nicht mit den idealen Heizelementen begonnen, sondern mit wasserführenden Radiatoren. Deswegen ist die gelb markierte Variante, mit idealen Heizelementen, eine Unterkategorie
und keine Hauptkategorie. Dies ist im Nachhinein aber eine weniger logische Vorgehensweise
als mit den idealen Heizelementen zu beginnen, denn man braucht die Information der Simulation mit idealen Heizelementen um die Radiatoren zu dimensionieren. Die Untervarianten
ideal Heat“ wurden aus den Basisvarianten mit Hilfe des Skripts aus Anhang ?? erstellt.

![[data/assets/IDA_ICE_Tutorial/fig_1_45.png]]
*Abbildung 1.45: Projektmanager Waffenplatzstrasse*
2. Difference“ Skript Waffenplatzstrasse
Es gibt sechs Difference“ Skripte für die sechs Untervarianten ( l, s, hl, hs, fl und fs).
Dabei sind die Skripte fast identisch für eine Untervariante von Variante 1, 2 oder 3. Sie
unterscheiden sich lediglich in der maximalen Leistung des Wärmeerzeugers. Diese Leistung
ist angepasst an die Heizlast des Gebäudes. Beispielsweise wird die Leistung für Variante 1
auf 30kW eingestellt, weil das Gebäude eine Heizlast von 27.0kW aufweist (Siehe Resultate
in Kapitel ??). Die Skripte sind im Anhang ?? gelistet.
#### 1.3.2 Basisvarianten 1, 2, 3 und 4
Ander Waffenplatzstrassewurdendie Hauptvarianten,diesichinder Gebäudehüllevoneinander unterscheiden, jeweils als eigene Basis im Projektmanager gespeichert. Man erkennt dies
daran, dass sie im Hierarchiebaum ganz links stehen (Abbildung 1.45). Das ist im Nachhinein
eher nicht die beste Lösung, da die Unterschiede zwischen den Varianten so im Difference
Skript nicht ersichtlich sind. Das Difference Skript einer Basis“ ist nämlich immer leer. Die
Differenz wird dann jeweils für Untervarianten im Verhältnis zu derer Basis im Skript der
Untervarianten gespeichert.
Im Nachhinein wäre es sinnvoller gewesen, eine Basis zu bilden (Variante 0 mit idealen
Heizelementen) und daraus Variante 1, 2 und 3 als Untervariante zu bilden. Die unterschiedlichen Heizungssysteme (Untervarianten l, s, hl, hs, fl und fs) könnten dann wiederum
Untervarianten der Varianten 1 bis 3 sein. Der Hierarchiebaum hätte dann 3 Ebenen.
Im Folgenden wird das Vorgehen mit Varianten bei der Simulation der Waffenplatzstrasse
beschrieben, mit dem Wissen, dass es vermutlich nicht das beste Vorgehen ist.
