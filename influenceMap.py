import math

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the
# updateMap() giving it the information from the pysc2 api.

class InfluenceMap:
    I_map = []

  def __init__(self):

    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map

  def update_map(self, enemy_array):
    for enemy in enemyArray:
      dmax = enemy.dmax
      #TODO: convert screen to minimap position 
      x = enemy.position[0]
      y = enemy.position[1]

      # the following embedded for loops serve to update the
      # cell of the enemy and the 8 remaining neighboring cells
      # in the influence map

      for dy in range(-1, 2):
        for dx in range(-1, 2):
          distance = math.sqrt(dx ** 2 + dy ** 2)
          if distance <= dmax:
            self.I_Map[x + dx][y + dy] = enemy.dps
          else:
            self.I_Map[x + dx][y + dy] = 0
