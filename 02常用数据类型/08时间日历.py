# 开发时间：2024/5/15 22:50
"""
时间日期类型的定义与常见操作
"""
# Python 程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
# 获取当前时间戳
# 	概念
# 		从0时区的1970年1月1日0时0分0秒, 到所给定日期时间的秒数
# 		浮点数
# 	获取方式
# 		import time
# 		time.time()
import time
res=time.time()
year=res/(60*60*24*365)+1970
print(year)
# 获取时间元组
# 	概念
# 		很多python时间函数将时间处理为9个数字的元组
# 		图解
# 	获取方式
# 		import time
# 		time.localtime([seconds])
# 			seconds
# 				可选的时间戳
# 				默认当前时间戳

res=time.localtime()
print(res)
# (tm_year=2024, tm_mon=5, tm_mday=15, tm_hour=22, tm_min=55, tm_sec=57, tm_wday=2, tm_yday=136, tm_isdst=0)
# 	年			月			日			时			分			秒			周的第几天  	月的第几日	夏令时：-1, 0, 1, -1是决定是否为夏令时的旗帜

# 获取格式化的时间
# 	秒 -> 可读时间
# 		import time
# 		time.ctime([seconds])
# 			seconds
# 				可选的时间戳
# 				默认当前时间戳
res=time.ctime()
print(res)
# 	时间元组 -> 可读时间
# 		import time
# 		time.asctime([p_tuple])
# 			p_tuple
# 				可选的时间元组
# 				默认当前时间元组
time_tuple=time.localtime()
res=time.asctime(time_tuple)
print(res)

# 格式化日期字符串 <--> 时间戳
# 	时间元组 -> 格式化日期

# 		time.strftime(格式字符串, 时间元组)
# 		例如
# 			time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 			2017-09-02 17:21:00
res=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#格式由里面的格式符决定，如%Y表示4位年份
print(res)
# 	格式化日期 -> 时间元组
# 		time.strptime(日期字符串, 格式符字符串)
# 		time.mktime(时间元组)
# 		例如
# 			time.mktime(time.strptime("2017-09-02 17:21:00", "%Y-%m-%d %H:%M:%S"))
# 			1504344060.0

time_str = "2024-05-15 23:06:40"
print(type(time_str))
res = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
# res=time.strftime("2024-05-15 23:06:40","%Y-%m-%d %H:%M:%S")#错误，time.strftime()函数需要接受一个时间元组或struct_time对象作为第一个参数，字符串不可以
print(res)

t=time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))
print(t)

# 获取当前CPU时间
# 	time.clock( )
# 		浮点数的秒数
# 	可用来统计一段程序代码的执行耗时
# 在python3.8及其以上版本已经移除了clock(),用perf_counter()代替


start_time = time.perf_counter()
for i in range(1, 1000):
    print(i)
end_time = time.perf_counter()
spend_time = end_time - start_time
print(spend_time)

# 休眠n秒
# 	推迟线程的执行, 可简单理解为, 让程序暂停
# 	time.sleep(secs)

# start_time = time.perf_counter()
# for i in range(1, 3):
# 	print(i)
# 	time.sleep(1)
#
# end_time = time.perf_counter()
# spend_time = end_time - start_time
# print(spend_time)

# calendar模块
# 	提供与日历相关的功能，比如: 为给定的月份或年份打印文本日历的功能
# 	获取某月日历
import calendar
m=calendar.month(2017, 9)
print(m)

# datetime模块
# 	Python处理日期和时间的标准库
# 		这个模块里面有datetime类，此外常用的还有date类，以及time类
# 		可以做一些计算之类的操作
# 	获取当天日期
# 		import datetime
# 		print(datetime.datetime.now())
# 		print(datetime.datetime.today())
# 	单独获取当前的年月日时分秒
# 		datetime对象里面的一些属性
# 			year
# 			month
# 			day
# 			hour
# 			minute
# 			second
import datetime#这是一个模块
t=datetime.datetime.now()#第二个datetime是一个类（对象）
print(t)
print(type(t))#<class 'datetime.datetime'>
print(t.year)
print(t.hour)#这些都是这个对象的属性

# 	计算n天之后的日期
# 		import datetime
result = datetime.datetime.today() + datetime.timedelta(days = 7)
print(result)

# 	获取两个日期时间的时间差
# 		import datetime
first = datetime.datetime(2017, 9, 1, 12, 0, 0)
second = datetime.datetime(2017, 9, 2, 12, 0, 0)
result = second - first
print(result.total_seconds())