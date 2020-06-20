# file = open("names.txt", "r")
# for line in file:
#     line = line.strip()
#     line = line.lower()
#     print(line)
# file.close()
# 编写一个函数判断一个人名是不是一个回文字符串
f = open("./names.txt", "r");
def is_panlindrom(name):
    low = 0
    high = len(name) - 1
    while low < high:
        if name[low] != name[high]:
            return False
        low += 1
        high -= 1

    return True

#方法2，递归方式实现
def is_panlindrom2(name):
    if len(name) <= 1:
        # 说明是个空字符串
        return True
    else:
        if name[0] != name[-1]:
            return False
        else:
            return is_panlindrom2(name[1:-1])

# print(is_panlindrom("BOBs"))
# print(is_panlindrom2("BOB"))

# 习题 ：判断一个人名是不是全部是升序的字符串。
def is_ascending(name):
    p = name[0]
    for c in name:
        if p > c:
            return False
        p = c
        
    return True

# print(is_ascending("abc"))

# 使用递归函数实现判断一个人名的字母是否为升序排列的函数 is_ascending

def is_ascending_re(name):
    if len(name) < 2:
        return True
    if name[0] > name[1]:
        return False
    else:
        return is_ascending_re(name[1:])

# print(is_ascending_re("wang"))

# 习题 用正则来判断一个人名是不是 【c.a】格式的名字
def test_regular_expression(name):
    import re
    pattern = "(C.A)"
    result = re.search(pattern, name)
    if result:
        print(f"name:{name}符合{pattern}格式")

# test_regular_expression("CBA")