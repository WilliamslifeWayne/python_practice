#coding = utf-8
#由下面的例子可以得出，range产生的值不包含末尾的那个数字，即range(a, b)将会产生 a,...(b-1)之间的数字
for value in range(1,10):
    print(value)

#通过range生成一个列表
numbers = list(range(1,6))
print(numbers)

#range 可以指定步长
for oushu in range(2, 11, 2):
    print("1到10之间的偶数是：", oushu)

for jishu in range(1, 10, 2):
    print("1到10之间的基数是：", jishu)

#计算1-10的平方值
squares = []
for num in range(1, 11):
    square = num ** 2
    squares.append(square)
print(squares)

#对数字列表进行简单的数字统计
nums = []
for num in range(1, 11):
    nums.append(num)

print(nums)
print("nums列表中最大的数是：", max(nums))
print("nums列表中最小的数是：", min(nums))
print("nums列表中总和是：", sum(nums))


#-----------------------------4.3.4 列表解析-------------------------------
numbers = [value ** 3 for value in range(1,11)]
print(numbers)
