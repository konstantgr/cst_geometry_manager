import numpy as np

from cst_geometry_manager import Wire, Geometry


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


def get_cubic_grid_geometry(tau, lengths_of_wires, wire_radius=1e-3):
    """
    length_of_wires: np.array([[0., 0., 0.],
                               [0., 0., 0.],
                               [0., 0., 0.],
                               [0., 0., 0.]])
                     is a 4x3 array, left bottom corner is (0,0) point
    """

    number_of_wires_y, number_of_wires_x = lengths_of_wires.shape

    wires = []
    for i in range(number_of_wires_y):
        for j in range(number_of_wires_x):
            x = tau * j
            y = tau * i
            wire = Wire(
                r0=(x, y, -lengths_of_wires[i][j] / 2),
                r=(x, y, lengths_of_wires[i][j] / 2),
                radius=wire_radius
            )
            wires.append(wire)

    return Geometry(wires)


def get_shortened_taper_geometry(radius_inner, radius_outer, number_of_wires,
                                 taper_height, wire_radius=1e-3,
                                 delta_angle=0):

    angles = np.linspace(0, 2 * np.pi, number_of_wires, endpoint=False) + delta_angle

    wires = []
    for i in range(number_of_wires):
        phi = angles[i]
        wire = Wire(
            r0=(radius_outer * np.cos(phi), radius_outer * np.sin(phi), 0),
            r=(radius_inner * np.cos(phi), radius_inner * np.sin(phi), taper_height),
            radius=wire_radius
        )
        wires.append(wire)

    return Geometry(wires)
