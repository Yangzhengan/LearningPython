# @Author : Yzg
# @File   : 26_Python实例.py
# @Time   : 2024/9/26 19:18
# 利用递归方法求5!

def f1(n):
    if n == 0:
        sum_number = 1
    else:
        sum_number = n * f1(n - 1)
    return sum_number


print(f1(int(input("请输入你要求的阶乘数："))))
