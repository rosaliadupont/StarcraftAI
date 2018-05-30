from .position import Point3 # FIXME: where is position.py???
import math

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the
# updateMap() giving it the information from the pysc2 api.

class InfluenceMap:

  def __init__(self, size):

    I_Map = [[0 for x in range(32)] for y in range(32)] # influence map
    self.height = size.height
    self.width = size.width
    print(I_Map)

  def update_map(self, enemy_array, unit_stats):

    # this embedded for loop iterates through the influence map
    # entries and checks whether each enemy is within the range
    # of damage, if it is then the entry gets added with this dps

    for x in range(0,32):
      for y in range(0,32):
        self.I_Map[x][y] = 0
        for enemy in enemy_array: #[positon, d_max]
            e_x = int(enemy[0].x * 32 / self.width) #convert to cell in i_map
            e_y = int(enemy[0].y * 32 / self.height)
            distance = math.sqrt((e_x - x) ** 2 + (e_y - y) ** 2)
            if distance <= enemy.d_max:
                self.I_Map[x][y] += unit_stats.enemyStats[enemy.type]['DPS']

  def get_secure_position(self, actual_position):

    # this function returns a tuple as (x,y) indicating
    # where the secure closest position is

    r_x = int(actual_position.x * 32 / self.width)
    r_y = int(actual_position.y * 32 / self.height)

    if self.I_Map[x][y] == 0:
      return actual_position

    distances_to_coords = {}
    for x in range(0,32):
      for y in range(0,32):
        if self.I_Map[x][y] == 0:
          distance = math.sqrt((r_x - x) ** 2 + (r_y - y) ** 2)
          distances_to_coords[distance] = (x,y)

    if len(distances_to_coords) == 0:
      #-1 will be the error code returned
      return -1

    map_pos = distances_to_coords[min(distances_to_coords.keys())]
    x = map_pos[0] * self.width / 32 + self.width / 64 #convert to map size
    y = map_pos[1] * self.height / 32 + self.height / 64

    return Point3(x, y, 0)
