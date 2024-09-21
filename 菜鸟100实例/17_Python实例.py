# @Author : Yzg
# @File   : 17_Python实例.py
# @Time   : 2024/9/21 19:54

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


"""
本来自己的思路是：
输入一行字符，然后把字符串转成列表，这样每个元素就能被单独列出来
再去用isinstance函数判断每个元素对应相同，累加输出，但是调试后才想到
键盘输入的默认都是字符串，思路就不可行了
但是看到下面笔记有另一种思路就是利用字符在ASCII码中的位置逐个统计
于是又觉得可行了
"""
str_a = input("请输入一行字符：")
list_a = list(str_a)
count_str = 0
count_number = 0
count_space = 0
for i in range(0, len(list_a)):
    if isinstance(list_a[i], str):
        count_str += 1
    elif isinstance(list_a[i], int):
        count_number += 1
    else:
        count_space += 1
print(f"英文字母，数字，其他字符个数分别为{count_str} {count_number} {count_space}")

# 分隔符
print("-"*50)


str_a = input("请输入一行字符：")
count_str = 0
count_number = 0
count_space = 0
count_other = 0
for i in range(0, len(str_a)):
    if "0" <= str_a[i] <= "9":
        count_number += 1
    elif "A" <= str_a[i] <= "Z" or "a" <= str_a[i] <= "z":
        count_str += 1
    elif str_a[i] == " ":
        count_space += 1
    else:
        count_other += 1
print(f"所输入的字符串英文字母、数字、空格、其他字符的个数分别为"
      f"{count_str}{count_number}{count_space}{count_other}")

# 分隔符
print("-"*50)

# 才鸟教程里直接用的库函数，一步到位
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print(f"所输入的字符串英文字母、数字、空格、其他字符的个数分别为"
      f"{letters}{digit}{space}{others}")
