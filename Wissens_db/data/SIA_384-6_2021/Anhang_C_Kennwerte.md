---
tags: [Norm, Erdwärme, Geothermie, SIA384-6, Gebäudetechnik, Kennwerte, Wärmeleitfähigkeit]
normnummer: SN 546384-6:2021
gueltig_ab: "2021-05-01"
kapitel: "Anhang C"
titel: "Kennwerte"
anhang: informativ
---
> ◀ [[Anhang_B_Pruefungen|Anhang B]]  ·  [[_SIA_384-6_2021_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_D_Projektierungshinweise|Anhang D]] ▶

---

# Anhang C (informativ) – Kennwerte

---

## C.1  Allgemeines

Je nach Grösse eines Projekts (d. h. Anzahl EWS) können unterschiedlich aufwendige Verfahren zur Bestimmung der thermophysikalischen Parameter eingesetzt werden. Für die Dimensionierung der EWS werden die am Standort der EWS gemessenen oder geschätzten thermischen Gesteinseigenschaften (C.3) bestimmt.

---

## C.2  Bodentemperatur und Bodenoberflächentemperatur

### C.2.1  Allgemeines

**C.2.1.1** Die Bodentemperatur ist eine Funktion der Bodenoberflächentemperatur, des Temperaturgradienten, der Wärmeleitfähigkeit des Bodens, des Wärmeflusses und weiterer, lokaler Einflüsse wie Grundwasserströmungen. Die Bodenoberflächentemperatur wird durch mehrere Faktoren beeinflusst:

– Höhe,

– Lage (z. B. Nord/Süd-Exposition; Stadt/Land),

– Beschattung,

– Grundwasserfluss,

– lokaler geothermischer Wärmefluss.

**C.2.1.2** Die Bodenoberflächentemperatur am Standort kann in erster Annäherung aufgrund der Höhe über Meer bestimmt werden. Etwas genauer kann sie aus der mittleren Jahrestemperatur, die lokale Verhältnisse mitberücksichtigt, berechnet werden. Genaue Daten können durch die Messung eines Temperaturprofils entlang einer EWS erhalten werden.

**C.2.1.3** Gebräuchliche Messverfahren:

– Umlaufmessung: Messung der mittleren Erdreichtemperatur durch Anschluss einer Umwälzpumpe und Messung der Vorlauftemperatur ohne Wärmeeintrag. Auswertung nach minimal vier Umläufen.

– Kabelmessung: Messung des Temperaturverlaufs in der eingebauten und wassergefüllten Erdwärmesonde mithilfe einer kabelgeführten Temperatursonde.

– Diver-Verfahren: Messung des Temperaturverlaufs in der eingebauten und wassergefüllten Erdwärmesonde mithilfe einer kabellosen Druck- und Temperatursonde, die selbständig absinkt und dabei die Messwerte aufzeichnet.

– Faseroptische Messung: Messung des Temperaturverlaufs in der eingebauten Erdwärmesonde mithilfe eines faseroptischen Lichtwellenleiters. Er wird entweder eingeführt oder vor dem Einbau an der Erdwärmesonde befestigt.

**C.2.1.4** Die Reaktionsgeschwindigkeit der Messung muss so sein, dass Wärmeträger und Sensor beim Absinken des Divers oder Kabelfühlers im quasi thermischen Gleichgewicht sind.

### C.2.2  Bestimmung der Bodenoberflächentemperatur am Standort aus der Höhe über Meer

**C.2.2.1** Da ein Zusammenhang zwischen Höhenlage und Bodenoberflächentemperatur besteht, kann die Bodenoberflächentemperatur in erster Näherung direkt aus der Standorthöhe bestimmt werden. Lokale Verhältnisse sind dabei nicht berücksichtigt, entsprechend gross sind die Toleranzwerte zu bemessen. Ohne weitere Abklärungen ist im Heizfall zum Resultat aus den Gleichungen 4 und 5 ein Toleranzabzug von 1,5 K vorzunehmen, im Kühlfall ein Toleranzzuschlag von 1,5 K zu addieren.

