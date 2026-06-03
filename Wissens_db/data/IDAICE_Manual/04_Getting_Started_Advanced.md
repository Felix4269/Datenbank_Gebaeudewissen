---
tags: [IDA-ICE, Advanced, Equationsystem, Beispiel]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "Kap. 4"
titel: "Getting Started – Advanced Level"
---

# Kap. 4 – Getting Started – Advanced Level

> [[03_4_Building_Geometry|◀ Kap. 3.4]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[05_Tips_Tricks|Kap. 5 ▶]]

---

## 5. Getting started with the advanced level
> 📖 Tutorial: [[01_3a_Varianten_Erstellen|IDA ICE Tutorial – Varianten Erstellen (Standard Level als Basis)]]  ·  Kalibrierung: [[01_2d_Kalibrieren|IDA ICE Tutorial – Modell kalibrieren (Advanced Level Parameter)]]

The standard level interface covers the most common simulation tasks, but sometimes it is
useful to examine other variables than those available here or to replace a component model.
To accomplish this one turns to the advanced level interface, where the system is described in
a mathematical sense with components containing equations, variables and parameters.

Access to the advanced level is provided for both the Standard and Expert editions of IDA
ICE. However, Expert edition users can manually edit (reconnect) component diagrams at the
advanced level, while Standard edition users can only inspect, log variables and change
parameters. Some of the examples below require the Expert edition, but this will then be
mentioned in the introduction.

Work at the advanced level is best presented in terms of demonstration, so the written account
here is quite brief. Look also at the User s web page for more information on work at the
advanced level, demonstration movies etc.

In some cases the system structures at the standard and advanced levels match each other
quite well. The air handling unit, for instance, has different components: fans, coils etc. The
same description can then be used for both the standard and advanced levels. The same is true
for the primary system. However, for the actual building description entirely different
structures are used for the standard and advanced levels.

Most components at the advanced level are described with equations. Components are
interconnected by creating equalities between variables that appear on interfaces. An example
is the interconnection between the cooling and heating coils in the air handling unit. Both the
outflow interface of the heating coil and the inflow interface (terminal) of the cooling coil
contain variables for: pressure, temperature, massflow, moisture and carbon dioxide
concentrations.

To work on the advanced level, select Build model in the Simulation tab. This creates the
schematic view of the current building. If the model has been built previously, Schematic is
already available as a view of the system. Figure 5.1shows the appearance of the air handling
unit in the schematic view (which is also the standard view for the air handling system).

![[data/assets/IDAICE_Manual/fig_5_1.png]]
*Abb. 5.1 – The air handling unit*

The behavior of a component is described by equations, variables and parameters. The
difference between parameters and variables is that the former will never change their value
during a simulation, whereas a variable might. A window area is an example of a natural
parameter and the room air temperature is always a variable.

The description of most components is done using a special language called NMF (Neutral
Model Format). Click on the Code tab of any of the AHU components, to see the NMF code.
It contains the following main sections:

Abstract A brief textual description of the model
Equations The actual mathematical description (formalized according to a strict syntax
but quite readable also for humans)
Links/Interfaces A description of the ports or terminals of the component. A fan would
typically have at least two links for incoming and outgoing air flow and
could also have links for power supply and control signals.
Variables Variables to be calculated by the model.
Parameters Quantities that characterize the component, e.g. a vector of numbers
describing the fan curve.
Parameter Computer code which converts user supplied parameters into those that
processing actually appear in the equations

From version 4, some models in the ICE library are instead described by the Modelica
language (www.modelica.org) 12.

12 The IDA Modelica development environment is not yet publicly released and focus here will be on NMF. The
NMF development environment is shipped on request with the Expert edition of IDA ICE.

We will now go through a few examples of useful operations at the advanced level of ICE.
### 5.1. Example 1: Presenting more data in an existing diagram
Suppose we are interested in the air temperature after the heat exchanger in the air handling
unit and would like to see the graph together with the other temperatures of the AHU. Open
the AHU window (Figure 5.1) and double click on the connection between the heat exhanger
and the heating coil. A small window is opened showing the connection between the two
interfaces; SUPOUT (SUPply OUT) of the heat exchanger (hx) is connected to the
AIRFLOWIN interface of the heating coil (hc). To see the actual variables of the connection,
double click on the box hx.SUPOUT. TSUPOUT is the variable we are looking for. Double
click on it to get the form at the lower right of Figure 5.2.

![[data/assets/IDAICE_Manual/fig_5_2.png]]
*Abb. 5.2*

All relevant information about the variable is displayed in this window. At the bottom of the
window, there is a combo box for logging the variable to a diagram. Select AHU
temperatures in the combo box and give a meaningful name to this variable in the
corresponding field. Make a simulation, and inspect the added graph in the diagram.

5.2. Example 2: Shade control by zone temperature (Expert edition
required)
Normally, window integrated shading is controlled by the amount of radiation that penetrates
the glazing. However, in some applications it can be useful to let the zone air temperature
determine whether shades should be drawn instead. It is possible to define customized
controls for shading (and other devices) at the standard level.

We look at a simple case consisting of a single zone with a window in one wall and intend to
have an external blind shading the window depending on the zone air temperature and
governed by a thermostat. First insert an external blind. Double click on the window to open
the window form. Search in database under Integrated Window Shading and select
 External blind as Device as shown in Figure 5.3.

![[data/assets/IDAICE_Manual/fig_5_3.png]]
*Abb. 5.3*

Next we define the control system to use. Right below the previous choice in the window
form select New custom control as Control and give an appropriate name. An empty macro
form appears. Drag a thermostat from the Control palette and connect the AirTemp link on the
 Zone box to the measure link on the thermostat as shown in Figure 5.4. Click and hold to
draw the connection. Similarly, connect the out signal link of the Thermostat to the macro
output Shading signal .

![[data/assets/IDAICE_Manual/fig_5_4.png]]
*Abb. 5.4*

To achieve the right performance of the thermostat we have to give a dead band with sign; in
this case a negative sign to get out signal 1 for high measure signals and 0 for low. Finally we
insert a Constant field from the Utility palette and connect it to the setpoint link of the
thermostat. With a given setpoint value (22 C in Figure 5.5) the control system is defined.
After the simulation the effect of the shade control can be checked in the diagram Heat
balance .

![[data/assets/IDAICE_Manual/fig_5_5.png]]
*Abb. 5.5*
