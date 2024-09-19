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
