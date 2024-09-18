# @Author : Yzg
# @File   : 05_Python实例.py
# @Time   : 2024/9/18 19:53
# 输入三个整数x,y,z，请把这三个数由小到大输出。
x = input("请输入第一个数：")
y = input("请输入第二个数：")
z = input("请输入第三个数：")
# 比较x,y和x,z并且交换 此时的x是最小值
if x > y:
    x = y
    y = x
if x > z:
    x = z
    z = x
# 在判断z和y的值大小
if z > y:
    print(f"这三个数从小到大分别为{x}{y}{z}")
else:
    print(f"这三个数从小到大分别为{x}{z}{y}")
# 菜鸟方法就是直接用list的内置函数sort进行排序，输入也是进行循环输入不用三次input
# list1 = []
# for i in range(3):
#     x = int(input('integer:\n'))
#     list1.append(x)
# list1.sort()
# print(list1)
