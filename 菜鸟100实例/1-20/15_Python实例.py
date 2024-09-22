# @Author : Yzg
# @File   : 15_Python实例.py
# @Time   : 2024/9/19 19:19
# 利用条件运算符的嵌套来完成此题：
# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
socre = int(input("请输入你的成绩："))
if socre >= 90:
    print("恭喜你你的成绩为A")
elif socre >= 60:
    print("恭喜你你的成绩为B")
else:
    print("恭喜你你的成绩为C")

# 菜鸟上的一个笔记方法，方法跟实例2是同样的思路
# i = int(input('请输入成绩：'))
# ar = [90, 60, 0]
# res = ['A', 'B', 'C']
# for idx in range(0, 3):
#     if i >= ar[idx]:
#         print(res[idx])
#         break
