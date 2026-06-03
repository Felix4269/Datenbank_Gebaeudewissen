---
tags: [Norm, Geothermie, Erdwärmesonde, SIA384-6, Gebäudetechnik]
normnummer: SN 546384/6:2021
gueltig_ab: "2021-05-01"
kapitel: "Kap. 3.5"
titel: "Berücksichtigung künftiger Nachbarsonden"
---
> ◀ [[03_2_3_4_systemoptimierung_berechnung|Kap. 3.2–3.4 Systemoptimierung, Berechnung und Hydraulik]]  ·  [[_SIA_384-6_2021_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Baustoffe|Kap. 4 Baustoffe und Konstruktion]] ▶

---

# Kap. 3.5 – Berücksichtigung künftiger Nachbarsonden

### 3.5.1 Zielsetzung

Die nachfolgenden Ausführungen sollen es ermöglichen, den Einfluss künftiger Erdwärmesonden in einem Quartier im Rahmen der geplanten Erdwärmesonden-Anlage abzuschätzen und mit entsprechenden Massnahmen zu verhindern, dass die Sonden durch Überlastung Schaden nehmen.

---

### 3.5.2 Umsetzung

3.5.2.1 Für die Umsetzung wird davon ausgegangen, dass die künftigen Nachbarprojekte sich ähnlich verhalten wie das aktuell vorliegende Projekt und der gleichen Gebäudekategorie angehören sowie dass das aktuelle Projekt typisch ist für die vorliegende Bauzone. Als Basis wird der grundstückflächenbezogene Wärmeentzug $P_{GSF}$ der Erdwärmesonden genommen, der aus der Energiebezugsfläche $A_E$ des aktuellen Projekts, dem Grenzwert $Q_{H,li} + Q_W$ gemäss SIA 380/1, dem zu erwartenden Zubauanteil $f_{ZB}$ an gleichartigen Erdwärmesonden-Projekten und einer angenommenen mittleren Leistungszahl (COP) von 4 einer monovalenten Wärmepumpe ermittelt wird:

$$P_{GSF} = (Q_{H,li} + Q_W) \cdot \frac{A_E}{GSF_{eff}} \cdot \frac{COP - 1}{COP} \cdot f_{ZB} \qquad \text{in kWh/m}^2 \tag{1}$$

3.5.2.2 Zur Bestimmung des Grenzwerts $Q_{H,li}$ gemäss SIA 380/1 soll die Gebäudehüllzahl $A_{th}/A_E$ gemäss Tabelle 5 eingesetzt werden.

**Tabelle 5** Einzusetzende Gebäudehüllzahl $A_{th}/A_E$ zur Bestimmung von $Q_{H,li}$

| Gebäudekategorie | $A_{th}/A_E$ | Gebäudekategorie | $A_{th}/A_E$ |
|---|---|---|---|
| I – Wohnen MFH | 1,25 | VII – Versammlungslokal | 1,5 |
| II – Wohnen EFH | 2 | VIII – Spital | 1,5 |
| III – Verwaltung | 1,5 | IX – Industrie | 2 |
| IV – Schulen | 1,5 | X – Lager | 2 |
| V – Verkauf | 2 | XI – Sportbauten | 1,5 |
| VI – Restaurant | 1,5 | XII – Hallenbad | 1,5 |

3.5.2.3 Bei der Deckung des Heizwärmebedarfs $Q_{H,li}$ der künftigen Nachbarprojekte kann mit einem Neubauanteil und einem Sanierungsanteil von je 50 % gerechnet werden.

3.5.2.4 Der Betrachtungszeitraum zur Berücksichtigung künftiger Nachbarsonden soll 50 Jahre betragen. Für die Auslegung wird von der gleichzeitigen Inbetriebsetzung ausgegangen. Bei den Nachbargebäuden kann, ohne weitere Abklärungen, von einem geothermischen Deckungsgrad $f_{geo}$ im Quartier von 40 % in 50 Jahren ausgegangen werden. Sind im Quartier z. B. leitungsgebundene Energieträger (Fernwärmenetze, Anergienetze, Erdgas) vorhanden, so kann von einem reduzierten geothermischen Deckungsgrad $f_{geo}$ von 20 % ausgegangen werden. Der prognostizierte Zubauanteil $f_{ZB}$ an Erdwärmesonden über die nächsten 50 Jahre ergibt sich dann gemäss Gleichung 2:

$$f_{ZB} = f_{geo} - f_{50m} \tag{2}$$

| Symbol | Bedeutung |
|---|---|
| $f_{ZB}$ | Zubauanteil an Erdwärmesonden-Heizungen im Quartier über die nächsten 50 Jahre (Anteil an neuen Erdwärmesonden-Anlagen, bezogen auf alle Heizungen im Quartier) |
| $f_{geo}$ | geothermischer Deckungsgrad an Erdwärmesonden-Heizungen (bezogen auf den Wärmebedarf der Gebäude im Quartier) in 50 Jahren |
| $f_{50m}$ | geothermischer Bestandsanteil an Erdwärmesonden-Heizungen (bezogen auf den Wärmebedarf der Gebäude im Quartier) mit einem Betrachtungsradius von 50 m um das bestehende Projekt; flächengemittelt abschätzbar |

3.5.2.5 Zur anrechenbaren Grundstückfläche $GSF_{eff}$ können neben der reinen Grundstückfläche $GSF$ auch 50 % von angrenzenden Strassenflächen $ASF$ und angrenzenden, nicht bebaubaren Flächen $AFF$ (z. B. Waldflächen oder Freihaltezonenflächen) bis zu einem Abstand der halben Grundstückweite gerechnet werden:

$$GSF_{eff} = GSF + ASF + AFF \tag{3}$$

![[figur_2_gsf_eff.png]]

3.5.2.6 Unter der Annahme einer mittleren Bohrtiefe von 200 m kann, in Abhängigkeit vom grundstückflächenbezogenen Wärmeentzug $P_{GSF}$, mit einer zusätzlichen Temperaturabkühlung durch künftige Nachbarsonden gemäss Figur 3 gerechnet werden.

![[figur_3_temperaturabkuehlung.png]]

Ein Beispiel zur Berechnung ist unter D.4.8.4 enthalten.

---

> ◀ [[03_2_3_4_systemoptimierung_berechnung|Kap. 3.2–3.4 Systemoptimierung, Berechnung und Hydraulik]]  ·  [[_SIA_384-6_2021_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Baustoffe|Kap. 4 Baustoffe und Konstruktion]] ▶

---
