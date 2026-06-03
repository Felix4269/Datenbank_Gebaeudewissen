---
tags: [IDA-ICE, Modell, Primärsystem, Wärmepumpe, Kessel]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "Kap. 3.1"
titel: "Model Description – Introduction & Primary System"
---

# Kap. 3.1 – Model Description – Introduction & Primary System

> [[02_Basic_Principles|◀ Kap. 2]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_1_standard_plant|Kap. 3.2 ▶]]

---

## 3. Model description
> 📖 Tutorial: [[01_1_Modell_Grundsaetzliches|IDA ICE Tutorial – Kap. 1.1: Modell & Wärmesystem (Standard Level)]]  ·  Theorie: [[06_3_deckung_energiebedarf|Skript Energie Kap. 6.3 – Deckung Energiebedarf: Wärmepumpe & Kessel]]

This chapter treats the mathematical models of IDA ICE together with some of their input
forms. The reader is assumed to have mastered the basics of the program by first following
the getting started guides.

A building model consists of a single or several thermal zones, optional central air handling
units and a single primary system. When a new model is initiated at the standard level, a
default air handling unit and primary system are normally automatically inserted (may depend
on localization). The default systems have unlimited capacity for providing the zones with air
and water at given temperatures. By default, the supply air temperature is kept constant at
17 C; the chilled water temperature to zones is 15 C and the heated water temperature is a
function of the outdoor air temperature. For many studies nothing needs to be altered in the
HVAC systems.

The default air handling unit (AHU) can be removed, but a plant object must always be
present in a model. (However, without an AHU or any water based room units, the plant will
not use any energy.)

This description deals firstly with the primary system (plant), then follows the supply chain to
the AHU (Air Handling Unit), and finally to the zones.
3.1. The Primary system (Plant)
The primary system may be described in two separate ways, by using the Standard plant or by
replacing this by an ESBO plant model.
3.1.1. The Standard plant
In the default configuration, the primary system consists of six components (designated 1-6
respectively in Figure 3.1): chiller (1) and a schedule (2) for its operation as well as a boiler
(3), a controller (4) for hot water supply temperature and a schedule (5) for night setback
operation. Also connected to the boiler is a schedule for its operation (6). The six energy
meters in the lower right corner monitor energy consumption of various categories in the
primary system.

![[data/assets/IDAICE_Manual/fig_3_1.png]]
*Abb. 3.1 – The primary system in the default configuration*

