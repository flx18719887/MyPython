# coding=gbk
import numpy as np
import matplotlib.pyplot as plt

# 给定点x和y
plot_x = np.linspace(-1, 6, 141)
plot_y = (plot_x - 2.5) ** 2 - 1

# 画出二次函数的图像
plt.plot(plot_x, plot_y)
# plt.show()

# 定义梯度(计算曲线在theta点处的导数值)
def dJ(theta):
    return 2 * (theta - 2.5)

# # 定义代价函数
# def J(theta):
#     return (theta - 2.5) ** 2 - 1

# 梯度下降法
eta = 0.1   # 定义步长
epsilon = 1e-8    # 定义一个阈值

# theta = 0.0   # 设置初值
# while True:
#     gradient = dJ(theta)   # 梯度
#     last_theta = theta
#     theta = theta - eta * gradient    # 梯度下降计算参数theta的值
#
#     if(abs(J(theta) - J(last_theta)) < epsilon):    # 代价函数变化值近似为0
#         break
#
# print(theta)
# print(J(theta))

# # 画图
# theta = 0.0   # 设置初值
# theta_history = [theta]
# while True:
#     gradient = dJ(theta)   # 梯度
#     last_theta = theta
#     theta = theta - eta * gradient    # 梯度下降计算参数theta的值
#     theta_history.append(theta)
#
#     if(abs(J(theta) - J(last_theta)) < epsilon):    # 代价函数变化值近似为0
#         break
#
# plt.plot(plot_x, J(plot_x))
# plt.plot(np.array(theta_history), J(np.array(theta_history)), color="r", marker='+')
# plt.show()
#
# print(len(theta_history))






# 定义代价函数
def J(theta):
    try:
        return (theta - 2.5) ** 2 - 1
    except:
        return float("inf")


# 利用函数封装以上代码
theta_history = []

# 梯度下降法求解参数theta
def gradient_descent(initial_theta, eta, n_iters = 1e4, epsilon = 1e-8):
    theta = initial_theta
    i_iter = 0
    theta_history.append(initial_theta)

    while i_iter < n_iters:
        gradient = dJ(theta)
        last_theta = theta
        theta = theta - eta * gradient
        theta_history.append(theta)

        if(abs(J(theta) - J(last_theta)) < epsilon):
            break

        i_iter += 1

    return

# 绘图查看梯度下降过程
def plot_theta_history():
    plt.plot(plot_x, J(plot_x), color="r")
    plt.plot(np.array(theta_history), J(np.array(theta_history)), color="b", marker="*")
    plt.show()
    print(len(theta_history))


# # 不断变化eta的取值，查看梯度下降过程
# eta = 0.01 #eta = 0.01    eta = 0.001     eta = 0.8    eta = 1.1
# theta_history = []
# gradient_descent(0, eta)
# print(len(theta_history))
# plot_theta_history()


# eta取值过大
# # 不断变化eta的取值，查看梯度下降过程
# eta = 1.1  #eta = 0.01    eta = 0.001     eta = 0.8    eta = 1.1
# theta_history = []
# gradient_descent(0, eta)
# print(len(theta_history))
# # plot_theta_history()
# print(theta_history[-1])

# eta = 1.1
# theta_history = []
# gradient_descent(0, eta, n_iters=10)
# plot_theta_history()










