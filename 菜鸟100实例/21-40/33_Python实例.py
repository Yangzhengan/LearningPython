# @Author : Yzg
# @File   : 33_Python实例.py
# @Time   : 2024/9/27 16:06
# 按逗号分隔列表。
numbers = list(range(1, 9))
for i in numbers:
    if i == numbers[-1]:
        print(i)
    else:
        print(i, end=',')
