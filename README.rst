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

Usage
-----

During using scripts or notebooks for creating projects all the CST Microwave studio windows must be closed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

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



Examples
--------

.. image:: examples/CST_example.gif

Several examples with CST projects are located in ``examples/`` folder.


