# 开发时间：2024/5/7 17:50
"""
列表：有序的可变的元素集合
特点：有序  可变
"""
name="abc"
# name[0]='c'
# print(name)#错误，字符串的元素不可改变
"""----------------------------------------
定义方式1
"""

name=[1,2,3,4,5]
print(type(name))

name=[1,True,3,'ab',5]
print(name)
#列表嵌套：列表中的元素也可以是列表
item=[1,2,3]
name=[1,2,3,item]
print(name)

"""----------------------------------------
定义方式2：生成式
"""
list2=range(10)
print(list2)#range(0, 10)--->防止生成的列表没有使用，浪费空间
list3=range(0,10,2)#步长为2
print(list3)

"""
添加元素
"""
#原始
num1=[1,2,3,4,5]
numList=[]
for num in num1:
    res=num**2
    numList.append(res)
print(numList)
#列表推导式(先看后面，前面是结果)
numList2=[num**2 for num in num1]
print(numList2)
#解释：
# part1:for num in num1 #取出num
# part2:num#对num做运算
# part3:#赋值
#拓展
numList3=[num**2 for num in num1 if num%2!=0]
print(numList3)