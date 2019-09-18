# 字典的每个键值（key→value）对用冒号分割，每个对之间用逗号分割，整个字典包括在花括号{}中
# 值可以取任何数据类型，但键必须是不可变的，如字符串、数字和元组
if __name__ == '__main__':
    # 1. 创建字典
    # 方法1
    mdict1 = {"name":"flx", "age":22, "school":"bawei"}
    print("mdict1=>", mdict1)
    print(type(mdict1))

    # 方法2
    mdict2 = dict(name = "fux", age = 13, income = 2000)
    print("mdict2=>", mdict2)
    print(type(mdict2))

    # 方法3
    mdict3 = dict([("name", "Fls"), ("age", 12), ("sex", "male")])
    print("mdict3=>", mdict3)
    print(type(mdict3))

    # 方法4
    mdict4 = dict((("name", "FLX"), ("age", 15), ("sex", "fmale")))
    print("mdict4=>", mdict4)
    print(type(mdict4))

    # # 2. 字典索引
    print("==========================================================")
    print(mdict4["name"], "==>",  mdict4["sex"])
    # print(mdict4["income"], "查找的值不存在")     # 索引不存在的key会报错

    print("==========================================================")
    print(mdict4.get("name"), "==>", mdict4.get("age"))
    print(mdict4.get("income"), "查找的值不存在")     # 索引不存在的key不会报错




    # 2. 添加, 更改和删除键值对
    mdict = {"john":12, "Max":14, "Selo":19, "Hery":20}
    print(mdict)
    # 如果给一个原来存在的key赋值, 就是修改；如果给一个原来不存在的key赋值, 就是新增
    # 添加元素  方法1    key 存在即修改，key不存在即新增
    mdict["Jack"] = 32
    print(mdict)
    mdict["Jack"] = 11
    print(mdict)

    # 添加元素  方法2    只能新增，key存在不能修改，key不存在新增
    mdict.setdefault("Jerry",18)
    print(mdict)
    mdict.setdefault("Jerry", 22)
    print(mdict)

    # pop 删除指定key的value
    mdict.pop("Jack")
    print(mdict)

    # del: 删除指定key的value
    del(mdict["Max"])
    print(mdict)
    print("==========================================================")
    del mdict
    print(mdict["john"])

    # 字典内置函数 / 方法
    # len(dict): 计算字典元素个数，即键的总数
    mdict = {"john":12, "Max":14, "Selo":19, "Hery":20}
    print(len(mdict))

    # str(dict): 输出字典，以可打印的字符串表示。
    print(str(mdict))

    # dict.keys(): 返回包含该字典键的列表
    print(mdict.keys())

    # dict.values(): 返回包含该字典值的列表
    print(mdict.values())

    #  dict.items(): 将键/值对看成一个元素，并返回列表
    print(mdict.items())

    #  dict.get(key, default=value): 如果key对象存在，则返回value，value默认是None。
    print(mdict.get("Max"))















