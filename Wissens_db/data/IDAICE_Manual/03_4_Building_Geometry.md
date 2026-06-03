---
tags: [IDA-ICE, CAD, IFC, Geometrie, Import]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "Kap. 3.4"
titel: "Building Geometry – CAD & Image Import"
---

# Kap. 3.4 – Building Geometry – CAD & Image Import

> [[03_3_7_cooling_units|◀ Kap. 3.3]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[04_Getting_Started_Advanced|Kap. 4 ▶]]

---

## 4. CAD and image import
> 📖 Tutorial: [[01_2b_Variante0_Geometrie|IDA ICE Tutorial – Kap. 1.2b: Geometrie & Zonen zeichnen (Floor Plan)]]  ·  Vertiefung: [[04_Getting_Started_Advanced|IDA ICE Manual Kap. 4 – Advanced Level für Geometrieexport]]

In IDA ICE it is possible to import CAD objects and image files. These can be used as a base
when creating the simulation model, or as shading elements that cast shadows onto the
simulation model. There are three categories of CAD objects and image files; building
information models (BIM), CAD and vector graphic files, and image files.

BIM files contain 3D geometry as well as properties for rooms, walls, windows and materials
etc. An IDA ICE model, i.e. building bodies, zones and windows etc., can be automatically
created from the geometrical information. Furthermore, the properties of objects in the BIM
file can be mapped to the corresponding objects in the simulation model. The 3D geometry of
a BIM file can also be selected to shade the simulation model.

CAD and vector graphic files contain 3D or 2D geometry. A section of this geometry is
shown as lines in the floor plan tab and these lines can be used to snap building bodies and
zones etc. in the floor plan. Building bodies and zones can be automatically created from
graphic files if the imported geometry consists of volumes enclosed by polygon surfaces. 3D
CAD objects can be selected to shade the simulation model.

Image files contain raster (bitmap) images. These are shown in the floor plan tab when the
section is close to the location of the image. The images can be used as a background when
drawing building bodies and zones in the floor plan or when inserting windows and shading
objects in the 3D view.
### 4.1. Supported file formats
#### 4.1.1. BIM
Industry Foundation Classes (*.ifc)
#### 4.1.2. CAD and vector graphic files
AutoCAD (*.dwg8, *.dxf, *.dwf)
SketchUp (*.skp9)
3D Studio (*.3ds)
Wavefront (*.obj)
Computer Graphics Metafile (*.cgm)
Corel Presentation Exchange (*.cmx)
MicroStation DGN (*.dgn)
Micrografx DRW (*.drw)
Gerber File Format (*.gbr)
Scalable Vector Graphics (*.svg)
Printer Command Language (*.pcl, *.prn, *.prt)

8 IDA ICE supports DWG file formats up to AutoCAD 2004. DWG files of unsupported formats can be
converted with the free tool Autodesk DWG TrueView. DWG files are assumed to be two-dimensional, i.e. any
3D geometry is flattened to 2D at import.

9 IDA ICE supports SketchUp files up to version 2013. SketchUp files of later versions can be saved as version
2013 from SketchUp.

Macintosh PICT (*.pct)
HP-GL/HP-GL2 (*.plt)
WordPerfect Graphics (*.wpg, *.vwpg)
#### 4.1.3. Image files
Bitmap (*.bmp)
JPEG Interchange Format (*.jpeg,*jpg)
Portable Networks Graphics (*.png)
ZSoft PC Paint (*.pcx)
Tagged Image File Format (*.tiff,*.tif)
Adobe Photoshop (*.psd)
Truevision (*.tga)
Windows Meta File (*.emf,*.wmf)
### 4.2. Importing IFC files
In IDA ICE it is possible to import 3D building information models (BIM) via IFC files. Most
3D CAD applications can export architectural data in the IFC format.

The most important information that is transferred is geometrical data, i.e. the shape and
position of zones, windows, doors, building faces etc. Zones in IDA ICE are automatically
created from so called space objects in the IFC model. It is not sufficient that the CAD model
only contains wall objects, spaces that fill the voids between walls must also have been
created, a semi-automatic process in most CAD tools.

IDA ICE can also utilize other types of information in the CAD model, such as space types,
window types, wall constructions, should they be present. One can find more detailed
information about the ICE IFC implementation on the user s web page: Help menu, Support,
Download & info center. Select Documentation on the page and open the document IFC
Import .
### 4.3. Mapping data from IFC
Start with a building without zones and select the Floorplan tab. Press IFC > Import to
select an IFC file for loading. There are some sample IFC files in the installation, normally
located in C:\Program Files\IDA\samples\ICE\IFC.

