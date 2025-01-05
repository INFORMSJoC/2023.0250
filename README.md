# ParMOO Solvers: Sample Simulation Optimization Problems and Solvers

This repository contains samples of several multiobjective simulation
optimization (MOSO) problems that have been solved with ParMOO with the
corresponding solver scripts.

These scripts and the corresponding version of the ParMOO software are
available under a [BSD 3-clause license](LICENSE.md).

This work is associated with a journal article titled
*Designing a Framework for Solving Multiobjective Simulation Optimization Problems*
published in
[INFORMS Journal on Computing](https://pubsonline.informs.org/journal/ijoc).

The publication is available at

https://doi.org/10.1287/ijoc.2023.0250

## Citing

To cite this work, it is recommended to please cite the
[corresponding journal article](https://doi.org/10.1287/ijoc.2023.0250).
The repository itself can be cited with the following BibTex.

```
@misc{chang2024,
  author =        {Chang, Tyler H. and Wild, Stefan M.},
  publisher =     {INFORMS Journal on Computing},
  title =         {Designing a Framework for Solving Multiobjective Simulation Optimization Problems},
  year =          {2024},
  doi =           {10.1287/ijoc.2023.0250.cd},
  note =          {Available for download at https://github.com/INFORMSJoC/2023.0250},
}
```

## Reproducing Results

The `scripts` directory contains several subdirectories for reproducing the
experiments from Sections 4-6 the paper.

### Setup and Installation

To use or compare against any of the sample problem, enter into the
appropriate `scripts` subdirectory and ``pip``-install the ``REQUIREMENTS``
file for that example.

```
cd scripts/section-x/
python3 -m pip install -r REQUIREMENTS.txt
```

### Running Experiments

To run the experiments, see further instructions in the `README.md` file within
each of the corresponding subdirectories.

## Results

The raw performance data from our running of the above scripts are contained in
the `results` subdirectory.  This data is presented in Sections 4, 5, and 6 of
the journal article.

## Continued Development

ParMOO is under continuous development.  For the latest version of the ParMOO
library

 * visit our [GitHub](https://github.com/parmoo/parmoo) page or
 * view our documentation on [ReadTheDocs](https://parmoo.readthedocs.org)

Or contact our e-mail/support

 * ``parmoo@lbl.gov``

The solvers in this repository (within the `scripts` subdirectory) are fixed to
the version of ParMOO at the time of publication.  Updated versions may appear
in the future in the following repository

 * visit the [ParMOO Solver Farm](https://github.com/parmoo/parmoo-solver-farm).

