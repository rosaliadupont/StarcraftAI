
import math

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the 
# updateMap() giving it the information from the pysc2 api.
  
class InfluenceMap:
  
  def __init__(self):
    
    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map
    print(I_Map)

  def update_map(self, enemy_array, unit_stats):

    # this embedded for loop iterates through the influence map
    # entries and checks whether each enemy is within the range
    # of damage, if it is then the entry gets added with this dps

    for x in range(0,32):
      for y in range(0,32):
        self.I_Map[x][y] = 0
        for enemy in enemy_array:
          distance = math.sqrt((enemy.position[0] - x) ** 2 + (enemy.position[1] - y) ** 2)
          if distance <= enemy.d_max:
            self.I_Map[x][y] += unit_stats.enemyStats[enemy.type]['DPS']

  def get_secure_position(self,actual_position):

    # this function returns a tuple as (x,y) indicating
    # where the secure closest position is

    x = actual_position.x
    y = actual_position.y

    if self.I_Map[x][y] == 0:
      return (x,y)

    distances_to_coords = {}
    for i in range(0,32):
      for j in range(0,32):
        if self.I_Map[i][j] == 0:
          distance = math.sqrt((x - i) ** 2 + (y - j) ** 2)
          distances_to_coords[distance] = (i,j)

    if len(distances_to_coords) == 0:
      #-1 will be the error code returned
      return -1

    return distances_to_coords[min(distances_to_coords.keys())]
