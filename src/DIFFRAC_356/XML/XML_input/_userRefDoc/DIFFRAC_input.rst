*********************
Reference user manual
*********************

sim
###

This is the simulation, the top object in DIFFRAC.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - projectNumber
     - The user must specify the project number.
     - \-
     - \-
     - \-
   * - nProcs
     - The user may specify the number of openMP processors. Negative number means DIFFRAC decides the optimum value.
     - -1
     - \-
     - \-

parVTKDIF
*************

This is the VTKDIF parameters group. VTKDIF processes the vtk file, determines waterline elements and applies a horizontal shift or yaw rotation if specified. The position of the body/bodies can be viewed by importing the generated file VTKcombined.vtk in paraview.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program VTKDIF will be run. If "false" is selected the program VTKDIF is not run.
     - false
     - \-
     - \-
   * - areaTreshold
     - The user may specify the panel area treshold. Panels with an area smaller than this value are disregarded.
     - 0.002
     - \-
     - m^2
   * - refinementFactor
     - The user may specify the mesh refinement factor 1=no refinement, 2=all panels divided in two, 3=waterline panels divided in four, 4=all panels divided in four
     - 1
     - \-
     - \-

parINIDIF
*************

This is the INIDIF parameters group. INIDIF initializes the DIFFRAC database and determines the hydrostatic properties based on the panel geometry.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - dataBaseFn
     - The user must specify the name of the binary database (without extension) on which the hydrodynamic solution and geometry details are stored.
     - \-
     - \-
     - \-
   * - density
     - This is the water density.
     - 1.0260210
     - \-
     - tons/m^3
   * - refPntFn
     - The user may specify the name of the file (including extension) which contains the coordinates of the reference points. The reference points must be defined in the global earth-fixed coordinate system. Each line of the file should contain 1 reference point with space separated values (x,y,z).
     - NONAME
     - \-
     - \-
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program INIDIF will be run. If "false" is selected the program INIDIF is not run. Be aware that when inidif is run, old databases (mandat/hdf5) will be deleted!
     - false
     - \-
     - \-

quay
==================

This is the quay parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - apply
     - The user may specify the 'apply' (boolean) switch. If "true" is selected, then a quay is modelled with a symmetry plane at y=yQuay. If false is selected, no quay is modelled.
     - false
     - \-
     - \-
   * - yQuay
     - This is y-coordinate of the quay in the global earth-fixed coordinate system.
     - 0
     - \-
     - m

basinWall
=======================

This is the basin Wall parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - apply
     - The user may specify the 'apply' (boolean) switch. If "true" is selected, then a basin wall is modelled using 2 symmetry planes defined by x=xBasin and y=yBasin. If "false" is selected then no basin wall is modelled.
     - false
     - \-
     - \-
   * - origin
     - This is origin (xBasin, Ybasin) where the two basin walls x=xBasin and y=yBasin cross.
     - 0.,0.
     - \-
     - m

springMatrix
==========================

This is the spring Matrix parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - fromGeometry
     - The user must specify the 'fromGeometry' (boolean) switch. If "true" is selected, then the spring matrix is computed from the position of the centre of gravity and the panel mesh (so hydrostatics only). If "false" is selected then the spring matrix is imported from a space separated file with 6*Nbody rows amd 6*Nbody columns.
     - true
     - \-
     - \-
   * - springMatrixFn
     - The user may specify the name of the file (including extension) which contains the (6*Nbody)*(6*Nbody) spring matrix. The file must be space separated.
     - NOT SPECIFIED
     - \-
     - \-

dampLid
=====================

This is the dampLid parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - length
     - This is the length of the damping lid.
     - -1.0
     - \-
     - m
   * - width
     - This is the width of the damping lid.
     - -1.0
     - \-
     - m
   * - NrPanelsLength
     - This is the number of panels along the length of the damping lid.
     - -1
     - \-
     - \-
   * - NrPanelsWidth
     - This is the number of panels along the width of the damping lid.
     - 1
     - \-
     - \-
   * - dampingValue
     - This is the damping value.
     - \-
     - \-
     - \-
   * - orientation
     - This is the orientation of the damping lid.
     - 0.0
     - \-
     - deg
   * - turbineIndex
     - The user may specify the index of the turbine to which the damping lid belongs. Use index zero when this damping lid is not related to any turbine.
     - 0
     - \-
     - \-
   * - origin
     - This is the origin of the centre of the damping lid.
     - 0.0,0.0
     - \-
     - m,m
   * - bodyFixed
     - The user may specify the 'bodyFixed' (boolean) switch. If "true" is selected, then damp lid is fixed to the body indicated in the 'bodyIndex' field. If "false" is selected the damp lid is not fixed to any body.
     - false
     - \-
     - \-
   * - bodyIndex
     - The user may specify the index of the body to which the damping lid belongs. Used when damping lid is body-fixed.
     - 0
     - \-
     - \-
   * - dampIncWave
     - The user may specify the 'dampIncWave' (boolean) switch. If "true" is selected, then the incident wave will be damped by the damping lid. If "false" is selected the incoming wave will not be damped by the damping lid (only the radiation and diffraction potentials).
     - \-
     - \-
     - \-
   * - meshFn
     - The user may specify the name of the VTK file (including extension) which contains the damplid mesh.
     - NOT SPECIFIED
     - \-
     - \-

turbine
=====================

This is the turbine parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - constant
     - The user may specify the turbine constant, which determines the flow rate through the turbine.
     - \-
     - \-
     - s^2/m^2.5
   * - turbineType
     - The use may specify the turbine type (LINEAR, KNSWING)
     - LINEAR
     - LINEAR,KNSWING
     - \-
   * - bodyIndex
     - The user may specify the index of the body to which the turbine belongs.
     - \-
     - \-
     - \-

grid
==================

This is the grid parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - spacing_x
     - This is the grid spacing (distance between the points) in x-direction.
     - \-
     - \-
     - m
   * - spacing_y
     - This is the grid spacing (distance between the points) in y-direction.
     - \-
     - \-
     - m
   * - NrOfPointsX
     - This is the number of grid points in x-direction. The number should be odd.
     - \-
     - \-
     - \-
   * - origin
     - This is the origin (x,y,z) of the grid. z=0 corresponds to the free surface
     - \-
     - \-
     - m,m,m
   * - orientation
     - This is the orientation of the grid in degrees.
     - 0.0
     - \-
     - deg
   * - NrOfPointsY
     - This is the number of grid points in y-direction. The number should be odd.
     - \-
     - \-
     - \-

parDIFFRAC
**************

