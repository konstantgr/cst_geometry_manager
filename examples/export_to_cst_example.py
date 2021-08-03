from cst_geometry import Wire, Geometry
from cst_geometry import simple_geometries

path_to_CST_DE = r"ABSOLUTE\\PATH\\TO\\CST DESIGN ENVIRONMENT.exe"
route_to_folder = r"ABSOLUTE\\PATH\\TO\\FOLDER"


def circular_geometry_equal_wires(length, number_of_wires, radius):
    lengths = [length for i in range(number_of_wires)]

    circular_geometry = simple_geometries.get_circular_geometry(
        radius=radius, lengths_of_wires=lengths, wire_radius=1e-3, delta_angle=0
    )
    return circular_geometry


def main():
    circular_geometry = circular_geometry_equal_wires(2, 18, 4)
    output = circular_geometry.create_cst_project(
        name="circular_geometry",
        path_to_CST_DE=path_to_CST_DE,
        path_to_geometry_folder=route_to_folder,
        path_to_CST_project=route_to_folder
    )

    print(output)


if __name__ == '__main__':
    main()
