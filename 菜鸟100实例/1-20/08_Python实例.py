# @Author : Yzg
# @File   : 08_Python实例.py
# @Time   : 2024/9/19 16:10


# 输出 9*9 乘法口诀表。
for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print(f"{i}×{j}={i * j}", end=" ")
