import os
from ._script import Script


class Wire:
    def __init__(self, r0, r, radius):
        self.x0, self.y0, self.z0 = r0
        self.x1, self.y1, self.z1 = r
        self.radius = radius

    @property
    def length(self):
        return (self.x1 - self.x0) ** 2 \
               + (self.y1 - self.y0) ** 2 \
               + (self.z1 - self.z0) ** 2


class Geometry:
    def __init__(self, wires):
        self.wires = wires

    def get_coordinates(self):
        coords = []
        for wire in self.wires():
            coords.append([
                (wire.x0, wire.y0, wire.z0),
                (wire.x1, wire.y1, wire.z1)
            ])

    def export_geometry(self, path_to_geometry_folder, name):
        with open(f'{path_to_geometry_folder}\{name}.txt', 'w+') as file:
            file.write(f'{len(self.wires)} {self.wires[0].radius}\n')
            for wire in self.wires:
                file.write(f'{wire.x0} {wire.y0} {wire.z0} {wire.x1} {wire.y1} {wire.z1}\n')
        print(f'{name}.txt successfully added')

    def create_cst_project(self, name, path_to_geometry_folder,
                           path_to_CST_DE, path_to_CST_project):
        self.export_geometry(path_to_geometry_folder, name)

        script = Script(name=name, route_geometry=path_to_geometry_folder, route_cst=path_to_CST_project)

        path_to_script = os.path.abspath('script.bas'); print(f'"{path_to_CST_DE}" -m "{path_to_script}"')
        stream = os.popen(f'"{path_to_CST_DE}" -m "{path_to_script}"')
        script.remove_script()
        return stream.read()

