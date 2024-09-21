# @Author : Yzg
# @File   : 19_Python实例.py
# @Time   : 2024/9/21 20:58
# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。
for i in range(1, 1001):
    # 每次累加完要清0
    sum_number = 0
    # 限定为此数的因数范围内
    for j in range(1, i):
        if i % j == 0:
            sum_number += j
    if sum_number == i:
        print(i)
