# @Author : Yzg
# @File   : 24_Python实例.py
# @Time   : 2024/9/22 16:28
# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# 我的思路：分子分母分开看都是斐波那契数列
# 起始项为2的斐波那契数列
def f1(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    else:
        return f1(n - 2) + f1(n - 1)


# 起始项为1的斐波那契数列
def f2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return f2(n - 2) + f2(n - 1)


sum1 = 0
a = int(input("请输入项数："))
for i in range(1, a + 1):
    number1 = f1(i) / f2(i)
    sum1 += number1
print(f"前{a}项的和为{sum1}")
