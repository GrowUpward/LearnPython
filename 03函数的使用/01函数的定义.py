"""
概述：函数的定义、参数、返回值
"""
# 函数的概念
# 	概念
# 		写了一段代码实现了某个小功能; 然后把这些代码集中到一块, 起一个名字; 下一次就可以根据这个名字再次使用这个代码块, 这就是函数
# 	作用
# 		方便代码的重用
# 		分解任务, 简化程序逻辑
# 		使代码更加模块化
# 	函数分类
# 		内建函数
# 		三方函数
# 		自定义函数
print(1)
print(1)
print(1)
print(1)
# 函数的基本使用
# 	简单定义
# 		def 函数名():
# 			函数体
# 	函数的调用
# 		函数名()
def test(num):
    print(num)
test(1)
test(1)
test(1)
test(1)
#----------------------------------------函数的参数----------------------------------------------------
# 两个形参
def sum(num1,num2):
    res=num1+num2
    print(num1,num2,res)

sum(1,2)
sum(num2=3,num1=2)

#多个参数、不定长参数
# 方式一：元组
def sum2(t):
    print(t,type(t))
    result=0
    for v in t:
        print(v)
        result+=v
    print(result)
sum2((4,5,6))#传元组

#方式二：字典
def sum3(**kwargs):
    print(kwargs,type(kwargs))

sum3(name="sz",age=12)


def mysum(a,b,c,d):
    print(a+b+c+d)
def test(*ags):
    print(ags)
    # 拆包
    print(*ags)
    # mysum((1,2,3,4))#错误，函数有四个形参，这里只有一个——元组
    # mysum(ags[0],ags[1],ags[2],ags[3])
    mysum(*ags)
test(1,2,3,4)

def mysum2(a,b):
    print(a+b)
def test2(**kwargs):
    print(kwargs)
    # 拆包
    mysum2(**kwargs)
test2(a=1,b=2)

# 默认参数
def show(name="hhhh"):
    print(name)
show()


# 参数注意
# 	值传递和引用传递
# 		值传递
# 			是指传递过来的, 是一个数据的副本;
# 			修改副本, 对原件没有任何影响
# 		引用传递
# 			是指传递过来的, 是一个变量的地址
# 			通过地址, 可以操作同一份原件
# 	但是注意
# 		在Python当中, 你没得选, 只有引用传递(地址传递)
# 		但是
# 			如果数据类型是可变类型, 则可以改变原件
# 			如果数据类型是不可变类型, 则不可以改变原件

# 数据类型是不可变类型
# def sum5(num):
#     print(id(num))
#     #刚开始a,num指向同一个地址，但是由于num是tuple类型，不可改，给num重新赋一个值，会重新开辟一块内存，让num指向它，所以一旦值改变了，地址也要变
#     num=6
#     print(id(num))
#
# a=5
# print(id(a))
# sum5(a)
# print(a)

# 数据类型是可变类型
def sum5(num):
    print(id(num))
    #刚开始a,num指向同一个地址，但是由于num是list类型，可改，给num重新赋一个值，不会重新开辟一块内存，让num指向它，所以就算值改变了，地址也不变
    num.append(666)
    print(id(num))

a=[1,2,3]
print(id(a))
sum5(a)
print(a)

#----------------------------------------函数的返回值----------------------------------------------------
# 函数的返回值
# 	场景
# 		当我们通过某个函数, 处理好数据之后, 想要拿到处理的结果
# 	语法
# 		def 函数():
# 	函数体
# 	return 数据
# 	注意事项
# 		1. return 后续代码不会被执行
# 		2. 只能返回一次
# 		3. 如果想要返回多个数据, 可先把多个数据包装成一个集合, 整体返回
# 			列表
# 			元组
# 			字典
# 			...
def sum(num1,num2):
    return num1+num2
res=sum(1,2)
print(res)

def fun(a,b):
    sum=a+b
    sub=a-b
    return (sum,sub)#包装成集合
a,b=fun(6,2)#拆包
print(a,b)

#
# # 函数的描述
    # 定义格式
    # 	直接在函数体的最上面, 添加三个双引号对注释
    # 	def 函数():	''' 这里写帮助信息 '''
    # 查看函数使用文档
    # 	help(函数)
    # 一般函数的描述, 需要说明如下几个信息
    # 	函数的功能
    # 	参数
    # 		含义
    # 		类型
    # 		是否可以省略
    # 		默认值
    # 	返回值
    # 		含义
    # 		类型
def fun2(a,b=1):
    """
    计算两个数的和、查
    :param a:数值1，数值类型，不可选，没有默认值
    :param b:数值1，数值类型，不可选，有默认值
    :return:返回的是计算的结果，元组：(和，差)
    """
    sum=a+b
    sub=a-b
    return (sum,sub)#包装成集合

help(fun2)