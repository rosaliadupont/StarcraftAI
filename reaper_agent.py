'''tick() {
    target = targetSelection();
    if (canKite(target)) {
        kitingAttack(target);
    } else {
        attack(target);
    }
}
kitingAttack(target) {
    position = getSecurePosition(actualPos);
    if (position == actualPos) {
        attack(target);
    } else {
        move (position); //fleemovement
    }
}'''

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

class ReaperAgent(base_agent.BaseAgent):
    def __init__():
        #creates enemy array and unitstats and influence map

    def step(self, obs):
        update_obs()
        target = select_target()

        if can_kite(target): #method in unittype class
            kiting_attack(target)
        else:
            #what do we do in the else case?
            #if low health,run
            #else attack
            #check if you can kill them faster than they can
            #cant run, fight until death

    def update_obs():
        #fills enemy array
        #calls dmax
        #calls update map

    def select_target():
        #created by thomas
        #looks at enemy array and returns index of selected unit

    def kiting_attack(target):
        position = get_secure_pos(actual_pos)
        if position == actual_pos:
            attack(target)
        else:
            move(position)

    def attack(target):
        #sets action to be used by api

    def move(position):
        #sets action to be used by api
