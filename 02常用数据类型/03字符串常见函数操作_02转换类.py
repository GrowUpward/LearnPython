# 开发时间：2024/4/22 22:48
"""----------------------------------------
函数速览：
replace capitalize title lower upper
--------------------------------------------
"""

"""----------------------------------------
replace
    作用
        使用给定的新字符串 替换原字符串中的 旧字符串
    语法
        replace(old, new[, count])
    参数
        参数1-old
            需要被替换的旧字符串
        参数2-new
            替换后的新字符串
        参数3-count
            替换的个数
            可省略, 表示替换全部
    返回值
        替换后的结果字符串
    注意
        并不会修改原字符串本身
        """
name="wo shi wz"
print(name.replace("w","n"))
print(name)
"""
capitalize
    作用
        将字符串首字母变为大写
    语法
        capitalize()
    参数
        无
    返回值
        首字符大写后的新字符串
    注意
        并不会修改原字符串本身
        """
name="wo shi wz"
print(name.capitalize())
print(name)
"""
title
    作用
        将字符串每个单词的首字母变为大写
    语法
        title()
    参数
        无
    返回值
        每个单词首字符大写后的新字符串
    注意
        并不会修改原字符串本身,只要两个字母中间是其他任何符号，都被归为分隔符"""
name="wo s@h#i-w%z+b"
print(name.title())
print(name)
"""
lower
    作用
        将字符串每个字符都变为小写
    语法
        title()
    参数
        无
    返回值
        全部变为小写后的新字符串
    注意
        并不会修改原字符串本身

"""
name="WO SHI WZ"
print(name.lower())
print(name)
#应用于规范化输入，用户可能输入大写的，程序判断小写，就用词函数进行转换
"""upper
    作用
        将字符串每个字符都变为大写
    语法
        upper()
    参数
        无
    返回值
        全部变为大写后的新字符串
    注意
        并不会修改原字符串本身
    转换
"""
name="wo shi wz"
print(name.upper())
print(name)