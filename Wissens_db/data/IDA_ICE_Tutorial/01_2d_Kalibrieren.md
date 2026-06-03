---
tags: [IDA-ICE, Tutorial, Simulation, Gebäudesimulation, SIA, ZHAW, Deutsch]
normnummer: "IDA ICE Tutorial ZHAW v1.1"
gueltig_ab: "2024-01-01"
kapitel: "Kap. 1.2.1"
titel: "Modell kalibrieren"
---

# Kap. 1.2.1 – Modell kalibrieren

> ◀ [[01_2c_Variante0_Simulation|Kap. 1.2c]]  ·  [[_IDA_ICE_Tutorial_MOC|↑ Inhaltsverzeichnis]]  ·  [[01_3a_Varianten_Erstellen|Kap. 1.3]] ▶

---

#### 1.2.1 Modell kalibrieren
> 📖 Fallstudie: [[_NEST_Sprint_MOC|NEST Sprint Simulation – Kalibrierung einer Büroetage (NEST Empa)]]  ·  Theorie: [[03_1_2_waermedurchgang_waermeleitung|Bauphysik Kap. 3.1–3.2 – U-Wert-Anpassung bei der Kalibrierung]]

Vonder Waffenplatzstrassesind Messdatender Ölheizungvorhanden,diezur Kalibrierungder
Variante 0 mit idealen Heizelementen, so wie sie im Kapitel 1.2 Schritt für Schritt aufgebaut
wurde, dienen. Bei der Ölheizung wurde im Zeitraum von 17. Januar bis 7. Februar 2023 die
abgegebene Heizleistunggemessen.Zusätzlichwurdeauchdie Aussentemperaturam Standort
gemessen. Der Messbericht ist im Anhang ??.
Abbildung 1.38 zeigt den Standort und das Klimafile. Das Klimafile, das für die Kalibrierung verwendet wurde, ist aus unterschiedlichen Quellen zusammengestellt. Unter anderem
ist die Aussentemperatur Messung vom Standort darin enthalten. Details sind im Anhang ??
beschrieben.
Eswirdeine Benutzerdefinierte Simulationgestartetmit Einstellungengemässe Abbildung
1.39.
Nach der Simulation wird die Heizleistung der idealen Heizelemente zur weiteren Analyse
exportiert.Das Vorgehenistwiefolgt(Abbildung1.40):1.Im Tab Details“aus Gesamtheiz-
und kühlleistung“ doppelklicken, 2. Im Diagramm auf den Legendeneintrag Ideale Heizelemente und andere lokale Elemente, W“ doppelklicken. 3. Die Daten durch klicken auf das
Excel“ Symbol unten rechts exportieren. Im Excel Sheet unten auf Table klicken um die
Daten zu sehen.
Die Daten im Excel sheet sind Stunden Daten für die Stunde 408 bis 888 im Jahr. Dies
entspricht der Simulationszeitspanne gemäss Abbildung 1.39.
Tipp Zeitauflösung: Der Zeitschritt der Ergebnisdaten kann in den Simulationseinstellungen geändert werden. Siehe Zeitschritt für die Ausgabe“ in Abbildung 1.36.
Mittels Kombination aus Berechnungen in einem Excel Sheet und einem Matlab File
wurde aus den Leistungsdaten in Watt, Energie Daten in kWh berechnet und Tagessummen
gebildet. Die Tagesenergiesummen wurden dann verglichen mit den Tagessummen, die aus
der Leistungsmessung der Heizung gebildet wurden. Die verwendeten Files sind in Anhang ??
gelistet.
Zur Annäherung (Kalibrierung) des Simulationsmodells wurde im Besonderen die Bauteilkonstruktion der Aussenmauer (Abbildung im Anhang: ??) angepasst, da diese einen entscheidenden Einfluss auf den Heizenergiebedarf hat. Der U-Wert der Aussenmauer wurde
schlussendlich auf 1.4W/(m²K) eingestellt.
![[data/assets/IDA_ICE_Tutorial/fig_1_38.png]]
*Abbildung 1.38: Standort und Klima File Kalibrierung Waffenplatzstrasse*

![[data/assets/IDA_ICE_Tutorial/fig_1_39.png]]
*Abbildung 1.39: Simulationseinstellungen für die Kalibrierung*

![[data/assets/IDA_ICE_Tutorial/fig_1_40.png]]
*Abbildung 1.40: Simulation Kalibrierung Resultate*
