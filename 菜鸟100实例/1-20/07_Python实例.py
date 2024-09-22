# @Author : Yzg
# @File   : 07_Python实例.py
# @Time   : 2024/9/19 16:01

# 将一个列表的数据复制到另一个列表中

# 定义一个空列表，通过list.extend方法添加
a = []
b = [1, 2, 3]
# 将b列表中的元素全部一次性添加到a中
a.extend(b)
print(f"f两个列表a, b分别为{a}{b}")

a = b[:]  # 或者用菜鸟中的方法直接遍历b，将其赋值给a列表
print(f"f两个列表a, b分别为{a}{b}")
