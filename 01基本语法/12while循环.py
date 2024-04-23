# 开发时间：2024/4/5 23:56
"""
while:
 一定要注意, 以后, 写循环的时候, 要考虑好, 循环的结束
 修改条件
 打断循环, break

注意：①防止死循环；②没有do-while
"""
# 无限循环
# while(True):
#     print("哈哈")

#固定循环次数
num=0
while(num<10):
    print("第%d遍 哈哈" % (num+1))
    # num++#有问题，为啥不能这样写？
    num+=1

#限制条件（根据变量）
flag=True
num=0
while(flag):
    num+=1
    print("oo")
    if(num==5):
        flag=False

#小练习：求1~10的和
num=1
s=0
while num<=10:
    s+=num
    num+=1
print("%d" % s)