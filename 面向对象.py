# 类：抽象，描述的是一个集合，侧重于共性
# 对象：具体，描述的是个体
# 类的内容：动作(函数)；属性(变量)


# 定义学生类，和几个学生
class Student():
    name = "flx"
    age = 13
    course = "Python"

    def giveMeMoney(self):
        print("Show me money")
        return  None

    def giveYourMoney(haha):
        print("Show your money")
        return  None

stu = Student()
print(stu.name)
print(stu.age)
print(stu.course)

# self :可以用别的名称代替。self不是关键字，作用是指代本身
# 实例调用函数
stu1 = Student()
# 因为默认实例作为第一个参数传入
stu1.giveMeMoney()    # 此处的参数是stu1
stu1.giveYourMoney()




class Student():
    name = "July"
    age = 20

    def sayHi(self):
        print("My name is {}, I am {} years old".format(self.name, self.age))
        return None

haha = Student()
haha.sayHi()


class Student2():
    name = "July"
    age = 20

    def sayHi(self, n, a):
        self.name = n
        self.age = a

        print("My name is {}, I am {} years old".format(self.name, self.age))
        return None

haha = Student2()
haha.sayHi("haha", 16)
print("My name is {}, I am {} years old".format(Student2.name, Student2.age))
print("My name is {}, I am {} years old".format(haha.name, haha.age))




class Student3():
    name = "Mack"
    age = 10

    # 构造函数
    def __init__(self):
        print("我是构造函数")

haha = Student3()
print("--------------------------------------")
print(haha.name)
print(haha.age)























