**C.2.2.2** Figur 8 stellt die Bodenoberflächentemperatur für verschiedene Meereshöhen der Alpennordseite und der Alpensüdseite dar (berechnet anhand der Gleichungen 4 und 5). Diese Gleichungen gelten für einen Höhenbereich von 200 m bis 1800 m ü. M.

Alpennordseite – Bodenoberflächentemperatur (ausgezogene Kurve in Figur 8):

$$\theta_{G,s} = 1{,}373 \cdot 10^{-6} \cdot h_S^2 - 6{,}88 \cdot 10^{-3} \cdot h_S + 14{,}2 \tag{4}$$

Alpensüdseite – Bodenoberflächentemperatur (gestrichelte Kurve in Figur 8):

$$\theta_{G,s} = 2{,}277 \cdot 10^{-6} \cdot h_S^2 - 8{,}38 \cdot 10^{-3} \cdot h_S + 15{,}4 \tag{5}$$

Bodenoberflächentemperatur, mit Toleranzwert für den Heizfall:

$$\theta_{G,s,H} = \theta_{G,s} - 1{,}5 \text{ K} \tag{6}$$

Bodenoberflächentemperatur, mit Toleranzwert für den Kühlfall:

$$\theta_{G,s,C} = \theta_{G,s} + 1{,}5 \text{ K} \tag{7}$$

![[figur_8_bodenoberflaeche.png]]
> **Figur 8** – Bodenoberflächentemperaturen, abgeschätzt mit den Gleichungen 4 und 5, wenn die Jahresmitteltemperatur am Standort nicht bekannt ist, für einen Höhenbereich von 200 m bis 1800 m ü. M.

### C.2.3  Bestimmung der Bodenoberflächentemperatur bei bekannter Jahresmitteltemperatur

**C.2.3.1** Ist die Jahresmitteltemperatur am Standort bekannt (z. B. berechnet mit der Software Meteonorm [21]), kann die Bodenoberflächentemperatur aus der Standorthöhe nach folgenden Gleichungen berechnet werden [11].

Bodenoberflächentemperatur für Standorthöhe < 1000 m ü. M.:

$$\theta_{G,s} = \theta_{e,avg} + 1{,}55 \tag{8}$$

Bodenoberflächentemperatur für Standorthöhe > 1000 m ü. M.:

$$\theta_{G,s} = \theta_{e,avg} + 1{,}55 + \frac{h_S - 1000}{800} \cdot 2{,}45 \tag{9}$$

| Symbol | Bedeutung |
|---|---|
| $\theta_{G,s}$ | Bodenoberflächentemperatur, in °C |
| $\theta_{e,avg}$ | mittlere Jahresaussenlufttemperatur, in °C |
| $h_S$ | Höhe Standort über Meer, m ü. M. |

**C.2.3.2** Wegen lokaler Unsicherheiten (z. B. Einfluss der Exposition) wird für die Dimensionierung ein Toleranzwert von 1 K für Heizzwecke (Gleichung 10) subtrahiert und für Kühlzwecke (Gleichung 11) addiert.

Bodenoberflächentemperatur, mit Toleranzwert für den Heizfall:

$$\theta_{G,s,H} = \theta_{G,s} - 1 \text{ K} \tag{10}$$

Bodenoberflächentemperatur, mit Toleranzwert für den Kühlfall:

$$\theta_{G,s,C} = \theta_{G,s} + 1 \text{ K} \tag{11}$$

---

## C.3  Boden- und Stoffkennwerte

**Tabelle 11** – Bodenkennwerte. Der Wertebereich basiert auf Literaturdaten. Ohne weitere Kenntnisse sind die für die Schweiz empfohlenen Rechenwerte zu verwenden. In begründeten Fällen kann davon abgewichen werden. Werte teilweise aus Wärmeleitfähigkeiten im Schweizerischen Molassegestein [16].

