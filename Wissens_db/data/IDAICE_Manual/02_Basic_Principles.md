---
tags: [IDA-ICE, Simulation, Grundlagen, Architektur]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "Kap. 2"
titel: "Basic Principles of IDA ICE"
---

# Kap. 2 – Basic Principles of IDA ICE

> [[01_About_the_Manual|◀ Kap. 1]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  [[03_1_Model_Description_Intro|Kap. 3.1 ▶]]

---

2. Basic principles of IDA and IDA Indoor Climate
and Energy
### 2.1. Introduction
> 📖 Tutorial: [[01_1_Modell_Grundsaetzliches|IDA ICE Tutorial – Kap. 1.1: Modell & Grundsätzliches (Einstieg Standard Level)]]  ·  Theorie: [[01_Grundlagen|Skript Energie Kap. 1 – Energieflüsse im Gebäude (was IDA ICE simuliert)]]

IDA Indoor Climate and Energy (IDA ICE) is a program for study of indoor climate of
individual zones within a building, as well as the energy consumption for the entire building.
IDA ICE is an extension of the general IDA Simulation Environment. This means that the
advanced user can, in principle, simulate any system whatsoever with the aid of the general
functionality in the IDA environment.

Normally, the system to be simulated consists of a building with one or more thermal zones, a
primary system (plant) and one or more air handling systems. Surrounding buildings might
shade the building. The air inside the building contains both humidity and carbon dioxide.
Weather data is supplied by weather data files, or is artificially created by a model for a given
24-hour period. Consideration of wind and temperature driven airflow can be taken by a bulk
air flow model. Predefined building components and other parameter objects can be loaded
from a database.
2.2. The three levels of user interface
The user interface is divided into three different levels, with different support and scope for
the user. At the simplest level, called wizard, the scope is limited to a certain type of study
and level of approximation. The user is given the opportunity of carrying out a simulation
directly, or transferring the data entered to the next level, called the standard level. From
version 4.7, a new wizard interface IDA Early Stage Building Optimization (IDA ESBO) is
included, see Figure 2.1. It replaces the IDA Room wizard which is no longer included. To
learn more about IDA ESBO, press on the toolbar and then the F1 key on your keyboard to
launch the online help.

![[data/assets/IDAICE_Manual/fig_2_1.png]]
*Abb. 2.1 – The Building tab of IDA ESBO*

At the standard level (Figure 2.2), the user is given greater freedom to design a building
model. This level defines geometry, materials, controller settings, loads, etc., in a manner that
should be easy to handle for a majority of engineers. The basic steps of using the standard
level are covered by the Getting Started Guide. An interactive Process guide (Help menu) is
also available to guide you, by movies and other support, through the steps of building a
model at the standard level.

![[data/assets/IDAICE_Manual/fig_2_2.png]]
*Abb. 2.2 – Main form for the building at standard level*

At the advanced level (Figure 2.3), the simulation model is no longer defined in physical
terms, but in the form of connected component models, defined by equations. At this level,
the individual time evolution of variables can be studied. All equations, parameters and
variables can be examined at this level.

A user of the Expert edition of the program may also edit the connection structure at the
advanced level. Some of these operations are easy to carry out, e.g. changing a proportional
controller to a thermostat. Others are more complicated and require a deeper knowledge of the
design of the models.

Use of the advanced level is introduced in Chapter 5. EQUA also maintains some exercises
that can be used to gain familiarity with the advanced level. In addition, a great deal of
information is found in the on-line help texts. Make sure also to visit the User Forum, which
can be accessed as soon as you have IDA ICE running. You start the User Forum either from
the Portal page (the first screen that meets you) or from the Help menu -> Support-> Ask a
question.

![[data/assets/IDAICE_Manual/fig_2_3.png]]
*Abb. 2.3 – Main Form for the building at the advanced level*
### 2.3. Forms and dialogs
IDA ICE is built up around forms and dialogs. The forms contain no Cancel button, i.e. there
is no access to earlier versions of a form (except by using Undo). Forms do not lock each
other, and several windows with forms can be open simultaneously (but only the one where
work is in progress is active). A form can be printed. Simulations and many other operations
can be carried out without having to first close open forms. Dialogs, i.e. input windows with
OK and Cancel buttons, work in IDA as in most other Windows programs. They lock
everything else but the current dialog window.