This is the DIFFRAC parameters group. DIFFRAC computes the radiated, diffracted and undisturbed pressures and velocities for a set of wave frequencies by solving a Boundary Integral Equation for the unknown source strengths.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - NrOfGreenFunctionPointsPerWavelength
     - The user may speficy the number of Green function evaluations per wave length.
     - 12
     - \-
     - \-
   * - waterDepth
     - The user must specify the water depth.
     - \-
     - \-
     - m
   * - epsSym
     - Treshold to search for symmetrical panels.
     - 0.001
     - \-
     - m
   * - irregFreqSuppression
     - The user may specify the method for irregular frequency suppression: NO SUPPRESSION; RIGID LID; DAMPING LID; Suppression is only possible when free-surface lid panels are present in the vtk file(s) describing the body panel geometry.
     - RIGID LID
     - NONE, RIGID LID, DAMPING LID
     - \-
   * - irregFreqDamping
     - The user may input the damping value used for irregular frequency suppression with the option 'DAMPING LID'
     - 0.2
     - \-
     - \-
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program DIFFRAC will be run. If "false" is selected the program DIFFRAC is not run.
     - false
     - \-
     - \-
   * - minFrequency
     - The user must specify the minimum frequency for the diffraction computation.
     - \-
     - \-
     - rad/s
   * - frequencyStep
     - The user must specify the frequency step.
     - \-
     - \-
     - rad/s
   * - nFrequencies
     - The user must specify the number of frequencies.
     - \-
     - \-
     - \-
   * - porosity
     - The user may specify the 'porosity' (boolean) switch. If "true" is selected, then porosity (partially reflecting panels) will be applied. If "false" is selected, then porosity (partially reflecting panels) will not be applied. The porosity factors must be specified in the input vtk file of each body.
     - false
     - \-
     - \-
   * - solverType
     - The user may specify the solver for the radiation-diffraction problem: GMRES = Generalized Minimal Residual Method; LU = incomplete lower-upper decomposition method; IDRS=Induced Dimension Reduction method; PBJP_GMRES_MPI=MPI Parallel Block Jacobi Preconditioner GMRES
     - LU
     - GMRES_BJACOBI, GMRES_ILU, LU, IDRS, PBJP_GMRES_MPI
     - \-
   * - exportKinematicsVTK
     - The user may specify the 'exportKinematicsVTK' (boolean) switch. If "true" is selected, then velocities and pressures on hull panels are exported to a vtk file, for visualisation with paraview. If "false" is selected then velocities and pressures are not exported!
     - true
     - \-
     - \-
   * - nBlocksPrecon
     - The user may specify the number of matrix blocks for the preconditioner of the iterative solver. More blocks means less RAM usage but a worse preconditioning.
     - 4
     - \-
     - \-
   * - GMRES_RESTART
     - The user may specify the number of iterations after whhich GMRES is restarted. More iterations means faster convergence, but more RAM usage.
     - 200
     - \-
     - \-
   * - naturalFrequencies
     - The user may specify the method to determine the natural frequencies. COUPLED: couplings between motions are included. UNCOUPLED: couplings between motions are not included.
     - COUPLED
     - COUPLED, UNCOUPLED
     - \-
   * - waveDir
     - The user may specify the wave direction(s) in comma-bracket format, e.g. "0,45,90,135,180,210" or "0(45)180,210" (without quotation marks).
     - \-
     - \-
     - \-

current
======================

This is the DIFFRAC current parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - speed
     - This is the current speed.
     - 0.
     - \-
     - m/s
   * - direction
     - This is the current direction.
     - 0.
     - \-
     - deg

userDefinedWave
==============================

This is the userDefinedWave parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - apply
     - The user may specify the 'apply' (boolean) switch. If "true" is selected, then user-defined waves are applied. If "false" is selected then user-defined waves are not applied
     - false
     - \-
     - \-
   * - panelKinematicsFileName
     - The user may specify the name of the file containing the panel pressures and velocities
     - \-
     - \-
     - \-
   * - waterlineKinematicsFileName
     - The user may specify the name of the file containing the waterline wave elevation
     - \-
     - \-
     - \-

PBJPGMRESMPI
===========================

This is the PBJPGMRESMPI (mpi parallel block jacobi preconditioner gmres) parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - reordering
     - The user may specify the reordering procedure (Default NO)
     - NO
     - NO, FASTSV, RCM
     - \-
   * - reorderTol
     - The user may specify the tolerance for reordering
     - 0.03
     - \-
     - \-
   * - targetsizeJBreordering_dim1
     - if nrJacobiBlocks is set to -1, the user may specify the dim1 target size for Jacobi Blocks reordering (default=1000)
     - 1000
     - \-
     - \-
   * - targetsizeJBreordering_dim2
     - if nrJacobiBlocks is set to -1, the user may specify the dim2 target size for Jacobi Blocks reordering (default=1000)
     - 1000
     - \-
     - \-
   * - sizeSubProcReordering_dim1
     - if nrJacobiBlocks is set to -1, the user may specify the dim1 size for process subgrids reordering (Default = 4) 
     - 4
     - \-
     - \-
   * - sizeSubProcReordering_dim2
     - if nrJacobiBlocks is set to -1, the user may specify the dim2 size for process subgrids reordering (Default = 5) 
     - 5
     - \-
     - \-
   * - nrJacobiBlocks
     - The user may specify the size of Jacobi Blocks for reordering. The algorithm will determine optimal sizeSubProcReordering and targetsizeJBreordering parameters automatically. If it is set to -1, then it iwill be deteremined using those inputs. (Default = 4)
     - 4
     - \-
     - \-
   * - restartTolerance
     - The user may specify the tolerance to determine when GMRES is restarted. More iterations means faster convergence, but more RAM usage. (Default = 1.e-5)
     - 1.e-5
     - \-
     - \-
   * - restartAftIter
     - The user may specify the number of iterations after which GMRES is restarted. More iterations means faster convergence, but more RAM usage. (Default=200)
     - 200
     - \-
     - \-
   * - restartMaxIter
     - Maximun number of GMRES iterations. (Default = 500)
     - 500
     - \-
     - \-

sloshing
=======================

This is the sloshing input.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - apply
     - The user may specify the 'apply' (boolean) switch. If "true" is selected, then a sloshing analysis is performed. If "false" is selected a sloshing analysis is not performed.
     - false
     - \-
     - \-
   * - greenFunction
     - This is the type of Green Function used in the sloshing analysis. Full: frequency-dependent finite water depth Green Function. RANKINE: Rankine source only.
     - FULL
     - FULL, RANKINE
     - \-

parDBRESP
*************

This is the DBRESP parameters group. DBRESP recomputes the response of the body/bodies with possible additional damping, new springs, new mass matrix and new position of Centre of Gravity.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program DBRESP will be run. If "false" is selected the program DBRESP is not run.
     - false
     - \-
     - \-

BodyInput
=======================

This is the DBRESP input for a single body.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - index
     - The user must specify the index of the body
     - \-
     - \-
     - \-

massElement
-----------------------------------

This is the body inertial properties group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - COGwrtKeel
     - This is the center of gravity of the mass element. X and Y  (horizontal) with respect to the origin of the mesh. Z (vertical) with respect to the keel. (SI dimension = m, m, m).
     - \-
     - \-
     - m,m,m
   * - mass
     - This is mass of the mass element.
     - \-
     - \-
     - tons
   * - rollRadiusGyr
     - The user must specify the roll radius of gyration of the mass element (k_xx). Defined with respect to the mass element center of gravity
     - \-
     - \-
     - m
   * - pitchRadiusGyr
     - The user must specify the pitch radius of gyration of the mass element (k_yy). Defined with respect to the mass element center of gravity
     - \-
     - \-
     - m
   * - yawRadiusGyr
     - The user must specify the yaw radius of gyration of the mass element (k_zz). Defined with respect to the mass element center of gravity
     - \-
     - \-
     - m
   * - rollPitchRadiusGyr
     - This is the body roll-pitch radius of gyration. (k_xy)
     - 0
     - \-
     - m
   * - rollYawRadiusGyr
     - This is the body roll-yaw radius of gyration. (k_xz)
     - 0
     - \-
     - m
   * - pitchYawRadiusGyr
     - This is the body pitch-yaw radius of gyration. (k_yz)
     - 0
     - \-
     - m

totalDamping
------------------------------------

