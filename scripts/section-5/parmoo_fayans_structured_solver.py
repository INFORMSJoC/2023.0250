""" Apply ParMOO with libE plugin to solve the Fayans EDF callibration MOOP,
exploiting sum-of-squares structure in how simulation outputs are used.

Execute via one of the following commands (where N is the number of threads,
and the optional int M in [0, 2^32-1] is a random seed):

```
mpiexec -np N python3 parmoo_fayans_structured_solver.py [--iseed M]
python3 parmoo_fayans_structured_solver.py --nworkers N --comms local [--iseed M]
python3 parmoo_fayans_structured_solver.py --nworkers N --comms tcp [--iseed M]
```


The number of concurrent evaluations of the Fayans EDF model will be N-1,
since the first thread is reserved for the ParMOO generator.

"""

import numpy as np
import csv
import sys
from time import time_ns
from parmoo.extras.libe import libE_MOOP
from parmoo.optimizers import TR_LBFGSB
from parmoo.surrogates import LocalGaussRBF
from parmoo.searches import LatinHypercube
from parmoo.acquisitions import RandomConstraint, FixedWeights
import fayans_model

# Set the problem dimensions
n = 13
m = 198
o = 3

# Read the random seed from the command line
iseed = time_ns() % (2 ** 32) # default is to set from system clock
for i, opt in enumerate(sys.argv[1:]):
    if opt == "--iseed":
        try:
            iseed = int(sys.argv[i+2])
            del sys.argv[i+1]
            del sys.argv[i+1]
        except IndexError:
            raise ValueError("iseed requires an integer value")
        except ValueError:
            raise ValueError("iseed requires an integer value")

if __name__ == "__main__":
    """ For a libE_MOOP to be run on certain OS (such as MacOS) it must be
    enclosed within an ``if __name__ == '__main__'`` clause. """

    # Create a libE_MOOP
    fayans_moop = libE_MOOP(TR_LBFGSB, hyperparams={})
    # Add 13 design variables from fayans_model meta data
    for i in range(n):
        fayans_moop.addDesign({'name': fayans_model.DES_NAMES[i],
                               'lb': fayans_model.lb[i],
                               'ub': fayans_model.ub[i]})
    # Add 1 simulation
    fayans_moop.addSimulation({'name': "residuals",
                               'm': m,
                               'sim_func': fayans_model.fayans_sim_model,
                               'hyperparams': {'search_budget': 2000},
                               'search': LatinHypercube,
                               'surrogate': LocalGaussRBF})
    # Add 3 objectives
    fayans_moop.addObjective({'name': "binding energy",
                              'obj_func': fayans_model.binding_energy})
    fayans_moop.addObjective({'name': "std radii",
                              'obj_func': fayans_model.std_radii})
    fayans_moop.addObjective({'name': "other quantities",
                              'obj_func': fayans_model.other_quantities})
    # Add 3 constraints
    fayans_moop.addConstraint({'name': "binding energy max",
                               'constraint':
                               fayans_model.constraint_binding_energy})
    fayans_moop.addConstraint({'name': "std radii max",
                               'constraint':
                               fayans_model.constraint_std_radii})
    fayans_moop.addConstraint({'name': "other quantities max",
                               'constraint':
                               fayans_model.constraint_other_quantities})
    # Add 9 random acquisition functions
    for i in range(9):
        fayans_moop.addAcquisition({'acquisition': RandomConstraint,
                                    'hyperparams': {}})
    # Add a 10th acquisition function, which is the Chi^2 loss
    fayans_moop.addAcquisition({'acquisition': FixedWeights,
                                'hyperparams': {'weights': np.ones(o) / o}})
    # Fix the random seed for reproducability
    np.random.seed(iseed)
    # Solve the Fayans EDF callibration moop with a 10K sim budget
    fayans_moop.solve(sim_max=10000, wt_max=172800)
    full_data = fayans_moop.getObjectiveData()
    soln = fayans_moop.getPF()

    # Dump full data set to a CSV file
    with open("fayans_structured_results_seed_" + str(iseed) + ".csv",
              "w") as fp:
        csv_writer = csv.writer(fp, delimiter=",")
        # Define the header
        header = fayans_model.DES_NAMES.copy()
        header.append("binding energy")
        header.append("std radii")
        header.append("other quantities")
        # Dump header to first row
        csv_writer.writerow(header)
        # Add each data point as another row
        for xs in full_data:
            csv_writer.writerow([xs[name] for name in header])
