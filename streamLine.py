import numpy as np
import matplotlib.pyplot as plt

print("Enter x,y file path : ")
pathX = input()
pathY = input()

# path="C:/Users/sony/Downloads/Uf01.bin/Uf01.bin"
f1=open(pathX, "rb")
# path="C:/Users/sony/Downloads/Uf01.bin/Uf01.bin"
f2=open(pathY, "rb")

dataX = np.fromfile(f1, dtype='>f')
dataY = np.fromfile(f2, dtype='>f')

dim_x = 500
dim_y = 500
dim_z = 100
DataX = np.zeros((dim_x,dim_y,dim_z),dtype=float)
DataY = np.zeros((dim_x,dim_y,dim_z),dtype=float)

for indexX in range(dim_x):
    for indexY in range(dim_y):
        for indexZ in range(dim_z):
            DataX[indexX][indexY][indexZ] = dataX[(indexX + (500*(indexY + (500*(indexZ)))))]
            DataY[indexX][indexY][indexZ] = dataY[(indexX + (500*(indexY + (500*(indexZ)))))]

X,Y = np.meshgrid(np.array(range(500)),np.array(range(500)))

z=10
U = DataX[:, :, z]
V = DataY[:, :, z]
fig = plt.figure()
ax = fig.add_subplot()
ax.streamplot(X, Y, U, V)
ax.set_title('Stream Line')
plt.show()