This is the body totalDamping properties group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - mode
     - This is the mode to which the damping must be applied.
     - \-
     - SURGE, SWAY, HEAVE, ROLL, PITCH, YAW
     - \-
   * - value
     - This is the total damping value expressed as dimension-full damping value or as percentage of critical damping (then there must be a restoring term present!)
     - \-
     - \-
     - kN-s-rad or %
   * - type
     - This is the way the damping-value is interpreted. % of critical damping (total): damping is computed as % of crticial damping and interpreted as total damping including potential damping. dimension-full value (total): actual dimension-full damping value interpreted as total damping including potential damping. dimension-full value (added viscous damping): actual dimension-full damping value interpreted as added viscous damping excluding potential damping
     - \-
     - % of critical damping (total), dimension-full value (total), dimension-full value (added viscous damping)
     - \-
   * - allowNegativeAddedDamping
     - This is the boolean that inicates if the added/viscous damping is allowed to be negative or not.
     - false
     - \-
     - \-

freeze
------------------------------

This is the body freeze properties group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - mode
     - This is the mode which must be frozen.
     - \-
     - SURGE, SWAY, HEAVE, ROLL, PITCH, YAW
     - \-
   * - value
     - This is the boolean that inicates if the mode must be frozen or not.
     - false
     - \-
     - \-

springMatrix
==========================

This is the springmatrix parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - fileName
     - The user may specify the name of the file (including extension) which contains the (6*Nbody)*(6*Nbody) spring matrix. The file must be space separated.
     - NOT SPECIFIED
     - \-
     - \-
   * - isEarthFixed
     - The user must specify the 'isEarthFixed' (boolean) switch. If "true" is selected, then the N-body spring matrix is assumed to be defined in the earth-fixed reference system.  If "false" is selected, then the N-body spring matrix is assumed to be defined in the ship-fixed reference system.
     - true
     - \-
     - \-
   * - unit
     - The user may specify the unit used for the spring matrix (N/kN)
     - kN
     - kN, N
     - \-

dampingMatrix
===========================

This is the dampingMatrix parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - fileName
     - The user may specify the name of the file (including extension) which contains the (6*Nbody)*(6*Nbody) damping matrix. The file must be space separated.
     - NOT SPECIFIED
     - \-
     - \-
   * - isEarthFixed
     - The user must specify the 'isEarthFixed' (boolean) switch. If "true" is selected, then the N-body damping matrix is assumed to be defined in the earth-fixed reference system.  If "false" is selected, then the N-body damping matrix is assumed to be defined in the ship-fixed reference system.
     - true
     - \-
     - \-
   * - unit
     - The user may specify the unit used for the damping matrix (N/kN)
     - kN
     - kN, N
     - \-

hinge
===================

hinge

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - name
     - The user may specify the name of the hinge.
     - \-
     - \-
     - \-
   * - c11
     - This is the surge stiffness of the hinge.
     - 0.
     - \-
     - kN/m
   * - c22
     - This is the sway stiffness of the hinge.
     - 0.
     - \-
     - kN/m
   * - c33
     - This is the heave stiffness of the hinge.
     - 0.
     - \-
     - kN/m
   * - c44
     - This is the roll stiffness of the hinge.
     - 0.
     - \-
     - kNm/rad
   * - c55
     - This is the pitch stiffness of the hinge.
     - 0.
     - \-
     - kNm/rad
   * - c66
     - This is the yaw stiffness of the hinge.
     - 0.
     - \-
     - kNm/rad
   * - b11
     - This is the surge damping of the hinge.
     - 0.
     - \-
     - kNs/m
   * - b22
     - This is the sway damping of the hinge.
     - 0.
     - \-
     - kNs/m
   * - b33
     - This is the heave damping of the hinge.
     - 0.
     - \-
     - kN/m
   * - b44
     - This is the roll damping of the hinge.
     - 0.
     - \-
     - kNms/rad
   * - b55
     - This is the pitch damping of the hinge.
     - 0.
     - \-
     - kNms/rad
   * - b66
     - This is the yaw damping of the hinge.
     - 0.
     - \-
     - kNms/rad
   * - index1
     - The user must specify the index of the first body the hinge is connected to
     - \-
     - \-
     - \-
   * - index2
     - The user must specify the index of the second body the hinge is connected to
     - \-
     - \-
     - \-
   * - posWrtKeel1
     - The user must specify the coordinates (x,y,z) of the hinge position with respect to the origin of the mesh file (x,y) and wrt keel (z) of the 1st body.
     - \-
     - \-
     - m,m,m
   * - posWrtKeel2
     - The user must specify the coordinates (x,y,z) of the hinge position with respect to the origin of the mesh file (x,y) and wrt keel (z) of the 2nd body.
     - \-
     - \-
     - m,m,m
   * - coordSystem
     - The user must specify the index of the body in whose coordinate system the hinge stiffness/damping values are defined
     - \-
     - \-
     - \-
   * - unit
     - The user may specify the unit used for the hinge spring/damper (N/kN)
     - kN
     - kN, N
     - \-
   * - checkSameLocation
     - The user may specify the 'checkSameLocation' (boolean) switch. If "true" is selected, then a check is made if the hinge positions on the 2 bodies it connects are the same in the eath-fixed frame of reference. If "false" is selected the check is not made.
     - true
     - \-
     - \-
   * - allowedDistance
     - This is the allowed distance between the two hinge positions.
     - 0.001
     - \-
     - kNms/rad

parJOB
**********

This is the JOB generation parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - System
     - This is the system name for which job script, with adecquated parallelization parameters, will be generated.  If USERDEF is chosen then Hardware\_ inputs can be provided with local Hardware settings. If any of MARIN MARCLUS clusters is chosen then MARIN_Queue and MARIN_NrMaxNodesUse can be provided.
     - USERDEF
     - MARCLUS5,MARCLUS4,MARCLUS3,USERDEF
     - \-
   * - MARCLUS_Queue
     - This is the Cluster queue for MARCLUS MARIN clusters.
     - NORMAL
     - LARGE, NORMAL, SHORT, GPU
     - \-
   * - MARCLUS_NrMaxNodesUse
     - This is the maximun number of computing nodes to be used. Defatult values are MARCLUS5(2/32/6), MARCLUS4(2/10/10) and MARCLUS3(2/2/2) for (LARGE,NORMAL/SHORT) queues respectively.
     - -1
     - \-
     - \-
   * - Hardware_NrThreadNod
     - This is the number of threads available per computing node. If not provided DIFFRAC will check it by itself (default).
     - -1
     - \-
     - \-
   * - Hardware_NrMaxNodes
     - This is the maximun number of computing nodes that can be used.
     - 1
     - \-
     - \-
   * - Hardware_MemPerNode
     - This is the memory available per computing node in Gb. If not provided DIFFRAC will check it by itself (default).
     - -1
     - \-
     - \-
   * - UserDef
     - This is user defined code added after DIFFRACSUITE call on the job file. Limit lenght is 10000 charachters. Windows: batch; Linux: bash.
     - echo "//" end of file "//"
     - \-
     - \-
   * - MemConsumption_A
     - (A+B*NPanels+(C*NPanels)*NPanels)*(NCond*D)
     - 0.1
     - \-
     - \-
   * - MemConsumption_B
     - (A+B*NPanels+(C*NPanels)*NPanels)*(NCond*D)
     - 0.0002
     - \-
     - \-
   * - MemConsumption_C
     - (A+B*NPanels+(C*NPanels)*NPanels)*(NCond*D)
     - 0.0000000055
     - \-
     - \-
   * - MemConsumption_D
     - (A+B*NPanels+(C*NPanels)*NPanels)*(NCond*D)
     - 0.00000001
     - \-
     - \-

parPRIDAB
*************

