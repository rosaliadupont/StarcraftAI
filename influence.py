import math
from our_class_files import vOneZergling

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

import time

class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class UnitFeatures:
  def __init__(self, attackRange, speedOffCreep, speedOnCreep, dps):
    self.attackRange = attackRange
    self.speedOffCreep = speedOffCreep
    self.speedOnCreep = speedOnCreep
    self.dps = dps
   

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the 
# updateMap() giving it the information from the pysc2 api.
  
class Influence:
  
  def __init__(self):
    
    reaper = {'speed': 5.25,'acceleration' : 1000, 'deceleration': 0, 'attackTime': .79, 'turnTime': 0, 'kitingTime': 0}
    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map
    unitFeaturesDict = {} 
    unitDmaxDict = {}
    
    # Here is the feature dictionary that contains the features for each unit
    # The structure of each item in the dictionary is : 'name_of_unit' : UnitFeatures(attackRange, speedOffCreep, speedOnCreep, dps)
    unitFeaturesDict['Zergling'] = UnitFeatures(0.1, 4.13, 6.58, 100)
    unitFeaturesDict['ZerglingSpeedBoost'] = UnitFeatures(0.1, 5.37, 8.55, 10)    
    unitFeaturesDict['Roach'] =  UnitFeatures(, , ,)
    unitFeaturesDict['Baneling'] = UnitFeatures(, , ,)
    unitFeaturesDict['Queen'] = UnitFeatures( , , ,)
    unitFeaturesDict['Drone'] = UnitFeatures( , , ,)

    # unitDmaxDict is the dictionary that contains the oncreepdmax and offcreepdmax for each unit
    
    for name, unitFeatures in unitFeaturesDict:
      offdmax =  unitFeatures.attackRange + 1 + unitFeatures.speedOffCreep + self[reaper]['kitingTime']
      ondmax =  unitFeatures.attackRange + 1 + unitFeatures.speedOnCreep + self[reaper]['kitingTime']
      unitDmaxDict[name] = {'offcreepdmax': offdmax, 'oncreepdmax' : ondmax}
    
    
      
    #Realtime Enemy Observation
    def updateMap(self, enemyDict):
      # enemyDict is the dictionary containing the information of the enemies in the form: {'name_unit' : { 'location': Position(3,4), 'creep' : True }, ...} 
      for name,creepAndLocation in enemyDict:
      
        if creepAndLocation['creep']:
          dmax = unitDmaxDict[name]['oncreepdmax']
        else:
          dmax = unitDmaxDict[name]['offcreepdmax']
        
        enemyPosition = creepAndLocation['position']
      	self.updateNeighboringCells(dmax, enemyPosition, name)



    def updateNeighboringCells(dmax, enemyPosition, name):

      x = enemyPosition.x
      y = enemyPosition.y
      for dy in range(-1,2):
        for dx in range(-1,2):
          distance = math.sqrt(dx ** 2 + dy ** 2)
          if distance <= dmax:
            self.I_Map[enemyPosition.x + dx][enemyPosition.y + dy] = unitFeaturesDict[name].dps
          else:
            self.I_Map[enemyPosition.x + dx][enemyPosition.y + dy] = 0
