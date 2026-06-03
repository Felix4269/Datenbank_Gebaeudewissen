---
tags: [Lueftung, Lueftungstechnik, Raumlufttechnik, Klimaanlage]
skript: "Lueftung"
autor: "Prof. Markus Hubbuch"
version: "2025"
kapitel: "3.2"
titel: "Mechanische Lüftung"
---

> ◀ [[03_1_freie_lueftung|← Freie Lüftung]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[04_1_nur_luft_anlagen|Nur-Luft-Anlagen →]] ▶

---

# Lüftungstechnik – Kapitel 3.2: Mechanische Lüftung

### 3.2 Mechanische Lüftung
> 📖 Vertiefung: [[05_3_waermerueckgewinnung|Lüftung Kap. 5.3 – Wärmerückgewinnung (WRG)]]  ·  [[02_Waermeverluste|Skript Energie Kap. 2 – Lüftungswärmeverluste]]  ·  [[01_2a_Variante0_Schritte1_7|IDA ICE Tutorial – Lüftungsgerät & WRG im Modell]]

Für die Einteilung der mechanischen Lüftungsanlagen siehe Tabelle 1. Zusätzlich sind noch folgende Anlagentypen gebräuchlich:

- Umluftanlagen
- Spezialanlagen wie Reinraumanlagen

#### 3.2.1 Einfache Abluftanlagen

Dies sind die häufigsten Lüftungsanlagen, insbesondere im Wohnungsbau. Der Zweck besteht üblicherweise im Absaugen von Schadstoffen und Gerüchen aus Küchen, WCs oder Kehrichtcontainerräumen (Abbildung 7).

![[abb7_bad_abluftventilator_fer_unterputzeinbau.jpg]]
*Abbildung 7: Bad-Abluftventilator für Unterputzeinbau*

Teilweise werden einfache Abluftanlagen auch zum Abtransport von Wärme eingesetzt (z. B. bei Traforäumen). Jede Abluftanlage hat einen entsprechenden Bedarf an Nachströmluft von aussen.

Eine einfache Abluftanlage besteht mindestens aus einem Ventilator und einem Schalter (ein- oder mehrstufig) (z. B. Fenster- oder Wandventilator). Meistens sind noch Kanäle erforderlich sowie Abluftgitter oder -ventile, über welche die Luft aus dem Raum gesogen wird. Da die Abluft verunreinigt ist, muss sie üblicherweise über Dach ausgeblasen werden (z. B. Küchen- und WC-Abluft, ausser bei EFH). Dort ist ein Abluft-Regenhut erforderlich. In Ausnahmefällen kann unverschmutzte Abluft über die Fassade ausgeblasen werden, dann ist ein Wetterschutzgitter nötig.

Im Geschosswohnungsbau muss bei Abluftanlagen in einen gemeinsamen Kanal von Nassräumen oder Küchen der Gefahr einer Geruchs- und Schallübertragung zwischen den Wohnungen besondere Beachtung geschenkt werden (Telefonie-Schallübertragung). Auch eine Brandübertragung zwischen den Wohnungen muss verhindert werden. Dabei kann pro Absaugstelle ein separater Ventilator vorhanden sein, oder ein gemeinsamer Ventilator und ein einstellbares Absaugventil pro Absaugstelle. In diesem Fall sollte der gemeinsame Ventilator drehzahlgeregelt sein, um bedarfsabhängig geregelt zu werden.

Im gehobenen Wohnungsbau wird für jede Wohnung ein eigener Kanal in einem Schacht bis über Dach geführt. Der Ventilator ist bei der Absaugstelle platziert und drückt die Abluft durch den Kanal ins Freie.

Bei Abluftkanälen aus Küchen sind Brandschutzvorschriften zu beachten, da das Fett im Kanal Feuer fangen könnte.