This is the PRIDAB parameters group. PRIDAB prints hydrodynamic properties to ASCII file.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - waveSlopeCorrection
     - The user may specify whether the response (rotations) must be made non-dimensional using the wave slope
     - false
     - \-
     - \-
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program PRIDAB will be run. If "false" is selected the program PRIDAB is not run.
     - false
     - \-
     - \-
   * - accelerations
     - The user must specify the data to be exported.
     - NONE
     - NONE, WITH GRAVITY CORRECTION, WITHOUT GRAVITY CORRECTION
     - \-
   * - exportAmassDamp
     - The user may specify the 'exportAmassDamp' (boolean) switch. If "true" is selected, then the added mass and damping are exported. If false is selected, then the added mass and damping are not exported.
     - false
     - \-
     - \-
   * - exportWaveForces
     - The user may specify the 'exportWaveForces' (boolean) switch. If "true" is selected, then the wave forces are exported. If false is selected, then the wave forces are not exported.
     - false
     - \-
     - \-
   * - exportResponse
     - The user may specify the 'exportResponse' (boolean) switch. If "true" is selected, then the motion response is exported. If false is selected, then the motion response is not exported.
     - false
     - \-
     - \-
   * - exportRelativeMotions
     - The user may specify the 'exportRelativeMotions' (boolean) switch. If "true" is selected, then the relative motions are exported. If false is selected, then the relative motions are not exported.
     - false
     - \-
     - \-
   * - exportPQ
     - The user may specify the 'exportPQ' (boolean) switch. If "true" is selected, then the P and Q drift force matrices are exported. If false is selected, then the P and Q drift force matrices are not exported.
     - false
     - \-
     - \-
   * - exportMeanDrift
     - The user may specify the 'exportMeanDrift' (boolean) switch. If "true" is selected, then the mean drift forces are exported. If false is selected, then the mean drift forces are not exported.
     - false
     - \-
     - \-
   * - exportPressures
     - The user may specify the 'exportPressures' (boolean) switch. If "true" is selected, then the panel pressures are exported. If false is selected, then the panel pressures are not exported.
     - false
     - \-
     - \-
   * - exportRelmotRef
     - The user may specify the 'exportRelmotRef' (boolean) switch. If "true" is selected, then the relative motions in reference points are exported. If false is selected, then the relative motions in reference points are not exported.
     - false
     - \-
     - \-
   * - exportAbsmotRef
     - The user may specify the 'exportAbsmotRef' (boolean) switch. If "true" is selected, then the absolute motions in reference points are exported. If false is selected, then the absolute motions in reference points are not exported.
     - false
     - \-
     - \-

relativeMotions
=============================

This is the relative motions parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - body1Index
     - The user must specify the index of the first body for relative motion computation.
     - \-
     - \-
     - \-
   * - body2Index
     - The user must specify the index of the second body for relative motion computation.
     - \-
     - \-
     - \-
   * - apply
     - The user may specify the 'apply' (boolean) switch. If "true" is selected, then the relative motions are computed. If false is selected, then relative motions are not computed.
     - false
     - \-
     - \-

subset
====================

This is the subSet parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - option
     - The user must specify the identity of the subset
     - \-
     - frequency, waterDepth, waveDirection, bodyIndex
     - \-
   * - relation
     - The user must specify the relation operator
     - \-
     - ==, <>, >, <, =< =>
     - \-
   * - value
     - The user must specify the value for relation check
     - \-
     - \-
     - \-
   * - logicalOperator
     - The user must specify the logical operator
     - \-
     - &, , ||
     - \-

printHydFile
==========================

This is the printHydFile parameters group. printHydFile generates the hydrodynamic database (hyd-file).

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - includeAddDamping
     - The user may specify the 'includeAddDamping' (boolean) switch. If "true" is selected, then the additional damping from DBRESP (if any) will be added to the potential damping and written to the hyd-file. If "false" is selected then only the potential damping is written to the hyd-file.
     - false
     - \-
     - \-
   * - includeIncWaveForces
     - The user may specify the 'includeIncWaveForces' (boolean) switch. If "true" is selected, then the forces due to the incoming wave are included in the hyd-file (FAMP, FEPS RECORDS). If "false" is selected then the forces due to the incoming wave are excluded from the hyd-file (only diffraction forces remain). This should be done when incoming wave forces are computed by other means (i.e. Froude Krylov option in aNySIM).
     - true
     - \-
     - \-

parDBDRIFT
**************

This is the DBDRIFT parameters group. DBDRIFT computes the mean wave drift forces by means of pressure integration and by means of the Faltinsen-Michelsen method.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program DBDRIFT will be run. If "false" is selected the program DBDRIFT is not run.
     - false
     - \-
     - \-
   * - exportPressuresAndVelocities
     - The user may specify the 'exportPressuresAndVelocities' (boolean) switch. If "true" is selected, then the wave pressures and velocities are exported. If false is selected, then the wave pressures and velocities are not exported.
     - false
     - \-
     - \-
   * - exportContribution1
     - The user may specify the 'exportContribution1' (boolean) switch. If "true" is selected, then contribution 1 (due relative wave elevation on the waterline) of the drift forces is exported. If false is selected, then contribution 1 is not exported.
     - false
     - \-
     - \-
   * - exportContribution2
     - The user may specify the 'exportContribution2' (boolean) switch. If "true" is selected, then contribution 2 (due to square of water velocities on the hull) of the drift forces is exported. If false is selected, then contribution 2 is not exported.
     - false
     - \-
     - \-
   * - exportContribution3
     - The user may specify the 'exportContribution3' (boolean) switch. If "true" is selected, then contribution 3 (due to rotation of first-order forces) of the drift forces is exported. If false is selected, then contribution 3 is not exported.
     - false
     - \-
     - \-
   * - exportContribution4
     - The user may specify the 'exportContribution4' (boolean) switch. If "true" is selected, then contribution 4 (due to motion times pressure gradient) of the drift forces is exported. If false is selected, then contribution 4 is not exported.
     - false
     - \-
     - \-

subset
=====================

This is the subSet parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - option
     - The user must specify the identity of the subset
     - \-
     - frequency, waterDepth, waveDirection, bodyIndex
     - \-
   * - relation
     - The user must specify the relation operator
     - \-
     - ==, <>, >, <, =< =>
     - \-
   * - value
     - The user must specify the value for relation check
     - \-
     - \-
     - \-
   * - logicalOperator
     - The user must specify the logical operator
     - \-
     - &, , ||
     - \-

parDRIFTP
*************

