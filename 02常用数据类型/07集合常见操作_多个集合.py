# 集合之间操作
# 	交集
# 		intersection(Iterable)
# 			字符串
# 				只判定字符串中的非数字
# 			列表
# 			元组
# 			字典
# 				值判定key
# 			集合
# 			...
# 		逻辑与 '&'
# 		intersection_update(…)
# 			交集计算完毕后, 会再次赋值给原对象
# 				会更改原对象
# 				所以, 只适用于可变集合
s1={1,2,3,4,5}
s2=frozenset([3,4,5,6,7])
# res=s1.intersection(s2)#哪个在前结果就是那种类型
# res=s2 & s1 #哪个在前结果就是那种类型
res=s1.intersection_update(s2)
# res=s2.intersection_update(s1)#错误，该函数会将结果给到s2,但是s2不可变

print(res,type(res))
print(s1,s2)

#其他类型
s3={"1","2","3“，4"}
# res=s3.intersection("1,2,3")
# res = s3.intersection({"1": "a", "2": "b", "3": "c"})#取的还是键值
res=s3.intersection(["1","2"])
print(res)

# 	并集
# 		union()
# 			返回并集
s1={1,2,3,4,5}
s2=frozenset([3,4,5,6,7])
result=s1.union(s2)
print(type(result),result)
# 		逻辑或 '|'
# 			返回并集
s1={1,2,3,4,5}
s2=frozenset([3,4,5,6,7])
result=s1|s2
print(type(result),result)
# 		update()
# 			更新并集
s1={1,2,3,4,5}
s2=frozenset([3,4,5,6,7])
result=s1.update(s2)#更新s1
print(result,s1)
# 	差集
# 		difference()
# 		算术运算符减 ‘-‘
# 		difference_update()
s1={1,2,3}
s3={3,4,5}
# resutl=s1.difference(s3)
# result=s1.difference_update(s3)
result=s1-s3#s1也会改变
print(result,s1)
# 	判定
# 		isdisjoint()两个集合不相交
# 		issuperset()一个集合包含另一个集合
# 		issubset()一个集合包含于另一个集合

s1={1,2,3}
s2={3,4,5}
print(type(s2))
print(s1.isdisjoint(s2))

s2={1,2}
print(s1.issuperset(s2))
print(s2.issubset(s1))