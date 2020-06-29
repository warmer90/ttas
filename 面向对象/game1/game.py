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