---
tags: [IDA-ICE, ESBO, Wärmeanlage, Lüftungsanlage, Anlagentechnik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.1.2"
titel: "The ESBO Plant"
---

# Kap. 3.1.2 – The ESBO Plant

> [[03_2_1_standard_plant|◀ Kap. 3.1.1]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_3_air_handling|Kap. 3.2 ▶]]

---

3.1.2. The ESBO Plant
> 📖 Grundlage: [[03_2_1_standard_plant|IDA ICE Manual Kap. 3.1.1 – Standard Plant (Boiler & Chiller)]]  ·  Theorie: [[06_3_deckung_energiebedarf|Skript Energie Kap. 6.3 – Deckung Energiebedarf (Wärmepumpe, Solar)]]

By replacing the default Standard plant with an ESBO Plant, more complex plant models may
easily be constructed.

In the General tab, many different system configurations can be described by dragging in
various components from the palette (c.f. Figure 3.2). See the ESBO documentation for more
details about available components.

![[data/assets/IDAICE_Manual/fig_3_2.png]]
*Abb. 3.2 – The ESBO Plant General view*

In the next few sections, we describe the principles for the configuration and control of the
default ESBO systems. Here, the narrative will rely on system schematic diagrams as
displayed in the Advanced level. Press Build plant model in order to generate the Advanced
level for the ESBO Plant.
##### 3.1.2.1. Purpose and ambition of the default generated systems
In economically feasible real systems many compromises must be made. The total number of
valves, pumps and connections must be reasonable and control logic must not be overly
complex. In contrast, the purpose of the Esbo default systems is to exploit all significant
energy flows based on a minimum of input data from the user even if the physical
components needed are not economically justifiable in a real system. The generated systems
are technically realistic but might, at least for smaller installations, contain too many parts to
be economically attractive for realization in real life.

Furthermore, the control systems employed are extraordinarily decentralized. In order to
avoid the combinatorial explosion of having to define a central control system for each
possible system configuration, each subsystem is maximally self-sufficient. A flow controller
for, e.g., a ground source circuit will simply check when it is possible to deliver heat (or cold)
and does this until it is not energy-wise economical to continue (when pumping costs will
exceed the benefits). Long-term control strategies, for example to try to seasonally balance a
large thermal store, is out of scope of the automatically generated default systems. Whenever
the short-term benefit of a certain flow is in place, the flow will be activated.
3.1.2.2. The default tank models
All generated systems are centered around two stratified water tanks, one for hot and one for
cold water. These two tanks are mandatory for most system combinations, also for situations

where a real system would not include a tank. Furthermore, the tanks are by default equipped
with valves that will allow each entering and exiting flow to be made at the optimal height in
the tank. This way, minimal buoyant mixing will occur. Real tanks exist that behave in a
similar fashion, using for example heat lance technology. The tank is also by default equipped
with a bypass (shunt) circuit for each client-side (discharge) connection. This way, return
water from the same circuit is used first to attain the target temperature of the required supply
flow, thus minimizing the flow through the tank.

For situations where a storage tank is not part of the concept to be investigated, the volume of
the mandatory tanks is set to be fairly small with respect to surrounding systems, but not to
zero. The tanks can in this situation be thought of as temperature switchboards that
minimize the amount of temperature mixing in the system. Tank volume would then represent
the thermal mass of the actual HVAC system.

The default height to diameter ratio (shape factor) of the tanks is set to 5, representing a fairly
tall tank with, correspondingly, only a small amount of conduction between the water layers.
In order to create a less ideal tank and ultimately approaching a completely mixed tank, the
shape factor can be set smaller, so that conduction will even out temperature differences
between layers. Another way of gradually approaching a well-mixed tank is to decrease the
number of layers.

When working at the Advanced level, it is possible to turn off the ideal heat lance feature of
the tanks and select fixed vertical positions for tank ports. Buoyant mixing will then occur if a
hot water stream enters the lower part of a tank. The IDEAL parameter in the tank controls
the heat lance feature. Discharge-side bypass flow is controlled by the SHUNT parameter. For
a full mathematical description of the tank model, c.f. the Forum post
http://forum.equa.se/question/2777/stratified-tank-model-equations/ (open forum from IDA
ICE before following the link).

##### 3.1.2.3. An example of a generated system

