#习题1 求解一元二次方程 ax**2 + bx + c = 0
#他的解是 2a分之负b加减根号下b方减4ac
import math
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
if a != 0: 
    # 0不能做分母
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("无实根")
    elif delta == 0:
        print(f"有一个实根，X的解为：{-(b/2 * a)}")
    else:
        root = math.sqrt(b ** 2 - 4 * a * c)
        solution1 = (-b + root) / (2 * a)
        solution2 = (-b - root) / (2 * a)
        print("有两个实根，分别是{0},  {1}".format(solution1, solution2))

