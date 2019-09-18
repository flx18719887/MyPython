# # # 参数分类：
# # 普通参数（位置参数）
# def add(a, b, c):
#     print(a + b +c)
#     return None
#
# print("普通参数（位置参数用法）：")
# add(11, 22, 10)
# # add(10, 12)    # 缺少一个位置参数，报错

# #
# # print("-----------------------------------")
# # 默认参数
# def add(a, b, c=15):
#     print(a + b + c)
#     return None
#
# print("默认参数用法：")
# add(3, 5)

# #
# # print("-----------------------------------")
# # 关键字参数
# def add(a, b, c):
#     print(a + b + c)
#     return None
#
# print("关键字参数用法：")   # 函数调用不依赖参数的位置和顺序
# add(a=10, b=20, c=30)
# add(b=11, c=12, a=13)
# #
# #
# # print("------------------------------------------------------")
# # # 递归函数
# # def fun(n):
# #     print(n)
# #     # 递归一定要有结束条件
# #     if n==1:
# #         return 1
# #     else:
# #         return n * fun(n-1)
# #
# # print(fun(6))
# #
# #
# # print("------------------------------------------------------")
#
#
#
# # 在定义函数时，它的输入变量被称为函数的形参。
# # 执行函数时的输入变量被称为实参。
#
# # 更改实参
# # 对于不可变的参数(字符串，数字，元组)，更改函数内部的实参值通常不会影响函数外部的实参值。
# def subtract(x1, x2):
#     z =x1 - x2
#     x2 = 30
#     return z
# a = 50
# b = subtract(80, a)
# print(b)
# print(a)
#
#
# print("-------------------------------------------------------")
# # 对于可变的参数(字符串，数字，元组)，更改函数内部的实参值通常会影响函数外部的实参值。
# def subtract(x):
#     z =x[0] - x[1]
#     x[1] = 40
#     return z
# a = [10, 30]
# b = subtract(a)
# print(b)
# print(a)
#
#
# import matplotlib.pyplot as plt
# # 代码有误
# data = [[1, 2], [3, 4]]
# style = dict({'linewidth':3, 'marker':'o', 'color':'green'})
# plt.plot(*data, **style)
#
#
#
# print("------------------------------------------")
# def func(a, b, c):
#     return a + b + c
#
# arglist = [3, 4, 5]
# print(func(*arglist))
#
#
#
# print("------------------------------------------")
# def func(*args):
#     s = 0
#     for a in args:
#         s += a
#     return s
#
# args = [10, 20, 30]
# print(func(*args))
#
#
#
#
# import matplotlib.pyplot as plt
# # 代码有误
# data = [[1, 2], [3, 4]]
# style = dict({'linewidth':3, 'marker':'o', 'color':'green'})
# plt.plot(*data, **style)




# 非固定传参
# 　　　　这种传参方式可就大有讲究了，花样可谓繁多，自然本领也就大多了，不信往下看。
# 　　　　可以细分为两类：
#
# 　　　　非固定传参方式一:
# 　　　　　　　可同时指定多个用户，传过来的所有参数打包成元祖。如下：
#方式一
#
#
# 非固定传参方式二: 　　　　　　　
# 　　　　　　　　可同时指定多个用户，传过来的所有参数打包成元组或字典。如下：
def func(name,*args,**kwargs):  # 形参依次是位置参数，元组，字典
    print(name,args,kwargs)

func('Hope',22,'CN','tomorrow') #输出：Hope (22, 'CN', 'tomorrow') {}
func('Try',21,'will',addr='HG',num=666) #输出：Try (21, 'will') {'addr': 'HG', 'num': 666}

dit = {'major':'Math','interest':'reading'}
func('want',*['day','up'],**dit) #输出：want ('day', 'up') {'major': 'Math', 'interest': 'reading'}

