#例题：
"""
考拉兹猜想（Collatz Conjecture），也叫奇偶归一猜想、3n + 1猜想、冰雹猜想、角骨猜想、哈塞猜想、乌拉姆猜想、叙拉古猜想
算法介绍：
1.对于每一个正整数，如果他是奇数，就对他乘以3，再加1，如果是偶数则对他除以2，最终都能得到1.
"""
# def collatz_conjecture(number):
#     while number != 1:
#         if number % 2 == 0:
#             # 偶数
#             number /= 2
#             print(number)
#         elif number % 2 == 1:
#             # 奇数
#             number = number * 3 + 1
#             print(number)

# collatz_conjecture(6)



# 习题2: 打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{} x {} = {:<2d}".format(i, j, i * j), end='    ')
#         print(f"{i} x {j} = {i * j}", end='')
#         print("{0}x{1}={2:0>2}".format(i,j,i*j),end="\t")
#     print()


# 99乘法表的别的三角形写法
# for i in range(1,10):
#     j = 1
#     while j <= i:
#         print("{}x{}={:2d}".format(j, i, i*j), end="     ")
#         j +=1
#     print()



# 习题3：鸡兔同笼问题：鸡兔同笼是古代我们数学名题之一，大约在1500年前，《孙子算经》中记载：今有雉兔同笼，上有三十五头，下有九十四足，雉兔各几何？

#鸡兔共35只，用穷举法
# for rabbit in range(0, 35):
#     for chicken in range(0, 35):
#         if (rabbit + chicken) == 35 and (rabbit * 4 + chicken * 2 == 94):
#             print(f"鸡有{chicken}只，兔子有{rabbit}只")


#以下是个死循环
# while True:
#     for x in range(6):
#         y = 2 * x + 1
#         print(y)
#         if y > 9:
#             break


# import math
# # 二分法求平方根
# def square_root(num):
#     low = 0
#     high = num
#     guess = (high + low ) / 2
#     while abs(guess ** 2 - num) > 1e-6:
#         if guess ** 2 > num:
#             high = guess
#         else:
#             low = guess
#         guess = (low + high) / 2
#     print(guess)

# square_root(3) 



# 习题4: 从1开始，数 50 个素数
# count = 0
# num   = 2
# while count <= 50:
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end="  ")
#         count += 1
#     num += 1





# 习题5：判断一个数字是不是回文数 例如 13431就是个回文数
# def is_repeat_num(num):
#     if num / 10 < 1:
#         # 说明是个 个位数
#         print("{}是一个回文数".format(num))
#     elif num / 100 < 1:
#         # 说明是个两位数
#         shi = num // 10
#         ge  = num % 10
#         if shi == ge:
#             print(f"{num}是一个回文数")
#     elif num / 1000 < 1:
#         # 说明是个 三位数
#         bai = num // 100
#         shi = num // 10 % 10
#         ge  = num % 10
#         print(bai)
#         print(shi)
#         print(ge)
#         if bai == ge:
#             print("{0}是个回文三位数".format(num))
#         else:
#             print("{0}不是个回文三位数".format(num))


# is_repeat_num(886)

# 习题五 视频解法
# def judge_repeat_num(num):
#     num_t = num
#     num_p = 0
#     while num != 0:
#         print(f"{num_p} num_p")
#         print(f"{num_t} num_t")
#         print(f"{num} num")
#         num_p = num_p * 10 + num % 10
#         num = num // 10
        
#     if num_t == num_p:
#         print(f"{num_t}是一个回文数")
#     else:
#         print("{}不是一个回文数".format(num_t))

# judge_repeat_num(888)