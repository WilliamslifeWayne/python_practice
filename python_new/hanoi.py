import random
# 汉诺塔的实现原理
# def hanoi(num, a, b, c):
#     if num == 1:
#         print(f"将第{num}个盘子，从{a}移动到{c}")
#     else:
#         hanoi(num - 1, a, c, b)
#         print(f"将第{num}个盘子，从{a}移动到{c}")
#         hanoi(num - 1, b, a, c)

# hanoi(4, " 左侧 ", " 中间 ", " 右侧 ")



# 路边停车问题
# 长度为10的马路，平均能停多少辆长度为1 的汽车呢？
def parking(road_start,road_end):
    if road_end - road_start < 1:
        return 0
    else:
        start_point = random.uniform(road_start, road_end - 1)
        return parking(road_start, start_point) + 1 + parking(start_point + 1, road_end)
sums = 0
for i in range(10000):
    sums += parking(0,5)
final = sums / 10000
print(final)
# print(parking(0,10))
