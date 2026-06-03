---
tags: [Bauphysik, Wärmeschutz, Feuchteschutz, U-Wert, Gebäudetechnik]
skript: "Bauphysik"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "3.1–3.2"
titel: "Wärmefluss durch Bauteile und Wärmeleitung"
---

> ◀ [[02_Waermeverluste_Trans|← Verringerung der Wärmeverluste durc]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[03_3_4_waermeuebergang_konvektion|Wärmeübergang und Konvektion →]] ▶

---

# Bauphysik – Kapitel 3.1–3.2: Wärmefluss durch Bauteile und Wärmeleitung

## 3 Theorie Wärmedurchgang

### 3.1 Wärmefluss durch Wände, Fenster oder Dächer
> 📖 Anwendung: [[03_6_u_wert_berechnung|Bauphysik Kap. 3.6 – U-Wert-Berechnung einer Wand]]  ·  [[02_Waermeverluste|Skript Energie Kap. 2 – Wärmeverluste durch Transmission]]  ·  [[01_1_Modell_Grundsaetzliches|IDA ICE Tutorial – Bauteilkonstruktionen & U-Werte im Modell]]

Aus dem zweiten Hauptsatz der Thermodynamik geht hervor, dass Wärme immer nur von der höheren zur tieferen Temperatur fliesst. Zwei Körper, welche die genau gleiche Temperatur haben, tauschen keine Wärme aus. In der Physik wird dies als adiabatisch bezeichnet. Heisst dies nun umgekehrt, dass zwischen zwei benachbarten Körpern unterschiedlicher Temperatur immer Wärme fliesst? Ja! Aus der Erfahrung wissen wir beispielsweise, dass die Wärme aus einer Flasche heissen Tees unterschiedlich schnell „verloren" geht (d. h. zur kühleren Umgebung fliesst und sich dort verteilt), je nachdem ob es sich um eine gewöhnliche Glas- oder PET-Flasche oder eine Thermosflasche handelt. Der Unterschied liegt in der Isolation resp. Wärmedämmung der beiden Flaschen.

Der Wärmefluss, welcher zwischen zwei Körpern fliesst, bemisst sich also nach der Wärmedämmung resp. Isolation. Je besser diese Dämmung ist, desto weniger Wärme fliesst. Die Dämmung ist ein Widerstand gegen den Wärmefluss. Damit keine Wärme mehr fliesst, müsste der Wärmewiderstand unendlich gross sein. Wir wissen, auch der Tee in der besten Thermosflasche wird irgendeinmal kalt. Es fliesst immer mehr oder weniger Wärme, solange eine Temperaturdifferenz besteht. Eine unendlich dicke Wärmedämmung ist nicht machbar.

Die Temperaturdifferenz ist die antreibende Kraft für den Wärmefluss. Je höher die Temperaturdifferenz, desto mehr Wärme fliesst über eine bestimmte Fläche (bei konstanter Dämmung). Dieser Zusammenhang ist linear. Bei 10-facher Temperaturdifferenz fliesst 10-mal mehr Wärme.

Als drittes ist der Wärmefluss auch von der Fläche zwischen den beiden Körpern abhängig. Auch dieser Zusammenhang ist linear.

Der Wärmefluss ist die (Wärme-)Leistung, welche vom einem zum anderen Körper fliesst. Je grösser diese Leistung ist, desto mehr Energie wird pro Zeiteinheit ausgetauscht. Der Tee, welcher zu Beginn in der Glas- und der Thermosflasche gleich viel Wärmeenergie enthielt, wird in der Glasflasche viel rascher kalt, da die Wärmeleistung zur Umgebung viel grösser ist. Da die Wärme in der Umgebung nicht mehr nutzbar ist, spricht man in solch einem Fall auch von Verlustleistung resp. Wärmeverlust, obwohl die Wärme physikalisch gesehen immer noch vorhanden ist (erster Hauptsatz der Thermodynamik).

#### Wärmedurchgangskoeffizient U

