import os
import subprocess
#import numpy as np
import glob as glob
os.system("ls -l")
import pymeshlab as ml
ms = ml.MeshSet()

meshlist = glob.glob('results_*.stl')

cn = 1
for mesh in meshlist:
    #meshlabserver -i  -o output.ply -m vc fq wn -s meshclean.mlx
    mesh_smoothed = "results_0" + str(cn) + ".stl"
    ms.load_new_mesh(mesh_smoothed)
    ms.load_filter_script("taubin_smooth.mlx")
    ms.apply_filter_script()
    ms.save_current_mesh(mesh_smoothed)
    cn += 1