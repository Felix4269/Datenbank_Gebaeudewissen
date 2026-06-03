---
tags: [Norm, Geothermie, Erdwärmesonde, SIA384-6, Gebäudetechnik]
normnummer: SN 546384/6:2021
gueltig_ab: "2021-05-01"
kapitel: "Kap. 3.2–3.4"
titel: "Systemoptimierung, Berechnung und Hydraulik der Erdwärmesonden"
---
> ◀ [[03_1_anforderungen_auslegung|Kap. 3.1 Anforderungen an die Auslegung]]  ·  [[_SIA_384-6_2021_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_5_nachbarsonden|Kap. 3.5 Berücksichtigung künftiger Nachbarsonden]] ▶

---

# Kap. 3.2–3.4 – Systemoptimierung, Berechnung und Hydraulik der Erdwärmesonden

---

## 3.2 Grundsätze der Systemoptimierung

### 3.2.1 Allgemein

Eine Erdwärmesonden-Anlage ist auf Lebenszykluskosten zu optimieren. Dabei ist zu beachten, dass die Nutzungsdauer der Erdwärmesonde um ein Vielfaches grösser ist als die Nutzungsdauer der Wärmepumpe und der übrigen Komponenten.

### 3.2.2 Parameter für die Wirtschaftlichkeitsrechnung

Für die Wirtschaftlichkeitsrechnung sind die Werte gemäss SIA 480 einzusetzen. In Ergänzung dazu sind die Werte in Tabelle 4 zu verwenden.

**Tabelle 4** Parameter für die Wirtschaftlichkeitsrechnung

| Komponente | Jährliche Wartungs- und Unterhaltskosten (% des Anlagewertes) | Nutzungsdauer (Jahre) |
|---|---|---|
| Erdwärmesonde und Zuleitungen | 0 | 50 |
| Wärmepumpe | 2 | 25 |
| Frostschutz | 0,5 | 25 |
| Pumpen und Armaturen | 1 | 15 |

### 3.2.3 Erneuerung der Wärmepumpe

3.2.3.1 Bei der Planung einer Erdwärmesonden-Anlage ist zu berücksichtigen, dass mehrere Wärmepumpengenerationen nacheinander an der Erdwärmesonde angeschlossen werden.

3.2.3.2 Kommende Wärmepumpengenerationen werden sehr wahrscheinlich eine höhere Effizienz aufweisen. Dies bedeutet, dass bei gleicher Heizleistung eine grössere Kälteleistung zu erbringen ist und somit die Erdwärmesonde stärker belastet sein wird. Bei der Dimensionierung des Erdwärmesondenkreises sollte daher von zukünftig besseren Leistungsziffern der Wärmepumpe ausgegangen werden. Dies kann im Rahmen der Nutzungsvereinbarung ([[02_Strategische_Planung|2.4]]) berücksichtigt werden.

3.2.3.3 Wird die Wärmepumpe ersetzt, müssen die bestehenden Erdwärmesonden auf ihre Leistungsfähigkeit überprüft werden.

### 3.2.4 Regeneration

3.2.4.1 Bei grossen Objekten mit unausgeglichener Energiebilanz (Überschuss an Heiz- oder Kühllast) verschiebt sich die Wärmeträgertemperatur entsprechend der Belastung mit der Zeit. Eine Regeneration kann diesen Effekt kompensieren.

3.2.4.2 Die Regeneration kann z. B. mit Abwärme, Wärme aus Sonnenkollektoren oder Luftwärmetauschern erfolgen.

3.2.4.3 Die Regeneration kann bei Kleinanlagen eine Überlastung der Erdwärmesonden nicht kompensieren.

---

## 3.3 Berechnung der Erdwärmesonden

### 3.3.1 Allgemein

