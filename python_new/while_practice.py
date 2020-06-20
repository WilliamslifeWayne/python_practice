"""
while循环的实例
"""
#计算 1+2+3一直加到10的结果
# i = 1
# s = 0
# while i <= 10:
#     s += i
#     i += 1
# print(s)

sum = 0
i = 0
while i < 100:
    if i % 2 == 0:
        sum += i
    i += 2
print(sum)