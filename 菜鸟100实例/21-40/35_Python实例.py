# @Author : Yzg
# @File   : 35_Python实例.py
# @Time   : 2024/9/27 16:06
# 文本颜色设置
class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(Bcolors.WARNING + "警告的颜色字体?" + Bcolors.ENDC)
