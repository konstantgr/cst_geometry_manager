import os


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

    def export_geometry(self, name):
        with open(f'../exported_geometries/{name}.txt', 'w+') as file:
            file.write(f'{len(self.wires)} {self.wires[0].radius}\n')
            for wire in self.wires:
                file.write(f'{wire.x0} {wire.y0} {wire.z0} {wire.x1} {wire.y1} {wire.z1}\n')
        print(f'{name}.txt successfully added')

    def create_cst_project(self, name, path_to_CST_DE):
        self.export_geometry(name)

        path_to_geometry = os.path.abspath(f"..\exported_geometries\{name}.txt")
        path_to_cst_file = os.path.abspath(f"..\cst_projects\{name}.cst")
        path_to_script = os.path.abspath('../basic_script/script.bas')

        with open('../basic_script/script.bas', 'r') as f:
            lines = f.readlines()
            lines[1] = f'geometry_file = \"{path_to_geometry}\"\n'
            lines[-4] = f'proj.SaveAs \"{path_to_cst_file}\", True\n'

        with open('../basic_script/script.bas', 'w') as f:
            f.writelines(lines)

        stream = os.popen(f'"{path_to_CST_DE}" -m "{path_to_script}"')
        return stream.read()

