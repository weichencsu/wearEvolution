import os
import subprocess
import numpy as np
#import shutil
os.system("ls -l")

rang = np.arange(0.01, 1.1, 0.01)

cn = 2
for rat in rang:
    result = subprocess.Popen(["python.exe","mmig_open3d.py",str(rat),"shell_100.stl", "shell_0.stl"], stdout=subprocess.PIPE)
    output = result.communicate()[0]
    newName = "results" + "_0" + str(cn) + ".stl"
    os.rename("interpolated.stl", newName)
    cn += 1
