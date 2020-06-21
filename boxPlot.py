import matplotlib.pyplot as plt
import numpy as np

path="Downloads/Pf01.bin/Pf01.bin"
f1=open(path, "rb")
path="Downloads/Pf02.bin/Pf02.bin"
f2=open(path, "rb")
path="Downloads/Pf03.bin/Pf03.bin"
f3=open(path, "rb")
path="Downloads/Pf04.bin/Pf04.bin"
f4=open(path, "rb")
path="Downloads/Pf05.bin/Pf05.bin"
f5=open(path, "rb")
path="Downloads/Pf06.bin/Pf06.bin"
f6=open(path, "rb")
path="Downloads/Pf07.bin/Pf07.bin"
f7=open(path, "rb")
path="Downloads/Pf08.bin/Pf08.bin"
f8=open(path, "rb")
path="Downloads/Pf09.bin/Pf09.bin"
f9=open(path, "rb")
path="Downloads/Pf10.bin/Pf10.bin"
f10=open(path, "rb")
path="Downloads/Pf11.bin/Pf11.bin"
f11=open(path, "rb")
path="Downloads/Pf12.bin/Pf12.bin"
f12=open(path, "rb")

data1 = np.fromfile(f1, dtype='>f')
data2 = np.fromfile(f2, dtype='>f')
data3 = np.fromfile(f3, dtype='>f')
data4 = np.fromfile(f4, dtype='>f')
data5 = np.fromfile(f5, dtype='>f')
data6 = np.fromfile(f6, dtype='>f')
data7 = np.fromfile(f7, dtype='>f')
data8 = np.fromfile(f8, dtype='>f')
data9 = np.fromfile(f9, dtype='>f')
data10 = np.fromfile(f10, dtype='>f')
data11 = np.fromfile(f11, dtype='>f')
data12 = np.fromfile(f12, dtype='>f')

outlier = str(1.e+35)
actualdata1 = []
actualdata2 = []
actualdata3 = []
actualdata4 = []
actualdata5 = []
actualdata6 = []
actualdata7 = []
actualdata8 = []
actualdata9 = []
actualdata10 = []
actualdata11 = []
actualdata12 = []

for i in range(data1.size):
    if (str(data1[i]) != outlier):
        actualdata1.append(data1[i])
for i in range(data2.size):
    if (str(data2[i]) != outlier):
        actualdata2.append(data2[i])
for i in range(data3.size):
    if (str(data3[i]) != outlier):
        actualdata3.append(data3[i])
for i in range(data4.size):
    if (str(data4[i]) != outlier):
        actualdata4.append(data4[i])
for i in range(data5.size):
    if (str(data5[i]) != outlier):
        actualdata5.append(data5[i])
for i in range(data6.size):
    if (str(data6[i]) != outlier):
        actualdata6.append(data6[i])
for i in range(data7.size):
    if (str(data7[i]) != outlier):
        actualdata7.append(data7[i])
for i in range(data8.size):
    if (str(data8[i]) != outlier):
        actualdata8.append(data8[i])
for i in range(data9.size):
    if (str(data9[i]) != outlier):
        actualdata9.append(data9[i])
for i in range(data10.size):
    if (str(data10[i]) != outlier):
        actualdata10.append(data10[i])
for i in range(data11.size):
    if (str(data11[i]) != outlier):
        actualdata11.append(data11[i])
for i in range(data12.size):
    if (str(data12[i]) != outlier):
        actualdata12.append(data12[i])

red_square = dict(markerfacecolor='r', marker='s')
fig5, ax5 = plt.subplots()
Data = [actualdata1,actualdata2,actualdata3,actualdata4,actualdata5,actualdata6,actualdata7,actualdata8,actualdata9,actualdata10,actualdata11,actualdata12]
ax5.set_title('Horizontal Boxes')
ax5.boxplot(Data, vert=False, flierprops=red_square)
plt.show()