# print(len("hello world!"))
# 编写一个函数计算给定的字符串中有多少个元音字母（aeiou或AEIOU）
def vowels_count(str):
    vowels_counts = 0;
    for letter in str:
        if letter in "aeiouAEIOU":
            vowels_counts += 1

    return vowels_counts
print(vowels_count("hello world!"))