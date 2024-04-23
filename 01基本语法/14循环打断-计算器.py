# 开发时间：2024/4/6 20:30
"""
案例：
	做一个简单的加法计算器, 让用户输入两个数值, 输出对应的和
	要求
		用户如果不退出这个程序, 则输出完毕之后, 继续让用户使用
		如果用户输入一个标识: q, 识别成退出
		如果中间用户输入的数据有误, 则给出错误提示, 并从头开始, 让用户数据数值
"""
while True:
    num1=input("请输入第一个数值：")
    num1=float(num1)
    num2=input("请输入第二个数值：")
    num2=float(num2)
    result=num1+num2

    # 异常判断
    if num1>100 or num2>100:
        print("输入有问题，请重新输入！")
        continue
    # 输出结果
    print("结果为：",result)
    #是否继续
    isQ=input("是否继续：（q:退出，其他：不退出，继续）")
    if isQ=='q':
        break

