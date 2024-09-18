# @Author : Yzg
# @File   : 01_Python实例.py
# @Time   : 2024/9/16 12:40


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 给三位数字各个位置创建变量 i j k 循环执行且每两个数字都不能相等
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and i != k and j != k:
                print(f"三位数字分别是：{i}{j}{k}")
