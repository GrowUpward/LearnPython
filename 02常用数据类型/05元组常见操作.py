"""----------------------------------------
由于元组是不可变的，所以不能对元组里面的元素进行增删改，只能查询
--------------------------------------------
"""

# 获取单个元素
#     tuple[index]
#     index 为索引
#         可以为负
tuple0=(1,2,3,4,5)
print(tuple0[0])
# 获取多个元素
#     切片
#     tuple[start: end: step]
print(tuple0[0:3])#end取不到

# 额外操作
# 	获取
# 		tuple.count(item)
# 			统计元组中指定元素的个数
# 		tuple.index(item)
# 			获取元组中指定元素的索引
# 		len(tup)
# 			返回元组中元素的个数
# 		max(tup)
# 			返回元组中元素最大的值
# 		min(tup)
# 			返回元组中元素最小的值
t=(1,2,3,2,4)
res=t.count(2)
print(res)

idx=t.index(3)
print(idx)

length=len(t)
print(length)

ma=max(t)
mi=min(t)

print(ma,mi)
# 	判定
# 		元素 in  元组
# 		元素 not in 元组

print(1 in t)
print(12 not in t)
# 	比较
# 		cmp()
# 			内建函数
# 			如果比较的是元组, 则针对每个元素, 从左到右逐一比较
# 				左 > 右
# 					1
# 				左 == 右
# 					0
# 				左 < 右
# 					-1
# 			Python3.x不支持
# 		比较运算符
# 			==
# 			>
# 			...
# 			针对每个元素, 从左到右逐一比较：比对的是里面的每个元素
t2=(1,2,3,4,5)
print(t==t2)

# 	拼接
# 		乘法
# 			(元素1, 元素2...) * int类型数值
# 				=
# 					(元素1, 元素2..., 元素1, 元素2..., ...)
# 		加法
# 			(元素1, 元素2) + (元素a, 元素b)
# 				=
# 					(元素1, 元素2, 元素a, 元素b)

print('abc' *3)
print((1,2) *2)
print((1,2) +(2,3))
print((1,2) +('a','b'))
# print((1,2) +['a','b'])#错误，类型不同不能相加
# 	拆包
a, b = (1, 2)
t1=(a,b)
print(t1)
print(t1[0],t1[1])

#不用元组，这样更简单
a, b = (10, 20)#等价于==>a,b =10,20
print(a,b)

# 如何利用元组进行两个变量的交换
a=1
b=2
(b,a)=(a,b)
print(a,b)