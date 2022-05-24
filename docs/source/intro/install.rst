Install Guide
=============

Being a modern Python framework, zeuspy requires an up to date version of Python to be installed in your system.
We recommend using the latest versions of both Python 3 and pip.

.. contents:: Contents
    :backlinks: none
    :depth: 1
    :local:

-----

Install zeuspy
----------------

-   The easiest way to install and upgrade zeuspy to its latest stable version is by using **pip**:

    .. code-block:: text

        $ pip3 install -U zeuspy

-   or, with :doc:`TgCrypto <../topics/speedups>` as extra requirement (recommended):

    .. code-block:: text

        $ pip3 install -U zeuspy tgcrypto

Bleeding Edge
-------------

You can install the development version from the git ``master`` branch using this command:

.. code-block:: text

    $ pip3 install -U https://github.com/zeuspy/zeuspy/archive/master.zip

Verifying
---------

To verify that zeuspy is correctly installed, open a Python shell and import it.
If no error shows up you are good to go.

.. parsed-literal::

    >>> import zeuspy
    >>> zeuspy.__version__
    'x.y.z'

.. _`Github repo`: http://github.com/zeuspy/zeuspy
