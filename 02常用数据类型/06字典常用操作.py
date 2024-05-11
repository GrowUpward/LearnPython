"""
常用操作：增删改查+计算、判定
"""
# --------------------------增------------------------
# 	dic[key] = value
# 		当key在原字典中不存在时, 即为新增操作
d={"name":"sz","age":18}
print(d,id(d))
d["height"]=180
print(d,id(d))


#----------------------------删-------------------------
# 	del  dic[key]
# 		key, 必须要存在
del d["height"]
print(d)
# 	dic.pop(key[, default])
# 		删除指定的键值对, 并返回对应的值
# 		如果key, 不存在, 那么直接返回给定的default值; 不作删除动作
# 		如果没有给定默认值, 则报错
v=d.pop("age")
print(v,d)
# 	dic.popitem()
# 		删除按升序排序后的第一个键值对, 并以元组的形式返回该键值对
# 		如果字典为空, 则报错
d={"name":"sz","age":18,"height":180}
res=d.popitem()
print(res)
# 	dic.clear()
# 		删除字典内所有键值对
# 			返回None
# 		注意, 字典对象本身还存在, 只不过内容被清空
# 			注意和del的区别
d.clear()
print(d)

# ----------------------------改----------------------------
# 	只能改值, 不能改key
# 	修改单个键值对
# 		dic[key] = value
# 			直接设置, 如果key不存在, 则新增, 存在则修改
d={"name":"sz","age":18,"height":180}
d["name"]="sy"
print(d)
# 	批量修改键值对
# 		oldDic.update(newDic)
# 			根据新的字典, 批量更新旧字典中的键值对
# 			如果旧字典没有对应的key, 则新增键值对;若新字典的键值对没有旧字典多，则旧字典后面不用改
di={"name":"sz","age":18}
d.update(di)
print(d)

# -----------------------------查---------------------------------------
# 	获取单个值
# 		方式1
# 			dic[key]
# 				如果key, 不存在, 会报错
d={"name":"sz","age":18}
print(d["age"])
# print(d[0])#不可以通过下标获取值，会把0当成key

# 		方式2
# 			dic.get(key[, default])
# 				如果不存在对应的key, 则取给定的默认值default
# 				如果没有默认值,  则为None
# 					但不会报错
# 				但是, 原字典不会新增这个键值对
d={"name":"sz","age":18}
v=d.get("name")
print(v,d)
v=d.get("agel",666)
print(v,d)
# print(d.get())
# 		方式3
# 			dic.setdefault(key[,default])
# 				获取指定key对应的值
# 				如果key不存在, 则设置给定默认值, 并返回该值
# 				如果默认值没给定
# 					则使用None代替
d={"name":"sz","age":18}
v=d.setdefault("agel",666)#没有会将其添加到原字典中
print(v)
v=d.setdefault("agel")
print(v,d)


# 	获取所有的值
# 		dic.values()
d={'name': 'sz', 'age': 18, 0: 666}
print(d.values())
# 	获取所有的键
# 		dic.keys()
print(d.keys())
# 	获取字典的键值对
# 		dic.items()
print(d.items())


# 	遍历
# 		for in--->先获取key,再通过key遍历
d={'name': 'sz', 'age': 18, "height": 180}
keys=d.keys()#先获取key,再通过key遍历
for key in keys:
	print(key)
	print(d[key])
# 		for x,y in info.items()
d={'name': 'sz', 'age': 18, "height": 180}
items=d.items()
for k,v in items:
	print(k,v)

# 	注意
# 		Python2.x和Python3.x版本之间关于获取键, 获取值, 获取item, 之间的区别
# 			Python2.x 直接是一个列表
# 				可通过下标进行获取指定元素
# 			Python3.x 中是Dictionary view objects
# 				优势
# 					当字典发生改变时, view objects会跟着发生改变
# 				转换成列表使用
# 					list(result)
# 				转换成迭代器
# 					iter(result)
# 				也可以直接被遍历
# 		在Python2.x中提供了如下方法
# 			viewkeys()
# 			viewvalues()
# 			viewitems()
# 			作用如同Python3.x中的
# 				Dictionary view objects

# ----------------------------------------------------------
# 计算
# 	len(info)
# 		键值对的个数
d={'name': 'sz', 'age': 18, "0": 180}
print(len(d))
# 判定
# 	x in dic
# 		判定dic中的key, 是否存在x
# 	x not in dic
# 		判定dic中的key, 是否不存在x
# 	dic.has_key(key)
# 		已过期, 建议使用in来代替
print("name" in d)
print("0" not in d)#False
print(0 not in d)#True d={'name': 'sz', 'age': 18, 0: 180}--->False