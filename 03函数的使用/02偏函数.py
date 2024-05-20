# 偏函数：函数偏爱某一个值
# 	概念&场景
# 		当我们写一个参数比较多的函数时, 如果有些参数, 大部分场景下都是某一个固定值, 那么为了简化使用, 就可以创建一个新函数, 指定我们要使用的函数的某个参数, 为某个固定的值; 这个新函数就是"偏函数"
# 	语法
# 		方式1
# 			自己写一个新的
# 		方式2
# 			借助functools模块的partial函数
# 				import functools
# 				newFunc = functools.partial(函数, 特定参数=偏爱值)
# 	场景
# 		int()

def test(a,b,c,d=1):
    print(a+b+c+d)
#方式1
def test2(a,b,c,d=2):
    test(a,b,c,d)

test2(1,2,3)#d=2
#方式2
import functools
newFunc=functools.partial(test,c=5)
print(newFunc,type(newFunc))
newFunc(1,2)