**Probleme:**
Problematisch bei Abluftanlagen ist die Tatsache, dass keine Wärmerückgewinnung möglich ist und dass die Ersatzluft von irgendwoher nachströmen muss. Damit verbunden sind Wärmeverluste und die Gefahr von Zugluft. Bei neuen, dicht gebauten Gebäuden kann die Luft nicht über Ritzen nachströmen. Es braucht deswegen ein Konzept für die nachströmende Luft mit dem entsprechenden Bezug zu kontrollierten Öffnungen und zur Luftdurchlässigkeit von Innenwänden, Türen und Gebäudehüllen (Abbildung 8).

![[abb8_bad_und_kechen_abluftventilatoren_mit_luft.jpg]]
*Abbildung 8: Bad und Küchen-Abluftventilatoren mit Luftnachströmung über Nachströmöffnungen*

**Steuerung:**
Alle Abluftanlagen (ausser bei Küchenabluft im Wohnbau) müssen mit einer automatischen, bedarfsabhängigen Steuerung versehen sein, um die Anlage nur bei Bedarf in Betrieb zu halten und so unnötige Wärmeverluste zu vermeiden. Als Steuerungen kommen mit dem Licht gekoppelte Nachlauf-Timer, Thermostaten, Hygrostaten (bei Feuchte), Bewegungsmelder oder ev. Zeitschaltuhren in Frage.

**Abwärmenutzung (AWN):**
Insbesondere bei grossen Abluftanlagen (z. B. bei vielen Nasszellen, immer ab 2500 m³/h) wird der Einbau einer Abluftanlage mit Abwärmenutzung (AWN) mittels einer Wärmepumpe gefordert. Die Abwärme kann so auf ein höheres Temperaturniveau gebracht und für Heizung oder Warmwasser genutzt werden. AWN-Anlagen gibt es bereits ab 150 m³/h, z. B. für Einfamilienhäuser.

**Fettfilter:**
Abluftanlagen für Haushaltsküchen müssen, wie alle Küchenlüftungen, einen Fettfilter aufweisen (Abbildung 9). Dieser braucht eine regelmässige Wartung. Die Verschmutzung der Abluftkanäle mit Fett kann hygienische Probleme verursachen und stellt eine Brandgefahr dar. Für Küchenabluftanlagen gelten deshalb spezielle Brandschutzvorschriften. Küchenabluftkanäle sollten regelmässig gereinigt werden, entsprechende Reinigungsöffnungen sind erforderlich.

![[abb9_fettfilter.jpg]]
*Abbildung 9: Fettfilter*

#### 3.2.2 Einfache Zuluftanlagen

In Räumen mit grossem Luftbedarf (z. B. Heizräume oder Farbspritzräume) kann eine Zuluftanlage eingebaut werden, welche dem Raum die erforderliche Aussenluft zuführt. Meist ist ein Filter erforderlich, welcher den Eintrag von Staub (aus der Aussenluft) verhindert und die Zuluftkanäle sauber hält. Eventuell ist auch ein Zuluft-Heizregister oder ein Schalldämpfer (gegen aussen) erforderlich, dann handelt es sich um eine einfache Zuluftanlage mit Lufterwärmung.

Reine Zuluftanlagen ermöglichen weder eine Wärmerückgewinnung noch eine Abwärmenutzung. Deswegen sind sie nur sinnvoll, wo in einem Raum ein grosser Luftbedarf herrscht, welcher mit der Zuluftanlage gedeckt wird. Andernfalls würde zu reinen Zuluftanlagen ein Konzept für die abströmende Luft mit dem entsprechenden Bezug zu kontrollierten Öffnungen und zur Luftdurchlässigkeit von Innenwänden, Türen und Gebäudehüllen gehören.

#### 3.2.3 Lüftungsanlagen

Übliche mechanische Lüftungsanlagen mit Zu- und Abluft enthalten Kanäle, ein Zu- und ein Abluftgerät und eine Steuerung. Zu- und Abluftgeräte werden, infolge der Bauart, oft auch Monoblock genannt.

Eine solche Lüftungsanlage ist nach Abbildung 10 aufgebaut. Die normierte Bezeichnung der Luftströme ist dort angegeben.

