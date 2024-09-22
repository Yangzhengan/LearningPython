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
for i in range(1, n + 1):
    print("")
    # j控制空格个数
    for j in range(n - i):
        print(" ", end="")
    # k控制输出*的个数
    for k in range(2 * i - 1):
        print("*", end="")
