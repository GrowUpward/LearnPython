# 开发时间：2024/4/8 23:50
"""
三角函数:
    sin(x):正弦
    cos(x):余弦
    tan(x):正切
    asin(x):反正弦
    acos(x):反余弦
    atan(x):反正切
    degrees(x):弧度 -> 角度
    radians(x):角度 -> 弧度
"""
import math
# 正弦函数
# sin(x) ,参数，是一个弧度或 角度
# Π=180
jiaodu=30
# hudu=jiaodu/180 *math.pi
hudu=math.radians(jiaodu)
result=math.sin(hudu)
print(result)