# @Author : Yzg
# @File   : 37_Python实例.py
# @Time   : 2024/9/27 16:33
# 对10个数进行排序。冒泡排序
# 可以利用选择法，即从后9个比较过程中，
# 选择一个最小的与第一个元素交换，
# 下次类推，即用第二个元素与后8个进行比较，并进行交换。
import random

# 导入random模块，随机生成10个数到l1列表
l1 = []
for i in range(10):
    a = random.randint(1, 100)
    l1.append(a)
# 从小到大排序
# 排序前：
print(f"排序前：{l1}")
# j控制几轮排序
for j in range(0, len(l1) - 1):
    # k控制几次排序
    for k in range(0, len(l1) - 1 - j):
        if l1[k] > l1[k + 1]:
            l1[k], l1[k + 1] = l1[k + 1], l1[k]
print(f"排序后：{l1}")
