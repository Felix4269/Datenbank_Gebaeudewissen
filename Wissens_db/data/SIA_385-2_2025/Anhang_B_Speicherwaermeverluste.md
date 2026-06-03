---
tags: [Norm, Trinkwarmwasser, Sanitär, SIA385-2, Gebäudetechnik, Warmwasser]
normnummer: SN 546385/2:2025
gueltig_ab: "2025-02-01"
kapitel: "Anhang B"
titel: "Speicherwärmeverluste"
anhang: normativ
---
> ◀ [[Anhang_A_Warmwasserbedarf|Anhang A]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_C_Hilfsenergie|Anhang C]] ▶

---

# Anhang B (normativ) – Speicherwärmeverluste $Q_{W,sto,ls}$ bzw. $Q'_{W,sto,ls}$

---

B.1 In der vorliegenden Norm wird auf die detaillierte Berechnung der Speicherwärmeverluste gemäss SN EN 15316-5 verzichtet. Für die Berechnung der Speicherwärmeverluste $Q'_{W,sto,ls}$ bei der Grobauslegung und $Q_{W,sto,ls}$ bei der Feinplanung wird ein vereinfachtes Verfahren angewendet. Die zwei Berechnungen unterscheiden sich nur durch den Einsatz unterschiedlicher Werte. Bei der Grobauslegung werden die Symbole mit einem Apostroph gekennzeichnet.

---

## B.2 Nutzwarmwasserbedarf

B.2.1 Bei der Grobauslegung wird der Nutzwarmwasserbedarf $V'_{W,u}$ gemäss Gleichung 20 ermittelt:

