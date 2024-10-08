# @Author : Yzg
# @File   : 13_Python实例.py
# @Time   : 2024/9/19 17:45
# 打印出所有的"水仙花数"，
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print(f"水仙花水为：{i}")
