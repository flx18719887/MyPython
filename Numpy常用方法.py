# coding=gbk
import numpy as np
array1 = np.array([i for i in range(10)])
array2 = np.array(10, dtype = int)
print("array1=>", array1)
print("array2=>", array2)


print("---------------------------------------------")
array1 = np.zeros(10)
array2 = np.zeros((4,5))
array3 = np.zeros(shape=(5,6))
print("array1=>\n", array1)
print("array2=>\n", array2)
print("array3=>\n", array3)
# mzeros = np.zeros(10,dtype = int)
# mzeros = np.zeros(shape = 10,dtype = int)

print("---------------------------------------------")
array1 = np.ones(10)
array2 = np.ones((4,5))
array3 = np.ones(shape=(5,6))
print("array1=>\n", array1)
print("array2=>\n", array2)
print("array3=>\n", array3)
# mones = np.ones(10,dtype = int)
# mones = np.ones(shape = 10,dtype = int)

print("---------------------------------------------")
array1= np.full((4,5),66)
array2 = np.full(shape=(5,6), fill_value=77)
array3 = np.full(fill_value=88, shape=(5,6))

print("array1=>\n", array1)
print("array2=>\n", array2)
print("array3=>\n", array3)


mlist = [i for i in range(0,20,2)]
print("mlist=>",mlist)

marray = np.arange(0, 20, 2)
print("marray=>", marray)

nlist = [i for i in range(0,1,0.2)]
print("nlist=>",nlist)     # 报错，步长不能为浮点数

narray = np.arange(0, 1, 0.2)
array1 = np.arange(0, 10)
array2 = np.arange(10)
print("narray=>", narray)    #  [0.  0.2 0.4 0.6 0.8]


narray = np.linspace(0,20,10)
marray = np.linspace(0,20,11)

print("narray=>", narray)
print("marray=>", marray)


array1 = np.random.randint(0,10)   # 生成一个随机数
print("array1=>", array1)

array2 = np.random.randint(0,10,10)   # 生成一个包含10个元素的随机数向量
print("array2=>", array2)

array3 = np.random.randint(0,1,10)   # 生成一个包含10个元素的随机数向量，左闭右开（包头不包尾）
print("array3=>", array3)

array4 = np.random.randint(4,8,size=10)
print("array4=>", array4)

array5 = np.random.randint(4,8,size=(3,5))
print("array5=>\n", array5)

np.random.seed(555)
array = np.random.randint(2,10,size=(3,3))
print(array)

np.random.seed(1)
array = np.random.randint(2,10,size=(3,3))
print(array)


array1 = np.random.random()
print("array1=>",array1)

array2 = np.random.random(10)
print("array2=>\n", array2)


array3 = np.random.random((3,3))
print("array3=>\n",array3)


array1 = np.random.normal()
print("array1=>",array1)
array2 = np.random.normal(10,100)
print("array2=>",array2)
array2 = np.random.normal(10,100,(3,4))
print("array3=>\n",array2)
print(help(np.random.normal))


x = np.arange(10)
print("x=>", x)
X = np.arange(24).reshape(6,4)
print("X=>\n", X)
print("x.dim=>", x.ndim)
print("X.dim=>", X.ndim)
print("x.shape=>", x.shape)
print("X.shape=>", X.shape)
print("x.size=>", x.size)
print("X.size=>", X.size)

print(X[2,3])
print(X[:2,:3])
print(X[:4][:3])

X = np.arange(10)
# print(X.reshape(10,-1))
print(X.reshape(-1, 10))


# 合并操作
x = np.array([1,2,3])
y = np.array([3,2,1])
z = np.concatenate([x, y])

print("x=>",x)
print("y=>",y)
print("z=>",z)

A = np.array([[1,2,3],[4,5,6]])
print("A=>\n", A)
# 默认按行拼接
B1 = np.concatenate([A, A])
print("B1=>\n",B1)
B1 = np.concatenate([A, A],axis=0)
print("按行拼接：B1=>\n",B1)
B2 = np.concatenate([A, A, A])
print("B2=>\n",B2)
B3 = np.concatenate([A, A, A, A])
print("B3=>\n",B3)


