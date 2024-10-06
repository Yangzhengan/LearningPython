# @Author : Yzg
# @File   : 56_Python实例.py
# @Time   : 2024/10/6 17:51
# 画图，学用circle画圆形。
# GUI编程 编写界面
if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow')
    canvas.pack(expand=YES, fill=BOTH)
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
        k += j
        j += 0.3

    mainloop()
