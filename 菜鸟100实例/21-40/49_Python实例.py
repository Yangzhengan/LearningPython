# @Author : Yzg
# @File   : 49_Python实例.py
# @Time   : 2024/10/6 17:33
# 使用lambda来创建匿名函数
f1 = lambda x, y: (x > y) * x + (x < y) * y
f2 = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print(f1(a, b))
    print(f2(a, b))
