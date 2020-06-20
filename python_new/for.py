# 习题1  求常数e的值
# 常数e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/i!

# 方法1:
factorial = 1
plus = 1
for i in range(1, 101):
    factorial *= i
    plus += (1 / factorial)

print(plus)

# 方法2: 使用math模块中的factorial函数
import math
s = 1
for j in range(1, 101):
    s += 1. / math.factorial(j)
print(s)




# 习题2   求圆周率pai的值
# pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... + ((-1) ** (i + 1)) / (2 * i - 1))

sums = 0
for i in range(1, 1000000):
    sums += ((-1) ** (i + 1)) / (2 * i - 1)
sums *=4
print(sums)


# 习题3: 有多少个三位数字能被17整除？
count = 0
for i in range(100, 1000):
    if i % 17 == 0:
        count += 1
print(count)