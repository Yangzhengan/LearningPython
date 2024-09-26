# @Author : Yzg
# @File   : 23_Pyhon实例.py
# @Time   : 2024/9/22 16:28
# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 循环嵌套里面的知识
n = int(input("请输入层数："))
# 正序打印一遍，上菱形
for i in range(1, n + 1):
    print("")
    # j控制空格个数
    for j in range(n - i):
        print(" ", end="")
        # k控制输出*的个数
    for k in range(2 * i - 1):
        print("*", end="")
# 下菱形
for i in range(1, n):
    print("")
    for j in range(i):
        print(" ", end="")
        # 此处的k值取决于最大*的个数，与n关联
    for k in range(2 * n - 1 - 2 * i):
        print("*", end="")
