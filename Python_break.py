# @Author : Yzg
# @File   : Python_break.py
# @Time   : 2024/9/16 11:31
chance = 3
for i in range(1,4):
    name = input("请输入用户名:")
    if name == "张无忌":
        break
    else:
        chance -= 1
        print(f"登录失败，您的登录次数还剩{chance}次")

print("登录成功 888")
