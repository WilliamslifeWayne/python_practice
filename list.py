#coding = utf-8
#----------------------添加----------------
#1⃣️.append在列表末尾追加元素
motocycle = ['Honda', 'Ducati', 'Yamaha']
motocycle.append("Suzuki")
#print(motocycle)

#2⃣️.insert 在列表的指定位置插入新的值
motocycle.insert(0, "jialing")
#print(motocycle)

#----------------------删除---------------
#1⃣️.del删除  在列表中删除指定的元素
del motocycle[0]
#print(motocycle)

#2⃣️.pop删除  在列表中删除最后的一个元素并返回他的值   或者   在pop中添加元素的索引
motocycle.append("bullshit")
#print(motocycle)
motocycle.append("nothing")
motocycle.pop()
#print(motocycle)
motocycle.pop(4)
print(motocycle)

#3⃣️.remove删除 已知一个列表中元素的值的情况下，可以使用remove删除指定的元素
motocycle.insert(15, "Xuefulan")
print(motocycle)
motocycle.remove("Xuefulan")
print(motocycle)
