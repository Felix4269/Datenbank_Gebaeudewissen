---
tags: [Norm, Trinkwarmwasser, Sanitär, SIA385-2, Gebäudetechnik, Warmwasser]
normnummer: SN 546385/2:2025
gueltig_ab: "2025-02-01"
kapitel: "Anhang A"
titel: "Warmwasserbedarf und Wärmebedarf für Warmwasser"
anhang: normativ
---
> ◀ [[05_Waermebedarf_Hilfsenergie|Kap. 5]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_B_Speicherwaermeverluste|Anhang B]] ▶

---

# Anhang A (normativ) – Warmwasserbedarf und Wärmebedarf für Warmwasser

> 📖 Theorie: [[05_Warmwasser|Skript Energie Kap. 5 – Wärmebedarf Warmwasser (Grundlagen & Berechnung)]]  ·  [[06_1_berechnung_energiebedarf|Skript Energie Kap. 6.1 – Energiebedarf Heizung und Warmwasser]]

---

## A.1 Allgemeines

A.1.1 Die Warmwasserversorgung wird in Gruppen von Räumen gleicher Nutzung – die sogenannten **Nutzungseinheiten** – unterteilt.

A.1.2 Die Grobauslegung berücksichtigt Standard-Durchschnittswerte des Warmwasserbedarfs, während die Feinplanung auf tendenziell grösseren Werten aus der Nutzungsvereinbarung basiert.

---

## A.2 Berechnungsverfahren für die Grobauslegung

A.2.1 Für jede Nutzungseinheit $i$ wird der Nutzwarmwasserbedarf pro Bezugseinheit $V'_{W,u,i}$ der [[#Tabelle 2|Tabelle 2]] entnommen. Da bei der Grobauslegung von Normlitern, d. h. von einer Temperaturerhöhung des Wassers von 50 K, ausgegangen wird, wird der entsprechende Wärmebedarf für Warmwasser pro Bezugseinheit $Q'_{W,i}$ auch direkt der Tabelle 2 entnommen. Die effektive Temperatur am Austritt des Speichers wird nicht berücksichtigt, diejenige des Kaltwassers auch nicht. Eine mögliche Wärmerückgewinnung aus Duschwasser wird bei der Grobauslegung nicht berücksichtigt. Deshalb entspricht hier der Nutzenergiebedarf dem Wärmebedarf für Warmwasser.

A.2.2 Die Tabelle 2 gibt Werte des durchschnittlichen Nutzwarmwasserbedarfs pro Bezugseinheit $V'_{W,u,i}$ und des entsprechenden durchschnittlichen Wärmebedarfs für Warmwasser $Q'_{W,i}$ an, welche in einer frühen Planungsphase für Berechnungen im Sinne von SIA 2024 auch übernommen werden können.

##### Tabelle 2 – Durchschnittlicher Nutzwarmwasserbedarf pro Bezugseinheit $V'_{W,u,i}$ und entsprechender Wärmebedarf für Warmwasser $Q'_{W,i}$ für die Grobauslegung

| Nutzungseinheit | Bezugseinheit ^a) | $V'_{W,u,i}$ [Normliter/d] ^b) | $Q'_{W,i}$ [kWh/d] ^c) |
|---|:---:|:---:|:---:|
| **Wohnen** | | | |
| Einfamilienhaus, Eigentumswohnung | P | 40 | 2,32 |
| Mehrfamilienhaus | P | 35 | 2,03 |
| Büros (ohne Personalrestaurant) | P | 3 | 0,174 |
| **Gastronomie** (Kochen, Spülen, Geschirrwaschen) | | | |
| Cafeteria, Tea-Room | S | 15 | 0,87 |
| **Beherbergung** | | | |
| Gasthof, Hotel, Appartementhaus (ohne Küche und Wäscherei) | B | 40 | 2,32 |
| Kinderheim (Gesamtbedarf inkl. Küche und Wäscherei) | B | 50 | 2,90 |
| Altersheim (Gesamtbedarf inkl. Küche und Wäscherei) | B | 40 | 2,32 |
| Alters- und Pflegeheim (Gesamtbedarf inkl. Küche und Wäscherei) | B | 50 | 2,90 |
| Krankenhaus, Klinik | B | 60 | 3,48 |
| Restaurant | M | 8 | 0,464 |
| Wäscherei (pro kg Trockenwäsche) | kg | 4 | 0,232 |
| Duschen | D/P | 20 | 1,16 |
| Baden | B/P | 90 | 5,22 |

