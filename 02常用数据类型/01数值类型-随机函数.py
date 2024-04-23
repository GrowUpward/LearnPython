# 开发时间：2024/4/8 23:42
"""---------------------------------------
随机函数：
random
"""
import random
# random()
#   [0, 1):范围之内的随机小数
print(random.random())

# choice(seq)
# 	从一个序列中, 随机挑选一个数值
# 	random.choice((1, 3, 6, 8))
seq=[1,3,5,6,7,8]
print(random.choice(seq))

# uniform(x, y)
# 	[x, y]
# 		范围之内的随机小数
print(random.uniform(1,4))

# randint(x, y)
# 	[x, y]
# 		范围之内的随机整数
print(random.randint(1,4))# 1 or 2 or 3 or 4

# randrange(start, stop=None, step=1)
# 	给定区间内的一随机整数
# 	[start, stop)
print(random.ranrange(1,4)) #1 ,2,3
print(random.ranrange(1,4,2)) #步长为2-->1,3