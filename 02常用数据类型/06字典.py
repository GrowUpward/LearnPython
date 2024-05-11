"""
字典：无序的, 可变的键值对集合
意义：
1.可以通过key, 访问对应的值, 使得这种访问更具意义
2.查询效率得到很大提升
"""
# 方式1
# 	{key: value, key: value...}

person={"name": "sz", "age": 18}
print(type(person))
print(person["name"])
print(person["age"])

# 方式2
# 	fromkeys(S, v=None)
# 		静态方法
# 			类和对象都可以调用
# 		类调用
# 			dict.fromkeys("abc", 666)
# 			此处的dict, 是指字典类型

d=dict.fromkeys("abc", 666)
print(d)#{'a': 666, 'b': 666, 'c': 666}

# 		对象调用
# 			dic.fromkeys("abc", 666)
# 				{'a': 666, 'c': 666, 'b': 666}
# 			此处的dic, 是实例化的字典对象
d={1:2,2:3}.fromkeys("abc", 666)
print(d)#{'a': 666, 'b': 666, 'c': 666}
# 注意
    # key不能重复
    # 	如果重复
    # 	后值会把前值覆盖
d={1:2,1:3}
print(d)
    # key必须是任意不可变类型
    #   可变:列表,字典,可变集合...
    # 	不可变:数值,布尔,字符串,元组,...
