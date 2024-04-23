# 开发时间：2024/4/6 0:11
"""------------------------------
1.一般使用
"""

#遍历一个集合
# 字符串 列表

notice="社会我顺哥，人狠话不多"
for c in notice:
    print(c)

pets=["小花","小黑","小黄"]
for name in pets:
    print(name)

"""------------------------------
2.与else连用
"""

for c in notice:
    print(c)
    # break

else:
    print("执行完毕")