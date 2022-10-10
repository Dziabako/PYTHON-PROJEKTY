import random

class Beasts:
    LOOT = ['club', 'rusty dagger', 'rusty sword', 'sword', 'sharpened sword']
    ENEMY_LIST = ['Rat', 'Boar', 'Squirrel', 'WIld Dog', 'Wolf', 'Bear', 'Deer']

    def loot_quality(self, p_lvl):
        stat = {}
        for i in range(len(self.LOOT)):
            stat[self.LOOT[i]] = 5 * p_lvl
        return stat

    #def enemy_stat(self, p_lvl):
        


