mstr = "my name is flx and flx, flx, flx"
# find():  包含子字符串，返回开始的索引值，否则返回-1
print(mstr.find("flx", 1, 20))
print(mstr.find("num"))

# index():  包含子字符串，返回开始的索引值，否则抛出异常
print(mstr.index("flx", 1, 20))
print(mstr.index("num", 1, 20))

# count(): 返回子字符串在字符串中出现的次数
print(mstr.count("flx", 1, 40))
print(mstr.count("fux", 1, 40))


# replace(): 返回字符串中的旧字符串替换成新字符串后生成的新字符串
print(mstr.replace("flx", "fux", 3))
print(mstr.replace("flx", "fux"))


# split():返回分隔后的字符串列表
print(mstr.split(" ", 2))  # 字符串分隔，分隔符默认为所有的空字符，分隔次数默认为-1，即分隔所有。
print(mstr.split((" ,")))
print(mstr.split((" flx")))


# capitalize():返回一个首字母大写的字符串
print(mstr.capitalize())


# startswith():检查字符串是否以指定的子字符串开头。如果检测到字符串，则返回True,否则返回False。
print(mstr.startswith("name"))
print(mstr.startswith("my"))


# endswith():判断字符串是否以指定的后缀结尾。如果以指定的后缀结尾则返回True,否则返回False。
print(mstr.endswith("lx"))
print(mstr.endswith("ux"))
print(mstr.endswith("x"))


mstr1 = "   you are a beautiful girl"
# ljust():返回原字符串左对齐并使用空格填充至指定长度的新字符串。如果指定长度小于原字符串的长度则返回原字符串。
print(mstr1.ljust())

import numpy as np
from numpy import linalg
A = matrix([[1, 1, -1], [1, -1, 1], [-1, 1, 1]])
A2 = np.linalg.inv(A)
print(A2)




m1 = set((1,2))
m2 = set((3, 4, 5,6))
print(m1 <= m2)

mstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_@!#$%^&*()_+"
for i in len(mstr):
    # if mstr[i].isdigit():
    print(mstr[i])


import random
x=[random.randint(0,10) for i in range(30)]
print(x)



str = "I love fishc "
str1 = str[:5] + "jifaj;lgja" + str[5:]
print(str1)



print(sorted([111, 2, 33], key=lambda x: len(str(x))))

import math
print(math.fabs(-4.321))
counter = 1
def doLotsOfStuff():
    global counter
    for i in (1, 2, 3):
        counter += 1
doLotsOfStuff()
print(counter)


x = {1, 2, 3}
x.add(3)
print(x)


a = [1,2,3,None,(),[],]
print(len(a))

x = 'abcdefg'
print(x[3:] + x[:3])

print(len('SDIBT'))

print({1,2,3,4}-{3,4,5,6})


a = [1, 2, 3, 4, 5, 6]
print(a[-2::-2])


a=int(16**0.5)
b=int(2**2)
print(a == b)


def fun1(x,li=[]):
    for i in range(x):
        li.append(i*i)
    print(li)
fun1(2)


for i in range(3):
      print(i)





testList = ["l", "o", "v", "e"]
print(id(testList))
print(testList)

testList += testList
print(id(testList))
print(testList)

sStr1 = 'strcpy'
sStr2 = sStr1
sStr1 = 'strcpy2'
print(sStr2)


