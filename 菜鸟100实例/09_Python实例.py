# @Author : Yzg
# @File   : 09_Python实例.py
# @Time   : 2024/9/19 16:30

# 暂停一秒输出。
# 使用 time 模块的 sleep() 函数。

import time

# list1 = []
# for i in range(1, 5):
#     list1.append(i)
# print(list1)

list1 = [1, 2, 3, 4]
for i in range(len(list1)):
    # 遍历列表中的元素
    print(list1[i])
    time.sleep(1)
