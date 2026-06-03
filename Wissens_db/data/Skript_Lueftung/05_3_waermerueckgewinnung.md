---
tags: [Lüftung, Raumlufttechnik, Klimaanlage, Gebäudetechnik]
skript: "Lüftungstechnik"
autor: "Prof. Markus Hubbuch"
version: "2022"
kapitel: "5.3"
titel: "Wärmerückgewinnung"
---

> ◀ [[05_2_ventilatoren|← Ventilatoren]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[05_4_lufterhitzer_kuehler|Lufterhitzer/kühler →]] ▶

---

# Lüftungstechnik – Kap. 5.3: Wärmerückgewinnung

### 5.3 Wärmerückgewinnung
> 📖 Anwendung: [[02_Waermeverluste|Skript Energie Kap. 2 – Lüftungswärmeverluste]]  ·  [[05_8_9_mechanische_lueftung|Bauphysik Kap. 5.8 – Mechanische Lüftung (Komfortlüftung)]]

Zur Verhinderung grosser Energieverluste sowie aus finanziellen Gründen müssen in alle Lüftungsanlagen, welche beheizte Räume versorgen, Wärmerückgewinnungsanlagen (WRG) eingebaut werden. Eine fachgerechte WRG-Anlage muss den Wärmebedarf für die Zulufterwärmung um mindestens 75 % reduzieren. Bei Räumen mit internen oder externen Wärmegewinnen (und damit einer höheren Abluft- als Zulufttemperatur) kann die WRG-Anlage zusätzlich diese Wärme nutzen, im Idealfall wird eine Zulufterwärmung unnötig.

#### 5.3.1 Funktionsprinzip WRG

Das Funktionsprinzip der WRG in Lüftungsanlagen besteht aus der Übertragung der in der Abluft enthaltenen Wärme an die kalte Frischluft (Aussenluft), um diese vorzuwärmen. Die Abluft wird entsprechend abgekühlt. Infolge der internen Feuchtequellen enthält die Abluft im Allgemeinen auch mehr Feuchte als die Aussenluft. Um auch die Feuchte rückgewinnen zu können, gibt es dazu geeignete WRG-Anlagen (hygroskopisch beschichtete rotierende WRG-Räder, siehe unten). Diese werden auch Enthalpietauscher genannt.

Die Wärmerückgewinnung verursacht immer einen Mehrverbrauch an elektrischer Energie. Dieser rührt hauptsächlich vom erhöhten Druckverlust im Zu- und Abluftgerät her, was die erforderliche Antriebsleistung der Ventilatoren erhöht. Je nach WRG-System fallen auch Hilfsantriebe (insb. Pumpen) ins Gewicht. Daraus ergibt sich der elektrothermische Verstärkungsfaktor ETV:

```
elektrothermischer Verstärkungsfaktor (ETV) = Verhältnis Wärmegewinn zum Mehr-Stromverbrauch
```

Im Sommer kann die WRG-Anlage auch zur Vorkühlung der Aussenluft genutzt werden, solange diese wärmer als die Abluft ist. Um noch mehr Kälteenergie zu sparen, kann mit einem Abluftbefeuchter die Temperatur der Abluft noch mehr gesenkt werden, bis max. zur Feuchtkugeltemperatur. Mit der WRG kann dann die Zuluft entsprechend mehr gekühlt werden. Bedingung ist, dass keine Feuchte übertragen wird (kein Enthalpietauscher), sonst wird die Zuluft zwar kühl, aber auch sehr schwül und deswegen unangenehm. Diese Art von Kühlung wird adiabate Kühlung genannt, da die Abluft ohne Energiezu- oder -abfuhr befeuchtet wird (adiabate Zustandsänderung).

#### 5.3.2 Bauarten von WRG-Anlagen

Die Entscheidung, welcher WRG-Typ eingesetzt wird, hängt primär davon ab, ob die Zu- und Abluftgeräte beieinander liegen oder örtlich getrennt sind.

**Beieinander liegende Zu- und Abluftgeräte:**

