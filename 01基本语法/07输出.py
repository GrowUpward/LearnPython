# 开发时间：2024/3/19 12:53
import sys
from time import sleep
# 输出一个值
print(123)
# 输出一个变量
num=2
print(num)
# 输出多个变量：逗号分隔（给函数看的），打印出来是以空格分隔的
num2=3
print(num,num2)
# 格式化输出
name='zhang'
age=18

print("姓名：%s,年龄：%d"%(name,age))
print("姓名：{0}，年龄：{1}".format(name,age))#format里面是用索引的

# 输出到文件中
f=open("test.txt","w")
# print("xxxxxxxxxxxx",file=f)cccccccc
print("xxxxxxxxxxxx",file=sys.stdout)#标准输入输出-->输出到控制台

# 输出不自动换行
print("abc",end="")#没换
print("abc",end="\n")#换了,默认的

# 输出各个数据，使用分隔符分割
print("1","2","3",sep="&")#以“&”进行分割

#flush参数的说明
print("请输入账号：\n",end="",flush=True)#不换行

#休眠5s
sleep(5)
print("xxx")