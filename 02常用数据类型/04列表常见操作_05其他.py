# 额外操作
"""
判定：in,not in
比较：< > =之间的组会
排序：sorted() sort()
打乱：random.shuffle
反转：reverse() 切片：[:::-1]
"""
# 	判定
# 		元素 in  列表
# 		元素 not in 列表
s="abc"
print('a' in s)
print('a' not in s)

nums=[1,2,3,4,5]
print(1 in nums)
print(1 not in nums)
# 	比较
# 		cmp()
# 			内建函数
# 			如果比较的是列表, 则针对每个元素, 从左到右逐一比较
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
# 			针对每个元素, 从左到右逐一比较
print(1<3)

# 	排序
# 		方式1
# 			内建函数
# 				可以对所有可迭代对象进行排序
# 			语法
# 				sorted(itrearble, key=None, reverse=False)
# 			参数
# 				itrearble
# 					可迭代对象
# 				key
# 					排序关键字
# 					值为一个函数，此函数只有一个参数且返回一个值用来进行比较
# 				reverse
# 					控制升序降序
# 					默认False
# 						升序
# 			返回值
# 				一个已经排好序的列表
# 				列表类型
s="abc"
print(sorted(s))#默认升序

nums=[1,2,3,4,5]
print(sorted(nums,reverse=True))
#元组
tu=[('sz',18),('sz2',19),('sz1',20),('sz3',21)]#默认根据首元素排序
print(sorted(tu))
# 如何根据指定元素排序？
def getKey(x):
    return x[1]
print(sorted(tu,key=getKey,reverse=True))#不写getKey()的括号是要方法内部进行调用此函数，而不是一开始就调用此函数

# 		方式2
# 			列表对象方法
# 			语法
# 				list.sort(key=None, reverse=False)
# 			参数
# 				key
# 					排序关键字
# 					值为一个函数，此函数只有一个参数且返回一个值用来进行比较
# 				reverse
# 					控制升序降序
# 					默认False
# 						升序

l=[1,2,3,4,5,6]
res=l.sort()#更改了列表本身
print(res,l)

# 如何根据指定元素排序？
tu=[('sz',18),('sz2',19),('sz1',20),('sz3',21)]#默认根据首元素排序
def getKey(x):
    return x[1]
res=tu.sort(key=getKey)
print(res,tu)



# 	乱序
# 		可以随机打乱一个列表
# 			导入random模块
# 				import random
# 			random.shuffle(list)
import random
l=[1,2,3,4,5,6]
res=random.shuffle(l)
print(res,l)
# 	反转
# 		l.reverse()
# 		切片反转
# 			l[::-1]

l=[1,2,3,4,5,6]
res=l.reverse()
print(res,l)

res=l[::-1]
print(res,l)