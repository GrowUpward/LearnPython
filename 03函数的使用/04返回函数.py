# 返回函数
# 	概念
# 		是指一个函数内部, 它返回的数据是另外一个函数; 把这样的操作成为"返回函数"
# 	案例
# 		根据不同参数, 获取不同操作, 做不同计算

def getFunc(flag):
    def sum(a,b,c):
        return a+b+c
    def sub(a,b,c):
        return a-b-c

    if flag=="+":
        return sum
    elif flag=="-":
        return sub

result=getFunc("+")
res=result(1,2,5)
print(res)