# 关键字lambda用来定义匿名函数（没有名称且由单个表达式所描述的函数）
# lambda函数的定义只能由单个表达式组成，尤其是不能包含循环。
s = lambda x: x ** 2 + 3
print(s(3))


# 任何lambda结构都可以用一个显示定义函数来替换
s = lambda x: x ** 2 + 3

def s1(x):
    return x ** 2 + 3

print("lambda函数输出结果：", s(5))
print("普通函数输出结果：", s1(5))


# 使用lambda结构的主要原因是：对于非常简单的函数进行完整的定义非常麻烦。




















