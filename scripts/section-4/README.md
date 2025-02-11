# Timing ParMOO + libEnsemble parallel runs on DTLZ2 test problem

This directory contains several scripts for evaluating the parallel
performance of ParMOO v0.2.2 with libEnsemble.

Note that real-world performance will vary based on simulation expense,
problem type, choice of solver, available hardware, and many other
factors.

In this example, we use the DTLZ2 test problem from the multiobjective
test problem library DTLZ by Deb et al. (2005). In order to simulate
problem expense, we have created artificial simulation runtimes that
are uniformly distributed in the range [1, 3] seconds using the Python
``time.sleep(t)`` command.

These scripts correspond to the results described in Section 4 of the
[corresponding journal paper for this repository](https://doi.org/10.1287/ijoc.2023.0250).

## Setup and Installation

The requirements for this directory are:

 - [ParMOO](https://github.com/parmoo/parmoo),
 - [libensemble](https://github.com/libensemble/libensemble), and
 - [pymoo](https://pymoo.org/).

To try running these solvers yourself, clone this directory
and install the requirements, or install the included ``REQUIREMENTS.txt``
file.

```
python3 -m pip install -r REQUIREMENTS.txt
```

Note that several major libraries in ``REQUIREMENTS.txt`` have been pinned to
very specific versions.  Since these runs were used for timing, any change in
the version numbers could result in different results than those that we have
previously recorded.

The scripts in this directory will attempt to store results in the
subdirectory ``parmoo-dtlz2``. You must create this directory yourself.

```
mkdir -p parmoo-dtlz2
```

Alternatively, the ``run_timings.sh`` script will create them for you.

## Instructions and Structure

This particular directory contains three Python files.

 - ``parmoo_solve_dtlz2_serial.py`` provides scripts for solving the
   DTLZ2 problem with ParMOO, with serial simulation evaluations;
 - ``parmoo_solve_dtlz2_parallel.py`` provides scripts for solving the
   DTLZ2 problem with ParMOO, with parallel simulation evaluations; and
 - ``pymoo_solve_dtlz2_serial.py`` provides scripts for solving the DTLZ2
   problem with pymoo, with serial simulation evaluations.

And one additional run file:

 - ``run_timings.sh``, which can be used to reproduce our experiments. It
   will create and store results in the new folders ``parmoo-dtlz2`` and
   ``pymoo-dtlz2``.

```
./run_timings.sh
```

To most closely reproduce our results, make sure you are using
Python v3.8.3, and the library versions specified in the ``REQUIREMENTS.txt``
file. The results of our experiments are saved in:

 - ``parmoo-dtlz2-results-2024/size{SIZE}_seed{SEED}.csv``,
   where ``SIZE`` and ``SEED`` represent the batch size and random seed
   number from each experiment, respectively.
   Within each file, each line contains values: ``walltime, hypervolume``,
   and the lines are ordered in increasing number of parallel threads,
   specifically 1, 2, 4, 8.
