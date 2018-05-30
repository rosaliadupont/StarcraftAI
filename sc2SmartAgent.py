import sc2

#unit ids
_REAPER = 49

REAPER_DPS = ##

#Weights 3 > 1 > 2
W1 = 0.75
W2 = 0.5
W3 = 1

class sc2SmartAgent(sc2.BotAI):

    enemy_array = []
    reaper_array = []
    control_not_set = True
    not_centered = True

    def __init__(self):
        #creates enemy array and unitstats and influence map
        #super function class super class init
        unit_stats = UnitStats()
        i_map = InfluenceMap()

    async def on_step(self, iteration):

        if control_not_set:
            action = set_control_groups(obs)
            control_not_set = False

        elif not_centered:
            action = select_n_center()
            not_centered = False #TODO: check to see if still centered
        else:
            target = select_target()

            if can_kite(target): #method in unit-type class
                height = self.game_info.map_size.height
                width = self.game_info.map_size.width

                self.i_map.update_map(self.enemy_array)
                action = kiting_attack(target, actual_position)
                #we eventually want to do unit.action(), it might be more appropiate to do this in the kiting_attack method though
            else:
                #what do we do in the else case?
                #if low health,run
                #else attack
                #check if you can kill them faster than they can
                #cant run, fight until death
                #search for enemies

    def kiting_attack(target, actual_pos):
        position = get_secure_pos(actual_pos)
        if position == actual_pos:
            return attack(target)
        else:
            return move(position)

    def attack(target):
        # sets action to be used by api
