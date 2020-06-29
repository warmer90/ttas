"""
使用传参的方式传入hp和血量
第二个角色，叫后裔，后裔继承了角色的hp和power。并且多了护甲属性
重新定义一个defense方法：
final_hp=hp+defense-enemy_power
enemy_final_hp= enemy_hp-power
对比血量。多的胜利
"""
from 面向对象.game1.game import Game


class HouYi(Game):
    def __init__(self):
        super().__init__()
        self.defense=100

    def defense1(self,enemy_hp ,enemy_power):

        #while True:
            self.hp = self.hp +self.defense- enemy_power
            enemy_hp = enemy_hp - self.power
            print("我的血量:", self.hp)
            print("敌人血量:", enemy_hp)
            if self.hp >enemy_hp:
                print("我赢了")
               # break
            elif enemy_hp<self.hp:
                print("敌人输了")
             #   break
            else:
                raise Exception("No peace,keep fighting")


houyi=HouYi()
houyi.defense1(1000,300)