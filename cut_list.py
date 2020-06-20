#coding = utf-8
#切片 这两个数说的都是下标，例：list[a:b] 范围是 list[a] -- list[b-1]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])
#result: ['martina', 'michael']

#1⃣️ 如果你没有指定第一个索引，python将自动从头开始
print(players[:4])
#result: ['charles', 'martina', 'michael', 'florence']

#2⃣️ 没有指定结尾，将从指定位置到结尾
print(players[3:])
#result: ['florence', 'eli']

#3⃣️ 如果你要输出名单上的最后三名队友
print(players[-3:])
#result: ['michael', 'florence', 'eli']
