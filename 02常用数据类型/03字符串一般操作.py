# 开发时间：2024/4/9 21:54
"""----------------------------------------
字符串拼接
"""
# 使用加号
result="hello"+"world"
print(result)

#直接放在一排，中间可以有空格
result="hello""world"
print(result)

# 占位符
result="hello%s"%"world"
print(result)
result="hello%s,%d"%("world",123)
print(result)

#乘号
print("sz\t"*10)

"""----------------------------------------
字符串切片：获取字符串的某个片段
获取一个字符：name[下标]
获取一个片段：name[起始:结束:步长]
    注意：
    获取范围：[起始, 结束)
    默认值： 起始默认值: 0，结束默认值: len(name)即整个字符串的长度
        步长默认值: 1
    获取顺序步长 > 0从左边到右；步长 < 0从右往左
        注意: 不能从头部跳到尾部, 或者从尾部跳到头部
"""
name="abcdefg"
print(name[2])#注意下标不要越界
print(name[-1])#最后一位

print(name[0:len(name):1])
# print(name[0:len(name):-1])#当前在头部，-1表示从右到左，故下一个是尾部，不行×
print(name[4:1:-1])