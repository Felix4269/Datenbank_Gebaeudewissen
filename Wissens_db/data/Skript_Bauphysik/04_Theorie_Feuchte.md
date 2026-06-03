---
tags: [Bauphysik, Wärmeschutz, Feuchteschutz, U-Wert, Gebäudetechnik]
skript: "Bauphysik"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "4"
titel: "Theorie der feuchten Luft"
---

> ◀ [[03_6_u_wert_berechnung|← U-Wert-Berechnung]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[05_1_2_grundlagen_natuerliche_lueftung|Grundlagen und natürliche Lüftung →]] ▶

---

# Bauphysik – Kapitel 4: Theorie der feuchten Luft

## 4 Theorie der feuchten Luft
> 📖 Anwendung: [[05_5_luftfeuchtigkeit|Bauphysik Kap. 5.5 – Zu hohe Luftfeuchtigkeit & Kondensation]]  ·  [[03_2_mechanische_lueftung|Lüftung Kap. 3.2.9 – Lüftungsanlage mit Luftbefeuchtung]]

### 4.1 Verhalten von Gasgemischen als Grundlage

Die Umgebungsluft (die Erdatmosphäre) enthält neben Sauerstoff (ca. 20 %), Stickstoff (ca. 78 %) und Edelgasen immer auch Feuchtigkeit in Form von Wasserdampf.

Die Grundlage für das Verständnis der feuchten Luft sind zwei Tatsachen: das Verhalten der einzelnen Gase in einem Gasgemisch und die Tatsache, dass die Verdampfungstemperatur eines Stoffes vom Umgebungsdruck abhängig ist.

Zum ersten ist feuchte Luft ein Gasgemisch und verhält sich entsprechend: Jedes Gas resp. der Wasserdampf (auch ein Gas) nimmt einen Partialdruck an, wie wenn die anderen Gase in einem bestimmten Volumen nicht vorhanden wären. Die einzelnen Moleküle eines Gases spüren die Anwesenheit der Moleküle eines anderen Gases nicht. Die Summe der Partialdrücke aller einzelnen Gase ist der Druck des Gasgemisches (hier der Druck der Luft). Jedes Gas nimmt anders gesagt in einem bestimmten Volumen einen Partialdruck an, welcher von der Temperatur und der Anzahl der Moleküle (der Gasmenge) dieses Gases abhängig ist. Je mehr Moleküle vorhanden sind, resp. je höher die Temperatur ist, desto höher wird der Partialdruck dieses Gases. Dabei spielt es keine Rolle, um was für Moleküle es sich handelt. Würden also für ein bestimmtes Luftvolumen (z. B. 1 m³) bei konstanter Temperatur die Bestandteile (die Moleküle der einzelnen Gase) der Luft sortiert und in je ein separates, vorher völlig leeres Volumenbehältnis von 1 m³ gefüllt, so entspräche der Druck in diesen Volumenbehältern je dem Partialdruck der separierten Gase.

Zum zweiten ist die Verdampfungstemperatur jeden Stoffes, insbesondere auch von Wasser, vom Druck abhängig. Wasser siedet bekanntlich bei 100 °C. Dies gilt aber nur bei einem Druck von etwa 1 bar (100 000 Pa, resp. dem Umgebungsdruck etwa auf Meereshöhe). Sinkt der Druck, so sinkt auch die Verdampfungstemperatur, allerdings nicht linear, sondern nach einer Kurve, welche gemessen werden muss. Natürlich gilt umgekehrt, dass Wasser bei Drücken über 1 bar erst bei höherer Temperatur als 100 °C kocht. Auf diesem Prinzip beruht der Dampfkochtopf, welcher mit höherem Druck auch höhere Temperaturen erreicht, so dass das Gemüse rascher gar wird.

