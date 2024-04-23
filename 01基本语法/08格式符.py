# 开发时间：2024/3/21 13:01
# %[(name)][flags][width][.precision]typecode
age=18
name="zhang"
print("姓名：%s，年龄：%d" % (name,age))

# 使用[name]
# 使用命名的方式，name1和name2是变量的新名字
print("年龄：%(name2)d,姓名：%(name1)s" % ({"name1":name,"name2": age}))

# width表示占位的宽度
print("%10d" % age)#靠后
print("%-10d" % age)#靠前

# 可填充空格或0
min=5
second=18
print("%2d:%2d" % (min,second))#宽度为2，默认空格填充
print("%02d:%02d" % (min,second))#宽度为2，0填充
print("%12d:%02d" % (min,second))#宽度为12，不是1填充，而是12c

#
score=59.9
print("%d" %score)#整数
print("%i" %score)#整数
print("%.2f" %score)#两位小数

print("%d" % 0b1010)#以“0b“开头的表示二进制

print("%o" %12)#%o-->八进制

# c  # 整数：将数字转换成其unicode对应的值，10进制范围为 0 <= i <= 1114111（py27则只支持0-255）；
# # 字符：将字符添加到指定位置
print("%c" % 1010)
print("%c" % 19997)#汉字：丝
print("%g" % 1011111)#科学计算法


# %  # 当字符串中存在格式化标志时，需要用 %%表示一个百分号
print("%d%%" % score)