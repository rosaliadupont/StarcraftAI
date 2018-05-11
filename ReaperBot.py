# heavy influences from: https://github.com/skjb/pysc2-tutorial/blob/master/Building%20a%20Smart%20Agent/smart_agent_step5.py

from our_class_files import vOneZergling

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

import time

# Variable assignments blah blah blah

class ReaperManager(pos, health):
  def __init__(self):
    # GOALS SHOULD BE INITIALIZED HERE AS "self.goal1 = True, etc"
    # INFORMATION SHOULD ALSO BE INITIALIZED, EG: "self.enemyPos = [0,0]"
    
  # returns false if no actions are taken this step
  def doStuff():
    if goal1:
      actionToTake = vOneZergling(self.pos, self.health, self.enemyPos, self.enemyHealth)
    elif goal2:
      pass # etc etc
      
    return actionToTake

class StrategyManager(base_agent.BaseAgent):
  def __init__(self):
    super(ReaperBot, self).__init__()
    
    # SET UP STUFF HERE, FOR EXAMPLE:
    '''
    self.qlearn = QLearningTable(actions=list(range(len(smart_actions))))
    
    self.previous_killed_unit_score = 0
    self.previous_killed_building_score = 0
    
    self.previous_action = None
    self.previous_state = None
    '''
    
    # ALSO INITIALIZE ReaperManager INSTANCES 
    reaperList = [ReaperBot() for i in range(numBots)]
 
  
  # WE MIGHT NEED A TRANSFORM LOCATION FUNCTION?
  '''
  def transformLocation(self, x, x_distance, y, y_distance):
    if not self.base_top_left:
      return [x - x_distance, y - y_distance]
    
    return [x + x_distance, y + y_distance]
  '''
  
  def step(self, obs):
    super(ReaperBot, self).step(obs)
    
    # TAKE OBSERVATIONS FROM obs, LIKE THIS EXAMPLE:
    '''
    supply_limit = obs.observation['player'][4]
    army_supply = obs.observation['player'][5]
    '''
    
    # UPDATE PRIORITY MAP FOR EACH REAPER BASED ON OBSERVATIONS
    
    # LOOP THROUGH REAPER LIST, BREAK WHEN ACTION IS EXECUTED
    for reaper in reaperList:
      action = reaper.doStuff
      
      if action == no_op:
        continue
        
      else:
        reaper.didStuffThisLoop = True # must keep track of whether reapers did stuff
          # so that when we go through this loop again we don't stop for reapers that 
          # already did stuff this go around. This is necessary because the API requires
          # a "step" function which returns a single action
        return action
      
    
    
    
    
    
    
    
    
