# @Author : Yzg
# @File   : 46_Python实例.py
# @Time   : 2024/10/6 17:26
# 求输入数字的平方，如果平方运算后小于 50 则退出
while True:
    n = int(input("请输入一个数字:"))
    num = n * n
    if num < 50:
        break
    else:
        print(num)
