---
tags: [Norm, Beleuchtung, Elektrizität, SIA387-4, Gebäudetechnik, Licht, Energiebedarf]
normnummer: SN 565387/4:2023
gueltig_ab: "2023-08-01"
kapitel: "Kap. 3.1"
titel: "Berechnung – Allgemeines und Grundlagen"
---
> ◀ [[02_Projektierung|Kap. 2 Projektierung]]  ·  [[_SIA_387-4_2023_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_Spezifische_Leistung|Kap. 3.2 Berechnung – Spezifische Leistung]] ▶

---

# Kap. 3.1 – Berechnung – Allgemeines und Grundlagen

---

### 3.1 Allgemeines
> 📖 Anwendung: [[03_1_interne_waermegewinne|Skript Energie Kap. 3.1 – Interne Wärmegewinne: Beleuchtung (spez. Leistung, Wärmelast)]]  ·  Anforderungen: [[04_Anforderungen|SIA 387/4 Kap. 4 – Grenz- und Zielwerte Elektrizitätsbedarf]]

#### 3.1.1 Zweck der Beleuchtung

Der Elektrizitätsbedarf für Beleuchtung setzt sich zusammen aus dem Elektrizitätsbedarf für die Raum- und Akzentbeleuchtung. Die Raumbeleuchtung ermöglicht die im betreffenden Raum anfallenden Sehaufgaben. Die Akzentbeleuchtung dient der Beleuchtung von bestimmten Objekten.

#### 3.1.2 Bezugsgrösse

Der jährliche Elektrizitätsbedarf für die Beleuchtung wird in kWh/m² pro Raum oder pro Gruppe von Räumen mit gleichen Nutzungsbedingungen – bezogen auf die Nettogeschossfläche – ermittelt.

#### 3.1.3 Projektwert

Die Berechnung des Projektwertes erfolgt immer mit den im betreffenden Projektstand besten Annahmen für die Eigenschaften der betreffenden Beleuchtungsanlagen und deren Betriebsbedingungen.

#### 3.1.4 Spezifischer Elektrizitätsbedarf für die Raum- und Akzentbeleuchtung

Der spezifische Elektrizitätsbedarf $E_L$ ergibt sich aus der Multiplikation der spezifischen elektrischen Leistung $p_L$ mit den Volllaststunden $t_L$ (3.3, Methode 1).

$$E_L = \frac{p_L \cdot t_L}{1000} \tag{1}$$

| Symbol | Bedeutung |
|---|---|
| $E_L$ | spezifischer Elektrizitätsbedarf Beleuchtung, in kWh/m² · a |
| $p_L$ | spezifische Leistung Beleuchtung, in W/m² |
| $t_L$ | Volllaststunden Beleuchtung, in h/a |

Alternativ lässt sich der Elektrizitätsbedarf in Stundenschritten durch Aufsummierung der stündlichen Leistungswerte ermitteln (3.4, Methode 2).

#### 3.1.5 Spezifische elektrische Leistung für die Raum- und Akzentbeleuchtung

3.1.5.1 Die spezifische elektrische Leistung $p_L$ für die allgemeine Raumbeleuchtung ergibt sich aus der Summe der Leistungen aller Leuchten geteilt durch die Nettogeschossfläche des Raums bzw. der Raumgruppe.

3.1.5.2 Bei Verwendung einer ständig gedimmten Beleuchtung ist anstelle der installierten Anschlussleistung mit der effektiven Betriebsleistung zu rechnen.

3.1.5.3 Wenn in einem frühen Planungsstadium die Leuchten (Typ und Anzahl) noch nicht bestimmt sind, kann die spezifische elektrische Leistung $p_L$ mit der Näherungsmethode gemäss [[03_2_Spezifische_Leistung|3.2]] bestimmt werden.

#### 3.1.6 Berechnung der Volllaststunden für die Raum- und Akzentbeleuchtung (Methode 1)

3.1.6.1 Die Volllaststunden $t_L$ der Raumbeleuchtung sind auf Grund der Nutzungsstunden, der Tageslichtverhältnisse, der erforderlichen Beleuchtungsstärke und der Bedienung durch die Benutzer bzw. der automatischen Steuerungen der Beleuchtung und des Sonnenschutzes zu bestimmen.

