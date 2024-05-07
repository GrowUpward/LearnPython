# 开发时间：2024/5/7 18:03
"""----------------------------------------
函数速览：
append(),insert(),extend()
--------------------------------------------
"""
# append
# 	作用
# 		往列表中, 追加一个新的元素
# 		在列表的最后
# 	语法
# 		l.append(object)
# 	参数
# 		object
# 			想要添加的元素
# 	返回值
# 		None
# 	注意
# 		会直接修改原数组
num1=[1,2,3,4]
num1.append(5)
print(num1)
# insert
# 	作用
# 		往列表中, 追加一个新的元素
# 		在指定索引前面
# 	语法
# 		l.insert(index, object)
# 	参数
# 		index
# 			索引, 到时会插入到这个索引之前
# 		object
# 			想要添加的元素
# 	返回值
# 		None
# 	注意
# 		会直接修改原数组

num1.insert(0,5)#在第0个前面插入
print(num1)
# extend
# 	作用
# 		往列表中, 扩展另外一个可迭代序列
# 	语法
# 		l.extend(iterable)
# 	参数
# 		iterable
# 			可迭代集合
# 				字符串
# 				列表
# 				元组
# 				...
# 	返回值
# 		None
# 	注意
# 		会直接修改原数组
# 		和append之间的区别
# 			extend可以算是两个集合的拼接
# 			append是把一个元素, 追加到一个集合中
num2=['a','b','c']
num2="abc"#会被分解为a b c
print(num1.extend(num2))#直接在后面追加
print(num1)

# 乘法运算
num3=['a']
num4=num3*3
print(num3*3)
print(num4)
print(num3)
# 加法运算
# 	["a"] + ["b", "c"]
# 		=
# 			["a", "b", "c"]
# 	和extend区别
# 		只能列表类型和列表类型相加
num1=[1,2,3]
num2=['a','b']
num2="abc"#不可以
print(num1+num2)