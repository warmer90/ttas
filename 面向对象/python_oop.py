class Turtle:
    #类变量，静态变量
    legs =4
    mouth = 1
    eye = 2
    #类中的函数，方法
    def bite(self):
        print("乌龟咬人")
    def climb(self):
        print("爬走")

#直接调用类属性
print(Turtle.eye)
Turtle.bite

#类的实例化
Turtle()
turtle = Turtle()
#调用实例对象中的属性
turtle.bite()
print(turtle.eye)


