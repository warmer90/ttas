"""
一个回合制游戏，每个角色都有hp (血量) 和power(攻击力) hp初始值1000,power 初始值200
定义一个fight方法
final_hp= hp-enemy_power
enemy_final_hp= enemy_hp-power
对比血量。多的胜利
"""
class Game:
    def __init__(self):
        self.hp = 1000
        self.power =200
    def fight(self,enemy_hp ,enemy_power):
        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if final_hp>enemy_final_hp:
            print("我赢了")
        else:
            print("敌人赢了")

# game=Game()
# game.fight(1000,150)

"""
使用传参的方式传入hp和血量
第二个角色，叫后裔，后裔继承了角色的hp和power。并且多了护甲属性
重新定义一个defense方法：
final_hp=hp+defense-enemy_power
enemy_final_hp= enemy_hp-power
对比血量。多的胜利
"""
class HouYi(Game):
    def __init__(self):
        super().__init__()
        self.defense=100

    def defense1(self,enemy_hp ,enemy_power):

        while True:
            self.hp = self.hp +self.defense- enemy_power
            enemy_hp = enemy_hp - self.power
            print("我的血量:", self.hp)
            print("敌人血量:", enemy_hp)
            if self.hp <= 0:
                print("我输了")
                break
            elif enemy_hp<=0:
                print("敌人输了")
                break

houyi=HouYi()
houyi.defense1(1000,300)