# 开发时间：2024/4/6 20:40
"""
案例1:
	打印1-100之间, 所有3的倍数
"""
# 1.先造一个集合
nums=range(1,101)
# print(nums)

# 2.遍历集合
for num in nums:
    if(num%3==0):
        print(num)


"""
案例2:
	九九乘法表
"""
for i in range(1,10):
    for j in range(1,10):
        if(i>=j):
            print("%d*%d=%d" % (i,j,i*j),end=" ")
    print("\n")

