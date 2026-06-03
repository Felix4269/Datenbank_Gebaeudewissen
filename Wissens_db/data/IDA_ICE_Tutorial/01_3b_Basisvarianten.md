---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.3.2"
titel: "Basisvarianten 1, 2, 3 und 4"
---

# Kap. 1.3.2 – Basisvarianten 1, 2, 3 und 4

> ◀ [[01_3a_Varianten_Erstellen|Kap. 1.3]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_3c_Untervarianten|Kap. 1.3.3]] ▶

---

> 📖 Theorie: [[02_Waermeverluste_Trans|Bauphysik Kap. 2 – Wärmedämmung & U-Wert-Anforderungen]]  ·  [[04_Heizwaermebedarf|Skript Energie Kap. 4 – Heizwärmebedarf & Einfluss der Gebäudehülle]]

1. Erstellen von Variante 1
Als erstes wird ein neues Projekt erstellt indem das Simulationsmodell von Variante 0 über
Datei / Speichern als Variante...“ mit Namen Wpl77 simpl Var0 gespeichert wird. Der Eintrag von Variante 0 im Projekt Manager wird geöffnet, wieder als Variante gespeichert und
Wpl77 simpl Var1 genannt. Var1 ist nun als Untervariante von Var0 gespeichert. Mit der
Maus kann Var1 im Projektmanager nach links gezogen werden und wird somit selbst zu
einer Basis“.
Achtung: Im Moment wo eine Untervariante zu einer neuen Basis gemacht wird, wird
das Difference“ Skript gelöscht. In unserem Fall war es sowieso leer, da wir bislang Var1
gegenüber Var0 nicht verändert haben.
Die folgende Liste beinhaltet Unterschiede von Variante 1 zu Variante 0. Die Bauteilkonstruktionen sind in Anhang ?? gelistet.
1. Decke Keller:
(a) Var0: Unterteilt in Decke UG MitDaemm und Decke UG OhneDaemm
(b) Var1: Komplett Decke UG OhneDaemm
2. Boden Dachgeschoss:
(a) Var0: Boden Estrich Gedaemmt
(b) Var1: [Voreinstellung] Boden OG innen
3. Infiltration in allen Zonen im OG3:
(a) Var0: 0.04166L/(m²s)
(b) Var1: 0.08333L/(m²s)
2. Erstellen von Variante 2
Gleich wie oben bei Variante 1, wird auch für Variante 2 eine neue Basis erstellt mit dem
Namen Wpl77 simpl Var2. Die Bauteile in Variante 2, die gegenüber Variante 0 verbessert
werden, werden so zusammengestellt, dass der U-Wert unter dem Grenzwert des Einzelbauteilnachweises [2] liegt. Die Grenzwerte sind in der Abbildung 1.46 gezeigt. Die neuen Bauteildefinitionen, die sich von Variante 0 unterscheiden, sind im Anhang in Kapitel ?? gelistet.
Die folgende Liste zeigt die Unterschiede von Variante 2 gegenüber Variante 0 auf.
1. Decke Keller:
(a) Var0: Unterteilt in Decke UG MitDaemm und Decke UG OhneDaemm
(b) Var2/Var3: Komplett Decke UG Daemm Var2 3
2. Boden Dachgeschoss:
(a) Var0: Boden Estrich Gedaemmt
(b) Var2/Var3: Boden Estrich Daemm Var2 3
3. Fenster und Glas (Ausgenommen im Keller):
(Der gesamt U-Wert der Fenster ist sichtbar in der Liste Fenster“ im Tab Allgemein“)
(a) Var0: Gemäss Abbildung ??
Gesamt U-Wert für das Fenster (Glas und Rahmen) = 1.218W/(m²K)

