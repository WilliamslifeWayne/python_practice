#codig = utf-8
magicians = ['alice', 'williams', 'david', 'sophia']
# for magician in magicians:
#     print(magician)
for magician in magicians:
    print(magician.upper() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
print("Thank you, everyone.that was a great magic show!")

#测试for循环不带冒号将会发生什么错误，提示语法错误，程序不能正常运行
cars = ['maribu XL', 'toyota corolla', 'honda accord']
for car in cars:
    print(car)