![[abb10_schema_lueftungsanlage_sia382.png]]
*Abbildung 10: Schema Lüftungsanlage mit Bezeichnung der Luftströme nach SIA 382/1 (2014)*

#### 3.2.4 Bestandteile einer Lüftungsanlage

Eine Lüftungsanlage kann aus den folgenden Bestandteilen bestehen.

**Zuluftanlage:**
- Die Aussenluft wird über ein Wetterschutzgitter in einer Aussenwand angesaugt.
- Ein isolierter Aussenluftkanal leitet die Aussenluft zum Zuluftgerät.
- Im Zuluftgerät dient eine Aussenluftklappe zum Schliessen bei Anlagenstillstand.
- In der Mischkammer wird der Aussenluft unter Umständen Umluft (aus der Abluft) beigemischt.
- Ein Filter dient zum Reinigen der Aussenluft (und ev. Umluft).
- Heute ist vorschriftsgemäss eine Wärmerückgewinnung erforderlich.
- Ein Heizregister dient zur restlichen Erwärmung der Aussenluft.
- Der Frostschutzthermostat schützt das Heizregister vor Frostschäden, falls die Wärmezufuhr ins Heizregister nicht funktioniert.
- Der Zuluftventilator fördert die Luft durch Gerät und Kanäle.
- Ein oder zwei Schalldämpfer verhindern die Ausbreitung des Ventilatorgeräusches.
- Die Zuluftkanäle verteilen die Zuluft zu den Räumen.
- Vor jedem Raum oder Auslass sollte eine Regelklappe für den hydraulischen Abgleich vorhanden sein, oder ein Volumenstromregler, um die Luftmengen bedarfsabhängig regeln zu können.
- Zuluftauslässe blasen die Zuluft in den Raum.

**Abluftanlage:**
- Über Abluftgitter wird die Abluft aus dem Raum angesaugt.
- Abluftkanäle fördern die Abluft zum Abluftgerät.
- Ev. ist eine zusätzliche Abluftanlage, z. B. für Toiletten, vorhanden.
- Je nach Umständen wird ein Teil der Abluft als Umluft der Aussenluft beigemischt.
- Ein Abluftfilter verhindert die Verschmutzung der Wärmerückgewinnung.
- Der Abluftventilator fördert die Abluft durch Kanäle und Gerät.
- Ein oder zwei Schalldämpfer verhindern die Ausbreitung des Ventilatorgeräusches.
- Die Wärmerückgewinnung entzieht der Abluft die nutzbare Wärme.
- Fortluftklappen schliessen gegen aussen bei Anlagenstillstand.
- Der Fortluftkanal leitet die Fortluft Richtung aussen.
- Über ein Fortluft-Wetterschutzgitter oder über einen Regenhut wird die Fortluft ins Freie geblasen.

Ein Beispiel einer einfachen Lüftungsanlage ist in Abbildung 11 abgebildet.

![[abb11_wohnungs_leftungsanlage_mit_bestandteilen6.jpg]]
*Abbildung 11: Wohnungs-Lüftungsanlage mit Bestandteilen*

Das Schema einer Büro-Lüftungsanlage mit zusätzlich einem Kühlregister und Nachfilter zeigt Abbildung 12.

![[abb12.jpg]]
*Abbildung 12: Schema Büro-Lüftungsanlage*

#### 3.2.5 Lüftungsanlagen für unbeheizte Räume

Bei Lüftungsanlagen, welche unbeheizte Räume versorgen, können die Wärmerückgewinnung, das Zuluft-Heizregister und der Abluftfilter weggelassen werden. Eventuell, z. B. für Garagenlüftungen, sind auch keine Luftklappen erforderlich.

#### 3.2.6 Schalldämmmassnahmen

