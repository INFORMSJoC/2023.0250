..
  This is an archival version of ParMOO v0.2.2 for INFORMSJoC; users should
  to obtain the latest ParMOO source at https://github.com/parmoo/parmoo

Built-in Problem Libraries
--------------------------

We provide several modules containing common objective and constraint
functions, which match the ParMOO interface and already support
gradient-based solvers.

You can import these and use them to help define your MOOP.

.. code-block:: python

    from parmoo import objectives
    from parmoo import constraints

We also provide templates for defining callable objects, which match
ParMOO's interface.

.. code-block:: python

    from parmoo.simulations import sim_func
    from parmoo.objectives import obj_func
    from parmoo.constraints import const_func

Current options are:

.. toctree::
   :maxdepth: 1
   :caption: Modules:

   simulations
   objectives
   constraints
