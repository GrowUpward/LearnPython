# 开发时间：2024/4/8 0:17
"""
用户输入一个3位数值, 判定是否是水仙花数
水仙花数：百位的3次方 + 十位的3次方 + 个位的3次方= 数值本身
如153
"""
while True:
    # 输入数据
    num=input("请输入一个3位数：")
    num=int(num)

    # 判定
    if not(100<=num<=999):
        print("输入数据无效，退出程序！")
        exit()
    print("输入数据有效，即将进行判定！")
    c=num%10#个位
    a=num//10#注意这里必须得用两个斜杠，要整除，不然有问题
    b=a%10#十位
    a=a//10#百位
    print("%d %d %d" %(a,b,c))

    num2=a**3+b**3+c**3
    print(num2)
    if(a**3+b**3+c**3 == num):
        print("该数是水仙花数")
    else:
        print("该数不是水仙花数")

