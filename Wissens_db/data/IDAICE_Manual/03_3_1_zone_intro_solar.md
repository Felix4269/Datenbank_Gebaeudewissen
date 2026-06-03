---
tags: [IDA-ICE, Zonenmodell, HVAC, Strahlung, Hydronik]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "3.3–3.4"
titel: "Zone Models Introduction and Solar Radiation Modeling"
---

# Kap. 3.3–3.4 – Zone Models and Solar Radiation

> [[03_2_3_air_handling|◀ Kap. 3.2]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_2_airflows|Kap. 3.5 ▶]]

---

> 📖 Tutorial: [[01_2b_Variante0_Geometrie|IDA ICE Tutorial – Kap. 1.2b: Zonen zeichnen & Zonenmodell konfigurieren]]  ·  Theorie Solar: [[03_2_solare_waermegewinne|Skript Energie Kap. 3.2 – Solare Wärmegewinne & g-Wert]]  ·  Wärmespeicher: [[03_3_waermespeicherung|Skript Energie Kap. 3.3 – Wärmespeicherung]]

3.3. The zone models
For the HVAC systems, the presentations for the standard and advanced user interface levels
are the same (for the distinction between standard and advanced levels, see Section 5).
However, in the case of the zone models, the presentations are completely different. This
section explains the principal features of the zone models, and also provides a brief overview
of the advanced level in this context. Actually, most users will never have to deal with the
advanced level, but it is useful to know it exists, and the physics are more easily explained
from the point of view of the advanced level.

IDA ICE provides two different zone models. One of these, the climate model, is quite
detailed - it may for example calculate a vertical temperature gradient. The second model, the
energy model, has a more conventional level of precision, and is based on a mean radiant
temperature. Both zone models are based on the same description of the building, given in the
standard level. All models of components in and around the zone, such as windows, radiators,
controllers, leaks, terminals etc., are common to both the energy and climate models. The
climate model is currently available only for zones with a rectangular geometry. From version
4, the energy model is default for new zones, but this can easily be changed in the Defaults
form. More details about the mathematical models can be found in Models for Building
Indoor Climate and Energy Simulation or by studying the NMF code in the Code tab of the
component window at the advanced level.

Figure 3.6 shows a schematic view (advanced level) of a zone with the climate model. To
access this window, press Build model in the Simulation tab, after entering all the information
required in the standard level. In this case this includes selection of climate model, an ideal
heater, a cooling panel and external shading. After the advanced level model has been
generated, the user is able to select between General (standard level) and Schematic
(advanced level) tabs for zones as well as for the building. The various component groups are
numbered in the figure as follows:

1. Supply and exhaust air terminals
2. Ceiling/Floor (this object is both ceiling and floor, since the model was generated to represent zones above and below with identical conditions as the current zone)
3. Air leak to ambient
4. Solar irradiation and external film coefficient, external wall
5. One external and three internal walls
6. Window and shading calculation components
7. Proportional controller for occupant automatic clothing adaption
8. PI controller for ideal heater
9. Cooling panel with controller and ceiling section behind
10. The actual zone model in which radiation, convection and loads etc. are modeled
11. Post processing components for results capture.

![[data/assets/IDAICE_Manual/fig_3_6.png]]
*Abb. 3.6 – Schematic view (advanced level) of Climate zone model*

### 3.4. Solar radiation modeling
A key issue in building simulation is the treatment of direct and diffuse solar radiation. Let us
follow the main steps in the treatment of sunlight entering the building. If synthetic weather is
used, ICE first computes direct and diffuse sunlight intensities based on the clearness number
given in the Location object. At the advanced level, the components used for this computation
are found in the Schematic tab of the building form under the heading Climate processor.

In the next model in the chain, the solar position in the sky is computed and all the signals
computed so far are sent to a set of Face models, where the climatic conditions outside each
main building surface (Facade) are computed. In this model, the distribution of diffuse
radiation in the sky is also computed, by default using the Perez model.

In the next step, solar radiation on an individual object such as a window is computed.
Connected to each window model (See Figure 3.6) is a shading calculation model (Shade),
that computes the shading of both direct and diffuse light on the receiving surface. This model
puts all shading surfaces in one bin, including building self shading, shading by neighboring
buildings and shading by (possibly movable) objects directly outside of the window (External
shading). Diffuse light from the sky is also shaded, but no reflections other than ground
reflection are accounted for. Ground reflection for each face can be set from the Property page
if the face name is selected in the Floor plan tab. Diffuse radiation from the ground is not
shaded by external objects. All external shades are considered to be opaque.

The shade model is very difficult to interact with directly at the advanced level, since each
surface has been subjected to several coordinate transformations. The actual shading factors
are precomputed for all (plausible) solar locations and are stored as parameters in the shade
model for the simulation.

Once in the window model, diffuse and direct light are reflected and transmitted depending on
the window model used. The standard window model uses a fixed curve for the angle

dependence. Integrated window shading (internal, interpane or external shades in the plane of
the window) will reduce radiation by multiplying the basic window parameters. It may also
convert direct light to diffuse.

The detailed window model, makes a layer by layer computation of multiple reflections and
each layer temperature is computed. For glazings where all the glass panes and the integrated
shading have spectral data, the optical calculation in the solar range is made for each
wavelength and the values are then integrated to average values according to EN 410.

Once inside the zone, diffuse light is spread diffusely, while the exact target location of the
direct light beam is computed. However, the whole surface of the window is considered as the
light source, not just the portion of the glass which is actually not shaded by external objects.
After the first reflection on a zone surface, the direct beam is spread diffusely in the room.
And also here, the whole surface that is hit is regarded to reflect with equal intensity, not just
the lit portion of this surface.

Internal windows and open doors transmit light in a similar way as an external window, i.e.
the whole opening is regarded as being lit, even if only a small part of the door receives direct
sunlight. The light intensity is of course adjusted accordingly. Similarly, light that enters
through one window and exits through another external window, for example in a corner
room, is treated in a physically reasonable way.

---

> [[03_2_3_air_handling|◀ Kap. 3.2]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_3_2_airflows|Kap. 3.5 ▶]]