- **Rotierende Wärmetauscher (WRG-Rad)**

  Ein rotierendes Rad wird unten von der Zuluft, oben in Gegenrichtung von der Abluft durchströmt. Das Rad besteht aus feinen Lamellen aus zickzackförmig gebogenem Metallblech, durch welche die Luft strömt. Das Metall wird dabei erwärmt (in der Abluft) resp. in der Zuluft wieder abgekühlt. Auf diese Weise wird die Wärme aus der Abluft (im Metall gespeichert) durch die Rotationsbewegung zur Zuluft übertragen (Abbildung 24).

  ![[abb24_rotierendes_wrg_rad.jpg]]
  *Abbildung 24: Rotierendes WRG-Rad*

  **Vorteile:** Höchster Wirkungsgrad aller Systeme, günstiger Preis, wenig Druckverlust und Hilfsenergie, wenig Platzbedarf (kurze Baulänge) im Lüftungsgerät.

  **Nachteile:** Zu- und Abluftgerät müssen aufeinander liegen (ev. längere Kanäle, Platz in der Zentrale), mit der Rotation wird auch mehr oder weniger Abluft an die Zuluft übertragen. Wegen der Vorteile ist dieses System das am meisten angewendete.

- **Enthalpietauscher (rotierende WRG mit Wärme- und Feuchterückgewinnung)**

  Dabei handelt es sich um ein Rad, bei welchem die Oberflächen hygroskopisch, das heisst feuchtespeichernd, beschichtet sind (Abbildung 25). Damit wird auch eine Feuchteübertragung an die Zuluft möglich. Der Feuchtrückgewinngrad liegt dabei tiefer als der Wärmerückgewinngrad und ist abhängig von den herrschenden Bedingungen.

  ![[abb25_enthalpietauscher_einbaufertig.jpg]]
  *Abbildung 25: Enthalpietauscher einbaufertig*

  **Vorteile:** Dank Feuchterückgewinn noch mehr Energierückgewinn, ev. Verzicht auf einen Befeuchter.

  **Nachteile:** Zur Abluftübertragung kommt die Gefahr einer Geruchs- und Keimübertragung. Eine adiabate Zuluftkühlung im Sommer ist unmöglich.

- **Plattenwärmetauscher**

  Die Zu- und Abluft werden über Plattenwärmetauscher geführt. Durch die dünnen Platten wird die Wärme übertragen (Abbildung 26). Eine Vermischung von Zu- und Abluft kann nicht erfolgen, ausser der Wärmetauscher sei undicht. Die Plattenwärmetauscher werden im Gegenstromprinzip konstruiert, das heisst die Zu- und Abluft strömen in unterschiedlicher Richtung. Solche Wärmetauscher können je nach Tauscherfläche hohe Wirkungsgrade erreichen. Plattenwärmetauscher werden häufig angewendet, insbesondere wenn keine Abluft in die Zuluft überströmen darf.

  ![[abb26_plattenwarmetauscher_kreuzstrom.jpg]]
  *Abbildung 26: Plattenwärmetauscher (Kreuzstrom)*

  Infolge der Einfachheit werden Plattentauscher auch für kleine Anlagen (Wohnungslüftung) angewendet (Abbildung 27). Eine Feuchterückgewinnung ist oft nicht möglich. Heute gibt es Plattenwärmetauscher für Wohnungslüftungsgeräte mit hygroskopischen durchlässigen Platten, die auch einen Feuchteaustausch ermöglichen.

  ![[abb27_wohnungslef.jpg]]
  *Abbildung 27: Wohnungslüftungsgerät mit Plattenwärmetauscher*

  Für Fälle mit aggressiver Abluft werden solche Wärmetauscher auch aus Glas, in Röhrenbauform, gebaut (z. B. für Hallenbäder).

