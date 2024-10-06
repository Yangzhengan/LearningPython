# @Author : Yzg
# @File   : 47_Python实例.py
# @Time   : 2024/10/6 17:30
# 两个变量值互换
def exchange(a, b):
    a, b = b, a
    return a, b


if __name__ == '__main__':
    x = 10
    y = 20
    print(x, y)
    x, y = exchange(x, y)
    print(x, y)
