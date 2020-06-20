# 计算一个字符串中元音字母的数量

# def vowels_count(str):
#     count = 0
#     for s in str:
#         if s in "aeiouAEIOU":
#             count += 1

#     print(count)
# vowels_count("williamslife")

#将txt文本中的所有人名都转化为手写字母大写，其余字母小写的功能

# file_content = open("/Users/williamslife/Desktop/python_practice/python_new/names.txt", "r")
# for file_line in file_content:
#     file_line = file_line.strip()
#     print(file_line.title())




# 判断一个字符串是不是一个回文字符串
# file_contents = open("/Users/williamslife/Desktop/python_practice/python_new/names.txt", "r")

#循环版本
def is_palindrome(name):
    low = 0
    high = len(name) - 1
    if len(name) <= 1:
        return True
    else:
        while low < high:
            if name[low] != name[high]:
                return False
            low += 1
            high -= 1
        return True

#递归版本
def is_palindrome_rec(name):
    if len(name) <= 1:
        return True
    if name[0] == name[-1]:
        return is_palindrome_rec(name[1:-1])
    else:
        return False

#循环版本 以下方法不能实现！！！错误的方法🙅🙅
# def is_palindrome_v3(name):
#     start = 0
#     end = len(name) - 1
#     for i in range(start, start + 1):
#         for j in range(end, end - 1, -1):
#             if name[i] != name[j]:
#                 return False
#             else:
#                 if (start + 1 <= len(name) / 2) and (end - 1 >= len(name) / 2):
#                     start += 1
#                     end -= 1
#                     continue
#                 else:
#                     return True





print(is_palindrome("bob"))
print(is_palindrome_rec("bob"))
print(is_palindrome_v3("bob"))