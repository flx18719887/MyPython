# 集合对象支持union（联合），intersection（交），difference（差）和sysmmetric difference（对称差集）等数学运算
# 1. 添加元素：set.add(x)
# 将元素x添加到集合s中，如果元素已存在，则不进行任何操作：
s = set(('Google', 'Facebook', 'Alibaba', 'Amazon'))
s     # {'Alibaba', 'Amazon', 'Facebook', 'Google'}
s.add('Baidu')
print(s)    # {'Amazon', 'Google', 'Baidu', 'Facebook', 'Alibaba'}
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下
# set.update(x)    # x 可以有多个，用逗号分开
s = set(('Google', 'Facebook', 'Alibaba', 'Amazon'))
s     # {'Alibaba', 'Amazon', 'Facebook', 'Google'}
s.update({1, 2, 3})
print(s)    # {'Alibaba', 1, 2, 3, 'Facebook', 'Amazon', 'Google'}
s.update([1, 2], [3, 4])
print(s)    # {'Alibaba', 1, 2, 3, 4, 'Facebook', 'Amazon', 'Google'}

# 2. 移除元素
# set.remove(x)
# 将元素x从集合s中移除，如果元素不存在，则会发生错误
s = set(('Google', 'Facebook', 'Alibaba', 'Amazon'))
s     # {'Alibaba', 'Amazon', 'Facebook', 'Google'}
s.remove('Amazon')
print(s)    # {'Facebook', 'Google', 'Alibaba'}
# s.remove('Baidu')    # 报错，元素不存在

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
# set.discard(x)
s = set(('Google', 'Facebook', 'Alibaba', 'Amazon'))
s      # {'Alibaba', 'Amazon', 'Facebook', 'Google'}
s.discard('Facebook')
print(s)    # {'Amazon', 'Google', 'Alibaba'}
s.discard('Baidu')    # 不存在不会发生错误
print(s)

# 我们也可以设置随机删除集合中的一个元素，语法格式如下：
# set.pop()
s = set(('Google', 'Facebook', 'Alibaba', 'Amazon'))
s      # {'Alibaba', 'Amazon', 'Facebook', 'Google'}
x = s.pop()
print(x)   # Facebook
print(s)   # {'Amazon', 'Google', 'Alibaba'}

# 在交互模式，pop是删除集合的第一个元素（整理后的集合的第一个元素）
s = set(('Google', 'Facebook', 'Baidu', 'Amazon'))
s      # {'Amazon', 'Baidu', 'Facebook', 'Google'}
s.pop()
print(s)   # {'Baidu', 'Amazon', 'Google'}

# 3. 计算集合元素个数：len(set)
s = set(('Google','Facebook','Alibaba','Amazon', 'Baidu'))
len(s)   # 5

# 4. 清空集合： set.clear()
s = set(('Google','Facebook','Alibaba','Amazon', 'Baidu'))
print(s)    # {'Amazon', 'Google', 'Baidu', 'Facebook', 'Alibaba'}
s.clear()
print(s)   # set()

# 5. 判断元素是否存在于集合中： x in s
# 判断元素x是否在集合s中，存在返回True，不存在返回False
s = set(('Google','Facebook','Alibaba','Amazon', 'Baidu'))
print(s)    # {'Amazon', 'Google', 'Baidu', 'Facebook', 'Alibaba'}
'Facebook' in s   # True
'baidu' in s    # False

# s1 & s2 交集                 s1.intersection(s2)
# s1 | s2 并集                 s1.union(s2)
# s1 - s2 差集                 s1.difference(s2)
# s1 ^ s2 对称差               s1.symmetric_difference(s2)
# s1 <= s2 是否是s2的子集      s1.issubset(s2)
# s1 >= s2 是否是s2的超集      s1.issuperset(s2)
# s1 |= s2 用s2更新s1          s1.update(s2)

# 1. set.intersection()
# intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。
# 语法：  set.intersection(set1,set2,...)
# set1：必需，代表要查找相同元素的集合。
# set2：可选，代表其他要查找相同元素的集合。这里可以是多个，但需要使用逗号隔开。
# 返回值：返回一个新的集合。

# 实例：返回一个新集合，该集合的元素既包含在集合x中，又包含在集合y中：
x = {'apple', 'banana', 'lemon'}
y = {'Google', 'Facebook', 'apple'}
z = x.intersection(y)
print(z)  # {'apple'}

# 计算多个集合的交集：
x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'c', 'g', 'h'}
result = x.intersection(y, z)
print(result)  # {'c'}

