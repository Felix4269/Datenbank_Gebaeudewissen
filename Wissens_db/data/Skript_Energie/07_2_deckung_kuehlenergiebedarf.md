---
tags: [Energie, Heizwärmebedarf, Wärmegewinne, Gebäudetechnik]
skript: "Energieflüsse im Gebäude"
autor: "Prof. Markus Hubbuch"
version: "2026"
kapitel: "7.2"
titel: "Deckung Kühlenergiebedarf"
---

> ◀ [[07_1_bauweise_beschattung|← Bauweise und Beschattung]] · [[_Skript_Energie_MOC|↑ MOC]] · [[07_3_freie_kuehlung|Freie Kühlung →]] ▶

---

# Energieflüsse im Gebäude – Kap. 7.2: Deckung Kühlenergiebedarf

### 7.2 Deckung Kühlenergiebedarf
> 📖 Systeme: [[03_2_mechanische_lueftung|Lüftung Kap. 3.2.10 – Einfache Klimaanlage (Kühlung)]]  ·  Simulation: [[_NEST_Sprint_MOC|NEST Sprint – Parameter cooling_capacity_offices (Run 002)]]

Der Kühlenergiebedarf entspricht der Wärmemenge, die typischerweise im Sommerhalbjahr aus
einem Gebäude abgeführt werden muss, um zu hohe Temperaturen in den Räumen zu
verhindern. Um auch an den wärmsten Tagen mit hohen internen und externen Lasten die Räume
noch genügend kühlen zu können, muss auch die Kühlleistung ausreichen.
Räume werden im Wesentlichen aus zwei Gründen gekühlt:

Spezialräume mit durch die Nutzung bedingten hohen internen Lasten oder tiefen Temperaturen werden dauernd gekühlt. Solche Räume sind typischerweise Serverräume (hohe Lasten), Lebensmittelläden (keine zu hohen Temperaturen zulässig) oder Kühlräume (tiefe Temperaturen, in diesem Fall spricht man von gewerblicher Kühlung).
Solche Räume werden wegen der Nutzungsanforderungen gekühlt. Sie müssen meist während
dem ganzen Jahr gekühlt werden. Diese überschüssige Wärme kann genutzt werden, mittels
Wärmerückgewinnung aus der Abwärme der Kältemaschine oder bei Serverräumen eventuell
direkt. Wo etwa so viel Wärme anfällt, wie für die Erwärmung des Warmwassers benötigt wird, ist
diese Nutzung die sinnvollste und heute in den meisten Fällen wirtschaftliche Lösung. Wo mehr
Wärme anfällt, kann diese Wärme im Winter ggf. für die Raumheizung genutzt werden.
Wo die Abwärme genutzt werden kann, sollte diese als Wärmequelle betrachtet werden. Die
Kälteerzeugung wird zum erwünschten Nebeneffekt. Überschüssige Wärme muss an die
Umgebung (meist an die Aussenluft) abgegeben werden.
Räume wie Büros, Kinosaal, Hotelzimmer, Sitzungszimmer werden aus Komfortgründen gekühlt. Wenn auch die Raumluftfeuchte beeinflusst wird, spricht man von Klimatisierung.
Bei Kühlung aus Komfortgründen muss typischerweise nur im Sommer Kälte bereitgestellt
werden. Meistens muss die ganze überschüssige Wärme an die Umgebung abgegeben werden.
Eine Wärmerückgewinnung ist nur möglich, falls im Sommer ein Wärmebedarf besteht. Dies ist
bspw. bei einem Hallenbad der Fall. Aufgrund der oft nur kurzen Nutzungszeit ist es zudem
schwierig, eine solche Abwärmenutzung wirtschaftlich zu rechtfertigen. In einem Fall einer
Komfortkühlung oder Klimatisierung muss meistens reine Kälte erzeugt werden.
Im Falle der Klimatisierung aus Komfortgründen fällt der Kälteleistungsbedarf (wie der
Heizleistungsbedarf) proportional zur Temperaturdifferenz innen zu aussen an und damit mit
einer ausgeprägten Spitzenleistung. Die Zahl der Vollbetriebsstunden bleibt relativ klein (um die
500 h). Um die Spitze zu brechen werden üblicherweise bei hohen Aussentemperaturen auch
höhere Innentemperaturen akzeptiert.
Bei der Kälteerzeugung kann von zwei Arten gesprochen werden: der mechanischen Kühlung und
der freien Kühlung.

---

> ◀ [[07_1_bauweise_beschattung|← Bauweise und Beschattung]] · [[_Skript_Energie_MOC|↑ MOC]] · [[07_3_freie_kuehlung|Freie Kühlung →]] ▶

---
