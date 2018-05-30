import sc2

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
        target = select_target(0)

        if can_kite(target): #method in unittype class
            action = kiting_attack(target)
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
             enemy_array.append([unit.positon, unit_stats.d_max(unit.name)])

        i_map.update_map(enemy_array, unit_stats)

    def select_target(index):
        #looks at enemy array and returns index of selected unit
        #TODO: convert to using sc2 data
        max_score = 0
        select_index

        for index, unit in enumerate(enemy_array):
            d = Distance3D(unit, reaper_array[index])
            t = unit_stats.enemyStats[unit.type][tactical_threat]
            a = unit_stats[Reaper][DPS] / (reaper_array[index].health / unit_stats.enemyStats[unit.type][DPS])

            targeting_score = （a * W1） + （t * W2） + （d * W3）

            if targeting_score > max_score:
                max_score = targeting_score
                select_index = index
            else:
                continue

        return select_index

    def kiting_attack(target):
        position = get_secure_pos(actual_pos)
        if position == actual_pos:
            await self.do(reaper_array[0].attack(target))
        else:
            await self.do(reaper_array[0].move(positon))
