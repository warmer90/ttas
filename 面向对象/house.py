class Drawing:
    area =100
    style = "North"
    __style2 = "china style"

    def sleep(self):
        print(self.__style2)
        print("房子可以用来睡觉")
    def cook(self):
        print("房子可以用来做饭")

    def __sleep_bathroom(self):
        print("我在厕所")
        self.sleep()

my_house= Drawing()
my_house.sleep()

my_house._Drawing__sleep_bathroom()




# tom_house =Drawing()
# tom_house.sleep()




