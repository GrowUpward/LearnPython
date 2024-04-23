# 开发时间：2024/3/17 0:03
a="6"
print(type(a))
b=int(a)
print(type(b))

# score=input("请输入一个数字：\n")
# print(type(score))#控制台输入的一定是str类型
# print(int(score)+6)#数字的话需要手动转换

num="123a"
print(int(num))#出错，“a”不能转为数值类型