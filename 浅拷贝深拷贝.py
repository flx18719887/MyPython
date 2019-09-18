# coding=gbk
# import copy
# mlist = [1,2,[3,4]]
# nlist = copy.deepcopy(mlist)
# mlist[2] = 'a'
# print(mlist)   # [1, 2, 'a']
# print(nlist)   # [1, 2, [3, 4]]
# # copy.deepcopyΪ�������ȫ�İ�mlist������һ�ݣ�����mlist��ô�䶯�������nlist�й�ϵ



# ��չ��copy��deepcopy������
import copy
mlist = [1,2,[3,4]]
nlist = mlist.copy() # # ǳ����
slist = copy.deepcopy(mlist) #  # ���
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
# copy��ĵ�һ���б���ԭ�б�Ӱ�죬�ڶ����б�����ԭ�б��Ӱ��
print(nlist)    #[1, 2, [3, 4, 'b', 'b'], 'a']
# deepcopy����б���ȫ����������ԭ�б�Ӱ��
print(slist)    # [1, 2, [3, 4, 'b'], 'a']
