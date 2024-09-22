# @Author : Yzg
# @File   : 21_Python实例(2).py
# @Time   : 2024/9/16 11:31

# peach = 1
# def monkey(n):
#     if n == 10:
#         return 1
#     else:
#         return (monkey(n + 1) + 1) * 2
#
#
# print(monkey(int(input("请输入天数："))))

def f1(n):
    if n == 1:
        return 3
    else:
        return 2 * f1(n - 1) + 1


print(f1(10))
