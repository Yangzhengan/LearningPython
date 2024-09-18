# @Author : Yzg
# @File   : 04_Python实例.py
# @Time   : 2024/9/18 10:31

# 输入某年某月某日，判断这一天是这一年的第几天？
# 思路分析：
# 1.先用input函数接受用户所输入的年份月份天数
# 2.闰年2月29天，平年2月28天

# year = int(input("请输入年份："))
# month = int(input("请输入月份(月份大于等于1)："))
# day = int(input("请输入天数(天数大于等于1)："))
# total_day = 0
#
# if year % 4 == 0 or year % 400 == 0:
#     if month >= 2:
#         total_day +=
#     else:
#         total_day = day
# 做不下去
# 参考菜鸟教程上的，用了数据容器元组来记录每年的天数
year = int(input("请输入年份："))
month = int(input("请输入月份(月份大于等于1)："))
day = int(input("请输入天数(天数大于等于1)："))
sum_day = 0
# 元组列表都是可以的，主要为了把数据取出来用
months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
if 0 < month <= 12:
    # 根据索引值找对应天数
    sum_day = months[month - 1]
else:
    print("数据错误，请重新输入月份")
leap = 0
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    leap = 1
    if leap == 1 and month > 2:
        sum_day += 1
total_day = sum_day + day
print(f"这是第{year}的第{total_day}天")
