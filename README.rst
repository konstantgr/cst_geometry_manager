CST geometry manager
====================

It's a package that allows you to model geometries contain wires and
then export it into CST Microwave Studio project using python.

Features
--------

-  One file format for all wire geometries
-  Сreating a CST project directly from a script or notebook.
-  Convenient data structure for creating your own unique complex
   geometries from wires

Install
=======
For simple installation use pip: 
::

   pip install cst-geometry


Usage
-----

During using scripts or notebooks for creating projects all the CST Microwave studio windows must be closed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To create your own geometry use ``Wire`` and ``Geometry`` classes. ``Wire`` object initializing using start point ``r0``, finish point ``r1`` and its radius. Geometry object initializing using array of ``Wires`` objects. ``Geometry`` object has methods ``export_geometry`` for export .txt file and ``create_cst_project`` for creating project in CST Microwave Studio.

.. code:: python

   import numpy as np
   from cst_geometry import Wire, Geometry


   def get_circular_geometry(radius, lengths_of_wires, wire_radius=1e-3, delta_angle=0):
       number_of_wires = len(lengths_of_wires)
       angles = np.linspace(0, 2 * np.pi, number_of_wires, endpoint=False) + delta_angle

       wires = []
       for i, length in enumerate(lengths_of_wires):
           phi = angles[i]
           wire = Wire(
               r0=(radius * np.cos(phi), radius * np.sin(phi), -length / 2),
               r=(radius * np.cos(phi), radius * np.sin(phi), length / 2),
               radius=wire_radius
           )
           wires.append(wire)

       return Geometry(wires)

Examples
--------

.. code:: python

    from cst_geometry import simple_geometries

    # Path to CST DESIGN ENVIRONMENT.exe
    path_to_CST_DE = "Absolute\Path\To\CST DESIGN ENVIRONMENT.exe"

    # Route to folder with .txt geometries and CST projects
    route_to_folder = "Absolute\Path\To\FOLDER"


    def circular_geometry_equal_wires(length, number_of_wires, radius):
    	lengths = [length for i in range(number_of_wires)]

    	circular_geometry = simple_geometries.get_circular_geometry(
        		radius=radius, lengths_of_wires=lengths, wire_radius=1e-3, delta_angle=0
    	)
    	return circular_geometry


    # Creating an array of 18 vertical aligned wires with length 2
    # on of imaginary cylinder with radius 4
    circular_geometry = circular_geometry_equal_wires(2, 18, 4)
    output = circular_geometry.create_cst_project(
        name="circular_geometry",
        path_to_CST_DE=path_to_CST_DE,
        path_to_geometry_folder=route_to_folder,
        path_to_CST_project=route_to_folder
    )


This code creates simple geometry contain 18 wires equally distributed on
imaginary cylinder. Then ``create_cst_project`` method creates project.
To start using scripts firstly need to change ``path_to_CST_DE``
variable. CST project create in cst\_project folder.


.. image:: examples/CST_example.gif

Several examples with CST projects are located in ``examples/`` folder.


