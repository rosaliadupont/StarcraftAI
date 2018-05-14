import numpy
from our_class_files import vOneZergling

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

import time

class position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class UnitFeatures:
  def __init__(self, attackRange, speedOffCreep, speedOnCreep, dps):
    self.attackRange = attackRange
    self.speedOffCreep = speedOffCreep
    self.speedOnCreep = speedOnCreep
    self.dps = dps
    
  def dmax(self):
    return 

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the 
# updateMap() giving it the information from the pysc2 api.
  
class InfluenceMap():
  
  def __init__(self):
    
    reaper = {'speed': 5.25,'acceleration' : 1000, 'deceleration': 0, 'attackTime': .79, 'turnTime': 0, 'kitingTime': 0}
    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map
    
    # Here is the feature dictionary that contains the features for each unit
    # The structure of each item in the dictionary is : 'name_of_unit' : UnitFeatures(attackRange, speedOffCreep, speedOnCreep, dps)
    unitFeaturesDict = {} 
    unitFeaturesDict.add('Zergling': UnitFeatures(0.1, 4.13, 6.58, 100), )
    unitFeaturesArray.add('ZerglingSpeedBoost': UnitFeatures(0.1, 5.37, 8.55, 10))     
    unitFeaturesDict.add('Roach': UnitFeatures(, , , ,))
    unitFeaturesDict.add('Baneling': UnitFeatures(, , , ,))
    unitFeaturesArray.add('Queen': UnitFeatures( , , ,))
    unitFeaturesArray.add('Drone': UnitFeatures( , , ,))

    # unitDmaxDict is the dictionary that contains the oncreepdmax and offcreepdmax for each unit
    unitDmaxDict = {}
    for name, unitFeatures in unitFeaturesDict:
      offdmax =  unitFeatures.attackRange + 1 + unitFeatures.speedOffCreep + self[reaper]['kitingTime']
      ondmax =  unitFeatures.attackRange + 1 + unitFeatures.speedOnCreep + self[reaper]['kitingTime']
      unitDmaxArray.append(name: {'offcreepdmax': offdmax, 'oncreepdmax' : ondmax}) 
    
    
      
    #Realtime Enemy Observation
    def updateMap(self, enemyDict):
      # enemyDict is the dictionary containing the information of the enemies in the map
      for name,creepAndLocation in enemyDict:
        # get attack range, speed and dps of each
        if creepAndLocation['creep']:
          dmax = unitDmaxArray[name]['oncreepdmax']
        else:
        	dmax = unitDmaxArray[name]['offcreepdmax']
        
      	reaperOutRuns = false
        #update cell with DPS determined by dMax