This is the DRIFTP parameters group. DRIFTP computes the transfer function for the mean and low-frequency varying drift forces by means of pressure integration.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program DRIFTP will be run. If "false" is selected the program DRIFTP is not run.
     - false
     - \-
     - \-
   * - excludeFroudeKrylovAndHydrostatics
     - The user may specify the 'excludeFroudeKrylovAndHydrostatics' (boolean) switch. If "true" is selected, then the Froude-Krylov and hydrostatic forces are not included in the drift force computation. If "false" is selected then they are included.
     - false
     - \-
     - \-
   * - exportContribution1
     - The user may specify the 'exportContribution1' (boolean) switch. If "true" is selected, then contribution 1 (due relative wave elevation on the waterline) of the drift forces is exported. If false is selected, then contribution 1 is not exported.
     - true
     - \-
     - \-
   * - exportContribution2
     - The user may specify the 'exportContribution2' (boolean) switch. If "true" is selected, then contribution 2 (due to square of water velocities on the hull) of the drift forces is exported. If false is selected, then contribution 2 is not exported.
     - true
     - \-
     - \-
   * - exportContribution3
     - The user may specify the 'exportContribution3' (boolean) switch. If "true" is selected, then contribution 3 (due to rotation of first-order forces) of the drift forces is exported. If false is selected, then contribution 3 is not exported.
     - true
     - \-
     - \-
   * - exportContribution4
     - The user may specify the 'exportContribution4' (boolean) switch. If "true" is selected, then contribution 4 (due to motion times pressure gradient) of the drift forces is exported. If false is selected, then contribution 4 is not exported.
     - true
     - \-
     - \-
   * - exportContribution5
     - The user may specify the 'exportContribution5' (boolean) switch. If "true" is selected, then contribution 5 (due to 2nd order wave, or setdown) of the drift forces is exported. If false is selected, then contribution 5 is not exported.
     - true
     - \-
     - \-
   * - minFrequency
     - The user must specify the minimum frequency at which the wave drift forces are computed.
     - \-
     - \-
     - rad/s
   * - maxFrequency
     - The user must specify the maximum frequency at which the wave drift forces are computed.
     - \-
     - \-
     - rad/s
   * - numberOfWavefrequencyDiagonals
     - The user must specify the number of diagonals of the wave drift force matrix that have to be computed.
     - \-
     - \-
     - rad/s
   * - waveDirInteraction
     - The user may specify the 'waveDirInteraction' (boolean) switch. If "true" is selected, then the wave drift forces due to interaction between wave directions will be computed. If "false" they are not computed. Make sure to specify 'numberOfWavedirectionDiagonals' as well
     - false
     - \-
     - \-
   * - numberOfWavedirectionDiagonals
     - The user may specify the number of wave direction diagonals of the wave drift force matrix (4D QTF) that have to computed.
     - 1
     - \-
     - \-
   * - FaltinsenMichelsen
     - The user may specify the 'FaltinsenMichelsen' (boolean) switch. If "true" is selected, then (in addition to direct pressure integration) the mean wave drift forces will also be computed with the method of FaltinsenMichelsen. If "false" is selected they are not computed.
     - false
     - \-
     - \-
   * - CPU_RAM_priority
     - The user may specify the method to compute the wave drift forces, either fast but memory intensive (CPU_priority) or slower but memory-saving (RAM_priority)
     - RAM_priority
     - CPU_priority, RAM_priority
     - \-
   * - exportQTFtoVTK
     - The user may specify the 'exportQTFtoVTK' (boolean) switch. If "true" is selected, then the mean drift force QTF (all 6 modes) on each body is exported to a vtk file (one file per frequency) for visualisation. If "false" is selected the the QTF is not exported.
     - false
     - \-
     - \-

parSUMFREQUENCYWAVEFORCES
*****************************

This is the SUMFREQUENCYWAVEFORCES parameters group. SUMFREQUENCYWAVEFORCES computes the transfer function for the 2nd order sum-frequency wave forces.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program DRIFTP will be run. If "false" is selected the program DRIFTP is not run.
     - false
     - \-
     - \-
   * - exportContribution1
     - The user may specify the 'exportContribution1' (boolean) switch. If "true" is selected, then contribution 1 (due relative wave elevation on the waterline) of the drift forces is exported. If false is selected, then contribution 1 is not exported.
     - true
     - \-
     - \-
   * - exportContribution2
     - The user may specify the 'exportContribution2' (boolean) switch. If "true" is selected, then contribution 2 (due to square of water velocities on the hull) of the drift forces is exported. If false is selected, then contribution 2 is not exported.
     - true
     - \-
     - \-
   * - exportContribution3
     - The user may specify the 'exportContribution3' (boolean) switch. If "true" is selected, then contribution 3 (due to rotation of first-order forces) of the drift forces is exported. If false is selected, then contribution 3 is not exported.
     - true
     - \-
     - \-
   * - exportContribution4
     - The user may specify the 'exportContribution4' (boolean) switch. If "true" is selected, then contribution 4 (due to motion times pressure gradient) of the drift forces is exported. If false is selected, then contribution 4 is not exported.
     - true
     - \-
     - \-
   * - exportContribution5
     - The user may specify the 'exportContribution5' (boolean) switch. If "true" is selected, then contribution 5 (due to 2nd order wave, or setdown) of the drift forces is exported. If false is selected, then contribution 5 is not exported.
     - true
     - \-
     - \-
   * - minFrequency
     - The user must specify the minimum frequency at which the wave drift forces are computed.
     - \-
     - \-
     - rad/s
   * - maxFrequency
     - The user must specify the maximum frequency at which the wave drift forces are computed.
     - \-
     - \-
     - rad/s
   * - maxDiffDir
     - The user must specify the maximum difference direction of the waves at which the 2nd order wave forces are computed. A difference direction of 0 degrees means that no wave direction interaction is considered.
     - \-
     - \-
     - deg

parEXPORT
*************

This is the EXPORT parameters group. EXPORT exports hydrodynamic properties to ASCII file, including the hyd-file.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program EXPORT will be run. If "false" is selected the program EXPORT is not run.
     - false
     - \-
     - \-
   * - includeAddDamping
     - The user may specify the 'includeAddDamping' (boolean) switch. If "true" is selected, then the additional damping from DBRESP (if any) will be added to the potential damping and exported to hyd/h5m file. If "false" is selected then only the potential damping is exported to hyd/h5m file.
     - false
     - \-
     - \-
   * - monitorResponseAtCoG
     - The user may specify the 'monitorResponseAtCoG' (boolean) switch. If "true" is selected, then the motions at the CoG of all bodies are exported to h5m. If false is selected these motions are not exported to h5m.
     - true
     - \-
     - \-
   * - monitorRelativeWaveHeightAtWaterline
     - The user may specify the 'monitorRelativeWaveAtWaterline' (boolean) switch. If "true" is selected, then the relative wave height at all waterline points is exported. If false is selected the relative wave height is not exported.
     - false
     - \-
     - \-
   * - monitorHingeForces
     - The user may specify the 'monitorHingeForces' (boolean) switch. If "true" is selected, then the hinge forces (defined in DBRESP) are exported. If false is selected the hinge forces are not exported.
     - false
     - \-
     - \-
   * - monitorWaveForcesAtCoG
     - The user may specify the 'monitorWaveForcesAtCoG' (boolean) switch. If "true" is selected, then the 1st order wave forces at the CoG of all bodies are exported to h5m. If false is selected the wave forces are not exported to h5m.
     - true
     - \-
     - \-
   * - monitorDriftForcesAtCoG
     - The user may specify the 'monitorDriftForcesAtCoG' (boolean) switch. If "true" is selected, then the wave drift forces at the CoG of all bodies are exported to h5m. If false is selected the wave drift forces are not exported to h5m.
     - true
     - \-
     - \-
   * - monitorAmassDampAtCoG
     - The user may specify the 'monitorAmassDampAtCoG' (boolean) switch. If "true" is selected, then the added mass and damping at the CoG of all bodies are exported to h5m. If false is selected the added mass and damping are not exported to h5m.
     - true
     - \-
     - \-
   * - ASCII
     - The user may specify the 'ASCII' (boolean) switch. If "true" is selected, then the monitor results are exported to ASCII file. If "false" is selected, then the monitor results are not exported to ASCII file
     - false
     - \-
     - \-
   * - monitorTurbineFlowRate
     - The user may specify the 'monitorTurbineFlowRate' (boolean) switch. If "true" is selected, then the flow rate of turbines (if present) are exported. If "false" is selected the turbine flow rate is not exported
     - false
     - \-
     - \-

CGNS
==================

