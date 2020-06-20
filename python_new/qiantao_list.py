#嵌套列表
students = [["zhang", 84], ["wang", 96], ["li", 72]]
# 计算上述学生的分数平均数
sum = 0
for studnet in students:
    sum += studnet[1]
avg = sum / len(students)
print(avg)

# 列表解析的方法 下面的报错，但是我没看出来是哪儿错了
# avg1 = sum([part[1] for part in students]) / len(students)
# print(avg1)