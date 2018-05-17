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
    def step(self, obs):
        #updates obs 
