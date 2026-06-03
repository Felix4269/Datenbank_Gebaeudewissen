---
tags: [IDA-ICE, Zonenmodell, HVAC, Strahlung, Hydronik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.5"
titel: "Airflows"
---

# Kap. 3.5 – Airflows

> [[03_3_1_zone_intro_solar|◀ Kap. 3.4]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_3_4_zone_heaters|Kap. 3.6 ▶]]

---

### 3.5. Airflows
> 📖 Tutorial: [[01_1_Modell_Grundsaetzliches|IDA ICE Tutorial – Kap. 4: Infiltration im Modell konfigurieren]]  ·  Theorie: [[02_1_schadstoffabfuhr_luftfuehrung|Lüftung Kap. 2.1 – Schadstoffabfuhr & Luftführung im Raum]]

This section covers the models and input which determine the airflows through the building.
IDA ICE enables the user to take account of natural ventilation, i.e. flows driven by wind
pressure and the stack (chimney) effect.

In the simplest case, each zone has three paths for airflows: through the supply and exhaust
terminals and via leakage through the envelope. When two zones are placed adjacent to each
other and there is an opening in the common wall between them or when windows are open or
when additional leaks have been added, additional flow paths are created. However, let us
start with the simplest case.

The mechanical ventilation terminals are always of VAV (Variable Air Volume) type. This
means that as long as there is sufficient pressure head from the fans, a given flow is
maintained as requested by the zone itself. In CAV (Constant Air Volume), the control signal
is kept constant and a constant flow will be maintained, irrespective of pressure. In a VAV
system, a controller regulates the flow with respect to temperature, carbon dioxide, humidity
or pressure levels in the zone.

Since, in the simplest case, flows through two of the three paths are given, the size of the third
flow, through the leak, is important only for the pressure in the zone, and not for net flows.
Note that if the size of the leak is much too small, an unrealistic pressure may build up in the
zone. Such a pressure may become so large as to affect the air psychometric calculation
routines and may then be reported as a condensation problem, when, in fact, it is a pressure
problem.

It is also possible to define additional given in/exfiltration flows, i.e. balanced flows into and
out of a zone. Since these incoming and outgoing (mass) flows are always equal, they will not

affect the pressure of a zone. The given in/exfiltration will only act to exchange heat, moisture
and CO with the ambient.

#### 3.5.1. Air flow input forms

Figure 3.7 shows the zone form. The input fields in the Ventilation section govern air flows.
Also involved are Controller setpoints. Clicking on the link field opens the dialog (see Figure
3.8).

![[data/assets/IDAICE_Manual/fig_3_7.png]]
*Abb. 3.7 – The zone form*

![[data/assets/IDAICE_Manual/fig_3_8.png]]
*Abb. 3.8 – Control setpoints*

In the zone form, the user can select System type (CAV, VAV with temperature control, VAV
with CO control or VAV with humidity control, VAV with both temperature and CO

control, and VAV with pressure control, schedule controlled VAV etc.). For CAV, the
required airflows are given directly in the zone form. Leak area gives the size of the
combined envelope leak. (In the model, the combined envelope leak area is distributed on all
external walls, 1 m above floor level. The height is only relevant for natural ventilation
situations.) Both Leak area and Given additional in/exfiltration are by default computed
automatically based on information for the whole building that is given in the Infiltration form
which is reached from the Building form.

In the combo box Controller setpoints (Figure 3.7), the user can select an object with a
collection of relevant zone-level control setpoints. The Control setpoints dialog (Figure 3.8)
provides input data for zone climate quality requirements. Here, only those parameters, which
are of importance for airflows, are discussed. For a VAV system, the given minimum value of
Mechanical exhaust airflow provides the lowest allowable airflow, with the maximum value
providing the highest one. (In Figure 3.7, an exhaust only VAV system has been specified.) In
the case of CAV, as was already pointed out, the desired flow is given directly in the zone
form. If the chosen CAV flow falls out of the quality range provided in Control setpoints, a
warning is issued when the simulation is started.

The other values in Figure 3.8 may impact on the corresponding VAV control scheme. If the
user selects CO control, (see Figure 3.7), the airflow is varied in proportion to the CO
content of the air in the zone. For the VAV with CO control scheme, a CO value, which
equals or exceeds the given max-value (in Figure 3.8), results in the maximum flow through
the exhaust terminal, with a minimum CO value producing the given minimum airflow. The

humidity control function is entirely analogous with respect to relative humidity (assuming
supply air will dry the zone).

The option VAV with temperature control functions somewhat differently. Here, the
maximum comfort temperature value is used. Forcing of the VAV flow begins somewhat
below (normally 1 C) the indicated maximum value (P control). Full exhaust flow (see
Figure 3.8) is reached at somewhat above (normally 1 C) the maximum temperature value.
The throttling range is normally 2 C, but can be selected at the building level under System
parameters.

This scheme will assume that the supply air is able to cool the zone, i.e. if there is a need for
heat and the supply air is warmer than the zone, this will not be recognized by the controller.

The option VAV, temp+CO2, on the other hand, will be smart enough to both heat and
cool with the supply air. It relies on PI controllers instead of P ditto, and will therefore not
have any offset error. In addition, it will also force air flow if needed to maintain CO level at

the maximum limit. (The minimum limit is not used.)

Pressure controlled VAV is normally used for return air flow control where some other VAV
method is used to supply air into adjacent zones. It will attempt to maintain zone pressure,
within the given range, with respect to ambient pressure using a proportional controller
(measured as pressure drop in the local ambient leak). In the example in Figure 3.8, the zone
is maintained between 10 and 20 Pa below ambient pressure.

---

> [[03_3_1_zone_intro_solar|◀ Kap. 3.4]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_3_4_zone_heaters|Kap. 3.6 ▶]]