This is the CGNS parameters group. CGNS specifies the export options for the CGNS files.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - export
     - The user must specify the 'export' (boolean) switch. If "true" is selected, then CGNS files are generated. If "false" is selected then these files are not generated.
     - false
     - \-
     - \-
   * - numberOfTimeSteps
     - The user must specify the number of time steps for the export of the CGNS files.
     - 10
     - \-
     - \-
   * - movingBodies
     - The user must specify the 'movingBodies' (boolean) switch. If "true" is selected, then the bodies are moving in the CGNS visualisation files. If "false" is selected then the bodies are not moving.
     - false
     - \-
     - \-
   * - movingFreeSurface
     - The user must specify the 'movingFreeSurface' (boolean) switch. If "true" is selected, then the free surface is moving in the CGNS visualisation files. If "false" is selected then the free surface is not moving.
     - false
     - \-
     - \-
   * - forcedMotion
     - The user may specify the 'forcedMotion' (boolean) switch. If "true" is selected, then the cgns files with forced motion results are exported, otherwise not.
     - true
     - \-
     - \-
   * - waveAmplificationFactor
     - The user may specify the wave amplification factor. Wave kinematics and body motions are multiplied by this factor before exporting to CGNS
     - 1.
     - \-
     - \-
   * - waveFreq
     - The user must specify the wave frequency/frequencies in comma-bracket format, e.g. "0.2,0.4,0.6,0.8,2.0" or "0.2(0.2)0.8,2.0" (without quotation marks).
     - \-
     - \-
     - \-
   * - waveDir
     - The user must specify the wave direction/directions in comma-bracket format, e.g. "0,10,20,30,40,50,90" or "0(10)50,180" (without quotation marks).
     - \-
     - \-
     - \-
   * - unitMotion
     - The user may specify the unit motion in metres for the forced oscillation visualisation
     - 1.
     - \-
     - \-
   * - unitRotation
     - The user may specify the unit rotation in degrees for the forced oscillation visualisation
     - 1.
     - \-
     - deg

MonitorFlowData
----------------------------------

This is the MonitorFlowData group.

grid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the grid parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - spacing_x
     - This is the grid spacing (distance between the points) in x-direction.
     - \-
     - \-
     - m
   * - spacing_y
     - This is the grid spacing (distance between the points) in y-direction.
     - \-
     - \-
     - m
   * - NrOfPointsX
     - This is the number of grid points in x-direction. The number should be odd.
     - \-
     - \-
     - \-
   * - origin
     - This is the origin (x,y,z) of the grid. z=0 corresponds to the free surface
     - \-
     - \-
     - m,m,m
   * - orientation
     - This is the orientation of the grid in degrees.
     - 0.0
     - \-
     - deg
   * - NrOfPointsY
     - This is the number of grid points in y-direction. The number should be odd.
     - \-
     - \-
     - \-

MonitorFloaterData
================================

This is the MonitorFloaterData group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - bodyIndex
     - The user must specify the index of the body
     - \-
     - \-
     - \-
   * - acceleration
     - The user may specify the 'acceleration' (boolean) switch. If "true" is selected, then the acceleration response is exported. If false is selected, then the acceleration response is not exported.
     - false
     - \-
     - \-
   * - waveForces
     - The user may specify the 'waveForces' (boolean) switch. If "true" is selected, then the wave forces are exported. If false is selected, then the wave forces are not exported.
     - false
     - \-
     - \-
   * - meanDriftForces
     - The user may specify the 'meanDriftForces' (boolean) switch. If "true" is selected, then the body meanDriftForces are exported. If false is selected, then the body meanDriftForces are not exported.
     - false
     - \-
     - \-
   * - PQ
     - The user may specify the 'PQ' (boolean) switch. If "true" is selected, then the P and Q drift force matrices are exported. If false is selected, then the P and Q drift force matrices are not exported.
     - false
     - \-
     - \-
   * - waveSlopeCorrection
     - The user may specify whether the response (rotations) must be made non-dimensional using the wave slope
     - false
     - \-
     - \-
   * - name
     - The user must specify the name of the monitor, used for storing on h5m and for the ASCII filename
     - \-
     - \-
     - \-
   * - posWrtKeel
     - The user must specify the coordinates (x,y,z, in CSV format) of the point with respect to the origing of the body mesh file (x,y) and wrt keel (z).
     - \-
     - \-
     - m,m,m
   * - velocity
     - The user may specify the 'velocity' (boolean) switch. If "true" is selected, then the velocity response is exported. If false is selected, then the velocity response is not exported.
     - false
     - \-
     - \-
   * - relativeVelocity
     - The user may specify the 'relativeVelocity' (boolean) switch (motion induced velocity minus water velocity). If "true" is selected, then the relative velocity response is exported. If false is selected, then the relative velocity response is not exported.
     - false
     - \-
     - \-
   * - motion
     - The user may specify the 'motion' (boolean) switch. If "true" is selected, then the motion response is exported. If false is selected, then the motion response is not exported.
     - false
     - \-
     - \-
   * - accelerationType
     - The user may specify the method for computing the acceleration: SHIP-FIXED (INCLUDING GRAVITY CORRECTION); EARTH-FIXED (EXCLUDING GRAVITY CORRECTION);
     - SHIP-FIXED (INCLUDING GRAVITY CORRECTION)
     - SHIP-FIXED (INCLUDING GRAVITY CORRECTION), EARTH-FIXED (EXCLUDING GRAVITY CORRECTION)
     - \-
   * - addedMassDamping
     - The user may specify the 'addedMassDamping' (boolean) switch. If "true" is selected, then the added mass and damping is exported. If false is selected, then the added mass and damping is not exported.
     - false
     - \-
     - \-
   * - naturalFrequency
     - The user may specify the 'naturalFrequency' (boolean) switch. If "true" is selected, then the naturalFrequencies are exported (coupled and uncoupled). If false is selected, then the naturalFrequencies are not exported.
     - false
     - \-
     - \-

MonitorRelativeMotion
===================================

This is the MonitorRelativeMotion group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - name
     - The user must specify the name of the monitor, used for storing on h5m and for the ASCII filename
     - \-
     - \-
     - \-

relMotionBodyInput
------------------------------------------------------

This is the input for a single body to compute relative motions or wave heights.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - index
     - The user must specify the index of the body
     - \-
     - \-
     - \-

referencePoint
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the referencePoint parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - coordinate
     - This is the coordinate (x,y,z) of the reference point.
     - \-
     - \-
     - m,m,m

MonitorInternalLoad
=================================

This is the MonitorInternalLoad group.

cut
-------------------------------------

cut

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - index
     - The user must specify the index of the body in which the cut is located.
     - \-
     - \-
     - \-
   * - posWrtKeel
     - The user must specify the coordinates (x,y,z, in CSV format) of the cut position with respect to the origing of the body mesh file (x,y) and wrt keel (z).
     - \-
     - \-
     - m,m,m
   * - normal
     - The user may specify the cut normal vector which defines the longitudinal direction of the cut.
     - 1.,0.,0.
     - \-
     - \-
   * - trvsTangent
     - The user may specify the cut transverse tangent vector which defines the transverse direction of the cut.
     - 0.,1.,0.
     - \-
     - \-
   * - name
     - The user must specify the name of the monitor, used for storing on h5m and for the ASCII filename
     - \-
     - \-
     - \-
   * - referenceSystem
     - The user may specify the reference system for calculating the internal loads: SHIP-FIXED; CUT-FIXED;
     - CUT-FIXED
     - SHIP-FIXED, CUT-FIXED
     - \-

hydFile
=====================