Figure 3.3 shows an example of how the General tab may be populated with models. Some model has been chosen for each of the possible functions. Brine to water vapor compression machines have been defined for base heating as well as for cooling. Both ground heat exchange and ambient heat exchange have been defined. Below is a relatively detailed account of the workings of the plant model for this case. It can safely be omitted on a first reading, as no references are made to it in the subsequent text.

> **Abb. 3.3 – An example of the General tab of the ESBO Plant populated with models**
> *Konfiguriertes Beispiel: Wind turbine, Solar thermal (FLAT-PLATE), Photovoltaics, Generic Fuel heater als Topup heating, Brine-to-water Wärmepumpe für Base heating und Cooling, Ambient HX, Ground HX. Verteilung: Heat 70 °C / 60 °C AHU, Cold 14 °C / 5 °C AHU.*

Figure 3.4 shows the generated system at the Advanced level of IDA ICE. We will go through
and explain each major subsystem below.

![[data/assets/IDAICE_Manual/fig_3_4.png]]
*Abb. 3.4 – The ESBO Plant of Fig. 3.3 viewed at Advanced level of IDA ICE*

Organized around the two water tanks, the top one for heat and bottom one for cold storage,
are the various circuits that draw or feed tempered water from and to the tanks. Let us start
with the client circuits to the right, starting from the top right corner with the DHW circuit.

Domestic hot water is drawn from the hot tank, by the leftmost PMT-object, which has a
mass flow signal into it that gives the required DHW mass flow. The make-up water from the
water mains is furnished by the rightmost PMT-object and a given temperature (which is
computed to be the yearly average temperature of the current climate file). Each client circuit,
including this one, feeds a temperature setpoint into the tank. In this case this is the
temperature setpoint for the DHW (55 C).

As a simplification, no separate tank-in-tank has been defined for the DHW in the default
configuration. The heat exchange between DHW and surrounding water is regarded to be
infinite and immediate.

The meter objects to the top right are used to record results about DHW production.

Next below is the AHU hot water circuit, which is connected via a pump to the air handling
unit, providing it with heated water at given pressure and temperature. Similarly as for the
DHW, a temperature setpoint (60 C in the example) informs the tank about the temperature
that is required by this client. Also in the AHU box is an on-off controller for turning off the
hot water circulation to both AHU and zones when the ambient temperature is higher than,
here, 18 degrees. Actually a 3 C deadband is applied to this switch (only visible if the
component is opened) to avoid frequent switching events.

The Zone hot water circuit is similar, but has a more elaborate arrangement for the
calculation of the temperature setpoint, allowing it to be a function of ambient temperature as
well as a of a night set back schedule.

The AHU cold water and Zone cold water circuits connected to the cold tank are found in
the lower right corner. They have in this example simple fixed setpoints, 5 C and 14 C,
respectively, throughout the year.

On the production side, in the leftmost upper corner we have the PV (photovoltaics)
production circuit. It is, by default, not connected to any other model, but simply receives
appropriately shaded sunlight from the components feeding into it and converts it to
electricity, the amount of which is recorded by the connected meter.

Similarly, the Wind turbine, just below the PV, will generate electrical power only but in
response to wind velocity. This power is currently also just measured and reported.

To the right of the PV circuit, the Solar thermal collector model is located, with a circulation
pump and a separate expansion vessel. This separate brine circuit feeds into a heat exchanger
that is located at the bottom of the hot tank. In-tank heat exchangers are also served by
idealized heat lance technology. In the default set-up, the solar collector will never prioritize
the production of high-temperature DHW, but a fixed (in the example 5 C) temperature
difference is upheld in the circuit by a PI controller connected to the pump, instead
maximizing the collected amount of heat. When there is no sun, the pump will not operate
because the temperature difference over the collector will be negative or below 5 C even at
the minimal circuit flow which is always maintained.

A separate monitoring control circuit at the bottom of the Solar thermal area keeps track of
collected heat over a longer period of time (days). This signal is used to determine how much
the heat pump should be utilized. During the winter, when there is little hope for sun, the heat
pump will always attempt to keep the tank as full as possible, to avoid using the Top heating.

Next to the right is the Top heating circuit, which is the backup for keeping the top of the
tank at the maximal required client temperature. It feeds directly into the tank water, and since
expansion vessels are included in the tanks, only a pump is required in this circuit. The
control circuit measures the top level water temperature and asks the top up heater to heat,
provided the Base heating is already fully engaged.