Bei üblichen Umgebungstemperaturen nimmt die Feuchtigkeit in der Luft also einen Partialdruck an, der deutlich unter einem Bar liegt. Der Partialdruck des Wasserdampfes kann dabei maximal so hoch liegen, dass bei der herrschenden Temperatur das Wasser noch verdampft. Mit anderen Worten, bei 100 °C Lufttemperatur und 1 bar Luftdruck könnte die Umgebungsluft zu 100 % aus Wasserdampf bestehen. Je tiefer die Temperatur sinkt, desto tiefer muss der Partialdruck des Wasserdampfes sinken. Bei 20 °C beträgt er bspw. noch maximal 0,023 bar.

Daraus folgt, dass es für jede Temperatur der Luft einen maximalen Wasserdampfgehalt gibt. Mit zunehmender Temperatur nimmt dieser maximale Gehalt zu. Wenn Luft den maximalen Wasserdampfgehalt enthält, wird die Luft gesättigt genannt. Der zugehörende Partialdruck ist der Sättigungsdruck. Ist mehr Feuchte in der Luft, kondensiert der überschüssige Wasserdampf, entweder es bilden sich Tröpfchen oder Nebel, oder es gibt Oberflächenkondensation.

### 4.2 Die zwei Messgrössen für feuchte Luft

Aus diesem Verhalten von Gasen in einem Gasgemisch oder hier des Wasserdampfes in Luft, ergibt sich dass der Feuchtegehalt in der Luft auf zwei Arten angegeben werden kann: als relative Feuchte (in der Praxis ist dies das übliche Mass) oder als absoluten Feuchtegehalt.

Aus der Relation des effektiven zum maximalen Wassergehalt wird die relative Feuchte φ der Luft definiert. Die relative Feuchte φ wird in Prozent angegeben.

> [!info] Relative Feuchte
> φ = effektiver Wasserdampfgehalt / max. Wasserdampfgehalt (%)

Die absolute Feuchte v (früher x) ist dagegen der effektive Wasserdampfgehalt der Luft. Sie wird als Masse des Wassersdampfes pro Volumeneinheit trockene Luft angegeben, die Einheit ist g/m³. Auch hier gibt es eine von der Temperatur abhängige maximale Feuchte: $v_s$, die Sättigungsfeuchte.

> [!info] Absolute Feuchte
> v = effektiver Wasserdampfgehalt pro Kubikmeter trockene Luft (g/m³)

Die relative Feuchte φ allein sagt nichts über den effektiven Wassergehalt der Luft aus. Sie gibt nur an, wie viel Prozent der maximal möglichen Feuchte in der Luft bei der gerade herrschenden Temperatur vorhanden ist. Erst zusammen mit der Lufttemperatur kann aus Diagrammen (insb. dem Mollier-Diagramm) oder mit Berechnungsprogrammen bestimmt werden, wie viel dampfförmiges Wasser die Luft wirklich enthält.

Wenn feuchte Luft ohne weitere Feuchtezufuhr erwärmt wird, dann sinkt die relative Feuchte, weil der maximal mögliche Feuchtegehalt steigt. Umgekehrt, wenn feuchte Luft ohne Kondensation abgekühlt wird, dann steigt die relative Feuchte. Wird dann bei weiterer Abkühlung die Sättigungsgrenze erreicht (φ = 100 %), kondensiert das überschüssige Wasser (es «fällt aus»). Dabei bildet sich Nebel in der Luft und nahe Oberflächen können feucht werden (Kondensation, z. B. Tau). Nebel ist auskondensiertes Wasser, welches vorerst sehr kleine, schwebende Tröpfchen in der Luft bildet. Fällt die Temperatur weiter, kann es regnen (die Wassertröpfchen werden grösser und fallen zu Boden).

Sichtbar ist Wasserdampf in der Luft nicht, nur Tröpfchen (Nebel) sind sichtbar.

Der Mensch empfindet primär die relative Feuchte. Diese ist für das Trocknungsvermögen der Luft verantwortlich. In gesättigter Luft kann nichts getrocknet werden. In stark feuchter Luft kann deshalb die Körpertemperatur nur noch schlecht mit Schwitzen, das heisst durch Abgabe von Verdampfungswärme, reguliert werden (die Luft wird als schwül empfunden). In sehr trockener Luft dagegen trocknen die Schleimhäute oder die Augen vermehrt aus.

