import sc2
from .unit_stats import UnitStats
from .influenceMap import InfluenceMap
from .enemy import Enemy

#Weights 3 > 1 > 2
W1 = 0.75
W2 = 0.5
W3 = 1

class ReaperAgent(sc2.BotAI):
    enemy_array = []

    def on_start(self):
        #creates enemy array and unitstats and influence map
        #super function class super class init
        self.unit_stats = UnitStats()
        self.i_map = InfluenceMap(self.game_info.map_size)

    async def on_step(self, iteration):
        for reaper in self.state.units(REAPER).idle:
            self.update_obs()
            target = self.select_target(reaper) #target is unit object from sc2

            if self.unit_stats.can_kite(target):
                self.kiting_attack(target, reaper)
            else:

                #what do we do in the else case?
                #if low health,run
                #else attack
                #check if you can kill them faster than they can
                #cant run, fight until death
                #search for enemies

    def update_obs(self):
        #fills enemy array
        #calls d_max
        #calls update map
        self.enemy_array = []
        for unit in self.known_enemy_units.not_structure:
             self.enemy_array.append(Enemy(unit.positon, unit.name, self.unit_stats.d_max(unit.name)))

        self.i_map.update_map(self.enemy_array, self.unit_stats)

    def select_target(self, reaper):
        #returns position of most desirable enemy
        max_score = 0

        for unit in self.known_enemy_units.not_structure: # what is self.known_enemy_units.not_structure?
            d = Distance3D(unit, reaper) #FIXME: where does Distance3D come from?
            t = self.unit_stats.enemyStats[unit.name]['tactical_threat']
            a = self.unit_stats.Reaper['DPS'] / (reaper.health / self.unit_stats.enemyStats[unit.name]['DPS'])

            targeting_score = (a * W1) + (t * W2) + (d * W3)

            if targeting_score > max_score:
                max_score = targeting_score
                target = unit
            else:
                continue

        return target

    def kiting_attack(self, target, reaper):
        position = InfluenceMap.get_secure_pos(reaper.positon)
        if position == reaper.position:
            await self.do(reaper.attack(target.position))
        else:
            await self.do(reaper.move(position))
