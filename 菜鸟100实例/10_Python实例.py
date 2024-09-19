# @Author : Yzg
# @File   : 10_Python实例.py
# @Time   : 2024/9/19 16:39

# 暂停一秒输出，并格式化当前时间

import time
import datetime

time.sleep(1)
TIME = datetime.datetime.now()
print(TIME.strftime("%Y.%m.%d %H-%M-%S"))  # strftime函数用于格式化时间，返回以可读字符串表示的当地时间
# 后面那一串表示的是格式化输出
