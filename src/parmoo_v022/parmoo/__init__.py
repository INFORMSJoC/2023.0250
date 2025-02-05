# This is an archival version of ParMOO v0.2.2 for INFORMSJoC; users should
# to obtain the latest ParMOO source at https://github.com/parmoo/parmoo
#
"""
ParMOO.

A parallel multiobjective optimization solver that seeks to exploit
simulation-based structure in objective and constraint functions.

"""

from .version import __version__
__author__ = "Tyler H. Chang, Stefan M. Wild, and Hyrum Dickinson"
__credits__ = ("Argonne National Laboratory and " +
               "Lawrence Berkeley National Laboratory")

from .moop import MOOP
