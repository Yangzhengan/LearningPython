# @Author : Yzg
# @File   : 20_Python实例.py
# @Time   : 2024/9/21 20:59
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
length = 100
times = 10
sum1 = 0
for i in range(1, times + 1):
    if i == 1:
        sum1 += 100
    else:
        sum1 += length * 2
    length = length / 2
print(f"第十次落地时候共经过：{sum1}米，第十次反弹{length}")
