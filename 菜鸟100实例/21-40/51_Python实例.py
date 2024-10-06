# @Author : Yzg
# @File   : 51_Python实例.py
# @Time   : 2024/10/6 17:46
# 学习使用按位与 &
# 0&0=0; 0&1=0; 1&0=0; 1&1=1。
if __name__ == '__main__':
    a = 0x77
    b = a & 3
    print(b)
    b &= 7
    print(b)
