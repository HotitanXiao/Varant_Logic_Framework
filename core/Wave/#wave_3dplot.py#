# -*-coding:utf-8 -*-
# File Name: wave_3dplot.py
# Author   : H.Y
# Date     : 2015-11-7

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import wave_test
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
(x, y, z) = wave_test.main()
hist, xedges, yedges = np.histogram2d(x, y, bins=4)


dx = 0.5
dy = 0.5
zpos = np.zeros(len(z))
# 下面参数比较坑跌，x，y，z标明画图起始点
#dx dy dz 标明柱状图三位参数长宽高
ax.bar3d(x, y, zpos, dx, dy, z, color='y', zsort='average')
ax.set_xlabel('p')
ax.set_ylabel('q')
ax.set_zlabel('sum')

plt.show()
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x, y = np.random.rand(2, 100) * 4
# hist, xedges, yedges = np.histogram2d(x, y, bins=4)

# elements = (len(xedges) - 1) * (len(yedges) - 1)
# xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)

# xpos = xpos.flatten()
# ypos = ypos.flatten()
# zpos = np.zeros(elements)
# dx = 0.5 * np.ones_like(zpos)
# dy = dx.copy()
# dz = hist.flatten()
# print xpos
# print ypos
# print zpos
# ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

# plt.show()