$$V'_{W,u} = \frac{Q'_W}{\Delta\theta_{gen,i} \cdot \rho \cdot C_p} = \frac{Q'_W}{0{,}058} \tag{20}$$

| Symbol | Bedeutung |
|---|---|
| $V'_{W,u}$ | täglicher Nutzwarmwasserbedarf, in Normliter/d |
| $Q'_W$ | Wärmebedarf für Warmwasser gemäss [[03_Grobauslegung#3.3.3.2|3.3.3.2]] und [[Anhang_A_Warmwasserbedarf#A.2|A.2]], in kWh/d |
| $\Delta\theta_{gen,i}$ | Temperaturerhöhung bei der Wassererwärmung, in K |
| $\rho$ | Dichte des Wassers, in kg/l |
| $C_p$ | spezifische Wärmekapazität des Wassers, in kWh/(kg·K) |

$\rho \cdot C_p = 1{,}16 \cdot 10^{-3}$ kWh/(K·l)

Bei $\Delta\theta_{gen,i}$ = 50 K (Annahme für die Berechnung in Normlitern) beträgt $\Delta\theta_{gen,i} \cdot \rho \cdot C_p$ = 0,058 kWh/l.

B.2.2 Bei der Feinplanung wird der Nutzwarmwasserbedarf $V_{W,u}$ ebenfalls gemäss Gleichung 20 ermittelt, wobei $Q'_W$ durch den Wärmebedarf für Warmwasser $Q_W$ gemäss [[04_Feinplanung#4.1.3|4.1.3]] und [[Anhang_A_Warmwasserbedarf#A.3|A.3]] ersetzt wird.

---

## B.3 Annahme Speichervolumen

Für die Berechnung der Speicherwärmeverluste wird das Gesamtvolumen des/der Speicher $V'_{W,sto}$ (Grobauslegung) bzw. $V_{W,sto}$ (Feinplanung) 1,5-mal dem täglichen, gemäss Gleichung 20 ermittelten Nutzwarmwasserbedarf $V'_{W,u}$ (Grobauslegung) bzw. $V_{W,u}$ (Feinplanung) gleichgesetzt, und zwar unabhängig davon, ob die Speicher Trinkwasser, Betriebswasser oder eine Kombination beider Wasserarten in der ausgeführten Anlage enthalten sollen. Ebenfalls werden allfällig vorgesehene Vorwärm- und Mitteltemperaturzonen hier nicht berücksichtigt.

$$V_{W,sto} = 1{,}5 \cdot V_{W,u} \tag{21}$$

| Symbol | Bedeutung |
|---|---|
| $V_{W,sto}$ bzw. $V'_{W,sto}$ | Speichervolumen, in l |
| $V_{W,u}$ bzw. $V'_{W,u}$ | täglicher Nutzwarmwasserbedarf, in Normliter/d |

---

## B.4 Tägliche Speicherwärmeverluste

Die Wärmeverluste in 24 Stunden bei 45 K Temperaturdifferenz zur Umgebungsluft werden nach Gleichung 22 berechnet.

$$Q_{W,sto,ls} = c_1 \cdot \sqrt{\frac{V_{W,sto}}{V_0}} + c_2 \cdot (n_{cp} - 2) \tag{22}$$

| Symbol | Bedeutung |
|---|---|
| $Q_{W,sto,ls}$ bzw. $Q'_{W,sto,ls}$ | tägliche Speicherwärmeverluste, in kWh/d |
| $c_1$ | Koeffizient: 0,11 kWh/d |
| $V_{W,sto}$ bzw. $V'_{W,sto}$ | Speichervolumen, in l |
| $V_0$ | Referenzvolumen: 1 l |
| $c_2$ | Koeffizient: 0,10 kWh/d |
| $n_{cp}$ | Anzahl Wasser führender Stutzen am Speicher |

Gleichung 22 gilt für jede Speichergrösse. Siehe auch Figur 7.

![[Figur_7_Speicherwaermeverluste.png]]
**Figur 7** – Für die Speicherdimensionierung anzuwendende, tägliche Speicherwärmeverluste bei 2 Wasser führenden Stutzen gemäss Gleichung 22. Als Vergleich ist auch der Grenzwert der Speicherwärmeverluste gemäss EnEV dargestellt (siehe [[Anhang_J_Grenzwert_Speicher|Anhang J]]).

---

## B.5 Grenzwerte

In jedem Fall sind die Grenzwerte der Speicherwärmeverluste gemäss EnEV bei der Speicherwahl einzuhalten (siehe [[Anhang_J_Grenzwert_Speicher|Anhang J]]).

---

## B.6 Zielwert der Speicherwärmeverluste

Der Zielwert der Speicherwärmeverluste berechnet sich durch Multiplikation des Grenzwerts mit dem Faktor **0,73**. Dieser Faktor ist das Verhältnis der beiden $U_0$-Werte 0,15 bzw. 0,225 in Tabelle 2 von SIA 385/1:2020.

---

## B.7 Gültigkeitsbedingungen

Der gemäss B.4 ermittelte Wert von $Q'_{W,sto,ls}$ bzw. $Q_{W,sto,ls}$ gilt nur, wenn alle Rohranschlüsse am Speicher lückenlos wärmegedämmt und alle nicht ständig Wasser führenden Rohranschlüsse mit einem Wärmesiphon gemäss SIA 385/1 versehen werden.[^14]

---

## B.8 Dynamische Berechnung

Bei der dynamischen Berechnung der Energiebilanz der Warmwasserversorgung gemäss Kapitel 5 werden die Speicherwärmeverluste gemäss SN EN 15316-5 berechnet.

---

[^14]: Wenn Rohranschlüsse am Speicher nicht lückenlos wärmegedämmt sind oder Wärmesiphons bei nicht ständig Wasser führenden Rohranschlüssen fehlen, sind die Wärmeverluste des in Betrieb stehenden Speichers etwa doppelt so hoch. Wenn Rohranschlüsse am Speicher nicht lückenlos wärmegedämmt sind und gleichzeitig Wärmesiphons bei nicht ständig Wasser führenden Rohranschlüssen fehlen, sind die Wärmeverluste des in Betrieb stehenden Speichers etwa dreimal so hoch.

---

> ◀ [[Anhang_A_Warmwasserbedarf|Anhang A]]  ·  [[_SIA_385-2_2025_MOC|↑ Inhaltsverzeichnis]]  ·  [[Anhang_C_Hilfsenergie|Anhang C]] ▶

---