The first task is to map named data objects in the IFC model (if any are present) to
corresponding IDA resources. Press IFC > Mapping in the Floorplan tab to open the
Mapping dialog (Figure 4.1). If wall constructions have not been described in detail in the
CAD model, select directly Constructions in the Category combo box. This will present a list
of all wall types that have been found in the IFC model. Since IDA ICE needs more detailed
information about a wall, IFC wall types need to be manually associated with IDA ICE wall
constructions. To bind a certain IFC wall type to an IDA ICE construction, select both the IFC
wall type and the corresponding ICE resource and press Map to selected. A right pointing
arrow in the IFC Data list indicates that the item has been bound. Usually one first has to load
relevant IDA ICE resources from the database by pressing Load from Db. To inspect the
selected IDA resource, press View.

Repeat the procedure for window types as well. Here, one usually has to first create relevant
windows in the ICE database, including internal shadings etc.

If wall constructions have been described in the IFC model with layer thicknesses and
material names, one can automatically create corresponding IDA ICE constructions. In this
case, one starts instead with binding IFC material names with IDA ICE material resources.
Once the materials have been mapped, IDA ICE wall construction resources are created by
pressing Import from IFC when the relevant IFC wall type has been selected.

A useful addition, available from version 4.7, is the ability to map IFC space type names to
zone templates. This way, if you have created templates for your typical room types, zones
will be created with all input data already in place.

Any object in the IFC model which is not explicitly mapped to an IDA resource will be set to
its default value, which is given by pressing Defaults on the General tab in the building form.

![[data/assets/IDAICE_Manual/fig_4_1.png]]
*Abb. 4.1 – IFC Mapping dialog*

### 4.4. Changing position of IFC model
The position of an IFC model can be changed in IDA ICE. Press IFC > Shift to open the
Shift dialog. In this dialog an offset or desired position can be defined for the IFC model.

### 4.5. Create zones from IFC spaces
An IFC model may contain more than a single floor. A horizontal section (slice) of the
building at a certain level is shown in the Floorplan tab (Figure 4.2). To select a different
level, press the button Level: xx m, where xx is the floor height from ground of the current
level. In the Level dialog, the building height from ground (Building top) and height
coordinate of the floor slab with respect to ground (Building bottom) are also shown, as
interpreted from the IFC file. These numbers are not always correct for the user s purpose.

To define which spaces in the IFC model that should constitute a (thermal) zone in the
simulation model, click on (select) the neighboring spaces that should be included. (Click
again to unselect a space.) Think about zone economy, i.e. do not create more zones than you
think is physically motivated for the current study. To create an IDA ICE zone from the

selected IFC spaces, press New zone10. This will create zones using the currently selected
zone template, unless the IFC space type has been mapped to a given template. Try to give as
many reasonable defaults as possible for new zones using appropriate zone templates; after
creation these values must be edited separately for each created zone.

If you have a good quality IFC-file, you can also - from version 4.7 - instantiate all IFC
spaces to zones with a single press of the New zone button without first selecting the space.
To do this, select this alternative under the IFC button.

![[data/assets/IDAICE_Manual/fig_4_2.png]]
*Abb. 4.2 – IFC model with an ICE zone, a selected IFC space and unselected IFC spaces*

The IDA ICE zones are created from the geometry of the corresponding IFC space(es). If for
example a space is taller than the typical floor to floor distance of the building, the
corresponding ICE zone will also reach over more than a single floor. One can change the
horizontal section level during the zone creation process but it is currently not possible to
combine several spaces vertically into a single zone. Note that the Floorplan view displays
two models simultaneously, the zones of the created ICE model and the spaces of the IFC
model. Both categories of rooms can be individually selected and ICE zones can also be
opened.

If the IFC model is revised during the ICE modeling project, there is some support for
retaining previous work. New IFC models can be loaded while modeling, either replacing the
existing model or adding to it, e.g. loading several floors that are in separate IFC files. When
a new file is loaded, the user is given the option to replace or add to the current IFC model
and to replace or keep mapping information and existing ICE zones.

10 By default an individual zone is created for each selected IFC space. Optionally, all the selected spaces can be
merged (if they have the same floor and ceiling level) into larger zones. This setting is found under the IFC

