# 异常处理是编写可靠和可用代码的重要组成部分。
if __name__ == '__main__':

# 如果文件不存在，则会捕捉到OSError；如果文件第一行中的数据与浮点数据类型不兼容，则会捕捉到ValueError。
    try:
        f = open("data.txt", 'r')
        data = f.readline()
        value = float(data)
    except OSError as oe:
        print("{}: {}".format(oe.strerror, oe.filename))
    except ValueError:
        print("Could not convert data to float.")


print("---------------------------------------------------")
import random
if __name__ == '__main__':

# 要求：生成一个随机数，如果该数字小于0.5,则会出现异常并打印该值太小的消息；如果没有引发异常，则打印该数字。
    # 用户自定义异常
    class MyError(Exception):
        def __init__(self, expr):
            self.expr = expr
        def __str__(self):
            return str(self.expr)

    try:
        x = random.random()
        if x < 0.5:
            raise MyError(x)
    except MyError as e:
        print("Random number too small", e.expr)
    else:
        print(x)
















