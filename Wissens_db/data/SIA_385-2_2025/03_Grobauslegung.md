---
tags: [Norm, Trinkwarmwasser, Sanitär, SIA385-2, Gebäudetechnik, Warmwasser]
normnummer: SN 546385/2:2025
gueltig_ab: "2025-02-01"
kapitel: "Kap. 3"
titel: "Grobauslegung – Optimierung in der Vorprojektphase"
---
> ◀ [[02_Projektierung|Kap. 2 Projektierung]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Feinplanung|Kap. 4 Feinplanung – Auslegung]] ▶

---

# Kap. 3 – Grobauslegung – Optimierung in der Vorprojektphase

---

### 3.1 Allgemeines
> 📖 Bedarf: [[Anhang_A_Warmwasserbedarf|SIA 385/2 Anhang A – Normwerte Warmwasserbedarf nach Nutzungstyp]]  ·  Energie: [[05_Warmwasser|Skript Energie Kap. 5 – Wärmebedarf Warmwasser (Grundlagen & Formel)]]

3.1.1 Die Anordnung des technischen Raums, der Warmwasserentnahmestellen und der Warmwasserverteilleitungen im Gebäude wird anhand der Ausstosszeit und der Gesamtanforderung an die Warmwasserspeicherung und -verteilung überprüft und optimiert, um Wärmeverluste und die nicht nutzbare Warmwassermenge möglichst klein zu halten. Die entsprechenden Grenz- bzw. Zielwerte sind einzuhalten.

3.1.2 Dieses Optimierungsverfahren bezweckt die Erhöhung der Energieeffizienz der Warmwasserversorgung, die Erhaltung der Warmwasserhygiene sowie einen hohen Nutzungskomfort. Dies lässt sich insbesondere durch möglichst kurze Verteilleitungen, d. h. durch eine kompakte Warmwasserversorgung erreichen. Ebenso wichtig ist der systematische Einbau von Wärmesiphons, um nicht warmgehaltene Komponenten (z. B. Ausstossleitungen, Wärmeübertrager) wärmetechnisch von warmgehaltenen Leitungen bzw. Speicherstutzen zu trennen.

3.1.3 Die Anzahl der Entnahmestellen, die Länge der Warmwasserverteilleitungen, die Wärmeverluste der Warmwasserspeicherung und -verteilung und die Hilfsenergie werden durch das Optimierungsverfahren gesamthaft begrenzt.[^7]

3.1.4 Bei den Berechnungen werden fixe Parameterwerte eingesetzt.

3.1.5 Die Begrenzung der Verluste erfolgt bei Ausstossleitungen separat. Massgebend ist dabei der Grenzwert der Ausstosszeit gemäss SIA 385/1:2020, Ziffer 4.3.2. Es wird zwischen Warmwasserversorgungen mit und ohne warmgehaltene Leitungen unterschieden.

3.1.6 In Warmwasserversorgungen ohne warmgehaltene Leitungen erfolgt die Begrenzung der Speicherwärmeverluste allein mittels der Anforderungen an Speicherdämmung und Anschlüsse an den Speicher inkl. Installation von Wärmesiphons gemäss SIA 385/1:2020, Ziffern 5.2.4 und 5.5.

3.1.7 In Warmwasserversorgungen mit warmgehaltenen Leitungen muss zusätzlich die Gesamtanforderung an die Warmwasserspeicherung und -verteilung eingehalten werden. Diese Einhaltung wird am Wert der Warmwasser-Verlustzahl bemessen. Somit wird die gewichtete Summe der Speicherwärmeverluste, der Wärmeverluste der warmgehaltenen Leitungen und der Hilfsenergie bei der Standardnutzung der Warmwasserversorgung proportional zum Wärmebedarf für Warmwasser begrenzt.

3.1.8 Die Gesamtanforderung gilt nicht für Umbauten der Warmwasserversorgung, wenn Warmwasser-Verteilleitungen und Entnahmestellen – mit Ausnahme einer allfälligen Verbesserung der Wärmedämmung – unverändert bleiben.

