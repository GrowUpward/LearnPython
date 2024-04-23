#只要知道执行的流程即可
num=0
while num<10:
    num+=1
    print("num:",num)
    break #注意加了break,会被打断
else:
    print("整个循环结束")