| Gesteinstyp | $\lambda$ [W/(m·K)] Wertebereich | $\lambda$ empf. | $\rho \cdot c$ [MJ/(m³·K)] Wertebereich | $\rho \cdot c$ empf. | $\rho$ [10³ kg/m³] |
|---|---|:---:|---|:---:|---|
| **Lockergesteine und Torf** | | | | | |
| Ton trocken | 0,4–1,0 | 0,6 | 1,5–1,6 | 1,5 | 1,8–2,0 |
| Ton wassergesättigt | 0,9–2,3 | 1,4 | 2,0–2,8 | 2,3 | 2,0–2,2 |
| Sand trocken | 0,3–0,8 | 0,5 | 1,3–1,6 | 1,4 | 1,8–2,2 |
| Sand wassergesättigt | 1,5–4,0 | 2,3 | 2,2–2,8 | 2,4 | 1,9–2,3 |
| Kies/Steine, trocken | 0,4–0,5 | 0,4 | 1,3–1,6 | 1,4 | 1,8–2,2 |
| Kies/Steine, wassergesättigt | 1,6–2,0 | 1,7 | 2,2–2,6 | 2,3 | 1,9–2,3 |
| Moräne fest gelagert | 1,7–2,4 | 1,8 | 1,5–2,5 | 2,0 | 1,9–2,5 |
| Torf | 0,2–0,7 | 0,4 | 0,5–3,8 | 1,6 | 0,5–0,8 |
| **Sedimentäre Festgesteine** | | | | | |
| Schweizer Molassegestein (Mittelland) | *siehe Tabelle 12* | | 1,8–2,6 | 2,1 | 2,4–2,7 |
| Elsässer Molasse | 1,6–2,3 | 1,9 | 2,1–2,4 | 2,2 | 2,2–2,8 |
| Septarienton | 1,6–2,3 | 1,9 | 2,1–2,4 | 2,2 | 2,2–2,8 |
| Tonstein | 1,1–3,5 | 1,9 | 2,1–2,4 | 2,2 | 2,4–2,6 |
| Sandstein | – | 2,3 | 1,8–2,6 | 2,1 | 2,2–2,7 |
| Konglomerat (Nagelfluh) / Brekzie | 1,3–5,1 | 2,6 | 1,8–2,6 | 2,1 | 2,2–2,7 |
| Mergelstein | 1,5–3,5 | 2,1 | 2,2–2,3 | 2,2 | 2,3–2,6 |
| Kalkstein | 2,5–4,0 | 2,8 | 2,1–2,4 | 2,2 | 2,4–2,7 |
| Sulfatgestein (Gips) | 1,3–2,8 | 1,6 | – | 2,0 | – |
| **Magmatische Festgesteine** | | | | | |
| Granit | 2,1–4,1 | 2,8 | 2,1–3,0 | 2,4 | 2,4–3,0 |
| Diorit | 2,0–2,9 | 2,3 | – | 2,7 | 2,9–3,0 |
| Gabbro | 1,7–2,5 | 2,0 | – | 2,6 | 2,8–3,1 |
| **Metamorphe Festgesteine** | | | | | |
| Tonschiefer | 1,5–2,6 | 1,9 | 2,2–2,5 | 2,3 | 2,4–2,7 |
| Marmor | 1,3–3,1 | 1,9 | – | 2,0 | 2,5–2,8 |
| Quarzit | 5,0–6,0 | 5,3 | – | 2,1 | 2,5–2,8 |
| Glimmerschiefer | 1,5–3,1 | 2,0 | 2,2–2,4 | 2,3 | 2,4–2,7 |
| Gneis | 1,9–4,0 | 2,6 | 1,8–2,4 | 2,0 | 2,4–2,7 |
| Amphibolit | 2,1–3,6 | 2,6 | 2,0–2,3 | 2,1 | 2,6–2,9 |
| **Diverse Stoffe** | | | | | |
| Bentonit-Zement-Gemisch (Hinterfüllung ausgehärtet) | – | 0,8 | – | 3,0 | 1,2 |
| Beton | 0,9–2,0 | 1,4 | – | 1,8 | 2,0–2,42 |
| Eis (–10 °C) | – | 2,32 | – | 1,87 | 0,91 |
| Polyethylen (PE 100) | – | 0,4 | – | 1,63 | 0,96 |
| Luft (0 °C–20 °C) | – | 0,02 | – | 0,0012 | 0,00124 |
| Stahl | – | 60,0 | – | 3,12 | 7,8 |
| Wasser (10 °C) | – | 0,6 | – | 4,15 | 0,99 |