Der Wärmedurchgangskoeffizient (auch Wärmedurchgangszahl) U gibt an, wie gut ein Bauteil isoliert ist. Er bedeutet den Wärmefluss in Watt pro m² senkrecht zur Oberfläche bei einer Temperaturdifferenz eines Grades Kelvin (oder Celsius). Je kleiner der U-Wert ist, desto besser ist die Dämmung. Aufgrund der EU-Normung wird die angelsächsische Abkürzung U verwendet. Die Einheit ist W/(m²K). Früher hiess dieser Wert in der Schweiz k-Wert.

Der U-Wert stellt den Schlüssel zum Wärmedurchgang dar. Er beruht auf drei wesentlichen Formen des Wärmedurchgangs: Wärmeleitung, Wärmeübergang, Strahlung.

Unten findet sich die Formel zur Berechnung des Wärmeflusses durch eine Wand, in Abhängigkeit des U-Wertes.

$\dot{Q} = \Delta T \cdot A \cdot U \quad \left(\text{W} = \text{K} \cdot \text{m}^2 \cdot \dfrac{\text{W}}{\text{m}^2\text{K}}\right)$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $\dot{Q}$ | Wärmefluss | W |
| $\Delta T$ | Temperaturdifferenz | K oder °C |
| $A$ | Fläche | m² |
| $U$ | Wärmedurchgangskoeffizient | W/(m²K) |

### 3.2 Wärmeleitung

Die Wärmeleitung (auch Konduktion oder Wärmediffusion genannt) findet in festen, flüssigen oder gasförmigen Materialien statt, ohne den Wärmetransport durch eine Bewegung dieser Materialien. Die Stärke der Wärmeleitung ist von deren Eigenschaften abhängig. Jedes Material leitet mehr oder weniger Wärme. Dabei gibt es Stoffe, welche Wärme sehr gut leiten (z. B. Metalle, speziell Kupfer, Aluminium und Gusseisen, aber auch Beton), und Stoffe, welche dem Wärmefluss einen erheblichen Widerstand entgegensetzen, die Dämmmaterialien (z. B. Kork, Steinwolle, PU-Schaum, Polystyrol). Auch Flüssigkeiten und Gase leiten die Wärme. Luft leitet Wärme allerdings schlecht, so dass stehende Luft eine gute Dämmung bewirkt. Noch schlechtere Wärmeleiter sind Edelgase. Gar keine Wärmeleitung ist in Vakuum möglich.

Die Fähigkeit der Materialien, Wärme zu leiten, wird mit der Wärmeleitfähigkeit λ (Lambda) bezeichnet. Der λ-Wert ist eine Materialeigenschaft wie die spez. Wärmekapazität c<sub>p</sub> und ist ebenso sehr leicht von der Temperatur abhängig. Die Wärmeleitfähigkeit λ gibt an, wie viel Wärmefluss pro Grad Temperaturdifferenz und pro Meter Materialstärke fliesst. Die Wärmeleitfähigkeit wird bei sich nicht bewegendem Material gemessen, welches plattenförmig ist. Die Einheit von λ ist Watt pro Kelvin und pro Meter (W/(Km)).

Für die Berechnung des Wärmeflusses infolge Wärmeleitung gilt:

$\dot{Q} = \frac{A}{d} \cdot \lambda \cdot \Delta T \quad \left(\text{W} = \dfrac{\text{m}^2}{\text{m}} \cdot \dfrac{\text{W}}{\text{K} \cdot \text{m}} \cdot \text{K}\right)$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $\dot{Q}$ | Wärmefluss | W |
| $A$ | Fläche (rechtwinklig zum Wärmestrom) | m² |
| $d$ | Materialstärke (Dicke) | m |
| $\lambda$ | Wärmeleitfähigkeit | W/(Km) |
| $\Delta T$ | Temperaturdifferenz | K |

---

> ◀ [[02_Waermeverluste_Trans|← Verringerung der Wärmeverluste durc]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[03_3_4_waermeuebergang_konvektion|Wärmeübergang und Konvektion →]] ▶

---