Falls sich der Aussenluftansaug und/oder der Fortluftausblas in der Nähe von lärmsensiblen Orten befinden, sind zusätzliche Schalldämpfer nach aussen erforderlich. Es sind die Bestimmungen der Lärmschutzverordnung zu beachten. Diese legt die zulässigen Schallemissionen von gebäudetechnischen Anlagen nach aussen fest. Die Anforderungen hängen von der Zone (Wohnzone, Industriezone etc.), der Lärmart (Impulsgehalt, Gleichmässigkeit) und der Betriebszeit (Dauer, Tag oder Nacht) ab. Am Immissionsort (z. B. nächstgelegenes Schlafzimmerfenster) darf der dort messbare Schallpegel die Werte der Lärmschutzverordnung nicht überschreiten.

Gegen innen sind fast immer Schalldämpfer erforderlich. Damit wird verhindert, dass das Ventilatorengeräusch in den Räumen störend wirkt. Es gelten die Anforderungen nach SIA 181 (2020). Nur für Raumlüftungen ohne Schallanforderungen (Lager, Technikräume, Garagen) können die raumseitigen Schalldämpfer weggelassen werden.

#### 3.2.7 Zu- und Abluftanlagen (einfache Lüftungsanlagen)

Sobald die erforderliche Abluft in einem zu belüftenden Raum nicht frei von aussen oder von einem anderen Raum nachströmen kann, ist auch eine mechanische Zuluft erforderlich. Falls Räume nur belüftet werden müssen, das heisst wo die Raumtemperatur keine Rolle spielt, kann eine solche Lüftungsanlage aus Zuluftventilator, Kanälen und Abluftventilator bestehen. Wie immer ist eine Steuerung erforderlich, welche im Minimum das Ein- und Ausschalten der Anlage gestattet. Meistens ist es aber auch bei solchen Anlagen sinnvoll, eine bedarfsabhängige Steuerung einzubauen, um einen unnötigen Ventilatorbetrieb und damit Energiebedarf zu vermeiden. Je nach Umständen und Anforderungen sind zudem Zuluftfilter und Schalldämpfer erforderlich. Solche Anlagen werden z. B. für Einstellhallen, Technikräume oder Lager gebaut.

Bei Lüftungsanlagen für Lager und Technikräume kann ev. eine Wärmerückgewinnung sinnvoll sein, wenn die Lagerräume in Kellergeschossen oder stark speicherfähigen Räumen angeordnet sind oder wenn interne Abwärme anfällt. Im Winter kann so eine gewisse Vorwärmung der Aussenluft erreicht werden und die Raumtemperatur sinkt weniger stark ab. Damit reduzieren sich auch Probleme mit zu hoher relativer Luftfeuchte innen.

#### 3.2.8 Lüftungsanlagen mit Lufterwärmung

Sobald eine Lüftungsanlage für Räume gebaut wird, in welchen sich Personen während längerer Zeit aufhalten, muss für den Winterfall eine Zulufterwärmung eingebaut werden. Gemäss Bauvorschriften ist dann auch eine Wärmerückgewinnung erforderlich, welche mind. 75 % der Wärme für die Zulufterwärmung spart. Zum Schutz der dadurch im Zu- und Abluftgerät erforderlichen Wärmetauscher sind in beiden Lüftungsgeräten Feinstaubfilter erforderlich.

Die Steuerung einer solchen Anlage ist schon anspruchsvoller, da die Zulufttemperatur und die Wärmerückgewinnung selbsttätig geregelt werden müssen. Solche Anlagen sollten zudem im Minimum eine automatische Ein- und Ausschaltung nach Bedarf haben. Eine weitergehende, bedarfsabhängige Regulierung der Luftmenge und Zulufttemperatur kann hier noch wesentlich mehr einem energiesparenden und wirtschaftlichen Betrieb dienen.

#### 3.2.9 Lüftungsanlagen mit Lufterwärmung und -befeuchtung

