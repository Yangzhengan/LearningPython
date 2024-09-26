# @Author : Yzg
# @File   : 27_Python实例.py
# @Time   : 2024/9/26 19:28
# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来


def f1(char, l2):
    if l2 == 0:
        return
    print(char[l2 - 1], end="")
    f1(char, l2 - 1)


char1 = input("请输入字符串:")
l1 = len(char1)
f1(char1, l1)
