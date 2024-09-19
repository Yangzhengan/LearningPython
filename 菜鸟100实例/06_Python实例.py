# @Author : Yzg
# @File   : 06_Python实例.py
# @Time   : 2024/9/19 15:41

# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，
# 指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# 递归调用
number = fibonacci(int(input("请输入斐波那契数列对应的位数：")))
print(number)


# 需要把斐波那契数列输出出来的代码
def fibonacci1(n1):
    if n1 == 1:
        return [1]
    if n1 == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n1):
        fibs.append(fibs[-1] + fibs[-2])
    # 此处缩进要看清楚，如果放在for里面就会直接return，
    # 整个函数终止，实际要等循环完加完元素再return
    return fibs


print(fibonacci1(int(input("请输入你想要的位数："))))