Falls Räume belüftet werden, welche dem Aufenthalt von Personen dienen, soll eine genügende Innenraumfeuchte gewährleistet werden. Da die absolute Feuchte der Aussenluft bei tiefen Aussentemperaturen nur klein ist, wird bei solchen Verhältnissen die relative Feuchte der Innenluft im Winter oft tief. Bei mechanischen Lüftungen mit grossem Luftwechsel (alte Anlagen) kann die interne Feuchteproduktion der Personen und weiterer Quellen (Pflanzen etc.) die Raumluftfeuchte nicht auf die nach SIA und DIN mindestens erforderlichen 30 % rel. Feuchte bringen. In solchen Fällen sind ohne Befeuchtung der Zuluft bei kaltem Wetter eine zu tiefe Luftfeuchtigkeit und Reklamationen zu befürchten.

Das Problem wird entschärft, wenn nur kleine Aussenluft-wechsel gefahren werden. Deshalb wird empfohlen, bei tiefer Aussentemperatur die Zuluftmenge zu reduzieren (auf max. 25 m³/h und Person). Zudem sollten im Innenausbau Feuchte speichernde Materialien verwendet werden (z. B. Gips, Lehmputz). Mit einer Wärme- und Feuchterückgewinnung (siehe Kap. 5.3, Enthalpietauscher) kann so bei Bürolüftungen auf eine Befeuchtung verzichtet werden. Im Wohnungsbau mit relativ hohen internen Feuchtelasten (Kochen, Duschen) und bei kleinen Luftwechseln kann bei mechanischer Lüftung auf eine Befeuchtung verzichtet werden, auch hier ist eine Feuchterückgewinnung anzustreben.

Eine zusätzliche Zuluftbefeuchtung ist mit erheblichen Investitions- und Betriebskosten verbunden. Es wird ein Befeuchter nötig, welcher aus hygienischen Gründen gut unterhalten werden muss. Der Mehrbedarf an Wärme ist bedeutend, da das zuzuführende Wasser verdampft werden muss. Das Zusatzwasser muss bei allen heute üblichen Befeuchtern als entsalztes Wasser (mittels einer Osmoseanlage) zur Verfügung stehen. Die Zuluftbefeuchtung mit Dampfbefeuchtern, welche den Wasserdampf elektrisch erzeugen, ist aus energetischen Gründen (Verbrauch hochwertiger elektrischer Energie) oft verboten. Diese Lösung ist höchstens dort vertretbar, wo sehr hohe hygienische Anforderungen bestehen.

#### 3.2.10 Einfache Klimaanlagen

Für erhöhte Ansprüche an ein komfortables Innenklima genügt es in der Regel, eine Lüftungsanlage mit Kühlung zu erstellen. Eine solche Anlage wird auch als **Teilklimaanlage** bezeichnet. Falls die Kühlung zu einem Energieverbrauch über festgelegten Grenzen führt, ist diese in den meisten Kantonen bewilligungspflichtig. In diesen Fällen muss ein Bedarfsnachweis geführt werden.

Für die Luftkühlung ist ein Luftkühler (Kühlregister) erforderlich, welcher von kaltem Wasser (Vorlauftemperatur zwischen 6 und 12 °C) durchflossen wird. Je nach Wassertemperatur kondensiert mehr oder weniger Wasser am Luftkühler. Damit findet in jedem Fall eine Teilentfeuchtung statt, je nach Wassertemperatur mehr oder weniger.

Das kalte Wasser wird meist mittels einer Kompressions-Kältemaschine gekühlt. Als Antriebsenergie dient elektrischer Strom. Alternativ könnte auch eine Absorptions-Kältemaschine verwendet werden. Für diese dient Wärme (ab 70 °C) als Antriebsenergie, z. B. aus einem Blockheizkraftwerk, Prozessabwärme, Fernwärme im Sommer oder auch Solarenergie.

Ideal ist es, falls kaltes Grundwasser oder aus der Tiefe gefördertes Seewasser zur Kälteerzeugung genutzt werden kann. Auf eine Kältemaschine kann dann verzichtet werden.