- **Heat-pipe Wärmetauscher**

  In seltenen Fällen können Heat-pipes dazu genutzt werden, Wärme zu übertragen. Eine Heat-pipe (Wärmerohr) transportiert Wärme, indem an der warmen Seite ein Kältemittel verdampft, dampfförmig zur anderen Seite strömt (infolge des tieferen Dampfdruckes) und auf der kalten Seite kondensiert und so die Verdampfungswärme wieder freigibt. Im Innern des Rohres strömt das flüssige Kältemittel durch Schwerkraft oder Kapillareffekte wieder zurück, ähnlich wie Wachs durch einen Docht zur Flamme transportiert wird.

**Getrennt montierte Zu- und Abluftgeräte:**

Um Kanäle zu sparen oder aus Platzgründen müssen Lüftungsgeräte für Zu- und Abluft oft getrennt montiert werden. Dann kommen zwei Arten der Wärmerückgewinnung in Frage:

- **Verbund-WRG (mit Wasser-Glykol-Kreislauf)**

  Diese Art der Wärmerückgewinnung (Abbildung 28) besteht aus einem Abluftkühler, welcher der Abluft die nutzbare Überschusswärme entzieht, und einem Zuluft-Heizregister, welches mit dieser Wärme die Zuluft vorwärmt. Die Wärme wird vom Abluft- zum Zuluftgerät mit einem Leitungssystem transportiert (mit einer Umwälzpumpe). Im Kreislauf fliesst aus Frostschutzgründen eine Sole (ein Wasser-Glykolgemisch mit etwa 25 % Glykolanteil).

  ![[abb28_kompakte_verbund_wrg_mit_hydraulik_kompone.jpg]]
  *Abbildung 28: Kompakte Verbund-WRG mit Hydraulik-Komponenten*

  **Vorteile:** Die Abwärme kann über fast beliebige Strecken transportiert werden, die Platzierung der Zu- und Abluftgeräte kann optimiert werden. Eine Kontamination der Zuluft durch Abluft ist ausgeschlossen. Deshalb kann auch belastete Abluft genutzt werden (z. B. Küchen und WC-Abluft). Die Verbund-WRG eignet sich gut für adiabate Zuluftkühlung. Sie kann auch in bestehende Anlagen eingebaut werden (Nachrüstung).

  **Nachteile:** Es ist ein teures Sole-Netz erforderlich. Die Umwälzpumpe benötigt Strom. Der Luftwiderstand der WRG-Register in Zu- und Abluft ist bei hohem Wirkungsgrad hoch. Die Wirkungsgrade erreichen nicht ganz die Werte einer rotierenden WRG. Es kann keine Feuchtigkeit zurückgewonnen werden, die Enthalpie der feuchten Abluft kann aber teilweise durch Kondensation am Abluft-Wärmetauscher zurückgewonnen werden.

- **Abwärme-Wärmepumpe**

  Eine spezielle Art der Wärmerückgewinnung ist die Abwärmenutzung. Die in der Abluft enthaltene Wärme wird mit einer Wärmepumpe (Luft-Wasser-Wärmepumpe) genutzt. Die Wärme kann auf ein für Heizung oder Warmwasser nutzbares Temperaturniveau gehoben werden und dann in den Heizkreis eingespeist oder für Warmwasser genutzt werden. Es kann in der Übergangszeit mehr Wärme aus der Abluft gewonnen werden als mit einer Verbund-WRG, die Abluft kann sogar unter Aussenlufttemperatur abgekühlt werden. Eine Abkühlung unter ca. 2 °C ist aber nicht möglich, da sonst die Oberflächentemperatur zu tief wird und der Abluftwärmetauscher infolge der Abluft-Feuchtigkeit einfrieren würde. Diese Art der WRG stellt insbesondere für die kontrollierte Wohnungslüftung eine interessante Lösung dar. Die Zuluft kann direkt von aussen hinter den Heizkörpern einströmen, so dass das Zuluftsystem (Gerät und Kanäle) eingespart werden kann.

---

> ◀ [[05_2_ventilatoren|← Ventilatoren]] · [[_Skript_Lueftung_MOC|↑ MOC]] · [[05_4_lufterhitzer_kuehler|Lufterhitzer/kühler →]] ▶

---