^a) Personenbezogene Einheiten: P Person · B Bett · S Sitzplatz  
Sachbezogene Einheiten: M Mahlzeit · D/P Duschbad pro Person · B/P Wannenbad pro Person  
^b) Die Zahlenangaben gehen aus Auswertungen von Messungen und Statistiken des Warmwasserverbrauchs hervor. Sie beinhalten keine Verluste (Wärme- und Wasserverluste).  
^c) Entsprechender Energieinhalt (0,058 kWh pro Normliter).

A.2.3 Wird der Nutzwarmwasserbedarf pro Bezugseinheit für jede sachbezogene Nutzungseinheit separat in der Nutzungsvereinbarung definiert, kann ebenfalls auf Tabelle 2 Bezug genommen werden.

A.2.4 In Fällen, die nicht in Tabelle 2 aufgeführt sind, werden Werte aus Drittquellen unter Angabe der Quelle oder Werte aus dem nächstliegenden Fall aus Tabelle 2 eingesetzt. Der entsprechende Wärmebedarf für Warmwasser pro Bezugseinheit ergibt sich aus Gleichung 12:

$$Q'_{W,i} = V'_{W,u,i} \cdot \Delta\theta_{gen,i} \cdot \rho \cdot C_p \tag{12}$$

| Symbol | Bedeutung |
|---|---|
| $Q'_{W,i}$ | Wärmebedarf für Warmwasser pro Bezugseinheit für die Nutzungseinheit $i$, in kWh/d |
| $V'_{W,u,i}$ | Nutzwarmwasserbedarf pro Bezugseinheit für die Nutzungseinheit $i$, in l/d |
| $\Delta\theta_{gen,i}$ | Temperaturerhöhung bei der Wassererwärmung für die Nutzungseinheit $i$, in K |
| $\rho$ | Dichte des Wassers, in kg/l |
| $C_p$ | spezifische Wärmekapazität des Wassers, in kWh/(kg·K) |

$\rho \cdot C_p = 1{,}16 \cdot 10^{-3}$ kWh/(K·l)

Bei $\Delta\theta_{gen,i}$ = 50 K (Annahme für die Berechnung in Normlitern) beträgt $\Delta\theta_{gen,i} \cdot \rho \cdot C_p$ = 0,058 kWh/l.

A.2.5 Der Wärmebedarf für Warmwasser $Q'_W$ der Warmwasserversorgung ergibt sich gemäss Gleichung 13:

$$Q'_W = \sum_i \left( n_{P,i} \cdot Q'_{W,i} \right) \tag{13}$$

