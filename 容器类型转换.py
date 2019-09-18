# list:        访问方式(index)、   有序、     元素可重复、    值可变
# tuple:       访问方式(index)、   有序、     元素可重复、    值不可变
# dictionary:  访问方式(key)、     无序、     元素可重复、    值可变
# set:         访问方式(no)、      无序、     元素不可重复、  值可变



print("-------------------------------------------------------------")
# 1.列表转换为元组  tuple(list)
mlist = [1, 2, 3, 4, 5, 6, 7]
mlisttotuple= tuple(mlist)
print("原始列表=>", mlist)
print("列表转换为元组=>",mlisttotuple)



print("-------------------------------------------------------------")
# 2.元组转换为列表   list(tuple)
mtuple1 = (31, 32, 33, 34, 35, 36, 37)
mtupletolist = list(mtuple1)
print("原始元组=>",mtuple1)
print("元组转换为列表=>", mtupletolist)



print("-------------------------------------------------------------")
# 3.列表转换为集合set(list)
# 元组转换为集合set(tuple)
mlist2 = [11, 22, 33, 44, 55, 66, 77]
mtuple2 = (11, 12, 13,14, 15, 16, 17)
msettolist = set(mlist2)
msettotuple = set(mtuple2)
print("原始列表=>", mlist2)
print("列表转换为集合=>",msettolist)
print("原始元组=>",mtuple2)
print("元组转换为集合=>", msettotuple)



print("-------------------------------------------------------------")
# 4. 集合转换为列表
mset = {9, 8,11,34, 89, 0, 4}
mlisttoset = list(mset)
print("原始集合=>", mset)
print("集合转换为列表=>", mlisttoset)



print("-------------------------------------------------------------")
# 5.字典转换为列表
mdict = {"jack":19, "mary":22, "Hony":17}
mdicttolist = list(mdict)
mdicttolist1 = list(mdict.values())

print("原始字典=>", mdict)
print("字典转换为列表=>", mdicttolist)
print(mdicttolist1)






