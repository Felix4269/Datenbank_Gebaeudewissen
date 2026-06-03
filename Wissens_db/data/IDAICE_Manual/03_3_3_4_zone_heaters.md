---
tags: [IDA-ICE, Zonenmodell, HVAC, Strahlung, Hydronik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.6–3.7"
titel: "Zone Cooling/Heating Units and Ideal Heaters"
---

# Kap. 3.6–3.7 – Zone Cooling/Heating Units and Ideal Heaters

> [[03_3_2_airflows|◀ Kap. 3.5]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_5_6_fan_coil_hydronic|Kap. 3.8 ▶]]

---

### 3.6. General information regarding zone cooling and heating room units
> 📖 Tutorial: [[01_1_Modell_Grundsaetzliches|IDA ICE Tutorial – Lokale Heiz/Kühlelemente im Zonenmodell konfigurieren]]  ·  Theorie: [[03_3_5_6_fan_coil_hydronic|IDA ICE Manual Kap. 3.8–3.9 – Fan Coils & Hydronic Radiators]]

Local heating or cooling is supplied to the zone by room units. All room units are listed in the
zone form. Some units such as ideal heaters and coolers, do not have a given location in the
room. These can be introduced directly into the list in the zone form. Most hydronic units
may, on the other hand, be located on a specific zone surface and they are instead inserted by
dragging them onto a surface. From version 4.5, most hydronic units can also exist without a
specific position in the zone, i.e they can be dragged directly into the zone form. Note,
however, that all radiative units still require an explicit surface area. (Given on the Properties
page, when the input form of the unit is active.)

The temperature setpoint for cooling devices is normally taken directly from the Control
setpoints, max value for Temperature (see Figure 3.8). The corresponding value for heaters is
the Temperature min value. However, from version 4.5, it is also possible for the Expert
edition user to define any controller for an individual device.

### 3.7. Ideal heaters and coolers
Ideal room units should be used to condition the zone when no detailed information about an
actual room unit, such as a fan coil or active chilled beam, is available or this amount of detail
is unmotivated. They have no given physical location on any room surface and are not
connected to the plant of the building. They do have a maximum capacity parameter, enabling
the user to experiment with limited heating/cooling capacity. However, this parameter should
normally be set to a large enough value to always cover any foreseen need. However, do not
set the value to a totally unrealistic number, e.g., 100 times the reasonable heating load. This
will result in poor control action.

---

> [[03_3_2_airflows|◀ Kap. 3.5]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_5_6_fan_coil_hydronic|Kap. 3.8 ▶]]
