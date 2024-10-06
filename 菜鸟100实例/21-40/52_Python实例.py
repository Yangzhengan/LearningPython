# @Author : Yzg
# @File   : 52_Python实例.py
# @Time   : 2024/10/6 17:47
# 学习使用按位或 | 。
# 0|0=0; 0|1=1; 1|0=1; 1|1=1
if __name__ == '__main__':
    a = 0o77
    b = a | 3
    print(b)
    b |= 7
    print(b)
