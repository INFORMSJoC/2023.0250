# Calibrating the Fayans EDF Model with ParMOO

This directory contains several scripts for calibrating a neural-network
replica of the Fayans Energy Density Functional (EDF) model residuals based
on experimental data.

The significance of the problem and collection of the dataset used to train
our ``keras`` residual model is fully described in
*Bollapragada et al. (2020)
Journal of Physics G: Nuclear and Particle Physics 48(2):024001*.
For compatibility reasons, the ``keras`` residual model has been converted
into a ``torch`` model.
This means that ``pytorch``, not ``tensorflow``, is required for usage
of this model.

These scripts correspond to the results described in Section 5 of the
[corresponding journal paper for this repository](https://doi.org/10.1287/ijoc.2023.0250).

## Setup and Installation

The requirements for this directory are:

 - [ParMOO](https://github.com/parmoo/parmoo),
 - [libensemble](https://github.com/libensemble/libensemble),
 - [pymoo](https://pymoo.org/), and
 - [pytorch](https://pytorch.org/).

To try running these solvers yourself, clone this directory
and install the requirements, or install the included ``REQUIREMENTS.txt``
file.

```
python3 -m pip install -r REQUIREMENTS.txt
```

Then, to verify the installation, try running the faster test version of
the problem in ``parmoo_fayans_test.py``, to verify that ParMOO,
libEnsemble, and PyTorch are all working together correctly.

```
python3 parmoo_fayans_test.py --comms local --nworkers 4
```

Running the above test produces a CSV file containing ParMOO's final
database of design parameter and objective values in
``fayans_test_results.csv``.

## Instructions and Structure

This particular directory contains three Python files.

 - ``fayans_model.py`` defines a model of the residuals of the Fayans EDF
   calibration problem and provides several ParMOO compatible objective
   and constraint functions;
 - ``parmoo_fayans_structured_solver.py`` provides scripts for solving the
   problem with ParMOO, while exploiting the sum-of-squares structure in
   how the (blackbox) residuals are used to define the problem; and
 - ``parmoo_fayans_blackbox_solver.py`` provides an implementation where
   the problem structure is not available to ParMOO, thus allowing for
   comparison between exploiting vs. not exploiting the problem structure.
 - ``parmoo_fayans_test.py`` is a test case, to make sure that ParMOO,
   libEnsemble, and pytorch are working together.

An additional file:

 - ``fayans_weights.h5`` contains the weights for the pre-trained
   ``torch`` model of the  Fayans EDF residuals.

If ``name.py`` is one of

 - ``parmoo_fayans_structured_solver.py``
 - ``parmoo_fayans_blackbox_solver.py``

then you can reproduce our results by using the command:

```
python3 name.py --comms C --nworkers N [--iseed I]
```

or, if you are working on a Linux or MacOS system, run all of the experiments
from Section 5 of the paper with our ``run_all.sh`` script:

```
./run_all.sh
```

where ``C`` is the communication protocol (``local`` or ``tcp``);
``N`` is the number of libE workers (i.e., number of concurrent simulation
evaluations); and
``I`` is the random seed, which can be fixed to any integer for
reproducibility (when omitted, it is assigned by the system clock).

In the associated paper, we used the seed values ``I = 0, 1, 2, 3, 4``.

After running, the complete function-value database is saved to a file
``parmoo_fayans_structured_results_seed_I.csv`` or
``parmoo_fayans_blackbox_results_seed_I.csv``, depending on the method run
where ``I`` is as defined above.

To recreate the plots in the paper, run either of the plotting scripts in
the ``./plots`` subdirectory.
