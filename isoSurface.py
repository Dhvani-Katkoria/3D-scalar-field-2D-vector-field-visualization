import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure

print("Enter file path : ")
path = input()

# path="C:/Users/sony/Downloads/Uf01.bin/Uf01.bin"
f=open(path, "rb")

data = np.fromfile(f, dtype='>f')

dim_x = 500
dim_y = 500
dim_z = 100
Data = np.zeros((dim_x,dim_y,dim_z),dtype=float)

outlier = str(1.e+35)

for indexX in range(dim_x):
    for indexY in range(dim_y):
        for indexZ in range(dim_z):
            if (str(data[(indexX + (500 * (indexY + (500 * (indexZ)))))]) != outlier):
                Data[indexX][indexY][indexZ] = data[(indexX + (500 * (indexY + (500 * (indexZ)))))]
            else:
                Data[indexX][indexY][indexZ] = 0.0

x, y, z = np.mgrid[0:499:500, 0:499:500, 0:99:100]
vol = Data
verts, faces,p,q = measure.marching_cubes_lewiner(vol,-1000, spacing=(1, 1, 1))

fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2], linewidth=0.2, cmap="viridis", lw=1)
fig.colorbar(surf)
plt.show()



