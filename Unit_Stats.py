#Rename to UnitStats.py for consistency
#Internal Functions - see Kiting-RTS-Influence-Maps.pdf for definitions of these Functions
#Dmax
#canKite
#order of stats: speed, acceleration, deceleration, turn, windUp, windDown, attackRange, HP, DPS,
import math

class UnitStats:
    reaper = {'speed' : 3.75, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 1.1, 'windDown' : .75, 'attackRange' : 5, 'HP' : 60, 'DPS' : 7.27, 'radius' : 0.375}
    enemyStats = {'zergling' : zergling}
    zergling = {'speed' : 2.95, 'creepSpeed' : 3.84, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 0.696, 'windDown' : .5, 'attackRange' : 0.1, 'HP' : 35, 'DPS' : 7.14, 'radius' : 0.375}

def kitingTime():

    return reaper['windUp'] + (1/reaper['acceleration']) + (2 * math.pi * reaper['radius'] * (1/reaper['turnRate']))

def canKite(target):

    reaperFaster = reaper['speed'] > enemyStats[target]['speed']
    reaperOutrange = reaper['attackRange'] > enemyStats[target]['attackRange'] + (enemyStats[target][speed] * kitingTime())

def dMax(target)
