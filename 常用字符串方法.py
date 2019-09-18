# mstr = "xya abaac daaee f  abv"
# print(mstr.count("a"))
# print(mstr.find("c"))   #返回某字符第一次出现的索引位置
# print(mstr.replace("a", "A"))
# print(mstr.replace("a", "M", 1))
# print(mstr.title())   # 字符串首字母大写
#

# mstr = "xya abaac daaee f  abv"
# print("--".join(mstr))
# print(" ".join(mstr))
#
# print(mstr.split())   # 切割字符串，默认在空白处切分
# print(mstr.split("a"))



# mstr1 = "  ahkgla;ja   "
# print(mstr1.strip())    # 移除字符串两边的空白符号
# print(mstr1.lstrip())
# print(mstr1.rstrip())
#
# mstr2 = "我今天吃饭花了%d元，我就吃了%s饭" %(30, "两次")
# print(mstr2)
#
#
# mstr3 = "这是一个{0}的天气，我感到{1}".format("风和日丽", "开心无比")
# print(mstr3)


# mlist = [1, 2, 3, [3, "E", 4, 5], "a", "A", "ABC", (5, 6, 7)]
# print(mlist)
# print(mlist[3:7])
# print(mlist[3][1])
# print(len(mlist))
# mlist[2] = ["Hi, Python"]
# print(mlist)
# print(mlist[-3:-6])
# print(mlist[-3:-6:-1])
# print(mlist[-6:-3])
# print(mlist[-6:-3:-1])


# mlist1 = ["a", "ab", 1, 12]
# mlist2 = ["hi python", 4, 5]
# print(mlist1 + mlist2)
# print(mlist2 * 2)
# print(mlist1 + ["Excuse me!", "Mr Wang"])


# mlist3 = [2, 3, 3, 3, 4, 6, 8, 10]
# print(mlist3)
# mlist3.append(1)
# print(mlist3)
# mlist3.append([1, 3, 5, 7, 9])
# print(mlist3)
# mlist3.extend([1, 3, 5, 7, 9])
# print(mlist3)
# mlist3.insert(2, "python")
# print(mlist3)
# print(mlist3.count(3))


# mlist4 = [2, 3, 3, 3, 4, 6, "Python真有趣", 8, 10, "python", "hi"]
# print("当前列表为：", mlist4)
# print(mlist4.pop())
# print(mlist4.pop())
# print("当前列表为：", mlist4)
# print(mlist4.pop())
# print(mlist4.pop())
# print("当前列表为：", mlist4)
# print(mlist4.pop())
# print(mlist4.pop())
# print("当前列表为：", mlist4)


# mlist5 = [2, 3, 3, 3, 4, 6, "Python真有趣", 8, 10, "python", "hi"]
# mlist5.remove("python")
# print("mlist5----",mlist5)

# mlist5 = [2, 3, 3, 3, 4, 6, "Python真有趣", 8, 10, "python", "hi"]
# print("原始列表：", mlist5)
# mlist5.reverse()
# print("反转后的列表：", mlist5)

mlist6 = ["e","a","g","s"]
print("原始列表：", mlist6)
mlist6.sort()
print("排序后的列表：", mlist6)

mlist7 = [7, 17, 1, 4, 0, 55, 8, 23, 333]
print("原始列表：", mlist7)
mlist7.sort()
print("排序后的列表：", mlist7)






