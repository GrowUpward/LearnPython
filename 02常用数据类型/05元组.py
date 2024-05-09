# 开发时间：2024/5/9 23:39
"""
元组：有序的不可变的元素集合
特点：有序  不可变
	和列表的区别就是, 元组元素不能修改

"""
# 一个元素
t=(1,)
print(type(t))
# 多个元素
l=(1,2,3)
print(type(l))
l2=("abc",[1,2],3)
print(type(l2))
# 多个对象，以逗号隔开，默认为元组
tuple0 = 1, 2, 3, "sz"
print(tuple,type(tuple0))
# 将列表转化为元组
list0=[1,2,3]
tuple1=tuple(list0)
print(tuple1,type(tuple1))
# 补充: 元组嵌套    元组的中元素可以是元组
tuple3=(1, 2, ("a", "b"))
print(tuple3,type(tuple3))