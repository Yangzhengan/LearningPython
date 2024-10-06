# @Author : Yzg
# @File   : 54_Python实例.py
# @Time   : 2024/10/6 17:49
# 取一个整数a从右端开始的4〜7位。
if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print('%o\t%o' % (a, d))
