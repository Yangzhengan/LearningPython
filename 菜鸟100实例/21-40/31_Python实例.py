# @Author : Yzg
# @File   : 31_Python实例.py
# @Time   : 2024/9/27 16:05
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
alp = input("请输入第一个字母:")
if alp == "M":
    print("星期一")
elif alp == "W":
    print("星期三")
elif alp == "F":
    print("星期五")
if alp == "T":
    alps = input("请输入T后的第二个字母:")
    if alps == "U":
        print("星期二")
    elif alps == "H":
        print("星期四")
if alp == "S":
    alps = input("请输入T后的第二个字母:")
    if alps == "A":
        print("星期六")
    elif alps == "U":
        print("星期日")
