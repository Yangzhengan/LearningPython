# @Author : Yzg
# @File   : 29_Python实例.py
# @Time   : 2024/9/26 19:29
# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# 菜鸟方法太low了,我自己想了一种方法,正好用到今天学的类
number = (input("请输入一个不多于5位数的正整数:"))
if len(number) > 5:
    print("请重新输入")


class Number:
    def __init__(self, n1):
        self.number = n1

    def f1(self):
        a = len(self.number)
        print(f"这个数是{a}位数")

    def f2(self):
        for i in range(1, len(self.number) + 1):
            print(self.number[-i], end="")


number1 = Number(number)
number1.f1()
number1.f2()
