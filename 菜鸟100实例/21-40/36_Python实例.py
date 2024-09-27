# @Author : Yzg
# @File   : 36_Python实例.py
# @Time   : 2024/9/27 16:33

# 求100之内的素数。
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
