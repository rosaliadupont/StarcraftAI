from pysc2.agents import base_agent
from pysc2.lib import actions

class SimpleAgent(base_agent.BaseAgent):
    def step(self, obs):
        super(SimpleAgent, self).step(obs)


        time.sleep(0.5)

        return actions.FunctionCall(actions.FUNCTIONS.no_op.id, [])
