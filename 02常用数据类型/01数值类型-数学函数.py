# 开发时间：2024/4/8 23:26
"""---------------------------------------
数学函数：
abs,max,min,round,pow……
"""

# abs(num) 返回数字的绝对值
print(abs(-3))

# max() 返回最大值
print(max(-1,0,2))

# min() 返回最小值
print(min(-1,0,2))

# round(num[,n] 四舍五入
print(round(3.1415,2))#保留两位

# pow(x,y) 返回x的y次幂
print(pow(2,3))

"""------------------------------------------
math模块函数
先要导入模块，
使用：math.【函数名(参数)】
"""
import math
p1=3.1
print(round(p1))
# 上取整
print(math.ceil(p1))
# 下取整
print(math.floor(p1))

# 开平方
print(math.sqrt(9))
# 求对数 log(x, base) 以base为基数, x的对数
print(math.log(1000,10))#10的3次方=1000