#coding = utf-8
#3-8 practice 想出至少五个你渴望去旅游的地方
travel = ["Japan", 'America', 'Egypt', 'the united kingdom']
print(travel)

#按字母顺序打印这个列表，同时不需要修改这个列表
print(sorted(travel))

#再次打印该列表 核实排序没变
print(travel)

#shiyong sorted()按与字母相反的顺序打印这个列表，同时不要修改这个列表
print(sorted(travel, reverse = True))
print(travel)

#使用 方法reverse() 修改列表元素的排列顺序。
travel.reverse()
print(travel)
travel.reverse()
print(travel)

#shiyong 方法sort()修改该列表
travel.sort()
print(travel)
travel.sort(reverse = True)
print(travel)

print("There are ", len(travel), "areas I wanna visit.")