**Tabelle 12** – Wärmeleitfähigkeiten im Schweizerischen Molassegestein [16]. Der Wertebereich basiert auf Messdaten im Schweizer Mittelland. Ohne weitere Kenntnisse sind die für die Schweiz empfohlenen Rechenwerte zu verwenden. In begründeten Fällen kann davon abgewichen werden.

| Molasse | Gesteinstyp | $\lambda$ [W/(m·K)] Wertebereich | $\lambda$ empf. |
|---|---|---|:---:|
| **Obere Süsswassermolasse** | Tonstein – Siltstein | 2,3–2,4 | 2,3 |
| | Siltstein | 2,3–2,4 | 2,3 |
| | Feinsandstein | 2,3–2,6 | 2,3 |
| | Mittelsandstein | 2,5–2,8 | 2,6 |
| | Grobsandstein und Konglomerat | 2,5–2,8 | 2,6 |
| **Obere Meeresmolasse** | Tonstein – Siltstein | 2,6–2,9 | 2,7 |
| | Siltstein | 2,6–2,9 | 2,7 |
| | Feinsandstein | 2,7–3,3 | 2,9 |
| | Mittelsandstein | 2,7–3,2 | 2,8 |
| | Grobsandstein und Konglomerat | 2,6–3,0 | 2,7 |
| **Untere Süsswassermolasse** | Tonstein – Siltstein | 2,2–2,7 | 2,3 |
| | Siltstein | 2,3–2,8 | 2,4 |
| | Feinsandstein | 2,4–2,8 | 2,5 |
| | Mittelsandstein | 2,7–3,2 | 2,9 |
| | Grobsandstein und Konglomerat | 2,2–3,1 | 2,4 |

Die Wärmeleitfähigkeit der Hinterfüllung hängt stark vom Feuchtegehalt ab. Die Herstellerangaben gelten in der Regel nur für den frisch abgebundenen Zustand, bei dem der Wassergehalt im Mischverhältnis den Herstellerangaben entspricht. In trockener Bohrumgebung muss mit einer teilweisen Austrocknung der Hinterfüllung gerechnet werden. Bei trockener oder nicht bekannter Bohrumgebung muss deshalb für die Berechnung mit einem um 20 % reduzierten Wert für die Wärmeleitfähigkeit der Hinterfüllung gerechnet werden.

---

## C.4  Wärmeträger

**C.4.1** Die zulässigen Wärmeträger werden von den kantonalen Gewässerschutzstellen bestimmt. Hilfe dazu bietet [7].

**C.4.2** Zulässige Wärmeträger, inklusive Inhibitoren, gehören zur Klasse B gemäss [7] oder sind unbehandeltes Wasser. Von den in [4] aufgeführten Wärmeträgern erfüllen die folgenden diese Anforderung.

**Tabelle 13** – Zulässige Wärmeträger

| Wärmeträger | Verwendung | Bemerkung |
|---|---|---|
| Propylenglykol | oft | Unproblematisch, hat hohe Viskosität |
| Ethylenglykol | üblich | Unproblematisch, hat mittlere Viskosität |
| Ethylalkohol (Ethanol) | oft | Unproblematisch, soll inhibiert sein, hat mittlere Viskosität, grosser Ausdehnungskoeffizient |
| Calciumchlorid | selten | Früher verwendet, korrosiv |
| Kaliumsalze | unbekannt | – |
| Natriumchlorid | selten | Korrosiv |
| Wasser | oft | Trinkwasser kann unbehandelt, ohne Entsalzung verwendet werden. Dem Korrosions- und Frostschutz muss Beachtung geschenkt werden. |

