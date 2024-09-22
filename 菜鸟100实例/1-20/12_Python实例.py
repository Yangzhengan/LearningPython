# @Author : Yzg
# @File   : 12_Python实例.py
# @Time   : 2024/9/19 17:30

# 判断101-200之间有多少个素数，并输出所有素数。
leap = 0
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:  # 刚写完的时候else缩进不对，导致一个素数输出了很多遍，
        # 这里应该是如果if条件走不下去，就把此轮循环执行完后执行else下代码
        leap += 1
        print(f"此素数为{i}")
print(f"共有素数{leap}个")