Im Winter ist es aussen oft kalt und neblig. Die Aussenluft ist zu fast 100 % gesättigt. Der absolute Wassergehalt ist aber nur klein (Beispiel: bei 0 °C und 95 % rel. Feuchte ist die absolute Feuchte nur 4,63 g/m³). Beim Lüften mit Fenstern oder mit einer Lüftungsanlage gelangt diese Aussenluft ins Innere eines beheizten Hauses. Wird diese vermeintlich feuchte Aussenluft nun auf bspw. 20 °C erwärmt, bleibt ohne weitere Befeuchtung der absolute Feuchtegehalt gleich (4,63 g/m³). Die relative Feuchte beträgt im Innern dann noch knapp 25 %, es wird also trocken.

### 4.3 Energiegehalt von Luft

Der totale Energiegehalt (die Enthalpie) der feuchten Luft ist durch die Temperatur der Luft, durch den Gehalt an Wasserdampf und drittens durch den Druck bestimmt. Der Luftdruck ist üblicherweise recht konstant, es ist der atmosphärische Druck von etwa einem Bar. Solange kein Wasser zugeführt oder entzogen wird (keine Be- oder Entfeuchtung), kann der Energiegehalt der Luft wie folgt berechnet werden (bei konstantem Druck):

$$H = c_p \cdot m_L \cdot \Delta T$$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $H$ | Energiegehalt (Wärme) | kJ |
| $c_p$ | spez. Wärme (für Luft ca. 1 kJ/(kg K)) | kJ/(kg K) |
| $m_L$ | Luftmasse (1 m³ Luft ≈ 1,15 kg) | kg |
| $\Delta T$ | Temperaturdifferenz zu Null Grad | °C oder K |

Wird der Luft zusätzlich flüssiges Wasser zugeführt (üblicherweise in Form von Tröpfchen) oder entzogen (üblicherweise durch Kondensation an einer kalten Oberfläche), so muss für dieses Wasser die Verdampfungs- resp. Kondensationswärme aufgebracht werden. Diese Energie ist recht gross im Vergleich zur Wärme nach der obigen Formel. Diese gilt deshalb dann nicht mehr. Bei Befeuchtung durch Tröpfchen wird die Luft kälter, da der Luft die Verdampfungswärme entzogen wird (adiabatische Befeuchtung resp. Kühlung).

Die Energie der trockenen Luft und des Wasserdampfes zusammen ist die Enthalpie (die enthaltene Energie). Bei adiabatischer Kühlung oder Befeuchtung ändert die Enthalpie der Luft nicht, die Feuchte steigt, die Temperatur sinkt.

Die erforderliche Energie bei Zustandsänderungen mit Änderung der absoluten Feuchte v kann aufwändig berechnet werden, einfacher aber entnimmt man die Enthalpiedifferenz zwischen zwei Luftzuständen dem h-v resp. Mollier-Diagramm (Abbildung 10).

Wichtig ist zu verstehen, dass Änderungen der absoluten Feuchte immer viel Energie (Wärme zum Befeuchten oder Kälte zum Entfeuchten) benötigen. Der Rückgewinn von Feuchte im Winter kann deshalb eine wichtige Energiesparmassnahme bedeuten. Im Sommer kann der Verzicht auf eine verstärkte Entfeuchtung den Energiebedarf für die Klimatisierung verringern.

Würde der Luft hingegen Wasser in Form von Wasserdampf befeuchtet, welcher dieselbe Temperatur wie die Luft hat, steigt die Enthalpie der Luft, aber die Temperatur würde konstant bleiben (isotherme Befeuchtung).

![[abb10_mollier_h-x-diagramm_feuchte_luft.png]]
*Abbildung 10: Mollier h-x-Diagramm für feuchte Luft (Druck 0.95 bar, 537 m ü M, 10 °C, 80 % rF)*

---

> ◀ [[03_6_u_wert_berechnung|← U-Wert-Berechnung]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[05_1_2_grundlagen_natuerliche_lueftung|Grundlagen und natürliche Lüftung →]] ▶

---