This is the exportHydFile parameters group. exportHydFile generates the hydrodynamic database (hyd-file).

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - maxWavefrequency
     - The user may specify the maximum wave frequency for export to hyd-file of 1st order results.
     - -1.0
     - \-
     - \-
   * - numberOfWavefrequencyDiagonals
     - The user may specify the number of wave frequency diagonals of the wave drift force matrix that have to exported to the hyd-file.
     - -1
     - \-
     - \-
   * - includeIncWaveForces
     - The user may specify the 'includeIncWaveForces' (boolean) switch. If "true" is selected, then the forces due to the incoming wave are included in the hyd-file (FAMP, FEPS RECORDS). If "false" is selected then the forces due to the incoming wave are excluded from the hyd-file (only diffraction forces remain). This should be done when incoming wave forces are computed by other means (i.e. Froude Krylov option in aNySIM).
     - true
     - \-
     - \-
   * - exportQTFContribution1
     - The user may specify the 'exportQTFContribution1' (boolean) switch. If "true" is selected, then QTF contribution 1 (due relative wave elevation on the waterline) of the drift forces is exported to the hyd-file. If false is selected, then contribution 1 is not exported to the hyd-file.
     - true
     - \-
     - \-
   * - exportQTFContribution2
     - The user may specify the 'exportQTFContribution2' (boolean) switch. If "true" is selected, then QTF contribution 2 (due to square of water velocities) of the drift forces is exported to the hyd-file. If false is selected, then contribution 2 is not exported to the hyd-file.
     - true
     - \-
     - \-
   * - exportQTFContribution3
     - The user may specify the 'exportQTFContribution1' (boolean) switch. If "true" is selected, then QTF contribution 3 (due to motion times pressure gradient) of the drift forces is exported to the hyd-file. If false is selected, then contribution 3 is not exported to the hyd-file.
     - true
     - \-
     - \-
   * - exportQTFContribution4
     - The user may specify the 'exportQTFContribution4' (boolean) switch. If "true" is selected, then QTF contribution 4 (due to rotation of first-order forces) of the drift forces is exported to the hyd-file. If false is selected, then contribution 4 is not exported to the hyd-file.
     - true
     - \-
     - \-
   * - exportQTFContribution5
     - The user may specify the 'exportQTFContribution5' (boolean) switch. If "true" is selected, then QTF contribution 5 (due to wave setdown) of the drift forces is exported to the hyd-file. If false is selected, then contribution 5 is not exported to the hyd-file.
     - true
     - \-
     - \-
   * - excludeGhostForces
     - This is the 'excludeGhostForces' (boolean) switch. If "true", then the second-order forces due to the wave phase correction of the first-order wave excitation forces is excluded (to avoid double-count in aNySIM). If "false" then this term is not included.
     - false
     - \-
     - \-
   * - name
     - The user may specify the name of the hyd-file without extension. Otherwise the database name is used.
     - NOT SPECIFIED
     - \-
     - \-
   * - export
     - The user must specify the 'export' (boolean) switch. If "true" is selected, then the hyd-file is exported. If "false" is selected then this file is not exported.
     - true
     - \-
     - \-
   * - numberOfWavedirectionDiagonals
     - The user may specify the number of wave direction diagonals of the wave drift force matrix (4D QTF) that have to exported to the hyd-file.
     - 0
     - \-
     - \-
   * - bodyToExclude
     - The user may specify the indices of the bodies that must be excluded from the hyd-file in comma-bracket format, e.g. "2,4" or "2(2)4" (without quotation marks).
     - NOT SPECIFIED
     - \-
     - \-
   * - refPointSegmentHydFile
     - The user may specify the reference point for the hyd-files of the segments (defined by internal load cuts)
     - SEGMENTCOG
     - SEGMENTCOG, BODYCOG
     - \-

MonitorRelativeWaveHeight
=======================================

This is the MonitorRelativeMotion group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - name
     - The user must specify the name of the monitor, used for storing on h5m and for the ASCII filename
     - \-
     - \-
     - \-
   * - includeIncidentWave
     - The user may specify the 'includeIncidentWave' (boolean) switch. If "true" is selected, then the incident wave is included. If "false" is selected the incident wave is not included.
     - true
     - \-
     - \-
   * - includeDiffractedWave
     - The user may specify the 'includeDiffractedWave' (boolean) switch. If "true" is selected, then the diffracted wave is included. If "false" is selected the diffracted wave is not included.
     - true
     - \-
     - \-
   * - includeRadiatedWave
     - The user may specify the 'includeRadiatedWave' (boolean) switch. If "true" is selected, then the radiated wave is included. If "false" is selected the radiated wave is not included.
     - true
     - \-
     - \-
   * - includeMotions
     - The user may specify the 'includeMotions' (boolean) switch. If "true" is selected, then the vertical motions are included. If "false" is selected the vertical motions ar not included.
     - true
     - \-
     - \-

relWaveHeightBodyInput
--------------------------------------------------------------

This is the input for a single body to compute relative wave heights.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - index
     - The user must specify the index of the body
     - \-
     - \-
     - \-

referencePoint2D
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the referencePoint2D parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - coordinate
     - This is the coordinate (x,y) of the 2D reference point.
     - \-
     - \-
     - m,m

RAODB
===================

This is the RAODB parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - name
     - The user may specify the name of the RAODB-file without extension. Otherwise the database name is used.
     - \-
     - \-
     - \-
   * - export
     - The user must specify the 'export' (boolean) switch. If "true" is selected, then the a RAODB.ini file is generated. If "false" is selected then this file is not generated.
     - true
     - \-
     - \-
   * - DBRESPresponse
     - The user may specify the 'DBRESPresponse' (boolean) switch. If "true" is selected, then the responses computed by DBRESP are exported, with possible modifications to weight distribution, spring and damping. If "false" is selected, then the responses originally computed by DIFFRAC are exported (with INIDIF spring, original weight distribution and potential damping only)
     - true
     - \-
     - \-

H5M
=================

This is the H5M parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - name
     - The user may specify the name of the H5M-file without extension. Otherwise the database name is used.
     - NOT SPECIFIED
     - \-
     - \-
   * - export
     - The user must specify the 'export' (boolean) switch. If "true" is selected, then the a h5m file is generated. If "false" is selected then this file is not generated.
     - true
     - \-
     - \-
   * - exportQTFContribution1
     - The user may specify the 'exportQTFContribution1' (boolean) switch. If "true" is selected, then QTF contribution 1 (due relative wave elevation on the waterline) of the drift forces is exported to the h5m-file. If false is selected, then contribution 1 is not exported to the h5m-file.
     - true
     - \-
     - \-
   * - exportQTFContribution2
     - The user may specify the 'exportQTFContribution2' (boolean) switch. If "true" is selected, then QTF contribution 2 (due to square of water velocities) of the drift forces is exported to the h5m-file. If false is selected, then contribution 2 is not exported to the h5m-file.
     - true
     - \-
     - \-
   * - exportQTFContribution3
     - The user may specify the 'exportQTFContribution1' (boolean) switch. If "true" is selected, then QTF contribution 3 (due to motion times pressure gradient) of the drift forces is exported to the h5m-file. If false is selected, then contribution 3 is not exported to the h5m-file.
     - true
     - \-
     - \-
   * - exportQTFContribution4
     - The user may specify the 'exportQTFContribution4' (boolean) switch. If "true" is selected, then QTF contribution 4 (due to rotation of first-order forces) of the drift forces is exported to the h5m-file. If false is selected, then contribution 4 is not exported to the h5m-file.
     - true
     - \-
     - \-
   * - exportQTFContribution5
     - The user may specify the 'exportQTFContribution5' (boolean) switch. If "true" is selected, then QTF contribution 5 (due to wave setdown) of the drift forces is exported to the h5m-file. If false is selected, then contribution 5 is not exported to the h5m-file.
     - true
     - \-
     - \-

dryModes
======================

