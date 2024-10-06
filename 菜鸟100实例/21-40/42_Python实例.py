# @Author : Yzg
# @File   : 42_Python实例.py
# @Time   : 2024/10/6 16:21
# 学习使用auto定义变量的用法
num = 2


def autofunc():
    num = 1
    # 这里已经有提示告诉你是外部变量了
    print('internal block num = %d' % num)
    num += 1


for i in range(3):
    print('The num = %d' % num)
    num += 1
    autofunc()