3.1.6.2 Die Einschaltdauer der Beleuchtung ist stark von der Bedienung durch die Benutzer und vom Typ der Beleuchtungssteuerung abhängig. Bei der Steuerung nach Präsenz wird die Beleuchtung auf Grund der Personenpräsenz ein- und ausgeschaltet. Bei der Steuerung nach Tageslicht wird die Beleuchtung auf Grund des einfallenden Tageslichts geregelt, gesteuert oder ein- und ausgeschaltet.

3.1.6.3 Wenn keine genaueren Angaben vorhanden sind, kann die Zahl der Volllaststunden $t_L$ mit der Näherungsmethode gemäss [[03_3_Volllaststunden_Methode1|3.3]] bestimmt werden.

---

### 3.2 Berechnung der spezifischen Leistung

#### 3.2.1 Basisgleichung

Die spezifische Leistung berechnet sich näherungsweise nach der folgenden Gleichung:

$$p_L = \frac{E_0}{f_m \cdot \eta_{v,Lo} \cdot \eta_R} \tag{2}$$

| Symbol | Bedeutung |
|---|---|
| $p_L$ | spezifische Leistung Beleuchtung, in W/m² |
| $E_0$ | Referenzwert der Beleuchtungsstärke für die Leistungsberechnung in lx: $E_0 = k_0 \cdot E_{vm}$ |
| $f_m$ | Wartungsfaktor Beleuchtung (gemäss SN EN 12464-1) |
| $\eta_{v,Lo}$ | Leuchten-Lichtausbeute, in lm/W |
| $\eta_R$ | Raumwirkungsgrad |
| $k_0$ | nutzungsspezifischer Korrekturfaktor für die Referenzbeleuchtungsstärke |
| $E_{vm}$ | Wartungswert der Beleuchtungsstärke in lx (gemäss SN EN 12464-1) |

#### 3.2.2 Wartungsfaktor Beleuchtung

Der Wartungsfaktor Beleuchtung $f_m$ berücksichtigt folgende Kriterien:
– Lichtstromrückgang der Leuchte durch Alterung der Leuchtmittel,
– Lichtstromrückgang der Leuchte durch Verschmutzung,
– Verschmutzung und Alterung der Räume.

#### 3.2.3 Leuchten-Lichtausbeute

Die typischen Werte von Leuchten-Lichtausbeuten $\eta_{v,Lo}$ können in der Vorprojektphase der Tabelle 3 entnommen werden. In der Projektphase sollen die effektiven Werte der verwendeten Produkte oder von bauähnlichen Leuchten verwendet werden.

**Tabelle 3** Typische Leuchten-Lichtausbeute $\eta_{v,Lo}$ in lm/W von LED-Leuchten (Stand Mitte 2022)

| Leuchtenkategorie | niedrige Werte | mittlere Werte | hohe Werte |
|---|---|---|---|
| Anbau- und Pendelleuchten | 89 | 110 | 130 |
| Einbauleuchten | 87 | 109 | 131 |
| Stehleuchten | 90 | 113 | 137 |
| Downlights | 78 | 87 | 96 |
| Strahler, Spots | 70 | 84 | 98 |
| Wandleuchten | 60 | 76 | 93 |
| Industrieleuchten | 139 | 149 | 159 |
| Lichtleisten | 138 | 157 | 176 |
| Nassraumleuchten | 107 | 129 | 150 |
| **Mittelwert** | **90** | **107** | **125** |

Die Tabelle ergibt sich aus der statistischen Auswertung von rund 9000 professionellen Leuchten am Schweizer Markt im Jahr 2022. Die niedrigen Werte entsprechen den 20-Prozent-Perzentilen der Auswertung, d. h. 20 % der angebotenen Leuchten sind noch niedriger, 80 % liegen darüber (Grundlagen für Grenzwerte). Die hohen Werte entsprechen den 80-Prozent-Perzentilen, d. h. 80 % der angebotenen Leuchten sind niedriger, 20 % liegen noch höher (Grundlagen für Zielwerte).

---

> ◀ [[02_Projektierung|Kap. 2 Projektierung]]  ·  [[_SIA_387-4_2023_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_Spezifische_Leistung|Kap. 3.2 Berechnung – Spezifische Leistung]] ▶

---
