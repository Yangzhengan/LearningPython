# @Author : Yzg
# @File   : 32_Python实例.py
# @Time   : 2024/9/27 16:06
# 按相反的顺序输出列表的值
a = [1, 2, 3]
b = []
# 查了CSDN上的说法b = a[i:j:s]
# s<0时，i省略，默认为-1，j默认为-len(a)-1,步进为-1
for i in a[::-1]:
    b.append(i)
print(b)
