# 开发时间：2024/4/27 23:57
"""----------------------------------------
判定函数速览：
split() partition() rpartition() splitlines() join()
--------------------------------------------
"""
# isdigit
# 	作用
# 		字符串中是否所有的字符都是数字
# 			不包含该字母,特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isdigit()
# 	参数
# 		无
# 	返回值
# 		是否全是数字
# 		bool 类型

name="a13,@"
name1="123"
print(name.isdigit())
print(name1.isdigit())

# isalnum
# 	作用
# 		字符串中是否所有的字符都是数字或者字母
# 			不包含该特殊符号,标点符号等等
# 			至少有一个字符
# 	语法
# 		isalnum()
# 	参数
# 		无
# 	返回值
# 		是否全是数字或者字母
# 		bool 类型
name="a13,@"
name1="123a"
print(name.isalnum())
print(name1.isalnum())
# isspace
# 	作用
# 		字符串中是否所有的字符都是空白符
# 			包括空格,缩进,换行等不可见转义符
# 			至少有一个字符
# 	语法
# 		isspace()
# 	参数
# 		无
# 	返回值
# 		是否全是空白符
# 		bool 类型
name="\t"
name1=" "
print(name.isspace())
print(name1.isspace())
# startswith
# 	作用
# 		判定一个字符串是否以某个前缀开头
# 	语法
# 		startswith(prefix, start=0, end=len(str))
# 	参数
# 		参数1-prefix
# 			需要判定的前缀字符串
# 		参数2-start
# 			判定起始位置
# 		参数3-end
# 			判定结束位置
# 	返回值
# 		是否以指定前缀开头
# 		bool 类型
name="name:phy"
print(name.startswith('name:'))

# endswith
# 	作用
# 		判定一个字符串是否以某个后缀结尾
# 	语法
# 		endswith(suffix, start=0, end=len(str))
# 	参数
# 		参数1-suffix
# 			需要判定的后缀字符串
# 		参数2-start
# 			判定起始位置
# 		参数3-end
# 			判定结束位置
# 	返回值
# 		是否以指定后缀结尾
# 		bool 类型

name="acc:99%"
print(name.endswith('%'))
# 补充
# 	in
# 		判定一个字符串, 是否被另外一个字符串包含
# 	not in
# 		判定一个字符串, 是否不被另外一个字符串包含
print('abc' not in 'acd')
