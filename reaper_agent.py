from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

#unit ids
_REAPER = 49

class ReaperAgent(base_agent.BaseAgent):
    enemy_array = []
    reaper_array = []
    unit_stats
    i_map
    control_not_set = True
    not_centered = True

    def __init__(self):
        #creates enemy array and unitstats and influence map
        #super function class super class init
        unit_stats = UnitStats()
        i_map = InfluenceMap()

    def step(self, obs):
        if control_not_set:
            action = set_control_groups(obs)
            control_not_set = False

        elif not_centered:
            action = select_n_center()
            not_centered = False #TODO: check to see if still centered
        else:
            #main loop
            update_obs() #assumes screen is already in position
            target = select_target()

            if can_kite(target): #method in unittype class
                action = kiting_attack(target)
            else:
                #what do we do in the else case?
                #if low health,run
                #else attack
                #check if you can kill them faster than they can
                #cant run, fight until death
                #search for enemies

        return action

    def set_control_groups(obs):

    def update_obs():
        #fills enemy array
        #calls dmax
        #calls update map
        for unit = obs.observation.feature_units:
            if unit.alliance == _HOSTILE_ALLIANCE:
                #store relevent data in Enemy class
                new_enemy = Enemy(unit.health, [unit.x, unit.y], unit.unit_type, unit_stats.d_max(unit.unit_type))
                enemy_array.append(new_enemy)
            elif unit.type == _REAPER:
                #update reaper in reaper array. We only have one reaper rn
                reaper_array[0].update(unit.health, [unit.x, unit.y], unit.is_selected)

        i_map.update_map(enemy_array)

    def select_target():
        #created by thomas
        #looks at enemy array and returns index of selected unit

    def kiting_attack(target):
        position = get_secure_pos(actual_pos)
        if position == actual_pos:
            return attack(target)
        else:
            return move(position)

    def attack(target):
        #sets action to be used by api

    def move(position):
        #sets action to be used by api
