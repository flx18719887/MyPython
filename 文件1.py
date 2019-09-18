读取文件：
file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "r")   # 打开文件，返回文件对象
strVar = My_file.read()  # 读取文件全部内容
print(strVar)
My_file.close()   # 关闭文件

file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "r")   # 打开文件，返回文件对象
line = My_file.readline()  # 读取某一行文件内容
while line != "":
    print(line)
    line = My_file.readline()
My_file.close()   # 关闭文件

file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "r")   # 打开文件，返回文件对象
first_line = My_file.readline()
second_line = My_file.readline()
My_file.seek(0)   # 文件指针移动到文件起始位置
new_line = My_file.readline()
print(new_line)
My_file.close()   # 关闭文件


file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "r")   # 打开文件，返回文件对象
lines = My_file.readlines()
print(lines)
My_file.close()   # 关闭文件



# 写入文件：
file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "a")   # 打开文件，返回文件对象
My_file.write("\n Do you like Python?")
My_file.close()   # 关闭文件

file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "r")   # 打开文件，返回文件对象
strVar = My_file.read()  # 读取文件全部内容
print(strVar)
My_file.close()   # 关闭文件

file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "w")   # 打开文件，返回文件对象
My_file.write("今天是个好的天气")
My_file.close()   # 关闭文件



file = "C:\\Users\\Administrator\\Desktop\\hello.txt"   # 定义文件路径
My_file = open(file, "r")   # 打开文件，返回文件对象
strVar = My_file.read()  # 读取文件全部内容
print(strVar)
My_file.close()   # 关闭文件


# 文件：长久保存信息的一种数据信息集合
# 文件常用操作：
# （1）打开关闭（文件一旦打开，需要关闭操作）
# （2）读写内容
# （3）查找
# open函数：打开文件
# - open函数负责打开文件，带有很多参数
# - 第一个参数：必须有，文件的路径和名称
# - mode：表明文件用什么方式打开
#     - "r"：以只读方式打开
#     - "w"：写方式打开，会覆盖以前的内容
#     - "x"：创建方式打开，如文件已经存在，报错
#     - "a"：append方式，以追加的方式对文件内容进行写入
#     - "b"：binary方式，二进制方式写入
#     - "t"：文本方式打开
#     - "+"：可读写

# 打开文件，用写的方式
# f称之为文件句柄
# r表示后面字符串内容不需要转义
f = open(r"C:\Users\Administrator\Desktop\hello3.txt", 'w')
# 如果以写方式打开文件，默认是如果没有文件，则创建
f.write("nizaiganshneme")
# 文件打开后必须关闭
f.close()



with open(r"C:\Users\Administrator\Desktop\hello3.txt", 'r') as f :
    pass
    # 下面语句块开始对文件f进行操作
    # 在本模块中不需要再使用close关闭文件f

with open(r"C:\Users\Administrator\Desktop\hello3.txt", 'r') as f :
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline)
        strline = f.readline()



# seek(offset, from)
# - 移动文件的读取位置，也叫读取指针
# - from的取值范围：
#     - 0：从文件头开始偏移
#     - 1：从文件当前位置开始偏移
#     - 2：从文件末尾开始偏移
# - 移动的单位是字节（byte）
# - 一个汉字由若干个字节构成
# - 返回文件只针对当前位置

# 打开文件后，从第5个字节处开始读取
# 打开读写指针在0处，即文件的开头
with open(r"C:\Users\Administrator\Desktop\hello3.txt", 'r') as f :
    # seek移动单位是字节
    f.seek(4,0)
    strChar = f.read()
    print(strChar)

# 关于读取文件的练习
# 打开文件后，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟
# 让程序暂停，可以使用time下的sleep函数
import time
with open(r"C:\Users\Administrator\Desktop\hello3.txt", 'r') as f :
    # read参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar)
        # sleep参数单位是秒
        time.sleep(1)
        strChar = f.read(3)

# tell函数：用来显示文件读写指针的当前位置
with open(r"C:\Users\Administrator\Desktop\hello3.txt", 'r') as f :
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)
        strChar = f.read(3)
        pos = f.tell()
        print(pos)
        print(strChar)

# 以下结果说明：
# tell的返回数字的单位是byte
# read是以字符为单位的

# 文件的写操作-write
# - write(str):把字符串写入文件
# - writeline(str):把字符串按行写入文件
# - 区别：
#        - write函数参数只能是字符串
#        - writeline函数参数可以是字符串，也可以是字符序列

# 向文件追加一句诗
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'a') as f:
    # 注意字符串含有换行符
    f.write("\n生命的美好不仅在于运动， \n还在于挑战")

# 可以直接写入行，用writelines
# writelines表示写入很多行，参数可以是list格式
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'a') as f:
    # 注意字符串含有换行符
    f.writelines("生命的美好不仅在于运动")
    f.writelines("最美好的生活")

mlist = ["I", "love", "milk"]
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'w') as f:
    # 注意字符串内含有换行符
    f.writelines(mlist)


# 持久化：pickle
# - 序列化（持久化）：把程序运行中的信息保存在磁盘上
# - 反序列化：序列化的逆过程
# - pickle：python提供的序列化模块
# - pickle .dump:序列化
# - pickle.load:反序列化
# 序列化
import pickle
age = 18
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'wb') as f:
    pickle.dump(age, f)

# 反序列化
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'rb') as f:
    age = pickle.load(f)
    print(age)

# 序列化
import pickle
a = [12, "fulx", "I like shoping", [165, 50]]
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'wb') as f:
    pickle.dump(a, f)

# 反序列化
with open(r"C:\Users\Administrator\Desktop\hello.txt", 'rb') as f:
    a = pickle.load(f)
    print(a)

# 持久化-shelve
# - 持久化工具
# - 类似字典，用kv对保存数据，存取方式跟字典也类似
# - open, close
# 使用shelve创建文件并使用
import shelve
# 打开文件
# shv相当于一个字典
shv = shelve.open(r"C:\Users\Administrator\Desktop\Myfile\shv.db")
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3
shv.close()

# 通过以上案例发现，shelve自动创建的不仅仅是一个shv.db文件，还包括其他格式文件
# shelve读取案例
shv = shelve.open(r"C:\Users\Administrator\Desktop\Myfile\shv.db")
try:
    print(shv['one'])
    print(shv['threee'])
except Exception as e:
    print("烦死了")
finally:
    shv.close()



