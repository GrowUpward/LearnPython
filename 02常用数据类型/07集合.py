"""
列表：无序的, 不可随机访问的, 不可重复的元素集合

    与数学中集合的概念类似，可对其进行交、并、差、补等逻辑运算

    分为可变集合和非可变集合
        set
            为可变集合
                增
                删
                改
        frozenset
            不可变集合
                创建好之后, 无法增删改
 vs:
字符串、列表、元组、字典都是有序的，可以用下标进行访问，列表不可以用下标进行访问
"""

s="abc"
l=[1,2,3]
t=(1,2,3)
d={"name":"sz"}

#集合
j={1,2,3}
print(type(j),j)

#可变集合

s2=set("abc")#通过字符串生成
s2=set(l)
s2=set([1,2,3])
s2=set(d)#只会获取字典的键值
print(type(s2),s2)#无序的，可能出现cba

#通过推导式生成
# 	 s = set(x**2 for x in range(1, 10) if x % 2 == 0)
# 	s = {推导式}
s3=set(x for x in range(0,10) if x%2==0)
print(s3)

# 不可变集合
f=frozenset(s)
f=frozenset(x for x in range(0,10) if x%2==0)
print(f)

# 注意
# 	1. 创建一个空集合时, 需要使用set() 或者 frozenset(), 不能使用 s = {}
# 		会被识别成为字典
s4={}
print(type(s4))#<class 'dict'>
s4=set()
print(type(s4))#<class 'set'>
# 	2. 集合中的元素, 必须是可哈希的值
# 		如果一个对象在自己的生命周期中有一哈希值（hash value）是不可改变的，
# 那么它就是可哈希的（hashable）的
# 		暂时理解为 不可变类型

# s4={1,2,d}#错误，字典不可哈希
# s4={1,2,l}#错误，列表不可哈希
s4={1,2,t}#字符串、元组可以
print(s4)
# 	3. 如果集合中的元素值出现重复, 则会被合并为1个

s4={1,2,1}
print(s4)#1，2，会自动去除重复的，所以有时可以借助列表去重
