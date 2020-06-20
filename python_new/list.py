# 列表和元祖的概念
#例 一：读取10个数，并计算他们的平均数
'''
计算nums个数的平均数，并返回
'''
def get_avg(nums):
    sums = 0
    for i in range(0, nums):
        sums += int(input("请输入一个数"))
    return sums / nums
# print(get_avg(10))


# a = [1,2,3,4]
# b = a
# b[1] = 2890
# print(a[1])


# c = [1,2,3,4]
# d = c[:]
# d[1] = 213
# print(c[1])


# def exchange(lst, a, b):
#     tmp = lst[a]
#     lst[a] = lst[b]
#     lst[b] = tmp
# a = [1,2,3]
# exchange(a, 1, 2)
# print(a)


'''
二分法查找value
前提条件是：lst是个有序列表
时间复杂度是 O(logN)
'''
def bi_search(lst, x):
    begin = 0
    end = len(lst) - 1
    while begin <= end:
        mid = int((end + begin) / 2)
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            begin = mid + 1
        elif lst[mid] > x:
            end = mid - 1
    return -1

# print(bi_search([6, 8, 16, 27, 36], 16))


'''
选择排序法

'''
def select_sort(lst):
    # 循环列表的长度
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                # 互换两者的位置
                lst.insert(i, lst.pop(j))
    return lst

# print(select_sort([2, 10, 1, 23, 78, 15]))


def exchanged(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp
# 选择排序发版本二2⃣️
def select_sort_v2(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                exchanged(lst, i, j)
    return lst

# print(select_sort_v2([3, 56, 23, 76, 47, 1]))




# 冒泡排序算法
'''
以下的是冒泡排序算法，其中sort_way 有两个值：asc => 升序        desc => 降序[默认]
'''
def bubble_sort(lst, sort_way="desc"):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sort_way == "desc":
                #降序 就要判断后一个数是不是比前一个数大
                if lst[j] > lst[i]:
                    exchanged(lst, i, j)
            else:
                if lst[j] < lst[i]:
                    exchanged(lst, i, j)
    return lst


# 以下内容无法正确执行，虽然和老师写的一摸一样，暂时不以此为参考价值
def bubble_sort_v2(lst):
    is_exchanged = True
    top = len(lst) - 1
    while is_exchanged:
        is_exchanged = False
        for i in range(top):
            if lst[i] < lst[i + 1]:
                exchanged(lst, i, i + 1)
                is_exchanged = True
        top -= 1

# print(bubble_sort_([1,34,54,36,27,82,432,263], "asc"))
print(bubble_sort_v2([1,34,54,36,27,82,432,263]))