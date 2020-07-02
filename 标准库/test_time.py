import time

def test_time():
    #国外时间格式
    print(time.asctime())
    #时间戳，从1970.1.1
    print(time.time())

    #时间戳转换成时间元组
    print(time.localtime())
    #将当前时间转换成带时间格式
    print(time.strftime("%d-%m-%Y %H:%M:%S",time.localtime()))

#获取两天前时间
def test_twodays_ago():
    #获取当前时间戳
    now_timestamp = time.time()
    #两天前的时间戳
    two_days_before = now_timestamp - 60*60*24*2
    # 时间戳转换成时间元组
    time_tuple = time.localtime(two_days_before)
    print(time.strftime("%d-%m-%Y %H:%M:%S",time_tuple))

import math

def test_math():
    print(math.ceil(6.5))
    print(math.floor(7.2))
    print(math.sqrt(9))
    print(math.degrees(16))