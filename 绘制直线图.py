import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)   # 从0到10取100个数
# print(x)
y = np.sin(x)
# print(y)
# plt.plot(x, y)
# plt.show()

cosy = np.cos(x)
print(cosy.shape)
siny = y.copy()
# plt.plot(x, siny)
# plt.plot(x, cosy)
# plt.show()


# 修改绘制颜色
# plt.plot(x, cosy, color = "red")
# plt.plot(x, siny, color = "green")
# plt.show()

# 修改绘制样式  linestyle=>  -.   -    --    :
# plt.plot(x, cosy, color="red", linestyle="--")
# plt.plot(x, siny, color="green")
# plt.show()


# # 修改坐标轴范围
# plt.plot(x, siny)
# plt.plot(x, cosy, color = "red", linestyle = "--")
# # plt.xlim(-5, 15)  # 只调整x轴范围
# # plt.ylim(0, 1.5)    # 只调整y轴范围
# plt.axis([-1, 11, -2, 2])  # 同时调整 x和y 的范围
# plt.show()

# # 给坐标轴添加标签
# plt.plot(x, siny)
# plt.plot(x, cosy, color="red", linestyle="--")
# plt.xlabel("x axis")
# plt.ylabel("y value")
# plt.show()


# # 给图像添加图示
# plt.plot(x, siny, label="sin(x)")
# plt.plot(x, cosy, color="red", linestyle="--", label="cos(x)")
# plt.xlabel("x axis")
# plt.ylabel("y value")
# plt.legend()
# plt.show()


# # 给图添加标题
# plt.plot(x, siny, label="sin(x)")
# plt.plot(x, cosy, color="red", linestyle="--", label="cos(x)")
# plt.xlabel("x axis")
# plt.ylabel("y value")
# plt.legend()
# plt.title("Welcome to the ML World!")
# plt.show()

# 给图添加标题
plt.plot(x, siny, color="green", linestyle="-.", label="sin(x)")
plt.plot(x, cosy, color="red", linestyle=":", label="cos(x)")
plt.xlabel("x axis")
plt.ylabel("y value")
plt.legend()
plt.title("Welcome to the ML World!")
plt.show()