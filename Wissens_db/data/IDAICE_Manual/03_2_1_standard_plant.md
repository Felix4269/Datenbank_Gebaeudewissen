---
tags: [IDA-ICE, ESBO, Wärmeanlage, Lüftungsanlage, Anlagentechnik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.1.1"
titel: "Standard Plant – Boiler and Chiller"
---

# Kap. 3.1.1 – Standard Plant: Boiler and Chiller

> [[03_1_Model_Description_Intro|◀ Kap. 3.1]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_2_esbo_plant|Kap. 3.1.2 ▶]]

---

> 📖 Tutorial: [[01_2a_Variante0_Schritte1_7|IDA ICE Tutorial – Schritt 4: Wärmepumpe & Boiler konfigurieren]]  ·  Norm Geothermie: [[_SIA_384-6_2021_MOC|SIA 384/6:2021 – Erdwärmesonden (Sole-WP)]]  ·  Theorie: [[06_3_deckung_energiebedarf|Skript Energie Kap. 6.3 – Deckung Energiebedarf]]

3.1.1.1. The Boiler

The boiler converts purchased energy, e.g. gas, electricity or district heat, to warm water with
given temperature and pressure for circulation through water based heat exchangers in the
building. It also uses energy for production of domestic hot water and pumping. Boiler
efficiency is by default constant, as specified in the Defaults form. Open the component to
view key parameters.

It is also possible in the standard boiler to model water heating efficiency as a function of
boiler temperature and part load. The model and parameter definitions used are the same as
those of EnergyPlus. Currently, there is no database support for this performance data since
the IDA ESBO interface offers alternative ways of modeling more realistic equipment.

Pumping power consumption for heating water circulation can be specified in three ways: (1)
proportional to the water flow through the boiler (default), (2) as a proportion of distributed
heat, or (3) as a polynomial function of the water flow. The third option follows the
conventions of ASHRAE 90.1

The first option assumes an ideal pressure controlled pump with constant efficiency.
Alternatively, by setting the efficiency to some large number and specifying the k1 parameter,
pumping effort can be given in proportion to distributed heat. (PSetMax should still have a
somewhat realistic value.)

In the third option, the efficiency of different types of pumping solutions and control are
reflected by a user provided polynomial function. This requires the input of a design
massflow as a point of reference. Two standard curves from ASHRAE 90.1 are provided.

Pumping power for domestic hot water circulation can also be specified via k2, which
specifies pumping power as a fraction of domestic hot water heating power.

The setpoint for the hot water supply temperature comes from a special controller component
connected to the boiler. The controller provides a graph showing the setpoint as a function of
the outdoor air temperature. (Press F1 in the dialog for detailed instructions.)

3.1.1.2. The Chiller

The chiller and its circulation circuit operate in a similar way, but differ in some aspects from
the boiler. The chiller uses electrical power to produce chilled water at two different constant
temperatures (but with the same pressure). The colder water, normally 5 C, supplies the
AHU. The somewhat warmer temperature, normally 15 C, goes to the zones.

Similarly as for the boiler, EnergyPlus correlations for modeling temperature and part load
behavior may be applied. Pumping power is also specified as in the boiler.

---

> [[03_1_Model_Description_Intro|◀ Kap. 3.1]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_2_esbo_plant|Kap. 3.1.2 ▶]]
