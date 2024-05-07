"""----------------------------------------
函数速览：
del(),pop(),remove()
--------------------------------------------
"""
# 删
# 	del 语句
# 		作用
# 			可以删除一个指定元素(对象)
# 		语法
# 			del 指定元素
# 		注意
# 			可以删除整个列表
# 				删除一个变量
# 			也可以删除某个元素
num=[1,2,3,4]
del num[0]#删除一个元素
print(num)

del num#删除所有
# print(num)

# 	pop
# 		作用
# 			移除并返回列表中指定索引对应元素
# 		语法
# 			l.pop(index=-1)
# 		参数
# 			index
# 				需要被删除返回的元素索引
# 				默认是-1
# 					也就对应着列表最后一个元素
# 		返回值
# 			被删除的元素
# 		注意
# 			会直接修改原数组
# 			注意索引越界
num=[1,2,3,4]
print(num.pop())#移除并返回列表中指定索引对应元素
print(num)

print(num.pop(0))
print(num)

# print(num.pop(10))#报错
# print(num)

# 	remove
# 		作用
# 			移除列表中指定元素
# 		语法
# 			l.remove(object)
# 		参数
# 			object
# 				需要被删除的元素
# 		返回值
# 			None
# 		注意
# 			会直接修改原数组
# 			如果元素不存在
# 				会报错
# 			若果存在多个元素
# 				则只会删除最左边一个
# 			注意循环内删除列表元素带来的坑
num=[1,2,3,4]
print(num.remove(2))#移除并返回列表中指定索引对应元素
print(num)

num=[1,2,3,2,4]
print(num.remove(2))#移除并返回列表中指定索引对应元素
print(num)
#删除一个列表里面所有的2？
nums=[1,2,3,2,4,2,2]
for num in nums:
    if(num==2):
        nums.remove(2)#错误，此方法不行
print(nums)