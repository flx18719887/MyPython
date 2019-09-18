# coding=gbk
# import copy
# mlist = [1,2,[3,4]]
# nlist = copy.deepcopy(mlist)
# mlist[2] = 'a'
# print(mlist)   # [1, 2, 'a']
# print(nlist)   # [1, 2, [3, 4]]
# # copy.deepcopy为深拷贝，完全的把mlist拷贝了一份，所以mlist怎么变动都不会跟nlist有关系



# 扩展，copy和deepcopy的区别：
import copy
mlist = [1,2,[3,4]]
nlist = mlist.copy() # # 浅拷贝
slist = copy.deepcopy(mlist) #  # 深拷贝
print(mlist)  # [1, 2, [3, 4]]
print(nlist)  # [1, 2, [3, 4]]
print(slist)  # [1, 2, [3, 4]]


print("---------------------------------------------------")
mlist.append('a')
nlist.append('a')
slist.append('a')
print(mlist)    # [1, 2, [3, 4], 'a']
print(nlist)    # [1, 2, [3, 4], 'a']
print(slist)    # [1, 2, [3, 4], 'a']


print("---------------------------------------------------")
mlist.append('a')
print(mlist)    # [1, 2, [3, 4], 'a', 'a']


print("---------------------------------------------------")
mlist[2].append('b')
nlist[2].append('b')
slist[2].append('b')

print(mlist)    # [1, 2, [3, 4, 'b', 'b'], 'a', 'a']
# copy后的第一层列表不受原列表影响，第二层列表仍受原列表的影响
print(nlist)    #[1, 2, [3, 4, 'b', 'b'], 'a']
# deepcopy后的列表完全独立，不受原列表影响
print(slist)    # [1, 2, [3, 4, 'b'], 'a']