# 按列拼接
C1 = np.concatenate([A, A], axis=1)
print("按列拼接：C1=>\n", C1)

C2 = np.concatenate([A, A, A], axis=1)
print("C2=>\n", C2)

A = np.array([[1,2,3],[4,5,6]])
z = np.array([7,8,9])
# D1 = np.concatenate([A, z])   # 报错   concatenate只能合并维度一样的数组
# print(D1)
D2 = np.concatenate([A, z.reshape(1, -1)])
print(D2)
D3 = np.vstack([A, z])   # 不同维度竖直拼接
print("竖直拼接D3=>\n", D3)

B = np.full((2,2), 100)
D4 = np.hstack([A, B])   # 不同水平拼接
print("水平拼接D4=>\n", D4)


X = np.arange(16).reshape(2,8)
print(X)

invX = np.linalg.inv(X)
print(invX)

pinvX = np.linalg.pinv(X)
print(pinvX)
print(pinvX.shape)
print(X.dot(pinvX))

big_array = np.random.random(100)
print(sum(L))
print(np.sum(big_array))
print(big_array.sum())

print(np.max(big_array))
print(big_array.max())

print(np.min(big_array))
print(big_array.min())


X = np.arange(16).reshape(4, -1)
print(X)
X_col = np.sum(X, axis = 0)
print("X_col: ", X_col)   # 每一列的和

X_row = np.sum(X, axis = 1)
print("X_row: ", X_row)   # 每一行的和


X = np.arange(16).reshape(4, -1)
print(X)
print(np.prod(X+1))    # 所有元素之积
print(np.mean(X))    # 平均值
print(np.median(X))    # 中位数
print(np.percentile(X, q = 50))   # 求百分位    百分之五十小于所得值


big_array1 = np.random.random(100)
print(np.percentile(big_array1, q = 50))
print(np.median(big_array1))

print(np.percentile(big_array1, q = 100))
print(np.max(big_array1))
print("--------------------------------------")
for percent in [0, 25, 50, 75, 100]:
    print(percent, "分位数：", np.percentile(big_array1, q = percent))

np.random.seed(1)
x = np.array([21,43,45,1,2,35,6,799])
print(x)
print(np.min(x))
print(np.argmin(x))
print(np.argmax(x))


import random
x = np.arange(16)
print("原始值x：", x)
np.random.shuffle(x)
print("打乱顺序后x：", x)
y = np.sort(x)
print("np.sort(x)排序后x：", x)
print("y = np.sort(x)排序后y：", y)
x.sort()
print("x.sort()排序后x：", x)
print("排序后的索引：",np.argsort(x))
np.random.shuffle(x)
print(np.partition(x, 11))


np.random.seed(1)
X = np.random.randint(10, size = (4,4))
print(X)
print("默认按行排序：\n", np.sort(X))   # 沿着列方向
print("按行排序：\n", np.sort(X, axis=1))   # 沿着列方向,按行排序
print("按列排序：\n", np.sort(X, axis=0))   # 沿着行方向,按列排序


np.random.seed(1000000000)
x = np.random.random(16)
print(x)
ind = [1,3,5]
print("x[ind]: ", x[ind])
ind1 = np.array([[0,2],[1,3]])
print("x[ind1]: \n", x[ind1])

x = np.arange(16)
X = x.reshape(4, -1)
print("X: \n", X)
row = np.array([0,1,2])
col = np.array([1,2,3])
print("X[row, col]：\n", X[row, col])
print("X[:,col]: \n", X[:,col])
print("X[:2, col]: \n", X[:2, col])




print(bool([]))
print(bool(' '))
print(bool(0.0))
print(bool({0.0}))


import numpy
array1 = numpy.array([i for i in range(10)])
print(array1[2:7])

