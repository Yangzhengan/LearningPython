# @Author : Yzg
# @File   : 39_Python实例.py
# @Time   : 2024/9/27 16:33
# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
import random

l1 = []
flag = 0
for i in range(5):
    x = random.randint(4, 20)
    l1.append(x)
l1.sort()
print(l1)
a = int(input("请输入一个你想插入的整数数字:"))
for i in range(len(l1)):
    # 插入数字最大
    if a > l1[len(l1) - 1]:
        l1.append(a)
    # 插入数字最小
    elif a < l1[0]:
        l1.insert(0, a)
    # 插入数字中间大
    elif l1[i] < a < l1[i + 1]:
        # 第一次写的时候flag=i,发现不对，后来想了想插入元素就相当于多了一个
        flag = i + 1
        # 又进行测试发现如果插入的数最大，那么就会报错，需要在上面基础上改进：
        l1.insert(flag, a)

print(l1)
