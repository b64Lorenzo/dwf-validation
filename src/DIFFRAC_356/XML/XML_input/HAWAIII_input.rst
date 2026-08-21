*********************
Reference user manual
*********************

sim
###

This is the simulation, the top object in HAWAIII.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - nProcs
     - The user may specify the number of openMP processors. Negative number means HAWAIII decides the optimum value.
     - -1
     - \-
     - \-

parHAWAIII
**************

This is the HAWAIII parameters group. HAWAIII computes the first and second-order wave forces on a single or multi-body system due to waves from an external wave model.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - applyWall
     - The user may specify the 'applyWall' (boolean) switch. If "true" is selected, then a wall boundary condition will be applied at y=yWall. If "false" is selected the boundary condition is not applied.
     - false
     - \-
     - \-
   * - yWall
     - This is y-coordinate of the wall in the global earth-fixed coordinate system.
     - 0
     - \-
     - m
   * - waterDepth
     - The user must specify the constant water depth.
     - \-
     - \-
     - m
   * - tukeyRatio
     - The user may specify the tukey Ratio which is the ratio of the length of taper section to the total length of the window.
     - 0.5
     - \-
     - \-
   * - overlapRatio
     - The user may specify the overlap Ratio which is the ratio of the length of the overlapping part of adjacent windows to the total length of the window.
     - 0.75
     - \-
     - \-
   * - gravity
     - The user may specify the acceleration of gravity.
     - 9.81
     - \-
     - m/s^2
   * - windowLength
     - The user must specify the length of the time window for the Fourier Analysis of the wave kinematics time traces (at least 2.25 times as large as the longest period of interest, i.e. natural period of the moored system).
     - \-
     - \-
     - s
   * - timeStep
     - The user must specify the time step for the Fourier Analysis of the wave kinematics time traces (smaller than the shortest period of interest).
     - \-
     - \-
     - s
   * - maxSimulTime
     - The user may specify the maximum simulation time (should be smaller or equal to the wave model simulation time).
     - -1
     - \-
     - s
   * - maxDifferenceFrequency
     - The user may specify the maximum difference frequency for the 2nd order wave forces. It should be chosen larger than the largest natural frequency of interest.
     - 0.3
     - \-
     - rad/s
   * - runProgram
     - The user must specify the 'run program' (boolean) switch. If "true" is selected, then the program HAWAIII will be run. If "false" is selected the program HAWAIII is not run.
     - false
     - \-
     - \-
   * - restart
     - The user may specify the 'restart' (boolean) switch. If "true" is selected, then the computation is restarted from the existing output database. If false is selected the computation is started from scratch.
     - false
     - \-
     - \-
   * - onlyFFT
     - The user may specify the 'onlyFFT' (boolean) switch. If "true" is selected, then only the FFTs are determined. If "false" is selected the entire HAWAIII program is run.
     - false
     - \-
     - \-
   * - skipFFT
     - The user may specify the 'skipFFT' (boolean) switch. If "true" is selected, then the FFTs are skipped (assume to be done earlier). If "false" is selected then the FFTs are not skipped.
     - false
     - \-
     - \-
   * - waveKinematicsType
     - The user may specify the type of wave kinematics used for the coupling between wave model and frequency domain analysis. Choose from WAVEMODELDATABASE and INTERPOLATEDVALUES
     - NOT SPECIFIED
     - INTERPOLATEDVALUES, WAVEMODELDATABASE
     - \-
   * - bodyIndexTransparant
     - The user may specify the body index of bodies which are transparant to the incoming wave. These are bodies which were already included in the wave model, e.g. "1,2,4" or "1(1)2,4" (without quotation marks).
     - 0
     - \-
     - \-
   * - dataBaseFn
     - The user may specify the name of the binary database (without extension) on which the hydrodynamic solution and geometry details are stored.
     - HAWAIII
     - \-
     - \-
   * - density
     - This is the water density.
     - 1.0260210
     - \-
     - tons/m^3
   * - estimatePressureGradient
     - The user may specify the 'estimatePressureGradient' (boolean) switch. If "true" is selected, then the pressure gradient is estimated from the velocity time derivative. If "false" is selected the pressure gradient is not estimated. The pressure gradient is needed for the computation of the drift forces. It can also be specified in the wave model database.
     - false
     - \-
     - \-

waveModelDatabase
================================

This is the waveModelDatabase parameters group. It contains parameters that describe the contents of the wave model database.

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - fileName
     - The user must specify the database filename(s) containing the wave model output in comma separated format (i.e. file1.nc,file2.nc). The database is in netcdf or h5 format in accordance to the XBEACH output format or XBEACH 3D modified output.
     - \-
     - \-
     - \-
   * - depthAveragedNormalizedDynamicPressure_varname
     - The user may specify the variable name of the normalized dynamic pressure on the database.
     - pres
     - \-
     - \-
   * - normalizedPressure_varname
     - The user may specify the variable name of the normalized pressure on the database (used for 3D data).
     - p
     - \-
     - \-
   * - bedLevel_varname
     - The user may specify the variable name of the bed level on the database.
     - zb
     - \-
     - \-
   * - waveElevation_varname
     - The user may specify the variable name of the wave elevation on the database.
     - zs
     - \-
     - \-
   * - velocityX_varname
     - The user may specify the variable name of the x-velocity on the database.
     - ue
     - \-
     - \-
   * - velocityY_varname
     - The user may specify the variable name of the y-velocity on the database.
     - ve
     - \-
     - \-
   * - velocityZ_varname
     - The user may specify the variable name of the z-velocity on the database.
     - we
     - \-
     - \-
   * - time_varname
     - The user may specify the variable name of the time on the database.
     - globaltime
     - \-
     - \-
   * - xCoord_varname
     - The user may specify the variable name of the x-coordinate on the database.
     - globalx
     - \-
     - \-
   * - yCoord_varname
     - The user may specify the variable name of the y-coordinate on the database.
     - globaly
     - \-
     - \-
   * - zCoord_varname
     - The user may specify the variable name of the z-coordinate on the database.
     - globalz
     - \-
     - \-
   * - sigma_varname
     - The user may specify the variable name of the sigma-coordinate on the database.
     - sigma
     - \-
     - \-

