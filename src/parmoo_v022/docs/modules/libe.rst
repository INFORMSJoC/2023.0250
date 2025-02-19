..
  This is an archival version of ParMOO v0.2.2 for INFORMSJoC; users should
  to obtain the latest ParMOO source at https://github.com/parmoo/parmoo

Parallel Solvers using the libE_MOOP Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solve MOOPs in parallel using ParMOO together with libEnsemble.

.. code-block:: python

    from parmoo.extras import libE_MOOP

The ``libE_MOOP.solve(...)`` method will distribute simulations across
parallel resources using libEnsemble for this class.

.. automodule:: extras.libe
..    :members: extras/libe

.. autoclass:: libE_MOOP
   :member-order: bysource
   :members:

   .. automethod:: __init__
