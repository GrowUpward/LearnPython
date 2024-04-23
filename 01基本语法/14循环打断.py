# 开发时间：2024/4/6 20:25
"""
break跳出整个循环
continue 语句跳出本次循环，后面的还是会继续

continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
"""
for i in range(1,11):
    if i==6:
        break
    print(i)

for i in range(1,11):
    if i==6:
        continue
    print(i)