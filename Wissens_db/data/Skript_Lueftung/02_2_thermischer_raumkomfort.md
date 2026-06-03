---
tags: [Lueftung, Lueftungstechnik, Raumlufttechnik, Klimaanlage]
skript: "Lueftung"
autor: "Prof. Markus Hubbuch"
version: "2025"
kapitel: "2.2"
titel: "Thermischer Raumkomfort"
---

> ◀ [[02_1_schadstoffabfuhr_luftfuehrung|← Schadstoffabfuhr und Luftführung]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[03_1_freie_lueftung|Freie Lüftung →]] ▶

---

# Lüftungstechnik – Kapitel 2.2: Thermischer Raumkomfort

### 2.2 Thermischer Raumkomfort
> 📖 Theorie: [[03_1_interne_waermegewinne|Skript Energie Kap. 3.1 – Interne Wärmegewinne (Personen, Geräte, Beleuchtung)]]  ·  [[03_2_solare_waermegewinne|Skript Energie Kap. 3.2 – Solare Wärmegewinne & g-Wert]]

Soll die Lüftungsanlage auch den thermischen Komfort im Raum, das heisst die Raumlufttemperatur beeinflussen, so muss der Luftwechsel resp. müssen die Luftraten aufgrund der zu- oder abzuführenden thermischen Last (Heizung oder Kühlung) berechnet werden. In Westeuropa erfolgt die Wärmezufuhr (Raumheizung) meist über ein wasserführendes Heizsystem. Überschüssige Wärme abzuführen kann dagegen die Aufgabe einer Lüftungsanlage sein (Raumkühlung).

#### 2.2.1 Wärmelasten im Raum

Die in einem Raum anfallende Wärme wird als **Wärmelast** bezeichnet, wenn sie zu einer unerwünscht hohen Raumtemperatur (im Allgemeinen über 26 °C) führt.

Wärme, welche im Raum selbst anfällt, wird als **interne Last** bezeichnet.
Wärme, die von aussen bei Sonnenschein einfällt, wird als **externe Last** bezeichnet.

*Tabelle 7: Wärmelasten im Raum*

| Lasttyp            | Quelle                        | Richtwert                                                                                              |
| ------------------ | ----------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Interne Lasten** | Personen                      | 80 bis 100 W pro Person (sensible Wärme, je nach Raumtemperatur)                                       |
|                    | Computer                      | ca. 120 bis 150 W pro PC, 30 W pro Laptop                                                              |
|                    | Bildschirm                    | ca. 30 bis 60 W                                                                                        |
|                    | Drucker etc.                  | ca. 50 bis 200 W pro Gerät (Tintenstrahl / Laser)                                                      |
|                    | Beleuchtung                   | LED ca. 4 bis 6 W/m², Leuchtstofflampe 10 bis 20 W/m²                                                  |
|                    | Weitere Geräte                | fallweise entsprechend gemessenem Stromverbrauch (nicht nach Nennleistung gemäss Typenschild!)         |
| **Externe Lasten** | Sonnenstrahlung durch Fenster | abhängig von Orientierung, Verglasung, Sonnenschutz (→ Skript Kältetechnik / Energieflüsse im Gebäude) |
|                    | Warme Aussenluft              | bei ungekühlter Zuluft im Hochsommer                                                                   |
|                    | Transmissionswärme            | bei guter Dämmung sehr gering, im Hochsommer                                                           |

#### 2.2.2 Raumtemperatur

Die als komfortabel empfundene Raumtemperatur ist abhängig von der Bekleidung (Einheit clo) und der Aktivität (Einheit met). In der Norm SIA 180 (2014) ist die Grafik mit den als behaglich empfundenen Raumtemperaturen in Abhängigkeit der Bekleidung und der Aktivität zu finden. Die optimale Raumtemperatur liegt im Sommer höher und im Winter tiefer, weil dies durch unterschiedliche Bekleidung ausgeglichen werden kann.

Üblich genutzte Räume müssen bei kühlen Aussentemperaturen auf mindestens **20,5 °C** erwärmt werden (untere Temperatur tagsüber im Winter resp. Heizfall). Bei warmen Aussentemperaturen sollte die Raumtemperatur unter **26,5 °C** bleiben (= obere Temperatur im Sommer resp. im Kühlfall). Höhere Raumtemperaturen werden als unangenehm empfunden und senken die Leistungsfähigkeit einer Person. Raumtemperaturen über **30 °C** sind sehr unangenehm und sollten vermieden werden. Die Leistungsfähigkeit sinkt rapide, die Fehlerhäufigkeit und Unfallgefahr steigt.

Der Mensch empfindet nicht die Raumlufttemperatur, sondern einen Mittelwert aus Raumlufttemperatur und Oberflächentemperatur der Raumumschliessungsflächen (Strahlungstemperatur).

#### 2.2.3 Luftvolumenstrom thermisch erforderlich

Der aus thermischen Gründen erforderliche Luftvolumenstrom rechnet sich aus der abzuführenden Wärmeleistung, der Temperaturdifferenz zwischen Zu- und Ablufttemperatur (gleich Raumtemperatur) und der spezifischen Wärmekapazität der Luft $c_p$ nach Formel 1:

$$\dot{V} = \frac{P \cdot 3600}{c_p \cdot \Delta T}$$

*Formel 1: Thermisch erforderlicher Luftvolumenstrom*

| Variable | Bedeutung | Einheit |
|---|---|---|
| $P$ | thermische Leistung | kW (= kJ/s) |
| $\dot{V}$ | Luftvolumenstrom | m³/h |
| $\Delta T$ | Temperaturdifferenz | K (= °C, weil Temperaturdifferenz) |
| $c_p$ | spez. Wärmekapazität der Luft | kJ/(m³·K), Luft ca. 1,2 kJ/(m³·K) |
| 3600 | Umrechnungsfaktor | s/h |

---

> ◀ [[02_1_schadstoffabfuhr_luftfuehrung|← Schadstoffabfuhr und Luftführung]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[03_1_freie_lueftung|Freie Lüftung →]] ▶

---
