# 开发时间：2024/4/22 22:20
"""----------------------------------------
分类：
    1.内建函数, 直接使用
    2.对象方法，使用：对象.方法(参数)
"""

"""----------------------------------------
函数速览：
查找计算类： find rfind index rindex | len count
--------------------------------------------
len
    作用；计算字符串的字符个数
    语法：len(name)
    参数：字符串
    返回值：整型 字符个数
"""
name="wosh\n" #转义字符\n算一个
num=len(name)
print(num)

"""----------------------------------------
find
    作用: 查找子串索引位置
    语法: find(sub, start=0, end=len(str))
    参数: 
        参数1 sub
            需要检索的字符串
        参数2 start
            检索的起始位置
            可省略, 默认0
        参数3 end
            检索的结束位置
            可省略, 默认len(str)
    返回值
        找到了: 指定索引 整型
        找不到: -1
    注意
        从左到右进行查找
        找到后立即停止
"""
name="abcd abc"
num=name.find('c')#找子串
print(num)#下标为2

num=name.find('bc')
print(num)#下标为1
num=name.find('bd')
print(num)#找不到

num=name.find('c',3)#找子串,从下标为3的位置开始
print(num)#只能找到第二个c,在原串中下标为7

num=name.find('c',3,7)#找子串,从下标为3的位置开始
print(num)#[3,7),取不到7

"""---------------------------------------
rfind
    功能使用, 同find
    区别
        从右往左进行查找
        
index 同find一样，差别只是如果找不到它会报错
rindex 同index一样，只是从右往左进行查找
"""

"""---------------------------------------
count
    作用：计算某个子字符串的出现个数
    语法：count(sub, start=0, end=len(str))
    参数
        参数1-sub
            需要检索的字符串
        参数2-start
            检索的起始位置
            可省略, 默认0
        参数3-end
            检索的结束位置
            可省略, 默认len(str)
    返回值
        子字符串出现的个数
        整型
"""
name="abcd ab"
num=name.count("ab")
print(num)


