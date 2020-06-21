import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure

print("Enter file path : ")
path = input()
print("Enter axis for orthogonal slice: ")
axis = input()
print("Enter offset along specified axis: ")
offset = int(input())
# print("Enter colormap for slice: ")
# colormap_given = input()
# path="C:/Users/sony/Downloads/Uf01.bin/Uf01.bin"
f=open(path, "rb")

data = np.fromfile(f, dtype='>f')

dim_x = 500
dim_y = 500
dim_z = 100
Data = np.zeros((dim_x,dim_y,dim_z),dtype=float)

for indexX in range(dim_x):
    for indexY in range(dim_y):
        for indexZ in range(dim_z):
            Data[indexX][indexY][indexZ] = data[(indexX + (500*(indexY + (500*(indexZ)))))]

min_val = Data.min()
max_val = Data.max()
n_x, n_y, n_z = Data.shape
colormap = plt.cm.viridis

if (axis =='X'):
    x_cut = Data[offset,:,:]
    min_val = x_cut.min()
    max_val = x_cut.max()
    Y, Z = np.mgrid[0:n_y, 0:n_z]
    X = offset * np.ones((n_y, n_z))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z,facecolors=colormap((x_cut-min_val)/(max_val-min_val)))
    ax.set_title("X slice")
    ax.set_zlim3d(0, 100)
elif (axis == "Z"):
    z_cut = Data[:,:,offset]
    min_val = z_cut.min()
    max_val = z_cut.max()
    X, Y = np.mgrid[0:n_x,0:n_y]
    Z = offset* np.ones((n_x, n_y))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, facecolors=colormap((z_cut-min_val)/(max_val-min_val)))
    ax.set_title("Z slice")
    ax.set_zlim3d(0,100)
else:
    y_cut = Data[:,offset,:]
    min_val = y_cut.min()
    max_val = y_cut.max()
    X, Z = np.mgrid[0:n_x,0:n_z]
    Y = offset* np.ones((n_x, n_z))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, facecolors=colormap((y_cut-min_val)/(max_val-min_val)))
    ax.set_title("Y slice")
    ax.set_zlim3d(0,100)

fig.colorbar(surf)
plt.show()



