# 闭包
# 	概念
# 		1.在函数嵌套的前提下
# 		2.内层函数引用了外层函数的变量(包括参数)
# 		3.外层函数, 又把 内层函数 当做返回值进行返回
# 		这个内层函数+所引用的外层变量, 称为 "闭包"
# 	标准格式

def test():
    a=10;
    def test2():    #1.函数嵌套
        print(a)    #2.内层函数使用外层变量
    return test2    #3.返回内层函数，注意没有括号

newFunc=test()#返回的是test2,所以newFunc相当于test2
newFunc()#==>调用test2
"""
这个内层函数+所引用的外层变量, 称为 "闭包"
所以：
    a=10;
    def test2():
        print(a)
    return test2
这些称为闭包
"""
# 	应用场景
# 		外层函数, 根据不同的参数, 来生成不同作用功能的函数
# 	案例
# 		根据配置信息, 生成不同的分割线函数
# print("----------------123---------------------")
def line_config(content,length):
    print("-"*(length//2)+content+"-"*(length//2))

line_config("闭包",20)
line_config("闭包",20)
line_config("闭包",20)
line_config("闭包",20)
# 上面这种方法一看就麻烦
# 使用闭包
def line_config(content,length):
    def line():
        print("-"*(length//2)+content+"-"*(length//2))
    return line

line1=line_config("闭包",20)
line1()
line1()
line1()
line1()

line2=line_config("闭包2",40)
line2()
line2()
line2()
line2()

# 	注意事项
# 		1. 闭包中, 如果要修改引用的外层变量
# 			需要使用  nonlocal 变量  声明
# 			否则当做是闭包内, 新定义的变量
# 		2. 当闭包内, 引用了一个, 后期会发生变化的变量时, 一定要注意
# 			函数, 是被调用时, 才去确定变量标识所对应的值
# 这个内层函数+所引用的外层变量, 称为 "闭包"
#内部函数与外部函数就算使用相同的变量名，但它们也是独立的
def test3():
    a=3
    def test4():
        a=100
        print(a)

    print(a)#3
    test4()#100
    print(a)#3
    return test4
res=test3()
print("------------------------------------------------------")
def test3():
    a=3
    def test4():
        nonlocal a #修改引用的外层变量
        a=100
        print(a)

    print(a)#3
    test4()#100
    print(a)#100
    return test4
res=test3()

print("------------------------------------------------------")
def test():
    a=1
    def test2():
        print(a)
    a=2
    return test2
res=test()
res()#2
# 函数是什么时候才会确定内部变量标识对应的值？
# 当函数被调用的时候，才会去找标识对应的值，之前都是以普通的变量标识

print("------------------------------------------------------")

def test():
    funcs=[]
    for i in range(1,4):
        def test2():
            print(i)
        funcs.append(test2)
    return funcs#返回一个函数列表
newFuncs=test()#这里调用test,test2并未赋值，里面仍是print(i)，3次调用之后i=2,
print(newFunc)
newFuncs[0]()
newFuncs[1]()
newFuncs[2]()

print("------------------------------------------------------")
# 如何才能打印1，2，3
def test():
    funcs=[]
    for i in range(1,4):
        def test2(num):
            def inner():
                print(num)
            return inner
        funcs.append(test2(i))#这里是给test2传了值的，所以打印的是i的具体数值
    return funcs#返回一个函数列表
newFuncs=test()#这里调用test,test2并未赋值，里面仍是print(i)，3次调用之后i=2,
print(newFunc)
newFuncs[0]()
newFuncs[1]()
newFuncs[2]()