# 2. set.union()
# union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。
# 语法： set.union(set1,set2,...)
# set1：必需，代表合并的目标集合。
# set2：可选，代表其他要查找相同元素的集合。这里可以是多个，但需要使用逗号隔开。
# 返回值：返回一个新集合。
# 实例：合并两个集合，重复元素只会出现一次
x = {'apple', 'banana', 'lemon'}
y = {'Google', 'Facebook', 'apple'}
z = x.union(y)
print(z)  # {'banana', 'apple', 'lemon', 'Facebook', 'Google'}

# 合并多个集合：
x = {'a', 'b', 'c'}
y = {'c', 'd', 'e'}
z = {'f', 'g', 'h'}
result = x.union(y, z)
print(result)  # {'b', 'd', 'e', 'h', 'c', 'g', 'f', 'a'}

# 3. set.difference()
# difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合（方法的参数）中。
# 语法： set.difference(set)
# set：必需，用于计算差集的集合。
# 返回值：返回一个新的集合。
# 实例：返回一个集合，元素包含在集合x中，但不在集合y中。
x = {'apple', 'banana', 'lemon'}
y = {'Google', 'Facebook', 'apple'}
z = x.difference(y)
print(z)  # {'banana', 'lemon'}
p = y.difference(x)
print(p)  # {'Google', 'Facebook'}

# 4. set.symmetric_difference()
# symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
# 语法： set.symmetric_difference(set)
# 参数：set集合
# 返回值：返回一个新的集合。
# 实例：返回两个集合组成的新集合，但会移除两个集合的重复元素
x = {'apple', 'banana', 'lemon'}
y = {'Google', 'Facebook', 'apple'}
z = x.symmetric_difference(y)
print(z)  # {'lemon', 'Google', 'banana', 'Facebook'}

# 5. set.issubset()
# issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回True，否则返回False。
# 语法：set.issubset(set)
# 参数：set：必需，用来比较查找的集合。
# 返回值：返回布尔值，如果都包含返回True，否则返回False。
# 实例：判断集合x的所有元素是否都包含在集合y中
x = {'a', 'b', 'c'}
y = {'f', 'e', 'd', 'c', 'b', 'a'}
z = x.issubset(y)
print(z)  # set.issubset(set)
t = {'o', 'p', 'q'}
r = t.issubset(y)
print(r)  # False

# 6. set.issuperset()
# issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回True，否则返回False。
# 语法：set.issuperset(set)
# 参数：set：必需，用来比较查找的集合。
# 返回值：返回布尔值，如果都包含返回True，否则返回False。
# 实例：判断集合y的所有元素是否都包含在集合x中：
x = {'f', 'e', 'd', 'c', 'b', 'a'}
y = {'a', 'b', 'c'}
z = x.issuperset(y)
print(z)  # True
# 如果没有全部包含返回False：
x = {'f', 'e', 'd', 'c', 'b'}
y = {'a', 'b', 'c'}
z = x.issuperset(y)
print(z)  # False

# 7. set.update()
# update() 方法用于修改当前集合，可以添加新的元素或集合到当前集合中，
# 如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。
# 语法：set.update(set)
# 参数：set：必需，可以是元素或集合。
# 返回值：无
# 实例：合并两个集合，重复元素只会出现一次
x = {'apple', 'banana', 'lemon'}
y = {'Google', 'Facebook', 'apple', 'orange'}
x.update(y)
print(x)  # {'banana', 'apple', 'lemon', 'Facebook', 'Google', 'orange'}

# 1. set.isdisjoint()
# isdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回True，否则返回Fasle。
# 语法：set.isdisjoint(set)
# 参数：set：必需，要比较的集合
# 返回值：返回布尔值，如果不包含返回True，否则返回False。
# 实例：判断集合y中是否有包含集合x的元素
x = {'apple','banana','lemon'}
y = {'Google','Facebook','Amazon'}
z = x.isdisjoint(y)
print(z)    # True
x = {'Google','banana','lemon'}
y = {'Google','Facebook','Amazon'}
z = x.isdisjoint(y)
print(z)    # False

# 2. set.symmetric_difference_update()
# symmetric_difference_update() 方法移除当前集合中在另外一个指定集合相同的元素，
# 并将另外一个指定集合中不同的元素插入到当前集合中。
# 语法：set.symmetric_difference_update(set)
# 参数：set：要检测的集合
# 返回值：None
# 实例：在原始集合x中移除与y集合中的重复元素，并将不重复的元素插入到集合x中。
x = {'apple','banana','lemon'}
y = {'Google','Facebook','apple'}
x.symmetric_difference_update(y)
print(x)   # {'lemon', 'Google', 'banana', 'Facebook'}

