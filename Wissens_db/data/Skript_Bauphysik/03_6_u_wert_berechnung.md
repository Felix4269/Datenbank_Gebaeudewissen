---
tags: [Bauphysik, Wärmeschutz, Feuchteschutz, U-Wert, Gebäudetechnik]
skript: "Bauphysik"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "3.6"
titel: "Berechnung des U-Wertes einer Wand"
---

> ◀ [[03_5_strahlung|← Strahlung]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[04_Theorie_Feuchte|Theorie der feuchten Luft →]] ▶

---

# Bauphysik – Kapitel 3.6: Berechnung des U-Wertes einer Wand

### 3.6 Berechnung des U-Wertes einer Wand
> 📖 Anwendung: [[02_Waermeverluste|Skript Energie Kap. 2 – Wärmeverluste durch Transmission]]  ·  [[01_1_Modell_Grundsaetzliches|IDA ICE Tutorial – Bauteilkonstruktionen & U-Werte im Modell]]

Im Internet sind verschiedene U-Wert-Berechnungsprogramme zu finden, mit denen U-Werte einfach berechnet werden können. Mit den h-Werten für innen und aussen sowie den Wärmedurchgangswerten der verschiedenen Wandschichten rechnet sich der U-Wert für eine homogene Wand nach der folgenden Formel:

$$U = \dfrac{1}{\dfrac{1}{h_i} + \dfrac{d_1}{\lambda_1} + \dfrac{d_2}{\lambda_2} + \cdots + \dfrac{d_n}{\lambda_n} + \dfrac{1}{h_e}}$$

| Symbol | Bedeutung | Einheit |
|---|---|---|
| $U$ | Wärmedurchgangskoeffizient | W/(m²K) |
| $h_i$ | Wärmeübergangskoeffizient innen | W/(m²K) |
| $h_e$ | Wärmeübergangskoeffizient aussen | W/(m²K) |
| $d_n$ | Dicke der Schicht n | m |
| $\lambda_n$ | Wärmeleitfähigkeit Material n | W/(Km) |

Der U-Wert von Fenstern und inhomogenen Flächen ist mit besonderen Methoden zu rechnen. Im Falle einer Wärmedämmung, welche von weniger gut dämmenden Bauteilen unterbrochen ist (z. B. eine Dachdämmung zwischen den Sparren), kann auch der U-Wert beider Wandaufbauten berechnet werden und dem Flächenanteil entsprechend gewichtet zum U-Wert der ganzen Fläche zusammengefasst werden.

Typische Beispiele für U-Werte finden sich in der Tabelle 2.

*Tabelle 2: Beispiele für U-Werte von Bauteilen*

| Bauteil | U-Wert |
|---|---|
| Aussenwand unsaniertes Gebäude bis ca. 1973 | 0,8 bis 1,2 W/(m²K) |
| Aussenwand/Dach neues Gebäude (ab 2015) | < 0,2 W/(m²K) |
| Wand/Dach eines MINERGIE®-Hauses | < 0,15 W/(m²K) |
| Einfachverglasung | 5,8 W/(m²K) |
| Doppelverglasung (DV) | 2,8 W/(m²K) |
| 2-fach-Isolier-Verglasung (2 IV) | 3,0 W/(m²K) |
| 2-fach Wärmeschutzglas (2 WS) | 1,0 bis 1,4 W/(m²K) |
| 3-fach Wärmeschutzglas (3 WS) | 0,4 bis 0,7 W/(m²K) |
| Fensterrahmen ohne spezielle Dämmung | ca. 1,6 bis 2,0 W/(m²K) |
| Ganzes Fenster mit 2 WS-Verglasung | ca. 1,3 W/(m²K) |
| Ganzes Fenster mit 3 WS-Verglasung und isol. Rahmen | ca. 0,8 bis 1,0 W/(m²K) |

Die Abbildung 9 zeigt den berechneten Temperaturverlauf zwischen einer ungedämmten und einer gedämmten zweischaligen Aussenwand. Im zweiten Fall resultiert eine wesentlich höhere Temperatur der Innenoberfläche und der inneren Wandschicht. Dies beugt Problemen mit Kondensation vor und ergibt einen wesentlich besseren Komfort. Die gedämmte Wand verfügt zudem über eine Dampfbremse innen, um die Trockenheit aller Wandschichten zu garantieren. Im ungedämmten Zustand kann innen an der äusseren Klinkerschicht Kondensation auftreten (blau gefärbt).

#### Wärmewiderstand

Der Kehrwert des U-Wertes wird als Wärmewiderstand R bezeichnet. Die Wärmewiderstände der einzelnen Schichten einer Wand (inkl. der Wärmeübergangswiderstände innen und aussen) können aufaddiert werden. Die Summe aller Schichten ist der Wärmewiderstand der ganzen Wand. Der reziproke Wert ist wieder der U-Wert der ganzen Wand.

![[abb9_temperaturverlauf_in_einer_ungedammten_lin_1.jpg]]
![[abb9_temperaturverlauf_in_einer_ungedammten_lin_2.jpg]]
*Abbildung 9: Temperaturverlauf in einer ungedämmten (links) und einer gedämmten Wand (rechts)<sup>6</sup>*

<sup>6</sup> Quelle: eigene Berechnung mit www.ubakus.de

---

> ◀ [[03_5_strahlung|← Strahlung]] · [[_Skript_Bauphysik_MOC|↑ MOC]] · [[04_Theorie_Feuchte|Theorie der feuchten Luft →]] ▶

---
