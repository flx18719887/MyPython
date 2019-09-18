# coding=gbk
import numpy as np
import matplotlib.pyplot as plt

# ������x��y
plot_x = np.linspace(-1, 6, 141)
plot_y = (plot_x - 2.5) ** 2 - 1

# �������κ�����ͼ��
plt.plot(plot_x, plot_y)
# plt.show()

# �����ݶ�(����������theta�㴦�ĵ���ֵ)
def dJ(theta):
    return 2 * (theta - 2.5)

# # ������ۺ���
# def J(theta):
#     return (theta - 2.5) ** 2 - 1

# �ݶ��½���
eta = 0.1   # ���岽��
epsilon = 1e-8    # ����һ����ֵ

# theta = 0.0   # ���ó�ֵ
# while True:
#     gradient = dJ(theta)   # �ݶ�
#     last_theta = theta
#     theta = theta - eta * gradient    # �ݶ��½��������theta��ֵ
#
#     if(abs(J(theta) - J(last_theta)) < epsilon):    # ���ۺ����仯ֵ����Ϊ0
#         break
#
# print(theta)
# print(J(theta))

# # ��ͼ
# theta = 0.0   # ���ó�ֵ
# theta_history = [theta]
# while True:
#     gradient = dJ(theta)   # �ݶ�
#     last_theta = theta
#     theta = theta - eta * gradient    # �ݶ��½��������theta��ֵ
#     theta_history.append(theta)
#
#     if(abs(J(theta) - J(last_theta)) < epsilon):    # ���ۺ����仯ֵ����Ϊ0
#         break
#
# plt.plot(plot_x, J(plot_x))
# plt.plot(np.array(theta_history), J(np.array(theta_history)), color="r", marker='+')
# plt.show()
#
# print(len(theta_history))






# ������ۺ���
def J(theta):
    try:
        return (theta - 2.5) ** 2 - 1
    except:
        return float("inf")


# ���ú�����װ���ϴ���
theta_history = []

# �ݶ��½���������theta
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

# ��ͼ�鿴�ݶ��½�����
def plot_theta_history():
    plt.plot(plot_x, J(plot_x), color="r")
    plt.plot(np.array(theta_history), J(np.array(theta_history)), color="b", marker="*")
    plt.show()
    print(len(theta_history))


# # ���ϱ仯eta��ȡֵ���鿴�ݶ��½�����
# eta = 0.01 #eta = 0.01    eta = 0.001     eta = 0.8    eta = 1.1
# theta_history = []
# gradient_descent(0, eta)
# print(len(theta_history))
# plot_theta_history()


# etaȡֵ����
# # ���ϱ仯eta��ȡֵ���鿴�ݶ��½�����
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










