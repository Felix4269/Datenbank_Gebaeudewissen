---
tags: [IDA-ICE, Tipps, Numerik, Performance, Instabilität]
normnummer: "IDAICE Manual v4.8"
gueltig_ab: "2018-01-01"
kapitel: "Kap. 5"
titel: "Tips & Tricks / Numerical Instabilities"
---

# Kap. 5 – Tips & Tricks / Numerical Instabilities

> [[04_Getting_Started_Advanced|◀ Kap. 4]]  ·  [[_IDAICE_Manual_MOC|↑ Inhaltsverzeichnis]]  ·  *(Ende)* ▶

---

## 6. Tips and tricks
### 6.1. Speeding up computation
IDA ICE builds a single large simultaneous system of equations for all processes in the
building. This system of equations contains several ordinary differential equations and has
therefore different built in time constants. The room air will for example react quickly on a
convective heat load, while the ground layer below the building can have a time constant
several orders of magnitude larger. This system of equations is solved with numerical
methods that adapt the timestep to the frequency content of the solution. Short time constants
in the model in combination with high frequency content in driving functions (many starts and
stops) can lead to long execution times.

Internally generated starts and stops (events) will also lead to short timesteps. Try for example
to use a thermostat for radiator control.

The shear number of equations in the system is naturally significant for the execution time,
which increases roughly linearly with the problem size13. Therefore, it is vital not to model
any unnecessary detail, and not for example model a large number of identical objects such as
windows or cooling beams, when they could be replaced by a single larger one. Each added
zone will contribute about two thousand variables to the system of equations.

The single most important factor for speeding up calculations is to have a reasonable amount
of detail in time schedules (driving functions). Describing many sharp transitions will usually
only result in increased computation time and not have a significant impact on results. From
version 4, automatic smoothing is applied to key schedules to minimize these problems. (Can
be turned off under System parameters).

For a model with reasonably simple time schedules, it can often prove effective to loosen the
numerical tolerance to make the solver take longer and thereby fewer timesteps. Two
important solver parameters are Tolerance and Maximum timestep. These are accessed from
the Advanced tab of the Simulation data dialog. Often the tolerance can be relaxed to, say,
0.1-0.3 from the standard value 0.02. For problems with equations that are difficult to solve, it
can sometimes be beneficial to instead decrease the tolerance. (The solver spends less time on
failed attempts to take long steps.)

Looser tolerance will normally lead to acceptable loss of accuracy for accumulated quantities
such as monthly energy consumption. For computing design (extreme values) of quantities
such as heating or cooling load, one should be more careful with using loose tolerances and a
large max timestep. Too loose a tolerance will on the other hand lead to decreased robustness,
forcing the solver to often have to back up and retry with a smaller timestep, ultimately
leading again to even longer execution time (if indeed the simulation is successful).

13 For more primitive numerical methods, the execution time will typically grow as the cube of the problem size.

To learn about the statistics of a simulation in terms of number of timesteps, variables, restarts
etc. view the file screen.txt in the IDA temporary directory idamod4814. At the end of this file
some statistics are given.
### 6.2. Time-split Parallelization
The clock time of the simulation can be substantially decreased on a computer with more than
one core, able to run concurrent processes by splitting the whole simulation period into
smaller periods running on different cores. This is implemented in IDA ICE to been done
automatically if the box Time-split parallelization in the Advanced Simulation Data tab is
ticked, see Figure 6.1. The number of processes is set under the Simulation Preferences menu,
see Figure 6.2.

![[data/assets/IDAICE_Manual/fig_6_1.png]]

*Abb. 6.1*

![[data/assets/IDAICE_Manual/fig_6_2.png]]

*Abb. 6.2*

There is no gain in simulation time if the number of processes is higher than the total
available logical processors and this parallelization technique has some overhead which
makes it beneficial only for long simulation periods. The Speed-up is roughly 2-3 using 4
processes and roughly 4 using 12 processes.
### 6.3. Numerical instabilities
With a tool like IDA ICE it is easy to build large non-linear systems of equations and solve
them for thousands of time points. However, it is impossible to, even theoretically, guarantee
the success of the solution procedure. Any non-linear system of equations may have more
than a single solution or none at all. Numerical computer programs are in this respect different
from most other types of software, where it may be, at least theoretically, possible to create a
bug-free code. IDA ICE also has a more difficult task than most other building simulation
software, where less freedom is given to create mathematically complex models.

A major part of the IDA development work is devoted to improving the solver performance
on difficult cases. However, this work is altogether dependent on close interaction with users.
It is vital that users, which have built reasonable and meaningful models that are difficult to

14 This directory may occur in different locations depending on Windows version used. The path to the
temporary directory can be found under Options > Preferences > Advanced. Solver files can also be viewed from
the View menu > Solver files.

solve, take the trouble of sending the model to the support office. This is most easily done by
using the Mail support function on the Help menu.

Some physical processes more often lead to problematic models. Generally speaking, models
with significant natural ventilation flows through openings or leaks are the most difficult to
solve, especially when the effect of wind pressure is included. If, in addition, vertical
temperature gradients are to be simultaneously computed, one obtains a severely stiff and
non-linear system of equations.

Avoid to use vertical or horizontal openings unless the bidirectional flow is essential for the
study (use large leaks instead). Absolutely do not use large openings for the purpose of
recreating the exact geometry of a real building. Normally, precise geometry has a very small
impact on results.

A common type of error is when the user has graphically defined a piecewise linear controller
and unintentionally entered several points near each other, giving the curve (in micro scale)
several sharp corners and jumps. The solver will invariably have problems to negotiate the
sharp turns of such a graph. Check the table view of such a curve for unintentional points.

A general way of dealing with difficult cases is to decrease the tolerance parameter that was
discussed in the previous section. This forces the solver to be more careful and take smaller
steps, which in most cases improves robustness. A tolerance of 0.001 or even smaller can
sometimes be used.

A frequent situation is that any change in input data makes a previously failed run go through.
This is not as strange as it sounds, since each change will lead to a different sequence of
timesteps and in this way the exact combination of values that led to the failed timestep is
avoided.

Another often effective trick is to replace sharp steps in schedules with steep ramps,
especially for the fan control schedule. This will enable the solver to gradually over a short
time period approach the new solution and thereby reach it more securely. If, in addition, the
start and endpoints of the ramp are marked as input events (double entries of the same point in
the table view), the solver will be even more cautious. Input events are marked by repeating
the same time point twice in the profile, something best done in the Data tab view.

From version 4.7, a new useful diagnostic tool has been added. When the option Show
slowest model (Options menu, Preferences, Developer) has been selected, the component
with the slowest convergence in each timestep will blink red during simulation, when viewed
on the Schematic tab. For a case that runs well, the role of being the slowest model will
change among several components during the simulation. On the other hand, for models with
some particularly problematic equations, the components that are involved in this difficulty
will blink more than others and this will frequently lead the user to understand the root of the
problem.