Die für Luftkühlung erforderliche Kälteenergie ist stark von der gewünschten Zulufttemperatur abhängig. In der Schweiz (und Mitteleuropa generell) steigt die Temperatur nur während relativ wenigen Stunden pro Jahr über 20 °C. Es ist deshalb wesentlich, ob die Zuluft auf 16 °C oder auf 22 °C gekühlt werden muss. 
Dies veranschaulicht die untenstehende Abbildung 13.
![[abb13_relativer_kaeltebedarf_zuluft.png]]
*Abbildung 13: Relativer Kältebedarf für Zuluftkühlung*

> **Ablesebeispiel:** Wenn die Aussenluft ganzjährig nur auf 20 °C (= Referenzfall, rel. Kältebedarf = 1) statt auf 16 °C gekühlt werden muss, so ist 2,8-mal weniger Kälteenergie erforderlich.

Aus der Abbildung 13 ist ersichtlich, dass eine tiefe Zulufttemperatur einen wesentlichen Mehrbedarf an Kälteenergie erfordert. Eine Kühlung der Zuluft auf 22 °C benötigt hingegen nur wenig Energie, da die Aussentemperatur meistens bereits tiefer liegt.

#### 3.2.11 Klimaanlagen mit Luftbe- und -entfeuchtung

Unter einer **Klimaanlage mit Luftbe- und -entfeuchtung** wird eine Lüftungsanlage verstanden, welche eine Kontrolle der Raumlufttemperatur und der Raumluftfeuchte im Sommer und im Winter auf definierte Zustände zulässt. Dazu sind eine Lufterwärmung, ein Luftkühler (welcher auch der kontrollierten Entfeuchtung dient), ein Nachwärmer und ein Befeuchter erforderlich. Eine solche Klimaanlage umfasst also die folgenden vier thermodynamischen Luftbehandlungsfunktionen:

- Erwärmung
- Befeuchtung
- Kühlung
- Entfeuchtung

Im Unterschied zur einfachen Klimaanlage, wo die Entfeuchtung nur auf Werte erfolgt, welche sich infolge der Kühlung auf die gewünschte Zulufttemperatur mit einem Luftkühler ergeben (Kondensation an der kalten Kühleroberfläche), wird bei der Klimaanlage mit Luftentfeuchtung die Zuluft auf den erforderlichen Feuchtegehalt entfeuchtet. Dies macht üblicherweise eine Unterkühlung der Zuluft erforderlich, damit genügend Feuchte auskondensiert. Anschliessend wird eine Nachwärmung auf die gewünschte Zulufttemperatur erforderlich. Dieser Prozess ist energieaufwändig.

Eine Befeuchtung im Winter (Klimaanlage mit Luftbefeuchtung) kann notwendig sein, wenn keine Feuchterückgewinnung möglich ist und die Räume dem dauernden Aufenthalt von Personen dienen, bei Labors, oder bei Räumen mit empfindlichen Gegenständen.

Klimaanlagen mit Luftbe- und -entfeuchtung sind nur für Räume mit sehr hohen Anforderungen an das Innenklima erforderlich. In High-Tech-Fabriken, Labors oder Spitälern (Operationssäle) und in Arbeitsräumen für besondere Tätigkeiten kann es notwendig sein, die Temperatur und die Feuchte genau zu kontrollieren.

Der Betrieb einer solchen Klimaanlage führt zu hohen Betriebs- und Energiekosten. Deshalb sollten solche Anlagen nur dort vorgesehen werden, wo der Bedarf wirklich ausgewiesen ist. Bei Klimaanlagen ohne Entfeuchtung können im Sommerhalbjahr Zustände auftreten, welche als schwül empfunden werden. Für Büros, Sitzungszimmer und Schulräume kann mit einer einfachen Klimaanlage mit Kühlung (und damit einer Teilentfeuchtung) aber bereits ein sehr gutes Raumklima erreicht werden. Für Komfortanlagen ist eine Klimaanlage mit Luftentfeuchtung im Allgemeinen nicht erforderlich.

---

> ◀ [[03_1_freie_lueftung|← Freie Lüftung]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[04_1_nur_luft_anlagen|Nur-Luft-Anlagen →]] ▶

---
