# @Author : Yzg
# @File   : 61_python实例.py
# @Time   : 2024/10/19 16:06
# 打印出杨辉三角形
n = 10


def f1(i, j):
    if i == j or j == 1:
        return 1
    else:
        return f1(i - 1, j - 1) + f1(i - 1, j)


for i in range(1, n + 1):
    print()
    for j in range(1, i + 1):
        print(f1(i, j), end=" ")
