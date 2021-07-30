# CST geometry manager

It's a package that allows you to model geometries contain wires and then export it into CST Microwave Studio project using python.  

## Features

- One file format for all wire geometries
- Сreating a CST project directly from a script or notebook.
- Convenient data structure for creating your own unique complex geometries from wires

## Usage 

```python
# Path to CST DESIGN ENVIRONMENT.exe
path_to_CST_DE = "Absolute\Path\To\CST DESIGN ENVIRONMENT.exe"


def circular_geometry_equal_wires(length, number_of_wires, radius):
    lengths = [length for i in range(number_of_wires)]

    circular_geometry = simple_geometries.get_circular_geometry(
        radius=radius, lengths_of_wires=lengths
    )
    return circular_geometry


circular_geometry = circular_geometry_equal_wires(2, 4, 4)
circular_geometry.create_cst_project(
    name='circular_geometry',
    path_to_CST_DE=path_to_CST_DE
)
```

This code creates simple geometry contain 4 wires equally distributed on imaginary cylinder. Then `create_cst_project` method creates project. To start using scripts firstly need to change `path_to_CST_DE` variable. CST project create in cst_project folder.

#### During using scripts or notebooks for creating projects all the CST Microwave studio windows must be closed

## Examples

Several examples located in notebooks folder. `make_geometries_example.ipynb` shows how create sinmple geometries using `Wire` and `Geometry` classes. `export_to_cst_example.ipynb` shows how create a CST project using jupyter notebook. In `examples` also located a script shows how create a CST project without using jupyter notebook.


`