mstr = 'abCDef'
print(mstr[:len(mstr)//2+1].upper() + mstr[len(mstr)//2+1:].lower())
# 前半部分大写，后半部分小写，如果字符个数为奇数，中间字符大写





# 由于str是不可变的序列，其实只有查找方法，增删改不会改变字符串本身，只是结果改变。
# 1. 查
# (1) 检测字符串是否包含子串：index和find
# 两者区别在于如果没有找到，find返回-1，index报错
print('abc123'.index('c1'))     # 2
print('abc123'.find('c1'))      # 2
print('abc123'.find('c2'))      # -1
print('abc123'.index('c2')  )   # 出错
# (2) 统计子串出现次数：count
print('abc123abc'.count('b'))      # 2
# 2. 增
# (1) 用分隔符拼接字符串：join
print('1234'.join('abcd') )       # a1234b1234c1234d
# (2) 连接字符串：使用运算符  +
# (3) 复制字符串：使用运算符  *
# 3. 删
# (1) mystr.strip(|指定字符|) 删除字符串两端的指定字符，如果不指定默认是空格
print('#abc##'.strip('#') )     # abc
print(' abc '.strip())        # abc
# 另外，lstrip和rstrip，分别是删除左边空格和删除右边空格
# 4. 改
# (1) 转换小写：lower()
print('aBcD'.lower())      # abcd
#(2) 转换大写：upper()
print('aBcD'.upper())     # ABCD
#(3) 首字母大写，其他小写：capitalize()
print('aBcD'.capitalize())     # Abcd
#(4) 交换大小写：swapcase()
print('aBcD'.swapcase())      # AbCd
# 5. 分割
# split([分隔符]) 默认是空格，\t，\n分割
print('I love you'.split())    # 返回3个元素的列表
print('a#b#c'.split('#') )     # 返回3个元素['a','b','c']的列表
# 6. 检测
# startswith(prefix[,start [,end]])   # 是否以prefix开头
# endswith(suffix[,start[,end]])    # 以suffix结尾
# isalnum()     # 是否全是字母和数字，并至少有一个字符
# isalpha()     # 是否全是字母，并至少有一个字符
# isdigit()     # 是否全是数字，并至少有一个字符
# isspace()     # 是否全是空白字符，并至少有一个字符
# islower()     # str中的字符是否全是小写
# isupper()     # str中的字符是否全是大写
# istitle()     # str是否是首字母大写



# 判断字符串内的元素类型
# mystr.isalpha()：如果mystr所有字符都是字母，则返回True，否则返回False
# mystr.isdigit()：如果mystr只包含数字，则返回True，否则返回False
# mystr.isalnum()：如果mystr所有字符都是字母或数字，则返回True，否则返回False
# mystr.isspace()：如果mystr中只包含空格，则返回True，否则返回False
# mystr.islower()：如果mystr中的字母全是小写，则返回True，否则返回False
# mystr.isupper()：如果mystr中的字母全是大写，则返回True，否则返回False
# mystr.istitle()：如果mystr中的首字母大写，则返回True，否则返回False
str_2 = 'abferfsl34567ABC2'
str_2    # 'abferfsl34567ABC2'
str_2.isalpha()   # False
str_2.isdigit()   # False
str_2.isalnum()   # True
str_2.isspace()   # False
str_2.islower()   # False
str_2.isupper()   # False
str_2.istitle()   # False



# mystr中每个字符后面插入str，构造出一个新的字符串
# mystr.join(str)
'--->'.join('北京大学在北京')   # '北--->京--->大--->学--->在--->北--->京'
'==='.join('|--快使用双截棍--|')


# 把mystr以str分割成三部分，str前，str和str后
# mystr.partition(str)
a = 'abcdefgabcde'
print(a)    # 'abcdefgabcde'
print(a.split('e'))   # ['abcd', 'fgabcd', '']
print(a.partition('e'))  # ('abcd', 'e', 'fgabcde')


# 删除mystr字符串两端的指定字符，如果不指定默认是空格
# mystr.strip()
b = ' Goo gle '
print(b)    # ' Goo gle '
print(b.strip())   # 'Goo gle'
c = '* Goo gle '
print(c)   # '* Goo gle '
print(c.strip('*'))   # ' Goo gle '
print(c.strip())   # '* Goo gle'
print(c.strip('* '))   # 'Goo gle'

str_me = 'abCDdfGHabd'
print(str_me)  # 'abCDdfGHabd'
# 转换mystr中所有大写字符为小写
# mystr.lower()
print(str_me.lower())  # 'abcddfghabd'

# 转换 mystr 中的小写字母为大写
# mystr.upper(
print(str_me.upper())  # 'ABCDDFGHABD'



# 按照行分隔，返回一个包含各行作为元素的列表
# mystr.splitlines()
lst1 = '''关于你
关于你，我有太多东西关于你。
清醒的时候放不下矜持，不敢说我喜欢你，只有在某个夜晚多愁善感又萦绕在心头，或是朋友聚会上的大醉，才敢借着情绪
说，我喜欢你，喜欢了好久好久。'''
lst1 = lst1.splitlines()
print(lst1[1])   # '关于你，我有太多东西关于你。'
print(lst1[3])   # '说，我喜欢你，喜欢了好久好久。'



# 以 str 为分隔符切片mystr，如果maxsplit有指定值，则仅分隔maxsplit个字符串
# mystr.split(str=" ", 2)
a = 'abcdefgabc'
print(a)    # 'abcdefgabc'
print(a.split('b'))    # ['a', 'cdefga', 'c']
print(a.split('e'))   # ['abcd', 'fgabc']
print(a.split('q'))    # ['abcdefgabc']
print(a.split('c'))    # ['ab', 'defgab', '']
print(a.split('cd'))   # ['ab', 'efgabc']
print(a.split('b', 1)) # ['a', 'cdefgabc']



# 把mystr中的str1替换成str2,如果count指定,则替换不超过count次
# mystr.replace(str1, str2, mystr.count(str1))
a = 'abcdefgababacjhkleeejmn'
print(a.replace('a', '哈哈', 1))   # '哈哈bcdefgababacjhkleeejmn'
print(a.replace('a', '哈哈哈'))   # '哈哈哈bcdefg哈哈哈b哈哈哈b哈哈哈cjhkleeejmn'
print(a.replace('a', 'k'))  # 'kbcdefgkbkbkcjhkleeejmn'
print(a)  #'abcdefgababacjhkleeejmn'    注意替换之后a并没有改变



# 返回 str 在 start 和 end 之间在mystr里里面出现的次数
# mystr.count(str, start=0, end=len(mystr))
a = 'abcdefgababacjhkleeejmn'
print(a.count('e'))   # 4
print(a.count('e', 0, 5))  # 1
print(a.count('ba'))  # 2


# 检测 str 是否包含在mystr中,如果是则返回开始的索引值,否则返回-1
# mystr.find(str, start=0, end=len(mystr))
a = 'abcdefgabc'
q = a.find('a', 2, 3)
print(q)   # -1
print(a[a.find('e')])
k = a.find('abc', 3)
print(k)  # 7
print(a[k:k+2])   # 'ab'



str = 'cda123cda'    # 'cda123cda'
print(str[0])   # 'c'    获取第一个元素
print(str[-2]) # 'd'    获取倒数第二个元素
print(str[1:3]) # 'da'  获取从偏移为1的字符一直到偏移为3的字符串，不包括偏移为3的字符串
print(str[1:]) # 'da123cda'   获取从偏移为1的字符一直到字符串的最后一个字符（包括最后一个字符）
print(str[:3]) # 'cda'  获取从偏移为0的字符一直到偏移为3的字符串，不包括偏移为3的字符串
print(str[:-1]) # 'cda123cd'   获取从偏移为0的字符一直到最后一个字符（不包括最后一个字符串）
print(str[:]) # 'cda123cda' 获取字符串从开始到结尾的所有元素
print(str[-3:-1]) # 'cd'  获取偏移为-3到偏移为-1的字符，不包括偏移为-1的字符
print(str[-1:-3])   #  ''  获取的为空字符，系统不提示错误
print(str[2:0]) #  '' 获取的为空字符，系统不提示错误
print(str[::2]) #  'ca2ca'   步长为2，方向从左到右
print(str[-1:-5:-2]) #  'ac'  步长为2，方向从右往左str




