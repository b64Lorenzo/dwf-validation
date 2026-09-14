DWF (Diffraction XMF Node Validation)
====================================


Overview
--------

This repository contains the models, configuration files, post-processing scripts, and documentation used for the validation of the Diffraction Wave Field (DWF) XMF node against the VBM implementation.


Requirements
------------

DXNV will run if the following software is installed:

- xSimulation v2025.02 / aNySIM v2025.02.02 or higher
- DIFFRAC v3.5.6 or higher
- Python 3.9 or higher


Repository Structure
--------------------

The repository is organized into three main directories:

### data/

Contains all vessel-specific input data.

Example:

data/
└── LNGC/
    ├── databases/
    ├── geometry/
    └── grids/

- **databases/**: Stores the `.hdm.5` hydrodynamic databases generated with DIFFRAC.
- **geometry/**: Contains the vessel geometry files.
- **grids/**: Contains the panel-grid geometries used in the hydrodynamic analyses.

The `LNGC` folder corresponds to the LNG Carrier used in this validation study. For additional vessels, a new folder should be created following the same structure.


### docs/

Contains the project documentation, including the validation report and supporting materials.

docs/
└── Report/


### src/

Contains all source files and simulation configurations used throughout the project.

src/
├── diffrac356/
├── python/
└── xsimulation202502/

#### diffrac356/

Contains DIFFRAC v3.5.6 template files and example diffraction-node configurations used to generate the hydrodynamic databases.

#### python/

Contains the Python repository used for post-processing, validation, plotting, convergence studies, and result comparisons.

#### xsimulation202502/

Contains all aNySIM/XSimulation configuration files required to run the DWF and VBM simulations.


Running Simulations
-------------------

To run an aNySIM simulation:

1. Navigate to the appropriate simulation directory inside `xsimulation202502`.
2. Open the `simulations` folder.
3. Execute the desired main configuration file.

As a large number of simulations were required for the validation campaign, manually generating all configuration files would have been impractical. For this reason, both the DIFFRAC and aNySIM workflows make use of parameterized configuration templates.

The simulation files were automatically generated using **MultiGen**, a tool developed to create multiple configurations from a single template:

https://github.com/b64Lorenzo/MultiGen.git

Consequently, both the `diffrac356` and `xsimulation202502` directories contain configuration-template files in addition to the generated simulation files.


Author
------

Lorenzo Zambelli