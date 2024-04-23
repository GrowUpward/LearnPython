# 开发时间：2024/3/23 19:46
"""
单分支：if(条件满足即执行 )
双分支；if-else
多分支：if-elif-...-elif-else
"""

# 单分支：if
age=17
if age >=18:
    print("你已经成年")# 注意缩进
    print("可以去上网 ")

print("赶紧回家吃饭")



# 双分支；if-else

if age >=18:
    print("你已经成年")
else:
    print("你未成年")

"""
练习案例
	根据分数区间, 打印出对应的级别
	大于等于90  并且 小于等于100
		 优秀
	大于等于80  并且 小于90
		良好
	大于等于60  并且 小于80
		及格
	大于等于0  并且 小于60
		不及格
"""

score=50
# 单分支
# if score>=90 and score<=100:
#     print("优秀")
# if 80<=score<=90:#链式比较
#     print("良好")
# if score>=60 and score<=80:
#     print("及格")
# if score>=0 and score<=60:
#     print("不及格")

# 双分支
if score>=90 and score<=100:
    print("优秀")
else:
    if 80<=score<=90:#链式比较
        print("良好")
    else:
        if score >= 60 and score <= 80:
            print("及格")
        else:
            if score >= 0 and score <= 60:
                print("不及格")

# 多分支：if-elif-...-elif-else
score=50
if score>=90 and score<=100:
    print("优秀")
elif 80<=score<=90:#链式比较
    print("良好")
elif score >= 60 and score <= 80:
    print("及格")
elif score >= 0 and score <= 60:
    print("不及格")