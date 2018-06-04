
#Internal Functions - see Kiting-RTS-Influence-Maps.pdf for definitions of these Functions
#dMax
#canKite
#order of stats: speed, acceleration, deceleration, turn, windUp, windDown, attackRange, HP, DPS,
import math
from sc2.unit import Unit

class UnitStats:
    Reaper = {
            'speed' : 3.75,
            'acceleration' : 1000,
            'deceleration' : 0,
            'turnRate' : 999.8437,
            'windUp' : 1.1,
            'windDown' : .75,
            'attackRange' : 5,
            'HP' : 60,
            'DPS' : 7.27
        }
    Zergling = {
            'speed' : 1.5,
            'creepSpeed' : 3.84,
            'acceleration' : 1000,
            'deceleration' : 0,
            'turnRate' : 999.8437,
            'windUp' : 0.696,
            'windDown' : .5,
            'attackRange' : 0.1,
            'HP' : 35,
            'DPS' : 7.14,
            'tactical_threat' : 1
        }
    units = {'Reaper' : Reaper, 'Zergling' : Zergling}

    def kiting_time(self, unit = "Reaper"):
        # Takes a unit name string and returns a decimal number
        # Returns the time required to turn, attack, turn back,
        # and accelerate to full speed again (one complete "kite" rotation)

        return self.units[unit]['windUp'] +             \
               (1/self.units[unit]['acceleration']) +   \
               (2 * math.pi  * (1/self.units[unit]['turnRate']))
 
    def d_max(self, target, unit = "Reaper", k = 1):
        # Takes a unit name string and returns a decimal number
        # Returns the minimum distance required to perform one
        # complete "kite" rotation without taking damage

        return self.units[target]['attackRange'] +                              \
               (self.units[target]['speed'] * self.kiting_time(unit = unit)) +  \
               k

    def can_kite(self, target, unit = "Reaper"):
        # Takes a unit name string and returns a boolean
        # Determines whether or not it is possible for unit to
        # perfectly kite target

        is_faster = self.units[unit]['speed'] > self.units[target]['speed']

        # can_outrange represents whether or not we can get a shot off
        # before the enemy can close the distance between us
        can_outrange = self.units[unit]['attackRange'] > self.d_max(target, unit = unit, k = 0)

        return is_faster and can_outrange