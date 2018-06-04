import time
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.constants import *
from sc2.player import Bot, Computer
from Unit_Stats import UnitStats
from influenceMap import InfluenceMap
from enemy import Enemy
import sys
import pdb 
import asyncio

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
        #print("Map size:",self.game_info.map_size)
        #print("cell size:",self.game_info.map_size.height / 32, "by",self.game_info.map_size.width / 32)

    async def on_step(self, iteration):
        #if iteration == 1:
            #self.game_info.pathing_grid.save_image("path_map.rgb")
        #await asyncio.sleep(1)
        for reaper in self.state.units(REAPER).idle:
            self.update_obs()
            target = self.select_target(reaper) #target is unit object from sc2
            #pdb.set_trace()
            if target != -1: #we found an enemy  
                if self.unit_stats.can_kite(target.name):
                    #pdb.set_trace()
                    #kiting attack
                    position = self.i_map.get_secure_pos(reaper.position)
                    #print("reaper pos", reaper.position, "moving to", position,"zerging at",target.position)
                    #print("Actual distance:",target.distance_to(position))
                    if position == reaper.position:
                    #if reaper.position.distance_to(target.position) >= self.unit_stats.d_max(target.name):
                        #print("Attacking itr:",iteration)
                        await self.do(reaper.attack(target.position))
                    else:
                        #print("Moving itr:",iteration)
                        await self.do(reaper.move(position))
                else:
                    continue
                    #what do we do in the else case?
                    #if low health,run
                    #else attack
                    #check if you can kill them faster than they can
                    #cant run, fight until death
                    #search for enemies
            else: 
                #print("Searching itr:",iteration)
                await self.do(reaper.move(reaper.position.random_on_distance(5)))

    def update_obs(self):
        #fills enemy array
        #calls d_max
        #calls update map
        self.enemy_array = []
        for unit in self.known_enemy_units.not_structure:
             self.enemy_array.append(Enemy(unit.position, unit.name, self.unit_stats.d_max(unit.name)))
             #print("Zergling dmax",self.unit_stats.d_max(unit.name))

        self.i_map.update_map(self.enemy_array, self.unit_stats)

    def select_target(self, reaper):
        #returns position of most desirable enemy
        max_score = 0
        target = -1 #if theres no enemies will return -1
        for unit in self.known_enemy_units.not_structure:
            d = reaper.distance_to(unit.position)
            t = self.unit_stats.units[unit.name]['tactical_threat']
            a = self.unit_stats.units['Reaper']['DPS'] / (reaper.health / self.unit_stats.units[unit.name]['DPS'])

            targeting_score = (a * W1) + (t * W2) + (d * W3)

            if targeting_score > max_score:
                max_score = targeting_score
                target = unit

        return target

    """async def kiting_attack(self, target, reaper):
        position = InfluenceMap.get_secure_pos(reaper.position)
        if position == reaper.position:
            if reaper.distance_to(target.position) > self.unit_stats.Reaper['attackRange']:
                await self.do(reaper.move(reaper.position.towards(target.position)))
            else:
                await self.do(reaper.attack(target.position))
        else:
            await self.do(reaper.move(position))"""



def main():
    if len(sys.argv) <= 1:
        print("to run: reaper_agent.py \"map name\"")
        sys.exit()
    else:
        map_name = sys.argv[1]
        print("Running with " + map_name)

    sc2.run_game(sc2.maps.get(map_name), [
        Bot(Race.Terran, ReaperAgent()),
        Computer(Race.Zerg, Difficulty.Medium)
    ], realtime=True)

if __name__ == '__main__':
    main()
