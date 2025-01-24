# ParMOO Solvers: Sample Simulation Optimization Problems and Solvers

This repository contains samples of several multiobjective simulation
optimization (MOSO) problems that have been solved with ParMOO with the
corresponding solver scripts.

These scripts and the corresponding version of the ParMOO software are
available under a [BSD 3-clause license](LICENSE).

This work is associated with a journal article titled
*Designing a Framework for Solving Multiobjective Simulation Optimization Problems*
published in
[INFORMS Journal on Computing](https://pubsonline.informs.org/journal/ijoc).

The publication is available at

https://doi.org/10.1287/ijoc.2023.0250

## Citing

To cite this work, it is recommended to please cite the
[corresponding journal article](https://doi.org/10.1287/ijoc.2023.0250):
```
@article{chang2024,
  author =        {Chang, Tyler H. and Wild, Stefan M.},
  journal =       {INFORMS Journal on Computing},
  title =         {Designing a Framework for Solving Multiobjective Simulation Optimization Problems},
  year =          {2025},
  doi =           {10.1287/ijoc.2023.0250.cd},
  note =          {To Appear},
}
```

The repository itself can be cited with the following BibTex.

```
@misc{chang2024,
  author =        {Chang, Tyler H. and Wild, Stefan M.},
  publisher =     {INFORMS Journal on Computing},
  title =         {Repository for ``Designing a Framework for Solving Multiobjective Simulation Optimization Problems''},
  year =          {2024},
  doi =           {10.1287/ijoc.2023.0250.cd},
  note =          {Available for download at https://github.com/INFORMSJoC/2023.0250},
}
```

## Reproducing Results

The `scripts` directory contains several subdirectories for reproducing the
experiments from Sections 4-6 of the paper.

### Setup and Installation

To use or compare against any of the sample problem, enter into the
appropriate `scripts` subdirectory and ``pip``-install the ``REQUIREMENTS``
file for that example.

```
cd scripts/section-x/
python3 -m pip install -r REQUIREMENTS.txt
```

Note that the above instructions will install a specific older release of ParMOO, as was used
in our experiments.  However, newer releases of ParMOO can be obtained by following the links
in
[Continued Development](https://github.com/INFORMSJoC/2023.0250?tab=readme-ov-file#continued-development)
(recommended) or via the
[Archived Submodule](https://github.com/INFORMSJoC/2023.0250?tab=readme-ov-file#alternative-parmoo-submodule-installation).

### Running Experiments

To run the experiments, see further instructions in the `README.md` file within
each of the corresponding subdirectories.

## Results

The raw performance data from our running of the above scripts are contained in
the `results` subdirectory.  This data is presented in Sections 4, 5, and 6 of
the [corresponding journal article](https://doi.org/10.1287/ijoc.2023.0250).

## Alternative ParMOO Submodule Installation

For additional local archival processes, the ParMOO source code is made available
in this repository via a git submodule in the `src/parmoo` subdirectory.

If the archived version needs to be retrieved, then the latest version of this source
can be obtained by changing into the `src/parmoo` subdirectory and initializing the
repository.

```
cd src/parmoo
git submodule update --init --recursive
```

In order to use a specific version of ParMOO, the user must check-out the correct
version (again, we used ``v0.2.2`` for the ``results`` and ``scripts`` in this
repository).

```
git checkout tags/<tag>
```

The code in the submodule can be installed to make it available on the system, e.g., via pip:

```
pip install -e ".[extras]"
```

Again, the submodule is included here primarily for INFORMS Journal of Computing archival
purposes; we recommend that users obtain the latest version of ParMOO using any of the links
listed below.

## Continued Development

ParMOO is under continuous development.  For the latest version of the ParMOO
library

 * visit our [GitHub page](https://github.com/parmoo/parmoo) or
 * view our documentation on [ReadTheDocs](https://parmoo.readthedocs.org)

Or contact our e-mail/support

 * ``parmoo@lbl.gov``

The solvers in this repository (within the `scripts` subdirectory) are fixed to
the version of ParMOO at the time of publication.  Updated versions may appear
in the future in the repository

 * visit the [ParMOO Solver Farm](https://github.com/parmoo/parmoo-solver-farm).

