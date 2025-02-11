# Identifying CFR Material Manufacturing Conditions with ParMOO

This directory contains several scripts for calibrating a continuous flow
reactor (CFR) in order to maximize the production TFMC at high temperatures,
based on a model of of the expected products and byproducts, which was fit
using previously-collected experimental data.

The significance of the problem and collection of the dataset used to train
our model is fully described in
*Chang et al. (2023) ICLR 23, Workshop on ML4Materials*.
To reduce dependencies, the original ``sklearn`` model has been ported into
basic ``python`` and ``sklearn`` is not a dependency for this project.

These scripts correspond to the results described in Section 6 of the
[corresponding journal paper for this repository](https://doi.org/10.1287/ijoc.2023.0250).

## Setup and Installation

The requirements for this directory are:

 - [ParMOO](https://github.com/parmoo/parmoo), and
 - [pymoo](https://pymoo.org/).

To try running these solvers yourself, clone this directory
and install the requirements, or install the included ``REQUIREMENTS.txt``
file.

```
python3 -m pip install -r REQUIREMENTS.txt
```

Then, to verify the installation, try running the faster test version of
the problem in ``parmoo_cfr_test.py``, to verify that ParMOO is working
correctly.

```
python3 parmoo_cfr_test.py
```

## Instructions and Structure

This particular directory contains three Python files.

 - ``cfr_model.py`` defines a model of the product and byproduct NMR integrals
   and provides several ParMOO compatible objective and constraint functions;
 - ``parmoo_cfr_structured_solver.py`` provides scripts for solving the
   problem with ParMOO, while exploiting the heterogeneous objective structure
   of the problem; and
 - ``parmoo_cfr_blackbox_solver.py`` provides an implementation where the
   heterogeneous problem structure is not available to ParMOO, thus allowing
   for comparison between exploiting vs. not exploiting the problem structure.
 - ``parmoo_cfr_test.py`` is a test case, to make sure that ParMOO and the
   model definitions are working.

If ``name.py`` is one of

 - ``parmoo_cfr_structured_solver.py``
 - ``parmoo_cfr_blackbox_solver.py``

then you can reproduce our results by using the command:

```
python3 name.py [--iseed I]
```

or, if you are working on a Linux or MacOS system, run all of the experiments
from Section 6 of the paper with our ``run_all.sh`` script:

```
./run_all.sh
```

where ``I`` is the random seed, which can be fixed to any integer for
reproducibility (when omitted, it is assigned by the system clock).

In the associated paper, we used the seed values ``I = 0, 1, 2, 3, 4``.

After running, the complete function-value database is saved to a file
``parmoo_cfr_structured_results_seed_I.csv`` or
``parmoo_cfr_blackbox_results_seed_I.csv``, depending on the method run
where ``I`` is as defined above.

To recreate the plots in the paper, run either of the plotting scripts in
the ``./plots`` subdirectory.
