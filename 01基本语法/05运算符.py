# 开发时间：2024/3/17 22:58
# 支持中文：
# _*_coding:utf-8 _*_

# --------1.算术运算符--------
# 	+ 加法运算符
print(1+2)#数值
print("1"+"2")#字符串
print([1,2]+[3,4])#元组
# 	- 减法运算符
# 同上
print(4-8)
# 	* 乘法运算符
print(2*3)
# 	** 幂运算符
print(2**3)
# 	/ 除法运算符
print(3/2)
# 	// 整除运算符
print(3//2)#整数
print(4.2//2)#浮点数
# 	% 求模运算符（取余数）
print(5%2) #5➗2=2……1
# 	= 赋值运算符
# 			a = 10
# 			b = a + c
# 			a, b, c = 10, 20, 30
# 			链式赋值
# 				a = b = c = 3

# 	注意
# 		除以0
# 		优先级问题
# 			()使用
result=(1+2)*3/4
print(result)
# 	整除和求余的应用场景 --->求行列
"""
a=[[0,1,2,3],
   [4,5,6,7]]
"6":第2行第3列
6➗4=1……2 4：一行有4个，
第“2”行：商+1，
第“3”列：余数+1
"""

# --------2.复合运算符--------
# 	+=
num=10
num+=5
# num=num+5
print(num)
# 	-=
# 	*=
num=2
num*=3
print(num)
num=2
num=num*3
print(num)
# 	%=
# 	**=
# 	//=
# 本质：
# a  x= 值
# a = a x 值

# --------3.比较运算符--------
# >, <,!=, >=,<=, ==,
# 结果：bool
result=10>2
print(result)
num=10
print(id(num))#id表示变量num的唯一标识
# is用于比较唯一标识
a=10
b=10
print (id(a), id(b))
print(a is b)#true

a=[1]
b=[1]
print(a == b)#值相同
print(a is b)#分配的内存空间不同，唯一标识不一样
# 链式比较
# 其他语言：num>5 && num<10
num=8
print(5<num<10)

# --------4.逻辑运算符--------
b=False
# not 非 取反；真->假，假->真
print(not b)
#and 与 并且；两真才真
print(True and False)
# or 或 或者；一假就假
print(True or False)

"""
注意:
非布尔类型的值, 如果作为真假来判定, 一般都是非零即真, 非空即真
整个逻辑表达式的结果不一定只是True和False
"""
#非0即真
print(1 or False)#1  or运算符
# print(0 or False)#False ->只有0
print("0" or False)#0
#非空即真
print(bool(""))#False 没东西->空
print(bool("0"))#True 有东西->字符串0

#短路运算符：判断到哪儿，就返回前面的结果
print(1 or False)#1  or运算符，判断到1，就已经知道结果了，直接返回前面的值，不用接着判断了
print(1 and 3)#3->必须要判断到3才知道结果
print(1 or 3)#1->非0即真，一假就假->到1结束
print(0 or False or 6)#6