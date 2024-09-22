# @Author : Yzg
# @File   : 18_Python实例.py
# @Time   : 2024/9/21 20:34
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

from functools import reduce
import math

number1 = int(input("请输入多少个数字相加："))
number2 = int(input("请输入你想要的数字(1-9):"))
sum1 = 0
# 双嵌套即可完成，外层循环控制几个加数
for j in range(0, number1):
    # 内层控制加数大小，number1-j通过不断减少循环次数来减小数字大小
    for i in range(0, number1 - j):
        sum1 += (10 ** i) * number2

print(sum1)

# 菜鸟上的方法用的是reduce函数，反而更麻烦
# 把每次的加数放进一个列表，最后进行累加
Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

# 我查看了reduce函数的用法,并且此处用匿名函数一次性使用
# 对列表Sn进行累加
Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)
