# @Author : Yzg
# @File   : 11_Python实例.py
# @Time   : 2024/9/19 16:46

# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 还是斐波那契数列

print(fib(21))

# f1 = 1
# f2 = 1
# for i in range(1, 22):
#     print('%12ld %12ld' % (f1, f2), end=" ")
#     if (i % 3) == 0:
#         print('')
#     f1 = f1 + f2
#     f2 = f1 + f2
