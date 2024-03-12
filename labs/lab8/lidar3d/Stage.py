"""
# Please read the guideline before you run this script.
"""

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import vtkmodules.all as vtk
import lidar3d.utils as utils
import numpy as np


class Stage3d:
    def __init__(self):
        self.mesh = vtk.vtkPolyData()
        self.appendPolyFilter = vtk.vtkAppendPolyData()
        self.actor = vtk.vtkAssembly()

    def addObject(self, mesh):
        if isinstance(mesh, str):
            mesh = self.getPolyfromFile(mesh)

        if isinstance(mesh, vtk.vtkPolyData):
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputData(mesh)
            mesh = utils.makeActor(mesh)
            self.actor.AddPart(mesh)
        mesh = mesh.GetMapper().GetInput()
        self.appendPolyFilter.AddInputData(mesh)
        self.appendPolyFilter.Update()
        self.mesh = self.appendPolyFilter.GetOutput()

    @staticmethod
    def make_default_stage3d():
        stage = Stage3d()
        stage.addObject(utils.makeCube(center=[0, 0, 0], shape=[10, 100, 100]))
        stage.addObject(utils.makeCube(center=[0, 0, 0], shape=[100, 10, 10]))
        stage.addObject(utils.makeCube(center=[0, 0, 0], shape=[500, 500, 1]))
        stage.addObject(utils.makeSphere(center=[30, 30, 30], radius=20))
        # return Stage3d.make_your_stage3d()
        return stage

    @staticmethod
    def make_your_stage3d():
        stage = Stage3d()
        np.random.seed(5)
        cube = utils.makeCube(center=[0, 0, 0], shape=[10, 100, 100])

        ## TODO: Fill in needed parameters & modify the code to make your own stage
        ## Including both cube and sphere in your stage.
        for i in range(5):
            cube1 = utils.transModel(cube, rot=np.random.randint(-30,30, 3), pos=[(i-2)*100, 10 + (i-2)*30, 0])
            stage.addObject(cube1)
        stage.addObject(utils.makeCube(center=[0, 0, 0], shape=[500, 500, 1]))
        stage.addObject(utils.makeSphere(center=[75, -120, 35], radius=30))
        cube2 = utils.makeCube(center=[0, 0, 0], shape=[100, 10, 10])
        cube2 = utils.transModel(cube2, rot=[0, 0, 30], pos=[-150, 130, 10])
        stage.addObject(cube2)
        ##

        return stage

if __name__ == '__main__':
    # s = Stage3d.make_default_stage3d()
    s = Stage3d.make_your_stage3d()
    utils.show_in_vtk([s.actor])