| Symbol | Bedeutung |
|---|---|
| $Q'_W$ | Wärmebedarf für Warmwasser, in kWh/d |
| $n_{P,i}$ | massgebende Personenzahl bzw. Bezugseinheiten für die Nutzungseinheit $i$ bei der Normbelegung (Wohnbereich: siehe [[#A.4 Normbelegung im Wohnbereich|A.4]]) |
| $Q'_{W,i}$ | Wärmebedarf für Warmwasser pro Bezugseinheit für die Nutzungseinheit $i$, in kWh/d |

---

## A.3 Berechnungsverfahren für die Feinplanung

A.3.1 Die Nutzungsvereinbarung definiert gemäss [[Anhang_G_Nutzungsvereinbarung|Anhang G]] für jede Nutzungseinheit $i$ die Bezugstemperatur und den Nutzwarmwasserbedarf pro Bezugseinheit $V_{W,u,i}$. Aus der Bezugstemperatur und der Kaltwassertemperatur ergibt sich die Temperaturerhöhung bei der Erwärmung $\Delta\theta_{gen,i}$ für die Nutzungseinheit $i$ und daraus folgt der entsprechende Nutzenergiebedarf $Q_{W,u,i}$ gemäss Gleichung 12, in welcher $V'_{W,u,i}$ durch $V_{W,u,i}$ und $Q'_{W,i}$ durch $Q_{W,u,i}$ ersetzt werden.

A.3.2 Bei der Feinplanung können für die Festlegung von $V_{W,u,i}$ und $Q_{W,u,i}$ die Werte aus [[#Tabelle 3|Tabelle 3]] wie folgt beigezogen werden:

- In Tabelle 3 werden die durchschnittlichen Werte $V_{W,u,i,avg}$ und $Q_{W,u,i,avg}$ mit ihren Standardabweichungen $\sigma_{V,i}$ und $\sigma_{Q,i}$ abgelesen. Diese Werte verstehen sich ohne Wärmerückgewinnung aus Duschwasser. Eine allfällige Wärmerückgewinnung aus Duschwasser wird in einem späteren Berechnungsschritt gemäss Gleichungen 30 und 40 im Anhang K berücksichtigt.
- Mit den Gleichungen 14 und 15 werden Werte von $V_{W,u,i}$ und $Q_{W,u,i}$ berechnet, welche grösser sind, um der statistischen Streuung Rechnung zu tragen:

$$V_{W,u,i} = V_{W,u,i,avg} + k \cdot \sigma_{V,i} \tag{14}$$

$$Q_{W,u,i} = Q_{W,u,i,avg} + k \cdot \sigma_{Q,i} \tag{15}$$

| Symbol | Bedeutung |
|---|---|
| $V_{W,u,i}$ | Nutzwarmwasserbedarf pro Bezugseinheit, in l/d |
| $Q_{W,u,i}$ | entsprechender Nutzenergiebedarf pro Bezugseinheit, in kWh/d |
| $V_{W,u,i,avg}$ | durchschnittlicher Nutzwarmwasserbedarf pro Bezugseinheit, in l/d |
| $Q_{W,u,i,avg}$ | entsprechender durchschnittlicher Nutzenergiebedarf pro Bezugseinheit, in kWh/d |
| $\sigma_{V,i}$ | Standardabweichung des Nutzwarmwasserbedarfs, in l/d |
| $\sigma_{Q,i}$ | Standardabweichung des Nutzenergiebedarfs, in kWh/d |
| $k$ | statistischer Faktor (Gleichung 16) |

Der Faktor $k$ wird gleich 2 gesetzt. Gemäss der Statistik befinden sich bei Normalverteilungen 95 % aller Werte im Intervall von zwei Standardabweichungen.

- Für eine grössere Anzahl Bezugseinheiten $n_{p,i}$, z. B. ab 10, kann die Standardabweichung in den Gleichungen 14 und 15 gemäss Gleichung 16 reduziert werden (Äquivalent zum Gleichzeitigkeitsfaktor), da die Streuung mit steigenden Anzahlen abnimmt.

$$\sigma_{red} = \frac{\sigma}{\sqrt{n_{p,i}}} \tag{16}$$

| Symbol | Bedeutung |
|---|---|
| $\sigma_{red}$ | reduzierte Standardabweichung des durchschnittlichen Nutzwarmwasser- bzw. Nutzenergiebedarfs, in l/d bzw. kWh/d |
| $\sigma$ | Standardabweichung des durchschnittlichen Nutzwarmwasser- bzw. Nutzenergiebedarfs, in l/d bzw. kWh/d |
| $n_{p,i}$ | Anzahl Bezugseinheiten |

- Der Faktor $k$ kann erhöht werden, wenn für die Dimensionierung des Steuervolumens eine höhere Verfügbarkeitssicherheit bei sehr grossen Warmwasserentnahmen, d. h. ein höherer Nutzungskomfort gewünscht wird.

A.3.3 Sinngemäss kann auf A.3.1, A.3.2 und Tabelle 3 Bezug genommen werden, wenn der Nutzwarmwasserbedarf pro Bezugseinheit für jede sachbezogene Nutzungseinheit separat in der Nutzungsvereinbarung definiert wird.

A.3.4 In Fällen, die nicht in Tabelle 3 aufgeführt sind, werden Werte aus Drittquellen unter Angabe der Quelle oder Werte aus dem nächstliegenden Fall aus Tabelle 3 eingesetzt.

A.3.5 Der Wärmebedarf für Warmwasser $Q_W$ der Warmwasserversorgung ergibt sich gemäss Gleichung 17 durch Multiplikation des Wärmebedarfs für Warmwasser pro Bezugseinheit $Q_{W,u,i}$ mit der Anzahl Bezugseinheiten $n_{P,i}$ und Summierung über alle Nutzungseinheiten:[^11]

$$Q_W = \sum_i \left( n_{P,i} \cdot Q_{W,u,i} \right) \tag{17}$$

| Symbol | Bedeutung |
|---|---|
| $Q_W$ | Wärmebedarf für Warmwasser der ganzen Warmwasserversorgung (ohne WRG), in kWh/d |
| $n_{P,i}$ | massgebende Personenzahl bzw. Bezugseinheiten für die Nutzungseinheit $i$ bei der Normbelegung bzw. für die Sanitäranlage $i$ (Wohnbereich: siehe [[#A.4 Normbelegung im Wohnbereich|A.4]]) |
| $Q_{W,u,i}$ | Nutzenergiebedarf pro Bezugseinheit für die Nutzungseinheit $i$, in kWh/d |

##### Tabelle 3 – Durchschnittlicher Nutzenergiebedarf pro Bezugseinheit $Q_{W,u,i,avg}$ mit Standardabweichung $\sigma_{Q,i}$

> Zur Berechnung in der Feinplanung. Bei Warmwasserversorgungen ohne Wärmerückgewinnung entspricht diese physikalische Grösse dem durchschnittlichen Nutzwarmwasserbedarf pro Bezugseinheit $V_{W,u,i,avg}$ mit Standardabweichung $\sigma_{V,i}$.

| Nutzungseinheit | Hinweise | BE ^a) | $V_{W,u,i,avg}$ [Nl/d] | $\sigma_{V,i}$ [Nl/d] | $Q_{W,u,i,avg}$ [kWh/d] | $\sigma_{Q,i}$ [kWh/d] |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Wohnen** | | | | | | |
| Einfamilienhaus, Eigentumswohnung | einfacher Standard | P | 40 | 5,0 | 2,32 | 0,29 |
| | mittlerer Standard | P | 45 | 7,5 | 2,61 | 0,44 |
| | gehobener Standard | P | 55 | 7,5 | 3,19 | 0,44 |
| Mehrfamilienhaus | allgemeiner Wohnungsbau | P | 35 | 5,0 | 2,03 | 0,29 |
| | gehobener Wohnungsbau | P | 45 | 7,5 | 2,61 | 0,44 |
| Büros | ohne Personalrestaurant | P | 3 | 0,5 | 0,17 | 0,029 |
| **Gastronomie** (Kochen, Spülen, Geschirrwaschen) | | | | | | |
| Cafeteria, Tea-Room | Besetzung mässig | S | 20 | 5,0 | 1,16 | 0,29 |
| | Besetzung hoch | S | 30 | 5,0 | 1,74 | 0,29 |
| **Beherbergung** (ohne Küche und Wäscherei) | | | | | | |
| Gasthof, Hotel | einfach (Zimmer mit Dusche) | B | 40 | 5,0 | 2,32 | 0,29 |
| Appartementhaus | Mittelklasse (Zimmer mit Dusche) | B | 50 | 10,0 | 2,90 | 0,58 |
| | gehobene Klasse | B | 80 | 10,0 | 4,64 | 0,58 |
| | Luxus | B | 100 | 25,0 | 5,80 | 1,45 |
| **Beherbergung** (Gesamtbedarf inkl. Küche und Wäscherei) | | | | | | |
| Kinderheim | einfacher Standard | B | 50 | 5,0 | 2,90 | 0,29 |
| Altersheim | einfacher Standard | B | 40 | 5,0 | 2,32 | 0,29 |
| Alters- und Pflegeheim | einfacher Standard | B | 50 | 7,5 | 2,90 | 0,44 |
| Krankenhaus, Klinik | einfach | B | 60 | 10,0 | 3,48 | 0,58 |
| | durchschnittlich | B | 80 | 10,0 | 4,64 | 0,58 |
| | umfangreich | B | 120 | 15,0 | 6,96 | 0,87 |
| Restaurant | Essen einfach, Tellergerichte | M | 8 | 1,0 | 0,46 | 0,058 |
| | Essen mit mehreren Gängen | M | 10 | 2,5 | 0,58 | 0,145 |
| Wäscherei | Trockenwäsche | kg | 4 | 0,5 | 0,23 | 0,029 |
| Dusche | Schüler | D/P | 20 | 2,5 | 1,16 | 0,145 |
| | Sportler, Wohnen | D/P | 25 | 2,5 | 1,45 | 0,145 |
| | Fabrikarbeit schwach schmutzig | D/P | 30 | 2,5 | 1,74 | 0,145 |
| | Fabrikarbeit stark schmutzig | D/P | 35 | 2,5 | 2,03 | 0,145 |
| Badewanne | normale Wannen | B/P | 90 | 10,0 | 5,22 | 0,58 |
| | Grosswannen | B/P | 110 | 5,0 | 6,38 | 0,29 |
| | Grossraumwannen | B/P | 300 | 30,0 | 17,40 | 1,74 |

^a) Personenbezogene Einheiten: P Person · B Bett · S Sitzplatz; sachbezogene Einheiten: M Mahlzeit · D/P Duschbad pro Person · B/P Wannenbad pro Person  
^b) Die Zahlenangaben gehen aus Auswertungen von Messungen und Statistiken des Warmwasserverbrauchs hervor. Sie beinhalten keine Verluste (Wärme- und Wasserverluste). Für deren Anwendungen sind alle relevanten Einflussgrössen und objektbezogenen Randbedingungen mitzuberücksichtigen.  
^c) Entsprechender Energieinhalt (0,058 kWh pro Normliter).

---

## A.4 Normbelegung im Wohnbereich

Im Wohnbereich wird die Normbelegung der Räume bei der Standardnutzung gemäss Gleichung 18 bzw. Figur 5 auf der Basis der Nutzfläche separat für jede Wohneinheit ermittelt.[^12] Die Anzahl Personen $n_{P,i}$ muss keine ganze Zahl sein.

$$n_{P,i} = 3{,}3 - \frac{2}{1 + \left(\dfrac{A_{NF}}{A_0}\right)^3} \tag{18}$$

| Symbol | Bedeutung |
|---|---|
| $n_{P,i}$ | Anzahl Personen in der Wohneinheit |
| $A_{NF}$ | Nutzfläche der Wohneinheit gemäss SIA 416, in m² |
| $A_0$ | $= 100\,\text{m}^2$ |

![[Figur_5_Normbelegung.png]]
**Figur 5** – Normbelegung von Wohneinheiten gemäss Gleichung 18

Bei der Feinplanung können Belegungswerte aus anderen Quellen (z. B. Baugenossenschaften) berücksichtigt werden, die von Gleichung 18 und Figur 5 abweichen. Die gewählten Werte sind in der Nutzungsvereinbarung zu protokollieren.

---

## A.5 Stundenspitzen des Wärmebedarfs für Warmwasser

A.5.1 Im Wohnbereich ab 10 Personen wird bei der Feinplanung für die Dimensionierung des Spitzendeckungsvolumens die grösste Stundenspitze des Wärmebedarfs für Warmwasser gemäss Gleichung 19 bzw. Figur 6 ermittelt.[^13]

$$Q_{W,pk} = Q_W \cdot \left( 0{,}09 + \frac{0{,}66}{n_{P,W}} + \frac{1{,}98}{n_{P,W}} \right) \tag{19}$$

| Symbol | Bedeutung |
|---|---|
| $Q_{W,pk}$ | grösste Stundenspitze des Wärmebedarfs für Warmwasser im Wohnbereich, in kWh/d |
| $Q_W$ | Wärmebedarf für Warmwasser in der betrachteten Warmwasserversorgung, in kWh/d |
| $n_{P,W}$ | Anzahl Personen, die Warmwasser von der betrachteten Warmwasserversorgung beziehen |

![[Figur_6_Stundenspitze.png]]
**Figur 6** – Diagramm zur Bestimmung der Stundenspitze in % des täglichen Wärmebedarfs für Warmwasser $Q_W$ im Wohnbereich ab 10 Personen

A.5.2 Im Wohnbereich bei weniger als 10 Personen in der betrachteten Warmwasserversorgung wird die grösste Stundenspitze durch Betrachtung der einzelnen Warmwasserentnahmestellen, deren stündlichem Wärmebedarf und deren gleichzeitiger Nutzung in der betrachteten Stunde ermittelt. Tabelle 3 enthält einzelne Daten im Bereich der sachbezogenen Einheiten, die gemäss A.3.2 umgesetzt werden sollen.

A.5.3 Bei Nicht-Wohnbauten wird die grösste Stundenspitze des Wärmebedarfs für Warmwasser sinngemäss nach A.5.2 ermittelt.

A.5.4 In allen Fällen sind die getroffenen Annahmen in der Nutzungsvereinbarung festzuhalten.

A.5.5 Eine allfällige Wärmerückgewinnung aus Duschwasser wird für die Berechnung des Spitzendeckungsvolumens nicht berücksichtigt.

---

[^11]: Da eine allfällige Wärmerückgewinnung nicht berücksichtigt wird, ist der Wärmebedarf für Warmwasser (gemessen an Zapfstellen) gleich dem Nutzenergiebedarf (gemessen an Auslaufstellen).
[^12]: Datenbasis: Erhebung 2013 des Bundesamtes für Statistik (BFS). Dieses Amt benutzt den Begriff Wohnung statt Wohneinheit.
[^13]: Datenquelle: Messprojekt des Amts für Hochbauten der Stadt Zürich, 2008.

---

> ◀ [[05_Waermebedarf_Hilfsenergie|Kap. 5]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_B_Speicherwaermeverluste|Anhang B]] ▶

---