3.1.9 Das Vorgehen ist in der [[02_Projektierung#Figur 3|Figur 3]] schematisch dargestellt.

---

### 3.2 Warmwasserversorgungen ohne warmgehaltene Leitungen

3.2.1 In Warmwasserversorgungen ohne warmgehaltene Leitungen werden die Wärmeverluste der Warmwasserverteilung allein durch die Einhaltung der von SIA 385/1:2020, Ziffer 4.3.2 geforderten, maximalen Ausstosszeit von 15 s begrenzt.

3.2.2 Dabei wird die Ausstosszeit wie folgt ermittelt:

3.2.2.1 Der Wasserinhalt der für die jeweilige Zapfstelle relevanten, nicht warmgehaltenen Leitungsteile wird aus ihren Längen und Innendurchmessern berechnet.

3.2.2.2 Die Kaltphasendauer $t'_c$ wird gemäss Gleichung 1 berechnet:

$$t'_c = \frac{\sum V'_{W,em,i}}{q'_{v,W}} \tag{1}$$

| Symbol | Bedeutung |
|---|---|
| $t'_c$ | Kaltphasendauer, in s |
| $V'_{W,em,i}$ | Wasserinhalt des nicht warmgehaltenen Leitungsteils i, in Liter |
| $q'_{v,W}$ | Volumenstrom an der Zapfstelle bei voll geöffneter, auf warm positionierter Entnahmearmatur, in l/s, gemäss Tabelle 1 |

**Tabelle 1** – Rohrmasse- und Volumenstrom-Werte für die Berechnung der Kaltphasendauer

| Sanitärapparate | Rohrmasse (AD × Wandstärke, mm) | Volumenstrom $q'_{v,W}$ |
|---|---|---|
| Waschtisch, Handwaschbecken, Bidet | 12 × 1,8 oder 16 × 2,2 | 0,1 l/s (6 l/min) |
| Dusche, Spültisch, Putzausguss | 16 × 2,2 | 0,2 l/s (12 l/min) |
| Badewanne | 16 × 2,2 oder 20 × 2,8 | 0,3 l/s (18 l/min) |

Im Fall eines angeschlossenen Apparats (Geschirrspüler, Waschmaschine, usw.) wird der vom Hersteller geforderte Volumenstrom übernommen.

3.2.2.3 Die für die Planung geltende Ausstosszeit $t'_{em}$ ist das Doppelte der Kaltphasendauer. Die Betriebstemperatur am Eintritt der Ausstossleitung wird dabei nicht berücksichtigt.

$$t'_{em} = 2 \cdot t'_c \tag{2}$$

3.2.3 Überschreitet die berechnete Ausstosszeit $t'_{em}$ den Grenzwert von 15 s, dann sollen die Ausstossleitungen verkürzt werden. Ihre Führung, die Anordnung der Entnahmestellen, des Speichers und der Verteiler sowie die Raumanordnung werden überprüft und angepasst. Auch die passive Warmhaltung der Verteiler (siehe Figur 3a in SIA 385/1:2020) kann zur Einhaltung des Grenzwertes beitragen.

---

### 3.3 Warmwasserversorgungen mit warmgehaltenen Leitungen

3.3.1 In Warmwasserversorgungen mit warmgehaltenen Leitungen werden die Wärmeverluste der Warmwasserspeicherung und -verteilung durch die Einhaltung der von SIA 385/1:2020, Ziffer 4.3.2, geforderten, maximalen Ausstosszeit von 10 s ([[03_Grobauslegung|3.3.2]]) und durch die Einhaltung des Grenzwertes von 50 % der Warmwasser-Verlustzahl $\xi_{ls}$ ([[03_Grobauslegung|3.3.3]]) begrenzt. Der Zielwert der Warmwasser-Verlustzahl beträgt 40 %.

Die Warmwasser-Verlustzahl ist die konkrete Umsetzung der Gesamtanforderung an die Warmwasserspeicherung und -verteilung. Sie schliesst die Ausstosswärmeverluste nicht ein. Diese sind durch die Einhaltung der maximalen Ausstosszeit bereits begrenzt.

3.3.2 Die Ausstosszeit wird gemäss [[03_Grobauslegung|3.2.2]] ermittelt.

3.3.3 Die Warmwasser-Verlustzahl wird wie folgt berechnet:

3.3.3.1 Der Nutzwarmwasserbedarf pro Bezugseinheit wird bei der Standardnutzung der Warmwasserversorgung in Normlitern gemäss A.2 ermittelt. Auch kleinere Werte als die von Tabelle 2 können eingesetzt werden. In diesem Fall müssen sie in der Nutzungsvereinbarung protokolliert werden und führen zu kleineren und kompakteren Warmwasserversorgungen.

3.3.3.2 Der Wärmebedarf für Warmwasser $Q'_W$ wird gemäss A.2 und A.4 berechnet.

3.3.3.3 Die Speicherwärmeverluste $Q'_{W,sto,ls}$ werden auf der Basis des Wärmebedarfs für Warmwasser $Q'_W$ gemäss Anhang B berechnet.

3.3.3.4 Die Wärmeverluste $Q'_{W,hl,ls}$ der warmgehaltenen Leitungen werden gemäss D.2 berechnet.

3.3.3.5 Die Hilfsenergie $E'_{W,aux}$ wird gemäss Anhang C berechnet.

3.3.3.6 Die Warmwasser-Verlustzahl ergibt sich aus Gleichung 3 bzw. 4:

##### 3.3.3.6.1 Warmwasserversorgungen mit Zirkulation

$$\xi_{ls} = \frac{Q'_{W,sto,ls} + Q'_{W,hl,ls} + 2{,}5 \cdot E'_{W,aux}}{Q'_W} \tag{3}$$

| Symbol | Bedeutung |
|---|---|
| $\xi_{ls}$ | Warmwasser-Verlustzahl, in % |
| $Q'_{W,sto,ls}$ | Speicherwärmeverluste, in kWh/d |
| $Q'_{W,hl,ls}$ | Wärmeverluste der warmgehaltenen Leitungen, in kWh/d |
| $E'_{W,aux}$ | Hilfsenergie, in kWh/d |
| $Q'_W$ | Wärmebedarf für Warmwasser, in kWh/d |

Ist der Betrieb überwiegend mit erneuerbaren Energieträgern vorgesehen, empfiehlt es sich, die Warmhaltung mit Zirkulation zu realisieren.

##### 3.3.3.6.2 Warmwasserversorgungen mit Warmhaltebändern

$$\xi_{ls} = \frac{Q'_{W,sto,ls} + 0{,}333 \cdot Q'_{W,hl,ls} + 2{,}5 \cdot 0{,}667 \cdot Q'_{W,hl,ls}}{Q'_W} = \frac{Q'_{W,sto,ls} + 2 \cdot Q'_{W,hl,ls}}{Q'_W} \tag{4}$$

| Symbol | Bedeutung |
|---|---|
| $\xi_{ls}$ | Warmwasser-Verlustzahl, in % |
| $Q'_{W,sto,ls}$ | Speicherwärmeverluste, in kWh/d |
| $Q'_{W,hl,ls}$ | Wärmeverluste der warmgehaltenen Leitungen, in kWh/d |
| $Q'_W$ | Wärmebedarf für Warmwasser, in kWh/d |

Gleichung 4 ergibt sich aus der Annahme, dass die Wärmeverluste der warmgehaltenen Leitungen zu einem Drittel durch Wärme aus dem Speicher und zu zwei Dritteln durch die Warmhaltebänder gedeckt werden. Der gemäss C.2 berechnete Elektrizitätsbedarf der Warmhaltebänder wird dabei mit dem Faktor 2,5 multipliziert. Siehe auch C.3 und C.5.

3.3.4 Können die Anforderungen von 3.3.1 (Ausstosszeiten und Warmwasser-Verlustzahl) nicht eingehalten werden, soll die Warmwasserverteilung vor allem kompakter gestaltet werden. Die folgenden Optimierungsmöglichkeiten stehen zur Verfügung.

##### 3.3.4.1 Einflussfaktoren mit grosser Wirkung

3.3.4.1.1 Überarbeitung des Standorts aller Leitungen, Speicher, Verteiler oder Entnahmestellen sowie der Raumanordnung, insbesondere um die Gesamtlänge der warmgehaltenen Leitungen zu reduzieren oder in Einfamilienhäusern die Warmhaltung zu vermeiden. Bei der Verkürzung von warmgehaltenen Leitungen soll der Grenzwert der Ausstosszeit sämtlicher Ausstossleitungen immer noch eingehalten werden.

3.3.4.1.2 Überarbeitung des Warmwasserversorgungskonzepts: Warmwasserverteilung ohne warmgehaltene Leitungen erwägen, z. B. dezentrale Wassererwärmung. Dabei sind Rückwirkungen auf die Wahl des Energieerzeugers und seines Energieträgers mitzuberücksichtigen.

##### 3.3.4.2 Einflussfaktoren mit begrenzter Wirkung

3.3.4.2.1 Überprüfung der Warmhaltung der Warmwasserverteilung inkl. Verteiler, z. B. Rohr-an-Rohr-Zirkulationssystem statt separat geführter Zirkulationsleitung verwenden.

3.3.4.2.2 Elektrische Nennleistung der Umwälzpumpe des Zirkulationssystems gemäss Zielwert statt Grenzwert SIA 385/1:2020, Ziffer 5.6.1, einsetzen.

3.3.4.2.3 Bei Speichern mit einem Volumen über 2000 Liter: Speicherwärmedämmung gemäss Zielwert statt Grenzwert einsetzen; siehe SIA 385/1:2020, Tabelle 2; die Speicherwärmeverluste werden bei der wiederholten Berechnung der Warmwasser-Verlustzahl gemäss B.6 mit dem Faktor 0,73 verkleinert.

3.3.5 Die erforderlichen Massnahmen zur Einhaltung der Anforderungen von 3.3.1 müssen bei der Feinplanung übernommen und z. B. in der Nutzungsvereinbarung ausdrücklich vermerkt werden. Die entsprechende Umsetzung bei der Ausführung muss sichergestellt werden.

---

[^7]: Die Begrenzung der Wärmeverluste der Warmwasserspeicherung und -verteilung liegt im Interesse des thermischen Komforts sowie einer Reduktion des Kältebedarfs in klimatisierten Gebäuden. In einem Gebäude mit sehr gut wärmegedämmter Bauhülle ist im Sommer jede bedeutende Abwärmequelle im Wohn- und Arbeitsbereich unerwünscht.

---

> ◀ [[02_Projektierung|Kap. 2 Projektierung]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Feinplanung|Kap. 4 Feinplanung – Auslegung]] ▶

---