3.3.1.1 Einer Erdwärmesonde oder einem Erdwärmesondenfeld kann nicht direkt eine Leistung zugeordnet werden. Die Momentanleistung ist abhängig vom Bohrlochwiderstand und von der Temperatur um das Bohrloch. Diese Temperatur ist eine Funktion der bereits umgesetzten Energie, der Zeit, der Wärmeleitfähigkeit und -kapazität und eventueller Grundwasserströmungen. Aufgrund dieser Komplexität werden Erdwärmesonden vorwiegend mit numerischen Modellen ausgelegt.

3.3.1.2 Für die Dimensionierung der Erdwärmesonden sind generell folgende Grundlagen notwendig:

– behördliche Vorgaben,
– Erdwärmesonden in der Nähe,
– Bedarfsprofil des Gebäudes und des daraus resultierenden Belastungsprofils,
– Entzugs- bzw. Einspeiseleistung aufgrund des gewählten Betriebskonzepts mit der gewählten Wärmepumpe und allfälligen weiteren Anlagekomponenten,
– Temperaturlimiten der Erdwärmesonden aufgrund des gewählten Systemkonzepts (siehe 2.2 und 3.1.2),
– thermophysikalische Bedingungen am Standort (siehe [[02_Strategische_Planung|2.3.2]]),
– Platzangebot (siehe [[02_Strategische_Planung|2.3.3]]).

### 3.3.2 Belastungsprofil

Das Belastungsprofil muss die Extremwerte abbilden. Durchschnittliche Belastungen sind nicht zulässig. Es sind verschiedene Ansätze für Belastungsprofile möglich:

– Effektives Lastprofil der Wärmepumpe bzw. Kühlung (nicht des Gebäudes) in Stundenwerten. Bei Wärmepumpen mit variabler Leistung (z. B. Inverter-Wärmepumpen) ist die maximale Kälteleistung, die sich im Betrieb ergeben kann, einzusetzen.
– Bei Inverter-Wärmepumpen ist die maximal eingestellte Verdampferleistung massgebend.
– Volllaststundenansatz bei einfachen Anlagen gemäss D.4.5.
– Monatsmittelwerte mit mindestens 24 Stunden Spitzenlast der Wärmepumpe bzw. Kühlung pro Jahr im Monat mit der höchsten Belastung. 49 Jahre Mittelwert und saisonale Belastungskompensation und Spitzenlast der Wärmepumpe bzw. Kühlung im letzten Betriebsjahr gemäss D.5.

### 3.3.3 Vorgehen bei einfachen Erdwärmesonden-Anlagen

3.3.3.1 Einfache Anlagen sind monovalente Anlagen zur Wärmeerzeugung (Raumheizung, Trinkwassererwärmung), d. h. ohne Zusatzheizung mit einem zweiten Wärmeerzeugungssystem, im Wohnungsbau mit maximal vier Erdwärmesonden. Dazu können vereinfachte Berechnungsverfahren für die Wärmeerzeugung angewendet werden. Bei der Berechnung wird Geocooling nicht berücksichtigt.

3.3.3.2 Bei der vereinfachten Dimensionierung wird das Bedarfsprofil mit der Norm-Heizlast des Gebäudes nach SIA 384/2 sowie dem Jahreswärmebedarf der Warmwasseranlage oder nach dem effektiven Verbrauch erstellt. Diesem Energiebedarf entsprechend wird eine geeignete Wärmepumpe mit ausreichender Leistung bestimmt und ihre Laufzeit definiert. Sperrzeiten für die elektrische Energiezufuhr müssen berücksichtigt werden. Die standortabhängige Leistung der Erdwärmesonde wird durch die Höhenlage, die lokale Bodentemperatur sowie die lokale geologische Struktur bzw. die thermischen Gesteinseigenschaften bestimmt.

3.3.3.3 Die Bodenkennwerte sind in C.3 beschrieben.

3.3.3.4 Mögliche Verfahren sind in D.4 und D.5 beschrieben. Mit den darin enthaltenen Diagrammen, unter Verwendung der oben beschriebenen Daten, können Anzahl, Abstand und Länge der Erdwärmesonden für Anlagen bis maximal vier Erdwärmesonden bestimmt werden.

