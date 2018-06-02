#Internal Functions - see Kiting-RTS-Influence-Maps.pdf for definitions of these Functions
#dMax
#canKite
#order of stats: speed, acceleration, deceleration, turn, windUp, windDown, attackRange, HP, DPS,
import math
from sc2.unit import Unit

class UnitStats:
    Reaper = {'speed' : 3.75, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 1.1, 'windDown' : .75, 'attackRange' : 5, 'HP' : 60, 'DPS' : 7.27}
    Zergling = {'speed' : 2.95, 'creepSpeed' : 3.84, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 0.696, 'windDown' : .5, 'attackRange' : 0.1, 'HP' : 35, 'DPS' : 7.14, 'tactical_threat' : 1,}
    enemyStats = {'Zergling' : Zergling}

    def kiting_time(self):

        return self.Reaper['windUp'] + (1/self.Reaper['acceleration']) + (2 * math.pi  * (1/self.Reaper['turnRate']))


    def can_kite(self, target): # target is a string; eg. 'Zergling'

        reaperFaster = self.Reaper['speed'] > self.enemyStats[target]['speed']
        reaperOutrange = self.Reaper['attackRange'] > self.enemyStats[target]['attackRange'] + (self.enemyStats[target]['speed'] * self.kiting_time())

    def d_max(self, target): # target is a string; eg. 'Zergling'

      k = 1; #confidence constant value, can be adjusted
      return self.enemyStats[target]['attackRange'] + k + (self.enemyStats[target]['speed'] * self.kiting_time())
