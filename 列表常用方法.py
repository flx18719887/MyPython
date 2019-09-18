# 列表中添加元素
mlist = ["fff", "fl", "ls", "jfl", "jfal"]
print(mlist)
mlist.append("flx")
print(mlist)
mlist.extend(["lx", "fu"])
print(mlist)
mlist.insert(3, "ul")
print(mlist)


# 列表中删除元素
mlist.remove("ls")
print(mlist)
del mlist[2]
print(mlist)
mlist.pop()
print(mlist)
mlist.pop()
print(mlist)

# 列表的切片
print(mlist)
nlist = mlist[2:4]
print(nlist)


# 列表的操作符
# 比较操作符
list1 = [123]
list2 = [234]
print(list1 < list2)
print(list1 > list2)

list1 = [956, 234]
list2 = [678, 123]
print(list1 < list2)
print(list1 > list2)
print(list1 +list2)


mlist = [4, 2, 5, 1, 8, 9]
mlis1 = mlist
mlis2 = mlist[:]   # 列表的拷贝
mlist.pop()
mlist.sort()   # 列表排序
mlist.reverse()    # 列表反转
print(mlist)
print(mlis1)
print(mlis2)


# 列表合并——zip
# zip将两个给定的列表合并成一个新的列表，其结果是一个元组列表
# 合并列表的长度为两个输入列表中长度较短的那个
mlist1 = ["Jack", "Mack", "Luck", "Mary"]
mlist2 = [12, 23, 32, 15, 16]
mlist = list(zip(mlist1, mlist2))
print(mlist1)
print(mlist2)
print(mlist)
# 将两个列表转换为字典，一个列表作为字典的键，另一个列表作为字典的值
mdict = dict(zip(mlist1, mlist2))
print(mdict)


# 列表推导
L = [1, 2, 3, 4, 5, 6]
L1 = [2 * i for i in L]
L2 = [2 * i for i in  L if 2 < i < 6]
print(L)
print(L1)
print(L2)

print("------------------------------------------------------")
M = [[1, 2, 3], [4, 5, 6]]
Mlist = [M[i][j] for i in range(2) for j in range(3)]
print(Mlist)



# 列表（list）目的是存储或操作一组数据的集合。
# 当我有一百个数据要进行储存的时候，我可以选择用100个变量分别进行储存，但显然这不是一个更好的方案。
# 我们可以用一个集合形式的数据结构，把这一百个数据储存到一块，需要的时候再分别进行提取。
# 这就是列表、集合等数据类型存在的意义。
# 我们可以把它想象成一个大桶，当我们有一堆东西需要找个地方临时存放在一起，
# 以便后续进行排序、筛选等操作时，就可以弄一个列表，把这些东西放进去。
# 列表的定义方法：
# 列表是一种可变的数据类型；列表中的数据类型不限；列表中的多个值之间用逗号进行分割
list1 = [1234, 'Hello', 3.14, True, 'abc']  #  列表中的内容可以是任意的数据类型
print(list1)   # [1234, 'Hello', 3.14, True, 'abc']
list2 = [33434,
         '你好', 4545.565555,
         'iii',
         True]
print(list2)    # [33434, '你好', 4545.565555, 'iii', True]
list3 = [1, 2, 3, 'Hello', [1, 2, 3, 4, 5]]    # 二维列表
print(list3)    # [1, 2, 3, 'Hello', [1, 2, 3, 4, 5]]
list4 = [1, 2, 3, 'Hello', [1, 2, [1, [1, 2, 3], 3] , 4, 5 ]]  # 二维列表
print(list4)    # [1, 2, 3, 'Hello', [1, 2, [1, [1, 2, 3], 3], 4, 5]]
# 列表：有序的序列，所以每一个数据都有唯一对应的索引值。
# 列表的索引语法：列表[start:stop:step]
# 列表[起始位置:终止位置:步长和方向]，开始的位置包含在内，而终止的位置不包含在内
# 步长的默认值为1，当步长设置为正整数，代表方向从左往右，
# 当步长设置为负整数，代表从后往前进行切片
# 起始位置和终止位置，如果不填，代表从头到尾所有数据

# 二维列表的索引方法：
list5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list5)     # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list5[0][1])    # 2
print(list5[-1])     # [7, 8, 9]
print(list5[::-1])    # 反转     [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

# 更改列表中的值
list6 = ['零', '一', '二', '三', '四', '五', '六']
print(list6)     # ['零', '一', '二', '三', '四', '五', '六']
list6[1] = '壹'
print(list6)   # ['零', '壹', '二', '三', '四', '五', '六']
list6[2:5] = 2, 3, 4
print(list6)    # ['零', '壹', 2, 3, 4, '五', '六']

# test = [['python','C','C++','Java'],['Ruby','R','shell'],['go','Scala']]
test = [['python', 'C', 'C++', 'Java'], ['Ruby', 'R', 'shell'], ['go', 'Scala']]
print(test)  # [['python', 'C', 'C++', 'Java'], ['Ruby', 'R', 'shell'], ['go', 'Scala']]
# 1. 索引出C++，索引出R
print(test[0][2])  # 'C++'
print(test[1][1])  # 'R'
# 2. 同时索引出（C++和 Java）
print(test[0][2:])  # ['C++', 'Java']
# 3. 把列表中的go改成大写
test[2][0] = test[2][0].upper()
print(test)  # [['python', 'C', 'C++', 'Java'], ['Ruby', 'R', 'shell'], ['GO', 'Scala']]
# 4. 把python和C的大小写进行交换
test[0][0] = test[0][0].upper()
test[0][1] = test[0][1].lower()
print(test)  # [['PYTHON', 'c', 'C++', 'Java'], ['Ruby', 'R', 'shell'], ['GO', 'Scala']]


# 检查特定值是否包含在序列中，我们可使用运算符in。
#它检查是否满足指定的条件，并返回相应的值：满足时返回True，不满足时返回False
x = 'abcd'
print('a' in x)  # True
print('e' in x)   # False



# 列表的浅复制和深复制
a = [1, 2, 3]
b = a
print(b)   # [1, 2, 3]
b[1] = 4
print(a)   # [1, 4, 3]

# 要让a和b指向不同的列表，就必须将b关联到a的副本。
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)   # [1, 2, 3]
print(b)  # [1, 4, 3]
# 这类似于使用a[:]或list(a)，它们也都复制a。
a = [1, 2, 3]
b = a[:]
print(b)      # [1, 2, 3]


