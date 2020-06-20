#coding = utf-8
#1⃣️.使用sort方法对列表进行永久性的排序
cars = ["malibu XL", "bmw x5", "toyota royal"]
#cars.sort()
#print(cars)

#2⃣️.使用sorted函数对列表进行临时排序
# cars = ['malibu XL', 'audi', 'bmw', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)
# print("Here is the sorted list:")
# print(sorted(cars))
# print("Here is the original list again:")
# print(cars)
# print("that's told us that function sorted can not change the sort of the list")
# #按照与字母顺序相反的顺序排列列表
# print(sorted(cars,reverse = True))

#3⃣️.方法reverse() 倒着打印列表  反转列表元素的排列顺序，该方法永久性的改变了列表元素的排列顺序
cars = ['maribu XL', 'ferrari', 'camaro']
cars.reverse()
print(cars)


#---------------------------------确定列表的长度-------------------------------
#1⃣️。函数len() 来获取列表的长度
cars = ['malibu XL', 'audi', 'kia', 'hyndai']
length = len(cars)
print(length)
