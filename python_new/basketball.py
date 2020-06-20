# 习题 篮球比赛领先多少才算安全
"""
体育作家Bill James发明了一种算法用以判断当前领先的分数是否安全
算法描述：
1.获取领先的分数
2.减去三分
3.如果目前是领先队控球，则加0.5；否则减去0.5（数字小于0则变为0）
4.计算平方后的结果
5.如果得到的结果比当前比赛剩余时间的秒数大，则领先是“安全”的
"""
points = int(input("请输入领先的分数:"))
has_ball = input("请输入现在是否是领先队控球(y/n)?")
seconds = int(input("请输入当前的剩余的秒数："))

points -= 3
if has_ball == "y":
    points += 0.5
else:
    points -= 0.5
if points < 0:
    points = 0
if points ** 2 > seconds:
    print("It's safe")
else:
    print("It's not safe!")