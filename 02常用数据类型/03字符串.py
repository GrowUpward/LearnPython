# 开发时间：2024/4/9 19:39
"""
字符串：由单个字符组成的一个集合
非原始字符串:字符串里面可以用转义字符
	使用单引号包含的
		'abc'
	使用双引号包含的
		"abc"
	使用3个单引号
		''' abc '''
	使用3个双引号
原始字符串：字符串里面使用转义字符失效，--->是什么就是什么

"""

str1='abc'
print(str1,type(str1))
str2="bcd"
print(str2,type(str2))
str3='''abcd'''
print(str3,type(str3))
str4='''abcde'''
print(str4,type(str4))


"""
转义字符：通过转换某个指定的字符, 使它具备特殊的含义


\' 	单引号
\" 	双引号
\n 	换行
\t 	横向制表符
\(在行尾时) 	续行符
"""
name="我是'phy'" #怎么好像不用也行
name="我是\'phy\'"
print("我是'phy'")#混合使用可以避免转义字符的使用
print("我是\"phy\"")
print(name)
name="s"\
    "z"\
    "123"
print(name)


#打印出：我是\nsz
name1="我是\nsz"
name2="我是\\nsz"
name3=r"我是\nsz"
print(name1)
print(name2)
print(name3)