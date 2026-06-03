---
tags: [IDA-ICE, Zonenmodell, HVAC, Strahlung, Hydronik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.10"
titel: "Cooling Units"
---

# Kap. 3.10 – Cooling Units

> [[03_3_5_6_fan_coil_hydronic|◀ Kap. 3.9]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_4_Building_Geometry|Kap. 3.4 ▶]]

---

### 3.10. Cooling units
> 📖 Theorie: [[07_3_freie_kuehlung|Skript Energie Kap. 7.3 – Freie Kühlung (Kühldecken mit Erdsonden)]]  ·  Theorie: [[04_2_kombinierte_anlagen|Lüftung Kap. 4.2 – Kombinierte Luft-/Wassersysteme (Kühldecken)]]

The Cooling device is used for radiative and convective units. Cooling units operate
completely analogous to waterborne radiators, with the exception of a few differences in
input, which are discussed here.

![[data/assets/IDAICE_Manual/fig_3_10.png]]
*Abb. 3.10 – A cooling panel on the ceiling surface, its standard form, and a dialog for the Device type*

Here, the height of a radiator corresponds instead to a Module width, to which K and N refer.
The total length is calculated as the given box area divided with Module width. There is a
difference in that the heat transfer coefficient between the back of the device, and the surface
behind (often the ceiling) is given directly in the main form. If an (arbitrary) negative figure is
entered, the heat transfer coefficient is calculated in the same way as for the heating device,
i.e. as if all heat transfer was done by radiation. This is a good approximation for a device that
has no insulation at all.

The dialog for alternative input has somewhat different parameters for cooling units.
Absorbed power and temperature differences between air and water may be given for two
points on the power curve. For max power, the temperature rise of the water is also given.
#### 3.10.1. Active beams
Active beams serve both as supply air terminals and as cooling devices with significant
convection. Their performance depends on the amount of supply air that is passed through but
they normally retain a heat transfer contact with room air also in the case of zero supply air
flow. The radiative coupling with the room is neglected in the present model.

Two input data options are available: Simplified and Manufacturer's. The latter means that
the performance parameters K and N are given as functions of air flow. This alternative is
mostly used when data is automatically imported from an on-line manufacturer's database.
The Simplified option is based on two user supplied performance points, at design conditions
and at zero flow (Figure 3.11). N is for this case set to 1.5.

![[data/assets/IDAICE_Manual/fig_3_11.png]]
*Abb. 3.11 – Active beam form*

In the constant flow (CAV) case, the given Design air flow is regarded to pass through the
beam whenever fans are running. For VAV, the constant Design air flow will pass through the
beam whenever there is sufficient air into the room and surplus air will feed directly to the
room without first passing the beam. If the VAV flow is insufficient to serve the beam with
the full requested Design flow, the flow through the beam will reduced accordingly.

The total Design air flow through all beams must not exceed the total for the zone. If beam air
flow is less than the requested total for the zone, the remaining part is regarded as being
supplied through conventional terminals.

When the flow to the room is increased by forcing the central fan (or similarly reduced) the
beams will still keep their requested Design flow, as far as possible.
#### 3.10.2. Heating/Cooling floor
If a floor heating/cooling object is inserted on the floor of a zone, the floor construction for
this area is divided into two parts, above and below the heated layer. Between the two, a heat
exchanger model is inserted corresponding to the piping layer. Quite often a floor heating
circuit will heat the room below almost as much as the room it belongs to.

The floor coil model assumes that the active layer can be treated as an infinitely conductive
plane in the floor slab, i.e. all 2D effects are disregarded. Heat transfer is calculated with a
logarithmic temperature difference between the fluid and this plane of constant temperature.
The user supplied total heat transfer coefficient between the fluid and the plane, includes:
1. Convection between medium and tube wall
2. Heat conduction through the tube walls
3. Fin efficiency corresponding to the distance between immersed tubes or actual fins.

The modeling approach will in steady state correspond to the Resistance method of the
standard EN 15377-1.

The floor coil circuit can have its own three-way valve and pump circuit keeping the
massflow constant (default). Emitted power is then controlled by varying the supply water
temperature. PI, P or on-off control can be selected (PI is default). A further alternative
Always on is also available, which will keep both the boiler mass flow and the coil circulation
massflow permanently at their design values. Control must then be maintained by the boiler
temperature controller.

In the case where no separate coil pump circuit is used, the four control options will instead
act by limiting the massflow through the coil, or keeping it constant at design conditions in
the Always on case.

![[data/assets/IDAICE_Manual/fig_3_12.png]]
*Abb. 3.12 – Floor heating form*

---

> [[03_3_5_6_fan_coil_hydronic|◀ Kap. 3.9]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_4_Building_Geometry|Kap. 3.4 ▶]]
