---
tags: [IDA-ICE, ESBO, Wärmeanlage, Lüftungsanlage, Anlagentechnik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.2"
titel: "The Air Handling System"
---

# Kap. 3.2 – The Air Handling System

> [[03_2_2_esbo_plant|◀ Kap. 3.1.2]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_Zone_Models_HVAC|Kap. 3.3 ▶]]

---

> 📖 Tutorial: [[01_2a_Variante0_Schritte1_7|IDA ICE Tutorial – Schritt 5: Lüftungsgerät & WRG konfigurieren]]  ·  Theorie: [[03_2_mechanische_lueftung|Lüftung Kap. 3.2 – Mechanische Lüftung (WRG, Heizregister, Filter)]]

3.2. The air handling system
In the default configuration, the air handling system consists of the following components
(Figure 3.5): supply air temperature setpoint controller (1), exhaust fan (2), heat exchanger
(3), heating coil (4), cooling coil (5), supply fan (6), schedule (7) for operation of both fans
and a schedule for the operation of the heat exchanger (8). The unit provides temperature-
controlled air at a given pressure. Some key parameters of individual components are
presented in the form; open them to edit.

The supply air temperature setpoint is connected to the heat exchanger and to both coils. All
three components have separate ideal control circuits, which independently strive to maintain
the setpoint. After the coils, the supply fan raises the supply air temperature further by either a
fixed number of degrees (default) or by depositing motor and drive losses to the air stream.

In the setpoint controller, three methods are provided for setpoint selection. In the default
AHU, the setpoint is set to constant, 16 C. The second alternative is to let the setpoint vary
with time according to a schedule. Thirdly, an option is available where the setpoint is
calculated as a (user-defined) function of outdoor air temperature. Note that if for example the
chiller (that supplies the cooling coil from the plant) has been turned off or has insufficient
capacity, the supply air will not be cooled to the setpoint.

![[data/assets/IDAICE_Manual/fig_3_5.png]]
*Abb. 3.5 – Default air handling unit*

The heating coil (4) has two important parameters: the air side temperature effectiveness and
the desired water side temperature reduction. Capacity control is achieved by adapting the
actual effectiveness up to the given maximum level. The necessary water flow is calculated
and the water temperature is reduced, if possible, by the desired number of degrees. There is
no bypass on the liquid side; control is achieved by restricting the water flow.

In the default configuration, the temperature effectiveness is set at 1.0. There are basically two
situations when it may be desirable to change this to a more realistic value: when sizing the
actual coil by means of simulation experiments, or when making energy calculations in cases
where the heat generation efficiency is dependent on temperature conditions (nearly always
for the ESBO Plant.) In addition, the simplest and quickest way of removing the entire coil is
to set the effectiveness to zero.

The cooling coil (5) works in the same way as the heating coil, but is mathematically more
complicated because air dehumidification is calculated. For wet operation the given
effectiveness is defined as (1 - bypass factor ), according to ASHRAE s nomenclature.
Physically, this means that the state of the cooled air in the psychrometric chart lies
somewhere on a straight line between the state for the incoming air and the apparatus dew
point temperature on the saturation curve. In the model, the average temperature of the liquid
side defines the apparatus dew point. On this line, the given efficiency indicates the status: 0
is no cooling whatsoever, and 1 indicates maximum cooling, which also means that the air at
most is chilled to (the arithmetic) mean value of the liquid incoming and outgoing
temperatures.

Similarly, the air-to-air heat exchanger ( 3 in Figure 3.5) is controlled by adapting the actual
effectiveness selected by the model, up to the maximum limit set by the user, so that the
setpoint for the supply air temperature is reached (if enough heat is available). The
temperature of the (often chilled) exhaust air, which may not fall below a certain level
(TEXHOUTMIN parameter), sets another limit. This is to avoid freezing. Note that for rotating
heat exchangers, it is usually possible and desirable to cool the exhaust air below freezing. A
Capacity parameter for the rated air flow may optionally be provided in the heat exchanger. If
this parameter is provided, the actual effectiveness will be adjusted to compensate for lower
air flows as well as for unbalanced flow on the supply and exhaust sides.

The heat-exchanger will utilize the return air stream both to heat and to cool the supply air.

The heat exchanger takes into consideration condensation on both the supply and exhaust
sides. During wet processes, the given efficiency is interpreted as (1 - bypass factor ), in the
same way as for the cooling coil, but the apparatus dew point for the heat exchanger is
defined as the incoming temperature for the opposite medium.

The fans have ideal pressure control with given setpoints and by default constant efficiencies,
i.e. they supply a fixed pressure head. In most cases, both these parameters only have
significance for calculating fan electricity consumption. By default, the user gives directly the
increase in air temperature by the fan (and the system). As an option, the temperature rise may
be computed automatically with a given percentage of motor and drive losses being deposited
into the air.

For modeling of CAV systems, the fan pressure rise and efficiency at the intended operating
point should be entered (pressure can also be given in terms of specific fan power, SFP). For
VAV systems, on the other hand, the performance should be adapted for flows below the
design point. ASHRAE Standard 90.1 prescribes a way to do this that has been implemented
in the fan model. This part load efficiency reduction is activated selecting something else than
<unlimited> in the drop box. A rated flow must also be provided for this option.

The fans operational schedule (7) is connected to both the supply and exhaust fans. When the
control signal is zero, the fans supply a very low pressure head (for numerical reasons, greater
than zero). The fan schedule is also connected to all the air terminals in the zones. When the
fans switch off, all terminals are closed. This is to avoid a spontaneous flow through the
system caused by the chimney effect.

The fan schedule, like other schedules, gives normally values of 0 (off) and 1 (on) as output
signals. However, it is meaningful for the fan schedule to sometimes give other values,
thereby forcing ventilation flow. For example, if a value of 1.2 is given, all terminals will
supply a 20% higher flow than that selected locally in the zone. This applies to both CAV and
VAV systems. In the same way, a value of 0.5 results in half the flow.

The local terminal connection to the central schedule has no counterpart in actual systems, but
has been introduced partly to avoid unintentional spontaneous flow in the system, and partly
to permit forcing the flow in case of CAV.

The heat exchanger is similarly controlled by a schedule (8). To turn it off, the schedule
should give the value 0. A value 1 turns on the heat exchanger. Any value between 0 and 1
will be interpreted as using a corresponding fraction of the heat exchange surface.

