---
tags: [Bauphysik, Wärmeschutz, Feuchteschutz, U-Wert, Gebäudetechnik]
skript: "Bauphysik"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "3.5"
titel: "Strahlung"
---

> ◀ [[03_3_4_waermeuebergang_konvektion|← Wärmeübergang und Konvektion]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[03_6_u_wert_berechnung|U-Wert-Berechnung →]] ▶

---

# Bauphysik – Kapitel 3.5: Strahlung

### 3.5 Strahlung
> 📖 Anwendung: [[03_2_solare_waermegewinne|Skript Energie Kap. 3.2 – Solare Wärmegewinne & g-Wert]]  ·  [[03_3_1_zone_intro_solar|IDA ICE Manual Kap. 3.3–3.4 – Zone Models: Solar]]

Die dritte Grösse für den Wärmedurchgang ist die Strahlung. Diese ist ein nicht Materie-gebundener Wärmetransport zwischen zwei Körpern. Dieser Wärme- resp. Energietransport erfolgt mit relativ langwelliger elektromagnetischer Strahlung im gasgefüllten oder luftleeren Raum. Mit kürzer werdender Wellenlänge wird diese Strahlung zu sichtbarem Licht. Wärmestrahlung im nicht sichtbaren Bereich wird als Infrarot-Strahlung bezeichnet.

Die Strahlung ist uns täglich bekannt und Grundlage allen Lebens auf der Erde. Alle Energie von der Sonne gelangt so auf die Erde, gesendet durch das leere Weltall. Damit wird auch klar, dass die Strahlung nicht durch Distanz behindert wird. Jedoch wird die Strahlung ab einer punkt- oder scheibenförmigen Quelle mit zunehmender Distanz mehr verteilt und deswegen beim Absorber pro Flächeneinheit schwächer.

Jeder Körper sendet eine von seiner Temperatur und seiner Oberfläche abhängige Strahlung aus. Die totale Wärme, welche ein Körper emittiert, wird durch das Stefan-Boltzmann-Gesetz beschrieben:

$E_b = A \cdot \varepsilon \cdot \sigma \cdot T^4$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $E_b$ | totale Wärmeabstrahlung | W |
| $A$ | Aufsichtsfläche | m² |
| $\varepsilon$ | Emissionsverhältnis | dimensionslos |
| $\sigma$ | Stefan-Boltzmann-Konstante ($\sigma = 5{,}67 \times 10^{-8}$ W/(K⁴m²)) | W/(K⁴m²) |
| $T$ | Temperatur | K |

Die bei einer bestimmten Temperatur maximal mögliche Abstrahlung liefert ein schwarzer Körper (Schwarzkörper-Strahlung). Man nennt einen Körper schwarz, wenn er alle auftreffenden Strahlen absorbiert, weiss, wenn er alle auftreffenden Strahlen reflektiert. Jeder andere Körper emittiert weniger als der schwarze Körper, er wird als grau bezeichnet. Das Verhältnis seiner Abstrahlung zu der des schwarzen Körpers nennt man sein Emissionsverhältnis ε, es ist nach dem Kirchhoffschen Gesetz für grau-diffuse Flächen gleich seinem Absorptionsverhältnis a (ε = a). Damit kann ε (dimensionslos) zwischen 0 und 1 liegen. Eine schwarze, matte/diffuse Fläche hat ε = 1, ein idealer Spiegel (nicht diffus) oder eine perfekt weisse Fläche (diffus) ε = 0. Alltägliche Gegenstände liegen meist um ε = 0,9, polierte Metalloberflächen um ε = 0,3.

Die auftreffende Strahlung auf eine Oberfläche wird entweder reflektiert, absorbiert oder bei durchscheinenden Stoffen auch transmittiert. Die Summe der reflektierten, absorbierten und transmittierten Strahlung entspricht der auftreffenden Strahlung. Die Summe des reflektierten Bruchteiles (Reflexionsverhältnis r), des absorbierten Bruchteils (Absorptionsverhältnis a) und des durchgelassenen Bruchteils (Transmissionsverhältnis d) ist immer Eins (r + a + d = 1).

Wenn wir uns einen Körper im leeren Raum vorstellen, verliert dieser mehr oder weniger schnell seine gesamte Wärme durch Abstrahlung. Befindet sich ein anderer Körper in diesem Raum, tauschen die beiden Körper Wärme aus. Natürlich kann die resultierende ausgetauschte Wärme auch Null sein. Dies ist genau dann der Fall, wenn die Körper die gleiche Temperatur aufweisen. Gegenstände mit gleicher Temperatur tauschen keine Strahlungswärme aus. Der Strahlungsaustausch zwischen zwei undurchlässigen Flächen hängt von der Temperaturdifferenz in 4ter Potenz, der Fläche A, ihren ε-Werten (resp. den Absorptionsgraden a) sowie vom Raumwinkel (Θ) ab, unter dem sie sich sehen. Mit zunehmender Temperaturdifferenz nimmt der Strahlungsaustausch also stark zu, wegen der Abhängigkeit von der 4ten Potenz.

$\dot{Q}_{1-2} = f(\Delta T^4,\; A,\; \varepsilon,\; \Theta)$

Die manuelle Berechnung des Strahlungsaustausches ist schwierig, insbesondere wegen der Abhängigkeit vom Raumwinkel. Zudem sieht ein Körper meist verschiedene andere Flächen oder Körper mit je unterschiedlicher Temperatur und Emissionsverhältnis ε. Mit Computerprogrammen hingegen kann eine solche Berechnung gut erfolgen.

In der bauphysikalischen Praxis wird deswegen der Effekt der Strahlung für die Berechnung des U-Wertes in den h-Wert gepackt, das heisst der Wärmeübergangskoeffizient wird um einen mittleren Strahlungsanteil erhöht.

In Wirklichkeit ändert dieser Strahlungsanteil stark, insbesondere für Körper im Freien. Tagsüber bei Sonnenstrahlung wird deren Oberfläche stark aufgeheizt. Nachts kühlen Oberflächen, welche das kalte Weltall sehen, bei klarem Himmel stark ab und verlieren viel Strahlungswärme dorthin. Dies ist der Grund, warum am Morgen oft Reif von der Windschutzscheibe gekratzt werden muss, selbst wenn die Lufttemperatur nicht unter 0 °C fiel.

---

> ◀ [[03_3_4_waermeuebergang_konvektion|← Wärmeübergang und Konvektion]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[03_6_u_wert_berechnung|U-Wert-Berechnung →]] ▶

---
