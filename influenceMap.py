import math

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the 
# updateMap() giving it the information from the pysc2 api.
  
class InfluenceMap:
  
  def __init__(self):
    
    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map
    print(I_Map)

  def update_map(self, enemy_array):
    for enemy in enemy_array:
      d_max = enemy.d_max
      x = enemy.position.x
      y = enemy.position.y

      # the following embedded for loops serve to update the
      # cell of the enemy and the 8 remaining neighboring cells
      # in the influence map

      for dy in range(-1, 2):
        for dx in range(-1, 2):
          distance = math.sqrt(dx ** 2 + dy ** 2)
          if distance <= d_max:
            self.I_Map[x + dx][y + dy] = enemy.dps
          else:
            self.I_Map[x + dx][y + dy] = 0

  def get_secure_position(self,actual_position):

    x = actual_position.x
    y = actual_position.y

    distances_to_coords = {}
    for i in range(0,31):
      for j in range(0,31):
        if self.I_Map[i][j] == 0:
          distance = math.sqrt((x - i) ** 2 + (y - j) ** 2)
          distances_to_coords[distance] = (i,j)

    if len(distances_to_coords) == 0:
      #-1 will be the error code returned
      return -1

    return distances_to_coords[min(distances_to_coords.keys())]
