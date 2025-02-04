..
  This is an archival version of ParMOO v0.2.2 for INFORMSJoC; users should
  to obtain the latest ParMOO source at https://github.com/parmoo/parmoo

Base (serial) MOOP Class
~~~~~~~~~~~~~~~~~~~~~~~~

This is the base class for solving MOOPs with ParMOO.

.. code-block:: python

    from parmoo import moop

Use this class to define and solve a MOOP.
The ``MOOP.solve(...)`` method will perform simulations serially for this
class.

.. automodule:: moop
..    :members: moop

.. autoclass:: MOOP
   :member-order: bysource
   :members:

   .. automethod:: __init__
   .. automethod:: __extract__
   .. automethod:: __embed__
   .. automethod:: __generate_encoding__
   .. automethod:: __unpack_sim__
   .. automethod:: __pack_sim__