### 3.3.4 Vorgehen bei komplexen Erdwärmesonden-Anlagen

3.3.4.1 Komplexe Anlagen sind alle Anlagen, die nicht als einfache Anlagen gemäss 3.3.3.1 gelten.

3.3.4.2 Bei komplexen Erdwärmesonden-Anlagen kann das vereinfachte Berechnungsverfahren nach D.4 und D.5 nicht angewendet werden.

---

## 3.4 Auslegung und Hydraulikberechnung der Erdwärmesonden-Anlage

### 3.4.1 Allgemein

In der Erdwärmesonden-Anlage zirkuliert ein Wärmeträger (siehe [[04_Baustoffe|4.5]]). Diese Flüssigkeit übernimmt den Energietransfer zwischen der Erdwärmesonde und dem Energienutzer. Der Wärmeträger hat einen Einfluss auf den Wärmeübergang zum Erdwärmesondenrohr und damit auf die Wärmeträgertemperatur bzw. die Leistung einer Erdwärmesonde.

### 3.4.2 Aufbau der Erdwärmesonden-Anlage

3.4.2.1 Damit die Erdwärmesonden-Anlage ihre Funktion langfristig erfüllen kann, muss sie aus Sicherheitsgründen und zur Erleichterung von Servicearbeiten Absperrorgane, eine separate Füll- und Spüleinrichtung, Entlüftungen, ein Überdruckventil, einen Druckwächter, ein Expansionsgefäss und eine Umwälzpumpe aufweisen.

3.4.2.2 Jede Erdwärmesonde der Erdwärmesonden-Anlage muss mit Absperrorganen am Vor- und Rücklauf unterbrochen werden können.

3.4.2.3 Jede Erdwärmesonde muss zur Vermeidung von Lufteinschlüssen separat gefüllt und gespült werden können. Verdampfer und weitere Aggregate müssen ebenfalls separat gefüllt werden können.

3.4.2.4 Die vollständige Entlüftung der Anlage und der einzelnen Erdwärmesondenkreise muss sichergestellt sein. Werden die Erdwärmesonde und deren Zuleitungen gemäss [[05_Ausfuehrung|5.5]] gespült und gefüllt, dürfen die Sondenköpfe höher liegen als der Verteiler ([[05_Ausfuehrung|5.4.2]]). Entlüftungsautomaten müssen manuell abgesperrt werden können.

3.4.2.5 Die Dichtheit des Erdwärmesondenkreises ist durch einen Druckwächter kontinuierlich zu kontrollieren. Spricht er an, schalten die Soleumwälzpumpe und die Wärmepumpe ab.

3.4.2.6 Die Ausdehnung des Wärmeträgers wird mithilfe eines Expansionsgefässes kompensiert. Das Volumen des Expansionsgefässes wird mit einem dreifachen Sicherheitszuschlag der berechneten Ausdehnung von 0 °C auf 20 °C bzw. bis zur maximal möglichen Temperatur des Wärmeträgers bemessen (siehe C.4, Tabelle 14). Es muss eine Grösse von mindestens 18 Litern haben.

3.4.2.7 Der Vordruck des Expansionsgefässes ist kleiner oder gleich dem Minimaldruck der Anlage einzustellen, üblicherweise zwischen 0,7 und 1,0 bar. Der Auslösedruck der Lecküberwachung ist kleiner als der Vordruck einzustellen.

3.4.2.8 Der Querschnitt muss genügend gross bemessen werden, damit keine Strömungsgeräusche entstehen (3.4.2.10).

3.4.2.9 Der jährliche Stromverbrauch der Umwälzpumpe in der Erdwärmesonden-Anlage sollte weniger als 8 % der Wärmepumpe betragen.

3.4.2.10 Bei den Zuleitungen ab den Erdwärmesonden bis zum Verteiler und im Verteiler sollte die Strömungsgeschwindigkeit maximal 1 m/s betragen. Der Druckverlust der Verteiler (Vor- und Rücklauf inkl. allfälliger Abgleichorgane) darf zusammen maximal 15 kPa betragen. In der Solekreisleitung ab Verteiler bis zur Wärmepumpe sollen 1,5 m/s nicht überschritten werden.

