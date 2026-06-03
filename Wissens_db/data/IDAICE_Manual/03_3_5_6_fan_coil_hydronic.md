---
tags: [IDA-ICE, Zonenmodell, HVAC, Strahlung, Hydronik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.8–3.9"
titel: "Simple Fan Coil and Hydronic Heating Devices"
---

# Kap. 3.8–3.9 – Simple Fan Coil and Hydronic Heating Devices

> [[03_3_3_4_zone_heaters|◀ Kap. 3.7]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_7_cooling_units|Kap. 3.10 ▶]]

---

### 3.8. Simple fan coil
> 📖 Theorie: [[04_2_kombinierte_anlagen|Lüftung Kap. 4.2 – Kombinierte Luft-/Wassersysteme (Fan Coils & Kühldecken)]]  ·  Kühlung: [[07_4_5_mechanische_kuehlung_energiebedarf|Skript Energie Kap. 7.4 – Mechanische Kühlung: Leistung & Energiebedarf]]

From version 4.7, a new room unit, Simple fan coil, has been introduced. It is always
connected to the cold water circuit and, optionally, also connected to the hot water circuit.

Fan electricity use is specified as a percentage of cooling (or heating) power. This percentage
can be set to zero without affecting the operation of the device. Setting the fan electricity to
zero in a Simple fan coil is actually the computationally most economical way of heating or
cooling the room by water from the Plant.

The Simple fan coil on the advanced level is actually implemented by using Ideal heaters and
coolers in the zone and then simply removing the corresponding amount of heat from the
water stream.

### 3.9. Hydronic heating devices
Most other hydronic devices use a mathematical model that allows them to have a given
position on a zone surface. This enables the computation of correct local radiation near the
device (when the detailed zone model is used).

Heat emission from hydronic heating devices is calculated using

P = K*l*dTN,

where l is device length and dT is the temperature difference between the water and the zone
air. K and N are constants characterizing a device of a certain height (or width for ceiling
devices).

Figure 3.9 has a radiator inserted on a wall surface. Its main form has been opened and a
dialog for the Device type has been opened from the form. Often the values of K, N and
Height come from a database, which in the form can be opened under Use manufacturer's
data. The data for the Device type can also be altered and saved by the user with a new
name. The user must then only enter the surface area (given graphically) and the Design
conditions, from which the mass flow rate is calculated.

The warm radiator surface that is exposed to the zone is defined by the box that is drawn
when the unit is inserted on a wall surface. The size of this box has meaning for the heat
transfer. While the total emitted heat is always given by the expression for P, the division
between radiation and convection is calculated based on the surface temperature - which is
connected to the water temperature - and the given exposed surface. The zone sees a warm
surface and calculates the radiation and convection from this surface. The main part of the
remaining heat (needed to complete P) is emitted convectively directly to the air
(corresponding to convection behind a radiator). A small part of the heat goes to increase the
temperature on the portion of wall behind the heating device. The heat transfer coefficient
between the device surface and the wall behind is considered in the basic case to be
completely dominated by radiation and is calculated by the model.

![[data/assets/IDAICE_Manual/fig_3_9.png]]
*Abb. 3.9 – A radiator on an external wall, its standard form, and a dialog for the Device type*

To facilitate adding new heating devices without direct knowledge of K and N, a Simplified
model data input is given (see the form in Figure 3.9). The values for design mass flow and K
are calculated from the power given by the user at the specified Design conditions. The user
also provides a value for N in this case. Note that K is calculated from the information given in
the alternative input. This is thereafter the value for K. If the size of the graphical box is later
changed, the device is likely to have an unintended maximum power. Note also that the actual
maximum heating capacity of the device will vary with actual room and supply water
temperatures. The Design conditions are only used to calculate K and have no impact on the
simulated supply and return water temperatures.

---

> [[03_3_3_4_zone_heaters|◀ Kap. 3.7]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_7_cooling_units|Kap. 3.10 ▶]]