If the IFC information is incomplete or too complex for some part of the building, the user
can simply avoid to instantiate these zones based on IFC background and draw them manually
on the floor plan.
### 4.6. Exporting results to IFC
Results from heating and cooling load simulations in IDA ICE can be exported for merging
with IFC models. This is done by choosing Export to IFC in the Tools menu after
simulation of the heating and cooling loads.
### 4.7. Importing CAD objects as building bodies or zones
CAD objects can be imported as building bodies or zones if the imported geometry only
contains a volume enclosed by polygon surfaces (polyhedron) without holes between the
surfaces. The geometry should describe the inner surface of the external walls for a building,
and the inner surface of the zone walls for a zone. No other information than the pure
geometry of the building body or zone can be included in the CAD object. Click Import on
the floor plan tab and choose Import building body or Import zone geometry .

Imported building bodies and zones have protected geometry, i.e. their geometry is non-
editable. However, an imported building body is fully editable if the imported geometry only
has one floor and that floor is horizontal and does not contain any holes, and the geometry
does not have any outward leaning walls (surfaces with their exterior normal pointing
downwards). This is the same kind of geometry that can be created in the ICE roof editor.
Importing geometry as zone will also create a building body of the same shape as the zone.

If a geometry file contains multiple polyhedron geometries, each with a separate color, they
are imported as separate building bodies or zones in ICE. If surfaces are placed one wall
thickness apart, these are regarded as thermally connected internal walls.
### 4.8. Importing CAD objects and images as background
CAD objects and image files are either imported with respect to the building coordinate
system, and are then moved with the building if the building is repositioned or rotated, or they
are imported with respect to the site coordinate system, and remain fixed if the building is
repositioned or rotated.

Import a CAD object/image file with respect to the building coordinate system by clicking the
Import button on the floor plan tab and choosing CAD and vector graphic. Alternatively,
select Import CAD on the Insert menu while the 3D tab is shown.

Import a CAD object/image file with respect to the site coordinate system by clicking the
Import site CAD button on the Site object dialog opened by clicking Site shading and
orientation on the General tab. Alternatively, select Import CAD to site on the Insert menu
while the 3D tab is shown.

To place a CAD object/image at the current mouse pointer in the 3D view, use Right mouse
button menu > Import CAD or Right mouse button menu > Import CAD to site.
### 4.9. Moving and scaling CAD objects and images
A CAD object is automatically scaled and positioned so that it corresponds to the simulation
model. The scale and position of a CAD object can be seen and edited by double-clicking on

the object. A section of the CAD object or image is shown in the floor plan tab if the floor
plan level is within the bounds of the object. Select this section by clicking on it11. Move and
change size of the CAD object/image by dragging/resizing the section.

A CAD object can also be moved in the 3D view. Select the CAD object, hold down the ctrl-
key and drag the object. The object moves in the x-y plane. To move a CAD object along the
z-axis, hold down the ctrl-key and the shift-key while dragging.
### 4.10. Shading by imported 3D objects
3D CAD objects can be selected to shade the simulation model. Check the Calculate shadows
checkbox in the dialog shown when the object is double-clicked. Every surface of the 3D
object that is not fully transparent is included in the shadow calculation. Semi-transparent
surfaces are included and shade according to their transparency. Note that it is the surfaces
that shade, so for instance for semi-transparent sphere light will pass two surfaces and hence
be reduced by the semi-transparency twice.
### 4.11. Storage of CAD objects
By default the geometrical information of CAD objects is saved in the system file (*.idm).
The original CAD file is then not needed after the import. However, if a CAD file is big, very
large system files can be created and the performance of IDA ICE can be slowed down. Thus,
if a CAD file is big, the option of not saving it in the system file is given in the Preferences
dialog, which is opened at import. In that case, only a shortcut to the original CAD file is
saved in the system file and the original CAD file needs to be saved in the location specified
by the shortcut. If the CAD file is placed in the ICE system folder (the folder with the same
name as the system), the shortcut is relative and the CAD file is automatically copied with the
system to a new location. Otherwise the shortcut is absolute and the CAD file is not copied
with the system. The definition of a big CAD file can be changed in the Preferences dialog
from the default of 10000 vertices. The Preferences dialog can also be opened from the
Options menu.

11 To select a CAD object, click on the geometry lines. To select an object that is behind another object, press the
ctrl-key and click on the object until it is selected.
