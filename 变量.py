mstring = "abcdefghijklmn"
print(mstring)   # abcdefghijklmn
print(mstring[1:6])     # bcdef
print(mstring[::2])     # acegikm
print(mstring[::-2])    # nljhfdb
print(mstring[-7:-2:])   # hijkl
print(mstring[-2:-7:-2])   # mki

mstr = "abc"
print(mstr * 3)    # abcabcabc
print(mstr + "def")    # abcdef
mlist = [1, 2, 3, "a", "b", "c", [4, 5, 6]]
print(mlist)   # [1, 2, 3, 'a', 'b', 'c', [4, 5, 6]]
print(mlist[4])
print(mlist[1:6])     # [2, 3, 'a', 'b', 'c']
print(mlist[::2])     # [1, 3, 'b', [4, 5, 6]]
print(mlist[::-2])    # [[4, 5, 6], 'b', 3, 1]
print(mlist[-7:-2:])   # [1, 2, 3, 'a', 'b']
print(mlist[-2:-7:-2])   # ['c', 'a', 2]


mlist1 = [1, 2, 3]
mlist2 = ["I" , "have", 5, "money"]
print(mlist1)    # [1, 2, 3]
print(mlist2)
print(mlist1 * 2)   # [1, 2, 3, 1, 2, 3]
print(mlist1 + ["a", 4, "e", [3, 4, "c"]])   # [1, 2, 3, 'a', 4, 'e', [3, 4, 'c']]
print(mlist1 + mlist2)   # [1, 2, 3, 'I', 'have', 5, 'money']


mtuple = (1, 2, 3, "a", "b", "c", [4, 5, 6])
print(mtuple)   # (1, 2, 3, 'a', 'b', 'c', [4, 5, 6])
print(mtuple[1:6])     # (2, 3, 'a', 'b', 'c')
print(mtuple[::2])     # (1, 3, 'b', [4, 5, 6])
print(mtuple[::-2])    # ([4, 5, 6], 'b', 3, 1)
print(mtuple[-7:-2:])   # (1, 2, 3, 'a', 'b')
print(mtuple[-2:-7:-2])   # ('c', 'a', 2)


mtuple1 = (1, 2, 3)
mtuple2 = ("I" , "have", 5, "money")
print(mtuple1 * 2)   # (1, 2, 3, 1, 2, 3)
print(mtuple1 + ("a", 4, "e", [3, 4, "c"]))  # (1, 2, 3, 'a', 4, 'e', [3, 4, 'c'])
print(mtuple1 + mtuple2)   # (1, 2, 3, 'I', 'have', 5, 'money')


d1=dict({"id":101,"name":"Flx","age":13})
d2=dict(id=102,name="flx",age=23)
d3=dict([("id",103),("name","Fux"),("age",33)])
d4={"id":104,"name":"fux","age":43}
print(d1)   # {'id': 101, 'name': 'Flx', 'age': 13}
print(d2)   # {'id': 102, 'name': 'flx', 'age': 23}
print(d3)   # {'id': 103, 'name': 'Fux', 'age': 33}
print(d4)   # {'id': 104, 'name': 'fux', 'age': 43}
print(d2["name"])   # flx
print(d3["age"])    # 33


a = 8
b = 5
c = -5
print(a + b)     # 13
print(a - b)     # 3
print(a * b)     # 40
print(a / b)     # 1.6
print(a % b)     # 3
print(a // b)    # 1
print(a // c)    # -2

#
