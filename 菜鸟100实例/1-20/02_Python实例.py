# @Author : Yzg
# @File   : 02_Python实例.py
# @Time   : 2024/9/16 12:56

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

# 创建一个变量用于接受用户输入的月利润,再创建一个变量用来记录提成
profit = int(input("请输入当月利润："))
total = 0
# 给利润定档
if profit > 100:
    total += (profit-100)*0.01 + 40*0.015 + 20*0.03 + 20*0.05 + 10 * 0.075 + 10 * 0.1
elif profit > 60:
    total += (profit-60)*0.015 + 20*0.03 + 20*0.05 + 10 * 0.075 + 10 * 0.1
elif profit > 40:
    total += (profit-40)*0.03 + 20*0.05 + 10 * 0.075 + 10 * 0.1
elif profit > 20:
    total += (profit-20)*0.05 + 10 * 0.075 + 10 * 0.1
elif profit > 10:
    total += (profit-10)*0.075 + 10 * 0.1
else:
    total += profit*0.1
print(f"本月奖金为：{total}")

# 参考菜鸟教程上的写法
i = int(input('净利润:'))
# 存储利润档位
arr = [1000000, 600000, 400000, 200000, 100000, 0]
# 存储奖金率档位
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r用于接受奖金数并初始化为0
r = 0
for idx in range(0, 6):
    if i > arr[idx]:
        r += (i - arr[idx]) * rat[idx]
        print((i - arr[idx]) * rat[idx])
        i = arr[idx]
print(r)
# 两种代码都能解决对应问题，但是菜鸟教程会更加灵活，利用列表来遍历各个利润档位
