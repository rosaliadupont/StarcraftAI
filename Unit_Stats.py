#Rename to UnitStats.py for consistency
#Internal Functions - see Kiting-RTS-Influence-Maps.pdf for definitions of these Functions
#Dmax
#canKite
#order of stats: speed, acceleration, deceleration, turn, windUp, windDown, attackRange, HP, DPS,


class UnitStats:
    reaperStats = {'speed' : 3.75, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 1.1, 'windDown' : .75, 'attackRange' : 5, 'HP' : 60, 'DPS' : 7.27}
    enemyStats = {'zergling' : zergling}
    zergling = {'speed' : 2.95, 'creepSpeed' : 3.84, 'acceleration' : 1000, 'deceleration' : 0, 'turnRate' : 999.8437, 'windUp' : 0.696, 'windDown' : .5, 'attackRange' : 0.1, 'HP' : 35, 'DPS' : 7.14}
