---
tags: [Bauphysik, Wärmeschutz, Feuchteschutz, U-Wert, Gebäudetechnik]
skript: "Bauphysik"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "3.3–3.4"
titel: "Wärmeübergang an Oberflächen und Konvektion"
---

> ◀ [[03_1_2_waermedurchgang_waermeleitung|← Wärmefluss und Wärmeleitung]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[03_5_strahlung|Strahlung →]] ▶

---

# Bauphysik – Kapitel 3.3–3.4: Wärmeübergang an Oberflächen und Konvektion

### 3.3 Wärmeübergang (an Oberflächen)
> 📖 Kontext: [[03_1_2_waermedurchgang_waermeleitung|Bauphysik Kap. 3.1–3.2 – Wärmedurchgang & U-Wert (Gesamtbild)]]  ·  [[03_5_strahlung|Bauphysik Kap. 3.5 – Strahlung als dritter Wärmeübertragungsmechanismus]]

Der Wärmeübergang beschreibt den Wärmestrom an einer Grenze (Oberfläche) zwischen zwei Materialien mit unterschiedlichem Aggregatzustand. Dabei ist der Wärmestrom von der Bewegung des Fluides (flüssig oder gasförmig) abhängig. An solchen Grenzflächen geht die Wärme nicht einfach widerstandslos von einem Material zum anderen über, wie dies zwischen zwei Materialien mit gleichem Aggregatzustand der Fall ist (zwischen festen Stoffen ohne Luftspalt dazwischen). Vielmehr erfährt der Wärmefluss einen zusätzlichen Widerstand, der mit dem Wärmeübergangskoeffizienten h (früher α) erfasst wird. Dieser Wärmewiderstand ist eine Folge der Grenzschicht auf der Oberfläche des festen oder flüssigen Materials, die eine Dämmwirkung hat. Der h-Wert ist für den Wärmeübergang zwischen einem Gas (i. d. R. Luft) und einer festen Oberfläche (z. B. einer Wand) relevant, resp. zwischen festen und flüssigen Stoffen (z. B. in Wärmetauschern) oder zwischen flüssigen und gasförmigen Stoffen (z. B. Oberfläche von Badewasser). Der Wärmeübergangskoeffizient h gibt an, wie viel Wärmeleistung in W pro m² und einer Temperaturdifferenz von einem Grad fliesst. Seine Einheit ist W/(m²K).

Der Wärmefluss über eine solche Grenzfläche berechnet sich wie folgt:

$\dot{Q} = A \cdot h \cdot \Delta T \quad \left(\text{W} = \text{m}^2 \cdot \dfrac{\text{W}}{\text{K} \cdot \text{m}^2} \cdot \text{K}\right)$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $\dot{Q}$ | Wärmefluss | W |
| $A$ | Fläche (des Wärmeübergangs) | m² |
| $h$ | Wärmeübergangskoeffizient | W/(m²K) |
| $\Delta T$ | Temperaturdifferenz | K |

Der Wärmeübergangskoeffizient h hängt sehr stark von der Bewegung des flüssigen oder gasförmigen Stoffes ab. So ist der h-Wert von Luft von Haut zu Luft ohne Wind sehr viel kleiner, als wenn ein starker Wind weht. Deshalb friert man bei Wind viel mehr («Windchill»-Effekt). Die Bewegungen von Fluiden werden in laminare und turbulente Strömungen unterteilt. Bei laminaren Strömungen fliesst das Medium langsam und gleichförmig. Ab einer bestimmten Geschwindigkeit ändert die Strömungsart, es entsteht eine turbulente Strömung. Die Fliessbewegung wird voller Wirbel resp. Turbulenzen (z. B. ein Wildbach). Ob eine laminare oder turbulente Strömung vorhanden ist, kann mit der Reynolds-Zahl berechnet werden. Mit der Strömungsart ändert sich der Wärmeübergangskoeffizient h stark. Er nimmt bei turbulenter Strömung deutlich ab.

Die Berechnung von h ist schwierig und nicht exakt möglich. Es gibt empirische Formeln, mit denen dieser Wert berechnet werden kann (Formeln von Nusselt, mit Grashof bei freier Konvektion, und andere). In der Praxis werden oft Erfahrungswerte verwendet, für Berechnungen des U-Wertes bei Gebäuden gem. SIA 180:

- Luft zu Wand, Boden, Decke innen: h<sub>i</sub> = 7,7 W/(m²K)
- Luft zu Wand aussen: h<sub>e</sub> = 25 W/(m²K)

Der Unterschied zwischen innen und aussen bei diesen mittleren Erfahrungswerten rührt vom Wind aussen her. Bei windstillen Verhältnissen ist der Wert für innen und aussen fast gleich. Diese Erfahrungswerte sind eher auf der sicheren Seite, das heisst in Wirklichkeit dürften die Werte tiefer liegen. Sie beinhalten auch einen Anteil für Wärmeübergang infolge Strahlung.

Der Wärmeübergang hängt auch von der Oberflächenrauigkeit, der Geometrie des Körpers (Ausdehnung, Ausrichtung wie waagerecht oder senkrecht) und der Art des Fluides (Luft, Wasser, Öl usw.) ab.

### 3.4 Konvektion

Unter Konvektion wird ein Wärmetransport infolge der Eigenbewegung einer Flüssigkeit oder eines Gases verstanden. Da Fluide oft wenn nicht sogar meistens in Bewegung sind, ist die Konvektion meistens der bedeutendere Mechanismus von Wärmefluss als die Wärmeleitung. Dies gilt insbesondere für Gase.

Man kann grundsätzlich zwischen vier Formen der Konvektion unterscheiden:

- **Erzwungene Konvektion:** Die Fluidbewegung wird extern ermöglicht (Wind, Ventilator etc.)
- **Natürliche Konvektion:** Die Fluidbewegung wird durch den Dichteunterschied von verschieden warmen Fluiden verursacht. Das Fluid nahe an der Oberfläche hat eine andere Temperatur als das restliche und steigt bzw. sinkt daher ab. Natürliche Konvektion gibt es nur an nicht horizontalen Flächen.
- **Sieden:** Durch das Sieden steigen kleine Gasblasen in der Flüssigkeit auf, was einen sehr hohen Wärmeübergang an Oberflächen und eine starke Konvektion verursacht.
- **Kondensieren:** Ähnlich wie beim Sieden bilden sich beim Kondensieren kleine Tropfen, die nach unten fallen resp. sich auf der Oberfläche ablagern und somit den Wärmetransfer begünstigen.

---

> ◀ [[03_1_2_waermedurchgang_waermeleitung|← Wärmefluss und Wärmeleitung]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[03_5_strahlung|Strahlung →]] ▶

---
