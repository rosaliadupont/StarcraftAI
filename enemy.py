
class Unit:
    #cooldown
    #facing
    def __init__(self, health, pos, type):
        self.health = health
        self.position = pos #positon of screen
        self.type = type

class Enemy(Unit):
    def __init__(self, health, pos, type, dmax):
        super(Enemy, self).__init__(health, pos, type)
        self.dmax = dmax

class Reaper(Unit):
    def __init__(self, health, pos, select):
        super(Reaper, self).__init__(health, pos, _REAPER)
        self.is_selected = select

    def update(self, health, pos, select):
        self.heatlh = health
        self.positon = pos
        self.is_selected = select