(b) Var2/Var3: Gemäss Abbildung ??
Gesamt U-Wert für das Fenster (Glas und Rahmen) = 1.0W/(m²K)
![[data/assets/IDA_ICE_Tutorial/fig_1_46.png]]
*Abbildung 1.46: Tabelle Einzelbauteilnachweis aus [2]*
3. Erstellen von Variante 3
Gleich wie oben bei Variante 1, wird auch für Variante 3 eine neue Basis erstellt mit dem
Namen Wpl77 simpl Var3. Der einzige Unterschied von Variante 3 zur Variante 2, ist eine
zusätzliche Dämmschicht von 5cm an der Aussenfassade. Die Bauteildefinition der Aussenwand ist gemäss Abbildung ?? im Anhang. In der Praxis wäre die Dämmschicht ein sogenannter Dämmputz. Eine andere Art der Dämmung der Aussenmauern ist für die Waffenplatzstrasse nicht realistisch, weil das Aüssere des Gebäudes geschützt ist vom Ortsbildschutz
und der Wohnraum innen zu kostbar um innen Dämmung anzubringen.
Die folgende Liste zeigt die Unterschiede von Variante 3 gegenüber Variante 0 auf. Bauteildefinitionen sind im Anhang ??.
1. Decke Keller:
(a) Var0: Unterteilt in Decke UG MitDaemm und Decke UG OhneDaemm
(b) Var2/Var3: Komplett Decke UG Daemm Var2 3
2. Boden Dachgeschoss:
(a) Var0: Boden Estrich Gedaemmt
(b) Var2/Var3: Boden Estrich Daemm Var2 3
3. Fenster und Glas (Ausgenommen im Keller):
(Der gesamt U-Wert der Fenster ist sichtbar in der Liste Fenster“ im Tab Allgemein“)

(a) Var0: Gemäss Abbildung ??
Gesamt U-Wert für das Fenster (Glas und Rahmen) = 1.218W/(m²K)
(b) Var2/Var3: Gemäss Abbildung ??
Gesamt U-Wert für das Fenster (Glas und Rahmen) = 1.0W/(m²K)
4. Aussenwand:
(a) Var0: Aussenwand Backstein OhneDaemm (Abbildung ??)
(b) Var3/Var4: Aussenwand Backstein Daemmputz (Abbildung ??)
4. Erstellen von Variante 4
Auch Variante4isteineeigene Basis“Variante.Bei Variante4werdendie Deckeim OG3(Decke zum Dachboden) und die Kellerdecke nochmals zusätzlich gedämmt gegenüber Variante
2/3. Die Dämmschicht wird erhöht auf 30cm Dämmmaterial. Ausserdem werden die Fenster
verbessert und haben einen gesamt U-Wert (Fensterglas und Rahmen) von nur 0.7W/(m²K).
Die Aussenwand hingegen wird so belassen wie bei Variante 3. Ziel von Variante 4 ist die
Bauteile, die realistischerweise energetisch saniert werden können, so weit zu verbessern, bis
der Systemnachweis nach SIA 380/1 [4] erfüllt ist. Die Variante 4 wird nur dazu verwendet
im SIA“ Tab den Systemnachweis zu erstellen. Mehr dazu im Kapitel 1.4.2.
Die folgende Liste zeigt die Unterschiede von Variante 4 gegenüber Variante 0 auf. Bauteildefinitionen sind im Anhang ??.
1. Decke Keller:
(a) Var0: Unterteilt in Decke UG MitDaemm und Decke UG OhneDaemm
(b) Var4: Komplett Decke UG Daemm Var4 Systemnachweis
2. Boden Dachgeschoss:
(a) Var0: Boden Estrich Gedaemmt
(b) Var2/Var3: Boden Estrich Daemm Var4 Systemnachweis
3. Fenster und Glas (Ausgenommen im Keller):
(Der gesamt U-Wert der Fenster ist sichtbar in der Liste Fenster“ im Tab Allgemein“)
(a) Var0: Gemäss Abbildung ??
Gesamt U-Wert für das Fenster (Glas und Rahmen) = 1.218W/(m²K)
(b) Var4: Gemäss Abbildung ??
Gesamt U-Wert für das Fenster (Glas und Rahmen) = 0.7W/(m²K)
4. Aussenwand:
(a) Var0: Aussenwand Backstein OhneDaemm (Abbildung ??)
(b) Var3/Var4: Aussenwand Backstein Daemmputz (Abbildung ??)
