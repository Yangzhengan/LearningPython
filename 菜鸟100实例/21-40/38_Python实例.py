# @Author : Yzg
# @File   : 38_Python实例.py
# @Time   : 2024/9/27 16:33
# 求一个3*3矩阵主对角线元素之和。
"""
如何创建一个二维数组（矩阵）
"""
import numpy as np

l1 = []
sum1 = 0
sum2 = 0
# 第一种利用双重for循环创建
for i in range(3):
    l1.append([])
    for j in range(3):
        l1[i].append(int(input("input num:\n")))
for i in range(3):
    sum1 += l1[i][i]
print(sum1)

# 使用numpy库中的函数
array = np.mat("1 2 3;4 5 6;7 8 9")
print(array)
