# Scatter  Plot:散点图
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)   # 从0到10取100个数
# print(x)
y = np.sin(x)
# print(y)

cosy = np.cos(x)
# print(cosy.shape)
siny = y.copy()

# plt.scatter(x, siny)
# plt.scatter(x, cosy, color="red")
# plt.show()

# x = np.random.normal(0,1,100)   # 100个均值为0，方差为1的
# y = np.random.normal(0,1,100)   # 100个均值为0，方差为1的
#
# plt.scatter(x, y)
# plt.show()


x = np.random.normal(0,1,10000)   # 10000个均值为0，方差为1的
y = np.random.normal(0,1,10000)   # 10000个均值为0，方差为1的

# 设置透明度  alpha
plt.scatter(x, y,color="green", alpha=0.7)
plt.show()




