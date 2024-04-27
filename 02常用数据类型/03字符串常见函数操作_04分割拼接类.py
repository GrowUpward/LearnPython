# 开发时间：2024/4/27 23:57
"""----------------------------------------
分割拼接函数速览：
split() partition() rpartition() splitlines() join()
--------------------------------------------
"""

"""----------------------------------------
split
    作用
        将一个大的字符串分割成几个子字符串
    语法
        split(sep, maxsplit)
    参数
        参数1-sep
            分隔符
        参数2-maxsplit
            最大的分割次数
            可省略, 有多少分割多少
    返回值
        分割后的子字符串, 组成的列表
        list 列表类型
    注意
        并不会修改原字符串本身
"""
name="bea-wo-ie-we-122235"
print(name.split('-'))
print(name.split('-',2))#只会分割两个字符串

"""
partition
    作用
        根据指定的分隔符, 返回(分隔符左侧内容, 分隔符, 分隔符右侧内容)
    语法
        partition(sep)
    参数
        参数-sep
            分隔符
    返回值
        如果查找到分隔符
            (分隔符左侧内容, 分隔符, 分隔符右侧内容)
            tuple 类型
        如果没有查找到分隔符
            (原字符串, "", "")
            tuple 类型
    注意
        不会修改原字符串
        从左侧开始查找分隔符
        
rpartition:从右侧开始查找
"""
name="bea-wo-ie-we-122235"
print(name.partition('-'))

"""
splitlines
    作用
        按照换行符(\r, \n), 将字符串拆成多个元素, 保存到列表中
    语法
        splitlines(keepends)
    参数
        参数-keepends
            是否保留换行符
            bool 类型
    返回值
        被换行符分割的多个字符串, 作为元素组成的列表
        list 类型
    注意
        不会修改原字符串
"""
name="bea\nwo\r ie-we-122235\n"
result1=name.splitlines()#默认不保留
result2=name.splitlines(keepends=True)
print(result1)
print(result2)
# print(name)

"""
join
    作用
        根据指定字符串, 将给定的可迭代对象, 进行拼接, 得到拼接后的字符串
    语法
        join(iterable)
    参数
        iterable
            可迭代的对象
                字符串
                元组
                列表
                ...
    返回值
        拼接好的新字符串
"""
items=["always","chase", "light"]
result="-".join(items)
print(result)


