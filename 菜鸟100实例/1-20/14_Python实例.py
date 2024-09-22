# @Author : Yzg
# @File   : 14_Python实例.py
# @Time   : 2024/9/19 19:16
# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# 定义分解质因数函数
def f1(n):
    # 先输入n=""的提示信息，且不换行
    print(n, "=", end=" ")
    # 上网查了isinstance函数的用法，就是跟type()比较相似，
    # 判断类型的，只不过有继承不继承的区别，这一步参考菜鸟
    if not isinstance(n, int) or n <= 0:
        print("请您输入一个正确的数字")
        return 0
    # 此处考虑用户输入1的情况
    elif n in [1]:
        print(n)
    # 当用户输入不是负数、0、1时进入循环，且当n最终为1时退出循环
    while n not in [1]:
        for index in range(2, n + 1):
            # 如果能找到一个从2开始就整除的数字，就让这个n变为除后的商继续循环
            if n % index == 0:
                # 此处第一次运行报错，提示float，这里我做一个强整
                n = int(n / index)
                # 这一步表示除到最后了，只需要输入因子即可
                if n == 1:
                    print(index)
                # 还没除到底，要继续分解
                else:
                    print(index, "*", end=" ")
                # 退出for循环，重新从2开始找最小质因数
                break


f1(int(input("请任意输入一个数字：")))
