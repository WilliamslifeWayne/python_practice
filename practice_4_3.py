#coding = utf-8
#1⃣️。使用一个for循环打印数字1-20
for num in range(1, 21):
    print(num)

#创建一个数字列表，其中包含数字1-1000000使用 max  min
# numbers = []
# for numb in range(1, 1000000):
#     numbers.append(numb)

# print("numbers的最大值是：", max(numbers))
# print("numbers的最小值是：", min(numbers))
# print("numbers的总和是：", sum(numbers))


#4-6通过给函数range()指定第三个参数来创建一个列表，其中包含1-20的奇数，在使用一个for循环将这些数字都打印出来
jishu_list = []
for jishu in range(1, 20, 2):
    jishu_list.append(jishu)
print(jishu_list)

#4-7 3的倍数  创建一个列表，其中包含3-30中能被整除的数字;再使用for循环将这个列表中的数字都打印出来
chu_3_list = []
for value in range(3, 30):
    if(value % 3 == 0):
        chu_3_list.append(value)
print(chu_3_list)


#4-8 立方 请创建一个列表，其中包含前10个整数的立方，再使用一个for循环将这些立方数都打印出来
lifang = [value ** 3 for value in range(1, 11)]
print(lifang)
