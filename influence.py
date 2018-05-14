import numpy
from our_class_files import vOneZergling

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

import time


class UnitFeatures:
  def __init__(self, attackRange, speed, dps):
    self.attackRange = range
    self.speed = speed
    self.dps = dps

class InfluenceMap():
  
  def __init__(self):
    
    reaper = {'speed': 0,'acceleration' : 0, 'deceleration': 0, 'attackTime': 0, 'turnTime': 0, 'kitingTime': 0}
    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map
    unitFeaturesDict = {} # feature array for each unit
    
    #Features: AttackRange, Speed, DPS
    unitFeaturesDict.add('Zergling': UnitFeatures(attackRange = 0.1, speed = 4.13, dps = 10))
    unitFeaturesDict.add('Roach': UnitFeatures(4, 3.15, 11.2))
    unitFeaturesDict.add('Baneling': UnitFeatures(0.25, 3.5, 20))
    unitFeaturesDict.add('Queen': UnitFeatures(...))
    # add more units pls
    
    #Realtime Enemy Observation
    def updateMap(self, enemyCollection):
      # loop through collection
      for i in range(len(enemyCollection)):
        
        # get attack range, speed and dps of each
        name = enemyCollection[i]
        attackRange = self.unitFeaturesArray[name].attackRange
        speed = self.unitFeaturesArray[name].speed
        dps = self.unitFeaturesArray[name].dps
      
      	
        #perform calculations to get Ienemy
      	reaperOutRuns = false
        
        
        #update cell with DPS determined by dMax
      end loop if no more