This is the exportDryModes parameters group. exportDryModes specifies the export options for the dry natural eigenmodes.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - export
     - The user must specify the 'export' (boolean) switch. If "true" is selected, then the a vtk file with the dry natural modes is generated. If "false" is selected then this file is not generated.
     - false
     - \-
     - \-
   * - maxFrequency
     - The user may specify the maximum frequency for the export of the natural modes.
     - \-
     - \-
     - \-
   * - minFrequency
     - The user may specify the minimum frequency for the export of the natural modes.
     - \-
     - \-
     - \-
   * - includeHydroStiffness
     - The user may specify the 'includeHydroStiffness' (boolean) switch. If "true" is selected, then the hydrostatic stiffness is included in the computing the modes.
     - false
     - \-
     - \-
   * - exportRigidOnly
     - The user may specify the 'exportRigidOnly' (boolean) switch. If "true" is selected, then only the rigid body motions of the comboned system are exported as modes.
     - false
     - \-
     - \-

body
********

body

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - index
     - The user must specify the index of the body
     - \-
     - \-
     - \-
   * - isTransparant
     - The user may specify the 'isTransparant' (boolean) switch. If "true" is selected, then the body will be transparant to incoming waves. If "false" is selected then the body is not transparant to incoming waves.
     - false
     - \-
     - \-
   * - name
     - The user may specify the name of the body.
     - \-
     - \-
     - \-
   * - isFixed
     - The user may specify the 'isFixed' (boolean) switch. If "true" is selected, then the body is fixed and cannot move. If "false" is selected, then the body is not fixed and can move.
     - false
     - \-
     - \-
   * - checkDisplacement
     - The user may specify the 'checkDisplacement' (boolean) switch. If "true" is selected, then the sign of the displacement is checked. If "false" is selected the sign of the displacement is not checked. A wrong sign is an indication of a wrong normal direction (only for closed bodies). (default=true)
     - true
     - \-
     - \-

mesh
=============

This is the body mesh parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - meshFn
     - The user must specify the name of the VTK file (including extension) which contains the hydrodynamic mesh.
     - \-
     - \-
     - \-
   * - invertNormals
     - The user may specify the 'invertNormals' (boolean) switch. If "true" is selected, then the normal direction of the panels will be inverted.
     - false
     - \-
     - \-
   * - checkClosedWaterLine
     - The user must specify the 'checkClosedWaterLine' (boolean) switch. If "true" is selected, then it will be checked if the waterline is closed (important for consistent drift forces). If "false" is selected then the check is not made.
     - true
     - \-
     - \-
   * - scaleFactorX
     - Scale factor X direction
     - 1.0
     - \-
     - \-
   * - scaleFactorY
     - Scale factor Y direction
     - 1.0
     - \-
     - \-
   * - scaleFactorZ
     - Scale factor Z direction
     - 1.0
     - \-
     - \-

position
=================

The position (x,y) of the body origin and the rotation around the origin.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - translation
     - The user may specify the translation (x,y,z) of the body origin
     - 0.,0.,0.
     - \-
     - m,m
   * - rotation
     - The user may specify the yaw rotation of the body around its origin (0,0,0) in the mesh file.
     - 0.
     - \-
     - deg
   * - rotationOrigin
     - The user may specify the rotation origin (x,y) with respect to the origin of the mesh file
     - 0.,0.
     - \-
     - m,m

massElement
====================

This is the body inertial properties group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - COGwrtKeel
     - This is the center of gravity of the mass element. X and Y  (horizontal) with respect to the origin of the mesh. Z (vertical) with respect to the keel. (SI dimension = m, m, m).
     - \-
     - \-
     - m,m,m
   * - mass
     - This is mass of the mass element.
     - \-
     - \-
     - tons
   * - rollRadiusGyr
     - The user must specify the roll radius of gyration of the mass element (k_xx). Defined with respect to the mass element center of gravity
     - \-
     - \-
     - m
   * - pitchRadiusGyr
     - The user must specify the pitch radius of gyration of the mass element (k_yy). Defined with respect to the mass element center of gravity
     - \-
     - \-
     - m
   * - yawRadiusGyr
     - The user must specify the yaw radius of gyration of the mass element (k_zz). Defined with respect to the mass element center of gravity
     - \-
     - \-
     - m
   * - rollPitchRadiusGyr
     - This is the body roll-pitch radius of gyration. (k_xy)
     - 0
     - \-
     - m
   * - rollYawRadiusGyr
     - This is the body roll-yaw radius of gyration. (k_xz)
     - 0
     - \-
     - m
   * - pitchYawRadiusGyr
     - This is the body pitch-yaw radius of gyration. (k_yz)
     - 0
     - \-
     - m

hstat
==============

This is the body hydrostatic properties group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - checkEqual_CoB_CoG
     - The user may specify the 'checkEqual_CoB_CoG' (boolean) switch. If "true" is selected, then a check is made on equal COB and COG in the horizontal plane. If "false" is selected the check is not made.
     - true
     - \-
     - \-
   * - lengthBetweenPerp
     - The user must specify the body length between perpendiculars (L_pp).
     - \-
     - \-
     - m
   * - beam
     - The user must specify the beam (width) of the body (B).
     - 0.0
     - \-
     - m
   * - draft
     - The user must specifiy the draft. This is the draft at the location of the center of gravity.
     - \-
     - \-
     - m

parDBSNELH
**************

This is the DBSNELH parameters group. DBSNELH makes a forward speed correction to the hydrodynamic coefficients and can export kinematics in reference points.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program DBSNELH will be run. If "false" is selected the program DBSNELH is not run.
     - false
     - \-
     - \-
   * - exportRefPointKinematics
     - The user may specify the 'exportRefPointKinematics' (boolean) switch. If "true" is selected, then the kinematics (velocities, pressures) in reference points are exported. If "false" is selected then the kinematics are not exported.
     - false
     - \-
     - \-
   * - useHaskindRelation
     - The user may specify the 'useHaskindRelation' (boolean) switch. If "true" is selected, then the haskind relation is used to compute the wave forces. If "false" is selected then the haskind relation is not used.
     - false
     - \-
     - \-
   * - calcGreenWaterRAO
     - The user may specify the 'calcGreenWaterRAO' (boolean) switch. If "true" is selected, then green water RAOs are computed and stored in *.wav files. If "false" is selected then Green water RAOs are not computed.
     - false
     - \-
     - \-
   * - speed
     - The user may specify the speed(s) in m/s in comma-bracket format, e.g. "0,2,4,6,12" or "0(2)6,12" (without quotation marks). Maximum 7 speeds are allowed.
     - 0.
     - \-
     - m/s

referencePoint
=============================

This is the referencePoint parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - coordinate
     - This is the coordinate (x,y,z) of the reference point.
     - \-
     - \-
     - m,m,m

parDBG
**********

This is the DEBUG parameters group.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - checkHDF5
     - This is the boolean switch (true/1 or false/0) for checking calls to hdf5 functions.
     - false
     - \-
     - \-
   * - checkSolverNaNInfVal
     - The user may specify the boolean switch (true/1 or false/0) to activate NaN and Inf check for values passed to the solver. Note: this will increase running time considerably and its use is only meant for verifying system matrix on fast jobs with a few input conditions. In case NaN or Inf value elements are passed to the solver DIFFRAC will stops.
     - false
     - \-
     - \-
   * - checkMem
     - This is the boolean switch (true/1 or false/0) for exporting memory usage footprint (run-time monitor of /proc/procid/status) on Linux.
     - false
     - \-
     - \-
   * - checkMPIBarrier
     - This is the boolean switch (true/1 or false/0) for checking MPI Barrier calls.
     - false
     - \-
     - \-
   * - timerMPI
     - This is the boolean switch (true/1 or false/0) for checking MPI timers.
     - false
     - \-
     - \-

