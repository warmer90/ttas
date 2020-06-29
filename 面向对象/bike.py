"""
一个自行车类（Bicycle），run（骑行），调用显示骑行里程km（骑行里程传入的数字）
写一个EBicycle 继承 Bicycle，添加电量valume 属性通过参数传入，有两个方法
  1. fill_charge(vol)，用来充电。vol 为电量
  2. run（km） 方法骑行，   10km消耗一度电，电量耗尽调用Bicycle的run方法骑行

"""
class Bicycle:
    # 定义一个run方法，需要传入km参数
    def run(self,km):
        print(f"自行车骑行的里程数:{km}")

class EBicycle(Bicycle):
    #初始化
    def __init__(self,volume):
        #实例变量
        self.valume = volume

    def get_valume(self):
        print("当前电量:",self.valume)

    def fill_charge(self,vol):
        print("充电电量",vol)

    def run(self,km):
        #电量支持的最大里程数
        e_miles = self.valume*10
        ## 假如电瓶有10度电，我们支持的里程  10*10=100

        miles = km - e_miles
        if miles<=0:
            print("电瓶车骑了：",km)
        else:
            #因为子类中有个run，把父类的run覆盖掉了
            #self.run
            #应该传入参数是除了电瓶车之外的里程数
            print("电瓶车骑了",e_miles)
            super().run(miles)



# bicycle= Bicycle()
# bicycle.run(100)

#类在初始化时候，给init中定义的参数传参

# bike = EBicycle(100)
# bike.get_valume()

bike = EBicycle(16)
bike.run(250)








