"""----------------------------------------
查找列表中的元素：四种方式

--------------------------------------------
"""
# 查
# 获取单个元素
#     items[index]
#         注意负索引
# 获取元素索引
#     index()
# 获取指定元素个数
#     count()

name=[1,1,2,3,4,5]
print(name[1])
print(name.index(1))
print(name.count(1))
# 获取多个元素
#     切片
#         items[start:end:step]
n=name[1:5:2]#end取不到
print(n)
# 遍历
#     方式1
#         直接根据元素进行遍历
#             for item in list:
# print(item)
name=['a','b','c','d']
for n in name:
    print(n)
#     方式2
#         根据索引进行遍历
#             for index in range(len(list)):
# print(index, list[index])
name=['a','b','c','d']
length=len(name)
for i in range(length):
    print(i,name[i])
#     方式3(了解)
#         创建对应的枚举对象
#             概念
#                 通过枚举函数, 生成的一个新的对象
#             作用
#                 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
#                 同时列出数据下标和数据
#             语法
#                 enumerate(sequence, [start=0])
#                         sequence -- 一个序列、迭代器或其他支持迭代对象。
#                         start -- 下标起始位置。
#             举例
#                 l = ["a", "b", "c"]
#                 enumerate(l, 1)
#                     一个待枚举的对象
#                     转换成为list之后, 具体数据如下
#                         [(1, 'a'), (2, 'b'), (3, 'c')]
#         遍历枚举对象
#             for index, value in 枚举对象:
# print(index, value)
name=['a','b','c','d']
#创建枚举对象
# print(enumerate(name))
for idx,val in enumerate(name):
    print(idx,val)
for tupleVal in enumerate(name):
    print(tupleVal)
    # print(tupleVal[0])
    # print(tupleVal[1])
for tupleVal in enumerate(name):
  idx,val=tupleVal
  print(idx,val)
#     方式4(了解)
#         使用迭代器进行遍历
#             iterL = iter(list)
#             for item in iterL:
# print(item)

# 如何判定一个变量是否是迭代器
# import collections
# name=[1,2]
# result=isinstance(name,collections.Iterable)#isinstance()用于判断里面的元素是否具有某种属性
# print(result)
name=['a','b','c','d']
#创建一个迭代器对象
iterl=iter(name)
# for item in iterl:
#     print(item)

for i in range(len(name)):
    print(next(iterl))