Die kantonalen Gewässerschutzstellen können diese Liste einschränken oder ergänzen.

In Wärmeträgern dürfen als Zusatzstoffe (z. B. als Korrosionsinhibitor) keine biologisch schwer abbaubaren Stoffe, keine chlorierten Verbindungen und keine Schwermetallsalze verwendet werden.

### C.4.3  Eigenschaften von Wärmeträgern

Die Eigenschaften der Wärmeträger, insbesondere die Viskosität, sind von der Temperatur abhängig.

**Tabelle 14** – Eigenschaften der hauptsächlich eingesetzten Wärmeträger

| Träger (Mischung %v/v) | Dichte bei 0 °C [kg/m³] | Viskosität bei 0 °C [mm²/s] | Frostschutz [°C] | $\Delta V/V_0$ von 0 °C bis 20 °C |
|---|:---:|:---:|:---:|:---:|
| Ethylenglykol 20 % | 1037 | 3,49 | –10,6 | 0,0045 |
| Ethylenglykol 25 % | 1046 | 4,05 | –13,6 | 0,0051 |
| Ethylenglykol 30 % | 1056 | 4,72 | –16,9 | 0,0058 |
| Propylenglykol 25 % | 1032 | 5,97 | –10,1 | 0,0076 |
| Propylenglykol 30 % | 1038 | 7,58 | –13,5 | 0,0083 |
| Propylenglykol 35 % | 1044 | 9,65 | –18,5 | 0,0090 |
| Wasser (5 °C) | 1000 | 1,50 | 0,0 | 0,0016 |
| Ethanol 20 % | 978 | 4,64 | –7,8 | 0,0070 |
| Ethanol 25 % | 976 | 5,57 | –10,7 | 0,0113 |
| Ethanol 30 % | 975 | 5,59 | –14,3 | 0,0167 |

*Quellen: Ethylenglykol, Propylenglykol: Clariant AG, Muttenz; Ethanol: Hubbuch/Melinder, ZHAW, Wädenswil*

### C.4.4  Auslegung von Expansionsgefässen

Die volumetrische Ausdehnung von 0 °C auf 20 °C kann für die Berechnung des Expansionsgefässes für den Erdwärmesondenkreis verwendet werden (3.4.2.6), solange keine grösseren Kältelasten abgeführt werden (Anlagetemperaturen > 20 °C).

Beispiel: Anlageninhalt 1000 Liter, Frostschutz 20 % Ethylenglykol, Sicherheitsfaktor $s = 3$ (nach 3.4.2.6). Gesucht ist die Grösse des Expansionsgefässes.

Nutzungsgrad des Expansionsgefässes bei 1 bar Vordruck und einem maximalen Druck von 3 bar:

$$\eta_{exp} = \frac{p_{max} - p_p}{p_{max} + 1} = \frac{3 - 1}{3 + 1} = 0{,}5 \tag{12}$$

Minimales Volumen des Expansionsgefässes:

$$V_{exp,min} = \frac{\Delta V/V_0 \cdot V_{BHE} \cdot s}{\eta_{exp}} = \frac{0{,}0045 \cdot 1000 \cdot 3}{0{,}5} = 27 \text{ Liter} \tag{13}$$

| Symbol | Bedeutung |
|---|---|
| $\eta_{exp}$ | Nutzungsgrad des Expansionsgefässes |
| $p_{max}$ | maximaler Druck, in bar |
| $p_p$ | Vordruck, in bar |
| $\Delta V/V_0$ | volumetrische Ausdehnung bei Erwärmung von 0 °C auf 20 °C |
| $V_{BHE}$ | Inhalt Erdwärmesonden und Erdwärmesondenkreis, in Liter |
| $s$ | Sicherheitsfaktor nach Ziffer 3.4.2.6 = 3 |

---

> ◀ [[Anhang_B_Pruefungen|Anhang B]]  ·  [[_SIA_384-6_2021_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_D_Projektierungshinweise|Anhang D]] ▶

---
