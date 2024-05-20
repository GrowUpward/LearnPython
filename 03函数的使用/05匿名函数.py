# 匿名函数
# 	概念
# 		也称为 "lambda函数"
# 		顾名思义, 就是指没有名字的函数
# 	语法
# 		lambda 参数1, 参数2.. : 表达式
# 		限制
# 			只能写一个表达式
# 				不能直接return
# 			表达式的结果就是返回值
# 			所以, 只适用于一些简单的操作处理
# 	测试
result=func = (lambda x, y: x + y)(1,2)
print(result)
newFunc=lambda x,y:x+y
print(newFunc(1,2))

# 使用场景
# 对字典排序
stu = [{"name": "sz", "age": 18}, {"name": "sz2", "age": 17}, {"name": "sz3", "age": 19}]
# def getKey(x):
#     return x["name"]
res=sorted(stu,key=lambda x:x["age"])
print(res)
