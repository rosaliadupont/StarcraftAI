import sc2
from .unit_stats import UnitStats
from .influenceMap import InfluenceMap

#Weights 3 > 1 > 2
W1 = 0.75
W2 = 0.5
W3 = 1

class ReaperAgent(sc2.BotAI):
    enemy_array = []
    reaper_array = []

    def __init__(self):
        #creates enemy array and unitstats and influence map
        #super function class super class init
        self.unit_stats = UnitStats()
        self.i_map = InfluenceMap(self.game_info.map_size)

    async def on_step(self, iteration):

        update_obs()
        target_obj = enemy_array[select_target(0 '''reaper_index''')]
        target_name = 'Zergling' # FIXME: should use target_obj.type_id to refer to name string; eg: 84 --> 'Probe'

        if UnitStats.can_kite(target_name): #method in unittype class
            action = kiting_attack(target_obj)
            #we eventually want to do unit.action(), it might be more appropiate to do this in the kiting_attack method though
        else:
            #what do we do in the else case?
            #if low health,run
            #else attack
            #check if you can kill them faster than they can
            #cant run, fight until death
            #search for enemies

    def update_obs():
        #fills enemy array
        #calls dmax
        #calls update map
        enemy_array = []
        for unit in self.state.units.enemy.not_structure:
            if unit.is_visible:
                enemy_array.append([unit.positon, self.unit_stats.d_max(unit.type_id)]) # FIXME: unit.type_id is not a string, it's an int (I think)

        self.i_map.update_map(enemy_array, self.unit_stats)

    def select_target(reaper_index):
        #looks at units in enemy_array[], and returns the index of the appropriate one to attack
        #TODO: convert to using sc2 data
        max_score = 0
        select_index = -1

        for i, unit in enumerate(enemy_array):
            r = reaper_index
            d = Distance3D(unit, reaper_array[r]) # FIXME: must import Distance3D from somewhere
            t = self.unit_stats.enemyStats[unit.type][tactical_threat]
            a = self.unit_stats[Reaper][DPS] / (reaper_array[r].health / self.unit_stats.enemyStats[unit.type][DPS])

            targeting_score = （a * W1） + （t * W2） + （d * W3）

            if targeting_score > max_score:
                max_score = targeting_score
                select_index = i
        
        if select_index == -1
            print (f"Error: select_index is -1")
            
        return select_index

    def kiting_attack(target_obj):
        position = InfluenceMap.get_secure_pos(actual_pos)
        if position == actual_pos:
            await self.do(reaper_array[0].attack(target_obj))
        else:
            await self.do(reaper_array[0].move(positon))