3.4.2.11 Bei speziellen Anwendungen sollte ein Frostschutzwächter zur Überwachung der minimalen Wärmeträgertemperatur oder bei Wasser als Wärmeträger ein Strömungswächter zur Kontrolle des Durchflusses eingesetzt werden.

### 3.4.3 Anschluss der Erdwärmesonde

3.4.3.1 Die Erdwärmesondenrohre werden sternförmig an einen Verteiler angeschlossen. Jeder Anschluss am Verteiler muss einzeln und dicht abgesperrt werden können. Bei den üblicherweise eingesetzten Doppel-U-Rohr-Erdwärmesonden können die beiden Kreise auch mit Y-Formstücken zu je einem Vor- und Rücklauf in einer nächstgrösseren Rohrdimension zusammengefasst werden.

3.4.3.2 Bei einer einzelnen Erdwärmesonde mit Y-Formstücken kann die Wärmepumpe direkt an die Erdwärmesonde angeschlossen werden.

3.4.3.3 Werden Erdwärmesonden in Serie zu einer Einheit zusammengeschlossen, müssen die einzelnen Kreise bis zum Verteiler geführt werden und dürfen erst dort zusammengeschlossen werden, damit ein kontrolliertes Spülen und Entlüften sichergestellt ist.

### 3.4.4 Berechnung des Druckverlusts der Erdwärmesonden-Anlage

3.4.4.1 Die Anzahl und die Tiefe der Erdwärmesonden beeinflussen das hydraulische Verhalten des Wärmeträgers im Erdwärmesondenkreis. Die Auslegung des Erdwärmesondenkreises hat einen grossen Einfluss auf die Energieeffizienz und die Investitionskosten.

3.4.4.2 Die Strömung in den Erdwärmesondenrohren sollte im Auslegepunkt (maximale Entzugs- und Einspeiseleistung in die Erdwärmesonden) turbulent sein, damit ein guter Wärmeübergang zwischen Wärmeträger und Sondenmaterial ermöglicht wird. Im Teillastbereich kann die Strömung laminar werden.

3.4.4.3 Der Druckabfall im Erdwärmesondenkreis ist mithilfe eines geeigneten Verfahrens zu berechnen. Für die Bestimmung des Druckabfalls in den Sonden stehen in D.7 Diagramme für gebräuchliche Dimensionen von Duplex-Erdwärmesonden mit Korrekturfaktoren für unterschiedliche Viskositäten zur Verfügung.

3.4.4.4 Der Volumenstrom des Erdwärmesondenkreises wird am Verteiler aufgeteilt. Die Zuleitungen zu den einzelnen Erdwärmesondenrohren sind in der Regel unterschiedlich lang. Dadurch entstehen unterschiedliche Volumenströme in den einzelnen Zuleitungen. Ein unterschiedlicher Durchfluss von bis zu –15 % pro Erdwärmesonde zum nominalen Durchfluss ist mit vernachlässigbaren Leistungseinbussen zulässig. Bei grösseren Abweichungen soll die Leistungseinbusse berücksichtigt werden.

3.4.4.5 Die Temperaturdifferenz zwischen Ein- und Austritt am Verdampfer der Wärmepumpe soll 5 K nicht überschreiten. Als Richtwert gelten 3 K bis 4 K.

3.4.4.6 Die Umwälzpumpe muss für den verwendeten Wärmeträger und die zu erwartenden Wärmeträgertemperaturen geeignet sein (Vermeidung von Kondenswasser in der Pumpenelektronik bei Taupunktunterschreitungen).

---

> ◀ [[03_1_anforderungen_auslegung|Kap. 3.1 Anforderungen an die Auslegung]]  ·  [[_SIA_384-6_2021_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_5_nachbarsonden|Kap. 3.5 Berücksichtigung künftiger Nachbarsonden]] ▶

---
