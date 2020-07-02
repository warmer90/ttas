import yaml

"""
游戏角色有hp,power,skill  属性，配置在yaml文件
每三个回合可触发一次技能，血量先死的输
"""


class Game:
    def __init__(self):
        infor = yaml.safe_load(open("./game.yaml"))
        default = infor["default"]
        self.first = default[0]
        self.second = default[1]
        print(infor)
        # 第1个人物
        self.first_hp = infor[self.first]["hp"]
        self.first_power = infor[self.first]["power"]
        self.first_skill = infor[self.first]["skill"]
        # 第2个人物
        self.second_hp = infor[self.second]["hp"]
        self.second_power = infor[self.second]["power"]
        self.second_skill = infor[self.second]["skill"]

    def fight(self):
        round = 0
        while True:
            round += 1
            if round % 3 == 0:
                self.first_hp = self.first_hp - self.second_power * self.second_skill
                self.second_hp = self.second_hp - self.first_power * self.first_skill
            else:
                self.first_hp = self.first_hp - self.second_power
                self.second_hp = self.second_hp - self.first_power
            print(self.first,self.first_hp)
            print(self.second,self.second_hp)
            if self.first_hp <= 0:
                print("{} 输了".format(self.first))
                break
            elif self.second_hp <= 0:
                print("{} 输了".format(self.second))
                break


if __name__ == '__main__':
    game = Game()
    game.fight()