Next below is the Base heating circuit, where the condenser circuit of the brine to water heat
pump feeds into the tank directly. The heat pump and the condenser circuit pump are
controlled by a PI controller (baseCtrl) which attempts to keep the fill ratio of the tank at a
given setpoint (which is computed by the Solar thermal monitoring circuit.) The fill ratio is
defined as the degree at which the tank is filled with water at the highest required setpoint, i.e.
if all water is heated to the highest setpoint, the fill ratio is 1, while if the whole tank holds the
ambient temperature (20 C), the fill ratio is zero.

Furthermore, the base heating heat pumps will have a speed limitation of the condenser pump
circuit that will be active when the heat pump should prioritize hot water production, i.e. the
pump speed is limited in order to force the condensing temperature to increase.

On the evaporator side, the brine to water heat pump is connected to the Brine circuit. The
brine circuit is a more unconventional design and we will explain how it works here. The
basic idea is that all free heat and cold sources are connected in parallel to a single brine
circuit. The circuit will alternate to feed units that require heat (such as the present heat pump)
and cold, i.e. if free sources are available at the same time for both heating and cooling and
both a heating and a cooling need exists, a choice has to be made as to which one of these will
be satisfied. The idea behind the design is that this collision of interests occurs only rarely.

To illustrate the function of the brine circuit, let us look at what happens with the present base
heating evaporator brine flow. Once the base heating heat pump starts to operate, the
temperature of the return side brine will drop after the condenser. First the brine passes
through a PMT tap component, which also receives a signal to open the circuit through the
evaporator as the heat pump starts. Should it be beneficial to run the cooled water through a
heat exchanger at the top of the cool tank, this is done. After returning back through the PMT
tap, the brine is returned to the return brine manifold in the Brine box.

In the event that no free supply circuits exist or are able to operate, and the evaporator was
able to discharge to the cold tank, the flow in the brine circuit will be upheld by the pump in
the brine box, which monitors both PMT tap components for possible beneficial flows. More
commonly, one or several of the free supply circuits will instead pick up the heating need of
the heat pump evaporator. Let us look at one of these, the ambient heat exchanger.

The current Ambient HX circuit, found immediately to the left of the brine box, is in the
example a fan assisted ambient heat exchanger, that is able to both cool and heat the brine
when needed. All of the free supply circuits rely on a special pump/controller object
 FreeSupCtr that monitors the temperature difference between the supply and return brine
manifolds. When the temperature of the return manifold drops, it is a signal that heating is
required, and if the free source circuit is able to meet such a need, it will start its flow (and in
the example, the fan of the ambient hx). The circuit will, in heating mode, be operated at a
degree which keeps the contributed flow above (by default 5 C) the brine return. The
operation will be continued until it is no longer beneficial, for example because the fan power
is getting close to the useful delivered power.

All Free supply circuits operate independently of each other in trying to satisfy the current
predominant need. Any circuit which can help rise the supply side brine temperature will be
operated in a heating situation.

The free supply circuits can also be operated without any condenser or evaporator in the loop.
Suppose for example that the bottom of the hot tank has a temperature which is well below
outside air temperature. In this situation, the PMT tap component will open its circuit and the
ambient heat exchange circuit will start charging the tank directly. This type of situation is of
course much more common when it comes to cooling; the free sources will then often be able
to directly feed into the cold tank.

In the example, the Cooling brine to water chiller operates in a similar way. Any useful heat
after the condenser is directly tapped into the hot tank, a free supply circuit will pick up the
cooling need and start to operate.

There is nothing that formally prevents both the heat pump and the liquid chiller in the
example to operate in parallel, both cooling and heating the brine circuit simultaneously. In

this situation, the brine pump will initially keep the flow in the circuit going but after some
time one of the two compression cycles will win and create a net cooling (or heating) need,
which then is likely to be fulfilled by a free supply circuit.

The present example, with two brine connected vapor compression machines and multiple
free supply circuits represent the most complex type of system that can be described. In all
other situations, some of these components or connections are missing, creating a simpler
system schemata with a lower number of operation modes.

---

> [[03_2_1_standard_plant|◀ Kap. 3.1.1]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_2_3_air_handling|Kap. 3.2 ▶]]