interpolatedValues
=================================

This is the interpolatedValues parameters group. It contains parameters that describe the contents of the database file with interpolated values (wave kinematics in HAWAIII model points).

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - fileName
     - The user must specify the database filename containing the wave kinematics interpolated on the points required by the HAWAiii tool. The database is in netcdf or h5 format.
     - \-
     - \-
     - \-
   * - pressure_varname
     - The user may specify the variable name of the pressure on the database.
     - p
     - \-
     - \-
   * - pressureGradientX_varname
     - The user may specify the variable name of the pressure gradient in x-direction on the database.
     - gradpx
     - \-
     - \-
   * - pressureGradientY_varname
     - The user may specify the variable name of the pressure gradient in y-direction on the database.
     - gradpy
     - \-
     - \-
   * - pressureGradientZ_varname
     - The user may specify the variable name of the pressure gradient in z-direction on the database.
     - gradpz
     - \-
     - \-
   * - velocityX_varname
     - The user may specify the variable name of the x-velocity on the database.
     - u
     - \-
     - \-
   * - velocityY_varname
     - The user may specify the variable name of the y-velocity on the database.
     - v
     - \-
     - \-
   * - velocityZ_varname
     - The user may specify the variable name of the z-velocity on the database.
     - w
     - \-
     - \-
   * - time_varname
     - The user may specify the variable name of the time on the database.
     - time
     - \-
     - \-
   * - coordinate_varname
     - The user may specify the variable name of the coordinates (x,y,z) on the database.
     - coordinates
     - \-
     - \-

MonitorRelativeWaveHeight
========================================

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
---------------------------------------------------------------

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
   * - solverType
     - The user may specify the solver for the equation of motion matrix: GMRES = Generalized Minimal Residual Method; LU = incomplete lower-upper decomposition method
     - LU
     - GMRES_ILU, LU
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

joint
===================

joint

.. list-table::
   :widths: 25 75 25 25 25
   :header-rows: 1

   * - Property name
     - Description
     - Default value
     - List of possible values
     - Units
   * - name
     - The user may specify the name of the joint.
     - \-
     - \-
     - \-
   * - c11
     - This is the surge stiffness of the joint.
     - 0.
     - \-
     - kN/m
   * - c22
     - This is the sway stiffness of the joint.
     - 0.
     - \-
     - kN/m
   * - c33
     - This is the heave stiffness of the joint.
     - 0.
     - \-
     - kN/m
   * - c44
     - This is the roll stiffness of the joint.
     - 0.
     - \-
     - kNm/rad
   * - c55
     - This is the pitch stiffness of the joint.
     - 0.
     - \-
     - kNm/rad
   * - c66
     - This is the yaw stiffness of the joint.
     - 0.
     - \-
     - kNm/rad
   * - b11
     - This is the surge damping of the joint.
     - 0.
     - \-
     - kNs/m
   * - b22
     - This is the sway damping of the joint.
     - 0.
     - \-
     - kNs/m
   * - b33
     - This is the heave damping of the joint.
     - 0.
     - \-
     - kN/m
   * - b44
     - This is the roll damping of the joint.
     - 0.
     - \-
     - kNms/rad
   * - b55
     - This is the pitch damping of the joint.
     - 0.
     - \-
     - kNms/rad
   * - b66
     - This is the yaw damping of the joint.
     - 0.
     - \-
     - kNms/rad
   * - index1
     - The user must specify the index of the first body the joint is connected to. Index zero means connection to earth.
     - \-
     - \-
     - \-
   * - index2
     - The user must specify the index of the second body the joint is connected to. Index zero means connection to earth.
     - \-
     - \-
     - \-
   * - posWrtKeel1
     - The user must specify the coordinates (x,y,z) of the joint position with respect to the origin of the mesh file (x,y) and wrt keel (z) of the 1st body.
     - \-
     - \-
     - m,m,m
   * - posWrtKeel2
     - The user must specify the coordinates (x,y,z) of the joint position with respect to the origin of the mesh file (x,y) and wrt keel (z) of the 2nd body.
     - \-
     - \-
     - m,m,m
   * - coordSystem
     - The user must specify the index of the body in whose coordinate system the joint stiffness/damping values are defined
     - \-
     - \-
     - \-
   * - unit
     - The user may specify the unit used for the joint spring/damper (N/kN)
     - kN
     - kN, N
     - \-
   * - checkSameLocation
     - The user may specify the 'checkSameLocation' (boolean) switch. If "true" is selected, then a check is made if the joint positions on the 2 bodies it connects are the same in the eath-fixed frame of reference. If "false" is selected the check is not made.
     - true
     - \-
     - \-
   * - allowedDistance
     - This is the allowed distance between the two joint positions.
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

dampingLid
**************

This is the dampingLid parameters group.

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

