---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.2b"
titel: "Variante 0 Step-by-Step – Gebäudegeometrie & Zonen"
---

# Kap. 1.2b – Variante 0 Step-by-Step – Gebäudegeometrie & Zonen

> ◀ [[01_2a_Variante0_Schritte1_7|Kap. 1.2a]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_2c_Variante0_Simulation|Kap. 1.2c]] ▶

---

> 📖 Manual: [[03_4_Building_Geometry|IDA ICE Manual Kap. 3.4 – Building Geometry: CAD & IFC Import]]  ·  Solar: [[03_3_1_zone_intro_solar|IDA ICE Manual Kap. 3.3–3.4 – Zone Models & Solar Radiation]]

![[data/assets/IDA_ICE_Tutorial/fig_1_16.png]]
*Abbildung 1.16: Printscreen Tabelle 1 SIA 2024*
Die Folgende Listezeigtdieim Modellder Waffenplatzstrassevorhandenen Niveaus(Stockwerke)unddiedazugehörigen Zonen.Beachte:Zonenin OG1bis OG3sindidentischmitdenen
in Zone 0. Ausserdem: Zone Treppenhaus reicht von Niveau 0 bis 10.7 m.
• Niveau 13.5 m: Dachgeschoss
• Niveau 10.7 m: OG3
• Niveau 7.9 m: OG2
• Niveau 5.1 m: OG1
• Niveau2.3m:WoZi S OG0, Kue S OG0, SZ1 S OG0, SZ2 S OG0, Gang S OG0, Bad S OG0,
WoZi W OG0, Kue W OG0, SZ1 W OG0, SZ2 W OG0, Gang W OG0, Bad W OG0
• Niveau 0 m: Keller MitDaemm, Keller OhneDaemm, Treppenhaus
Die Zonenindenvier Wohngeschossen,wurdenmit Hilfeder Bauplänebenannt.Ein Blick
aufdieeingezeichneten Möbelund Inventarim Bauplanin Abbildung1.3offenbartdie Einteilung. Die Zonen werden ausserdem jeweils einer Gruppe gemäss der Liste in Abbildung 1.18
zugeteilt. Um eine Neue Gruppe zu erstellen, kann in das Feld des Drop-Down Menus auch
reingeschrieben werden. Die Gruppen sind nützlich, um in Listen die Übersicht zu behalten.
Zonen Zeichnen - UG
Wir beginnen im UG mit den Keller Zonen. Wie in Abbildung 1.19 ersichtlich, ist der Keller
in zwei Zonen unterteilt und befindet sich auf dem Niveau 0 m. Eine Zone hat im Rahmen
einer energetischen Sanierung eine Dämmschicht an der Kellerdecke erhalten (roter Rahmen)
und eine nicht (grüner Rahmen).
Wir zeichnen drei Zonen gemäss Abbildung 1.17. Die beiden Kellerzonen mit der 1.1
Wohnen MFH Bestand“ Vorlage und das Treppenhaus mit 12.3 Treppenhaus Bestand“. Die
Zonen benennen und der Gruppe zuordnen (Abbildunf 1.18.
Achtung: Wenn eine Zone fertig gezeichnet ist, werden im Hintergrund flächenabhängige
Parameterder Vorlageentsprechendder Flächeder Zoneautomatischparametrisiert.Ein Beispiel:Anzahl Personenim Raumpro Quadratmeter.Wirdeine Zoneim Nachhineinverändert,
z.B. durch drag & drop mit der Maus, werden die Parameter nicht mehr automatisch aktualisiert obwohl sich die Fläche der Zone verändert hat!
Um dies zu verhindern, folgendermassen vorgehen: Nachdem eine Zone verändert wurde,
die Zone mit der Maus anwählen (sie wird rot im Geschossplan), anschliessen die Zonenvorlage im Drop-down menu neben der Schaltfläche Neue Zone“ erneut auswählen und dann,

ebenfalls im drop-down menu, auf Ausgewählte Zonen Definitionen der aktuellen Zonenvorlage zuordnen“ klicken. Jetzt sind die flächenabhängigen Parameter der neuen Zonenfläche
entsprechend aktualisiert. Mehr Details dazu unter Punkt 2.1 Internal Gains“ im Anhang
??.
![[data/assets/IDA_ICE_Tutorial/fig_1_17.png]]
*Abbildung 1.17: Zonen UG*

![[data/assets/IDA_ICE_Tutorial/fig_1_18.png]]
*Abbildung 1.18: Name Zonen*

![[data/assets/IDA_ICE_Tutorial/fig_1_19.png]]
*Abbildung 1.19: Bauplan UG*
Zonen Anpassen - UG

Abbildung 1.20 zeigt die Kellerzone mit gedämmter Decke. Die Decke anklicken und Bauteil entsprechend auswählen. Die Bauteildefinition ist im Anhang ?? beschrieben. Interne
Wärmequellen löschen, ausser Personen. Es sollte eine Personengruppe in jeder Zone vorhandenseinumgewisse Resultateim Zusammenhangmit Operativer Temperatur“zuberechnen.
Fürweitere Informationeninder IDAICEHilfenach Index Operativetemperatures“suchen.
Falls im Raum aber eigentliche keine Personen simuliert werden sollen, kann die Gruppe auf
0 Personen gesetzt werden. Lokale Heiz- und Kühlelemente löschen, denn im Keller gibt es
keine Wärmeabgabe-Elemente.
Fenster im Keller sind Standard SIA Fenster mit Verglasung und Parameter wie in Abbildung 1.21 gezeigt. Zur Vereinfachung wurde die Fläche aller Fenster in einem Fenster pro
Aussenfläche zusammengefasst.
Türen werden aus dem selben Material wie die Wandkonstruktion simuliert (siehe Abbildung 1.5 bei Vorgabewerte Bauteil Tür). Ausserdem folgen sie dem Zeitplan immer geschlossen“. Im Unterschied zur Wandkonstruktion, stellen Türen eine Undichtigkeit dar.
Abbildung 1.22 zeigt die Kellerzone ohne Dämmung in der Decke. Bauteilkonstruktion
entsprechend auswählen.
Abbildung 1.23 zeigt die Zone Treppenhaus“. Höhe eingeben, Heizung und Kühlung
löschen und Deckenkonstruktion ändern. Alles andere wird von der Zonenvorlage ohne Anpassung übernommen.
![[data/assets/IDA_ICE_Tutorial/fig_1_20.png]]
*Abbildung 1.20: Zone UG mit gedämmter Decke*

![[data/assets/IDA_ICE_Tutorial/fig_1_21.png]]
*Abbildung 1.21: Fenster in Zone UG mit gedämmter Decke*

![[data/assets/IDA_ICE_Tutorial/fig_1_22.png]]
*Abbildung 1.22: Zone UG ohne gedämmter Decke*

![[data/assets/IDA_ICE_Tutorial/fig_1_23.png]]
*Abbildung 1.23: Zone Treppenhaus*
Information zur Belüftung: Die Zuluft- und Abluftvolumenströme unter Meschanische
Belüftung, Infiltration“ stammen aus der SIA 2024 und entsprechen dem sogenannten hygienebedingten Aussenluftvolumenstrom. Näheres dazu unter Punkt 5. Lüftungsgerät“. Die
Zusätzliche In-/Exfiltration“ wird aus dem Vorgabewert (Abbildung 1.8) übernommen.
Tipp Umrechnung Volumenstrom“: Zur Umrechnung der Masseinheiten von Volumenströmen kann eine Maske verwendet werden, die in den Zonen-Fenstern verfügbar ist.
Dazu eine Zone öffnen und die Masseinheit eines Volumenstroms im Bereich Mechanische
Belüftung, Infiltration“ anklicken. Dabei Öffnet sich die Maske, die in Abbildung 1.24 dargestellt ist.

![[data/assets/IDA_ICE_Tutorial/fig_1_24.png]]
*Abbildung 1.24: Umrechnung Volumenstrom*
Zonen Zeichnen - OG0 bis OG3
Die vier bewohnten Stockwerke sind alle gleich aufgebaut. Alle Zonen werden mit der Zonenvorlage 1.1 Wohnen MFH Bestand“ gezeichnet. Sie befinden sich auf den Niveaus: 2.3m,
5.1m, 7.9m und 10.7m. Um das Niveau 2.3m für das EG zu erstellen, auf Niveau klicken und
2.3m in die Drop-Down Maske eingeben. Siehe Abbildung 1.25. Es gibt pro Stockwerk zwei
Wohnungen, eine Süd und eine West. Das EG Stockwerk wird gezeichnet und anschliessend
auf die anderen Niveaus kopiert. Die Benennung der Zonen erfolgt in einer Art und Weise, dass die Nummerierung beim Kopieren fortlaufend erhöht wird. Beispielsweise heisst das
Wohnzimmer in der West-Wohnung im EG: WoZi W OG0. Diese Zone befindet sich auf dem
Niveau 2.3m, was dem EG entspricht. Wird die Zone auf das Niveau 5.1m kopiert, heisst
die Kopie automatisch WoZi W OG1. Auf dem Niveau 7.9m WoZi W OG2 usw. Kopieren und
einfügen erfolgt wie gewohnt, mit ctrl+c und ctrl+v.
Bevordie Zonenkopiertundaufeinemneuen Niveaueingefügtwerden,stellenwirerstdas
komplette OG0 Stockwert fertig. Danach kopieren wir alle Zonen des Stockwerks gemeinsam.

![[data/assets/IDA_ICE_Tutorial/fig_1_25.png]]
*Abbildung 1.25: Zonen EG*

Zonen Anpassen - OG0 bis OG3
Inden Zonenalle Kühlgerätelöschen.Ausserdemdieidealen Heizgeräteinden Zonenlöschen,
in denen gemäss dem Bauplan in Abbildung 1.3 keine Radiatoren verbaut sind.
Tipp 1 Listen“: Die Listen im Tab Allgemein“ können eine grosse Erleichterung
sein, wenn viele Daten auf einmal geändert werden müssen. Auf die Liste Lokale Heiz/Kühlelemente“ klicken und nach Typ sortieren um alle Kühlgeräte auf einmal zu löschen.
Nach Gruppe“Sortierenunddie Heizelementeder Zonenlöschen,indenenimechten Gebäude
keine Radiatoren verbaut sind. Siehe Abbildung 1.26.
Für die Masse der Fenster diente der Lieferschein der Fenster, die im Jahr 2006 eingebaut
wurden. Ausserdem die Fotos und Baupläne des Gebäudes. Die Fenster wurden definiert wie
in Abbildung 1.27 zu sehen. Die Glaskonstruktion ist im Anhang in Abbildung ?? gezeigt.
Der U-Wert von Rahmen sowie von der Glaskonstruktion stammen aus dem Dokument von
Lemonconsult in Anhang ??, Punkt 1.8. Fenster. Die Berechnung des Rahmenanteils ist im
Anhang in Abbildung ?? gezeigt.
An dieser Stelle kann das komplette OG0 auf OG1 bis OG3 kopiert werden. Dazu alle
Zonen im OG0 markieren und kopieren. Neues Niveau eingeben und einfügen.
![[data/assets/IDA_ICE_Tutorial/fig_1_26.png]]
*Abbildung 1.26: Liste der Lokalen Heiz- und Kühlgeräte*

![[data/assets/IDA_ICE_Tutorial/fig_1_27.png]]
*Abbildung 1.27: Fenster OG*

Dachgeschoss
Auch das Dachgeschoss wird mit der Zonenvorlage 1.1 Wohnen MFH Bestand“ gezeichnet.
Abbildung 1.28 zeigt wie die Zone zu bearbeiten ist. Die Zone ist so gross wie die gesamte Grundfläche. Heizung und Kühlung löschen, Personengruppe auf 0 setzen und die Höhe
bis zum Dach eingeben. Das Dach besteht nur aus Latten und Ziegeln. Deswegen wird die
Infiltration nicht aus den Standardwerten übernommen (0.04166L/(m²s)) sondern manuell
eingegeben. Sie wird erhöht auf 0.08333L/(m²s), was dem Wert für MFH Wohnen Bestand“ entspricht. Siehe dazu Punkt 4. Infiltration“. Den Boden der Zone anwählen und als
Boden Estrich Gedaemmt definieren (Abbildung 1.29).
Die Zone wird Dachgeschoss“ genannt und der Gruppe Dachgeschoss“ zugeordnet.
![[data/assets/IDA_ICE_Tutorial/fig_1_28.png]]
*Abbildung 1.28: Zone Dachgeschoss*

![[data/assets/IDA_ICE_Tutorial/fig_1_29.png]]
*Abbildung 1.29: Boden Zone Dachgeschoss*
10. Anpassen der Bauteilkonstruktion zwischen Nachbarzonen
Die Voreingestellte Konstruktion für Zwischenböden ist Boden OG innen (Siehe Abbildung
1.5). Diese Bodenkonstruktion passt nicht zur Kellerdecke und ebenso wenig zum Boden im
Dachgeschoss. Deswegen muss im OG0 der Boden und im OG3 die Decke wie folgt angepasst
werden.
Die Bodenkonstruktion der Zonen im OG0, muss gleich sein wie die Deckenkonstruktion
der Kellerzone darunter. Der Boden der Zone WoZi W OG0 ist besonders, denn die Zone steht
sowohl auf der gedämmten Kellerzone wie auch auf der ungedämmten. Der Boden der Zone
