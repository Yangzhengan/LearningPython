# @Author : Yzg
# @File   : 03_Python实例.py
# @Time   : 2024/9/16 13:24

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# 完全平方怎么表达？？
# 初步思路：定义一个number、number1、number2分别接收三个数字，再根据完全平方这个式子来表达

# 对照菜鸟教程自己分析：
# 1.列两个表达式
# 2.两者相减，平方差，表达m,n
# 3.判断i，j取值情况

# i是大于等于2的一个数字，又根据两者乘积判断只能到84
for i in range(2, 85):
    # i是属于168的一个因子，且i，j至少一个一定为偶数
    if 168 % i == 0:
        # 算j的值
        j = 168//i
        # 假定i是大于j（方便相减）两者之和，两者之差都为偶数，即两者都是大于等于2且都为偶数
        if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
            m = (i-j)//2
            x = m*m - 100
            print(f"这个整数是{x}")
