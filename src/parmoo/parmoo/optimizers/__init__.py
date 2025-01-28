# This is an archival version of ParMOO v0.4.1 for INFORMSJoC; users should
# to obtain the latest ParMOO source at https://github.com/parmoo/parmoo
#
from .pattern_search import GlobalSurrogate_PS, LocalSurrogate_PS
from .random_search import GlobalSurrogate_RS
from .lbfgsb import GlobalSurrogate_BFGS, LocalSurrogate_BFGS

# LocalGPS = LocalSurrogate_PS
# GlobalGPS = GlobalSurrogate_PS
# RandomSearch = GlobalSurrogate_RS
# TR_LBFGSB = LocalSurrogate_BFGS
# LBFGSB = GlobalSurrogate_BFGS
