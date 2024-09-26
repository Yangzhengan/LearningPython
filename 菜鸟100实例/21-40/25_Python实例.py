# @Author : Yzg
# @File   : 25_Python实例.py
# @Time   : 2024/9/22 16:29
# 求1+2!+3!+...+20!的和。
"""
本来想用嵌套循环写，外层控制个数，外层控制乘数个数，
但仔细想了个数就是乘数的个数
所以先算sum1作为每个阶乘数字，再用sum2累加
"""
sum1 = 1
sum2 = 0
n = int(input("请输入阶乘数："))
for i in range(1, n + 1):
    sum1 *= i
    sum2 += sum1
print(sum2)
