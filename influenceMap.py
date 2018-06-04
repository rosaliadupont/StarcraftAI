from sc2.position import Point2
from enemy import Enemy
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# The influence class is a helper class to the agent class that is instantiated in the agent class. The agent class calls the
# updateMap() giving it the information from the pysc2 api.

class InfluenceMap:

  def __init__(self, size):

    self.height = size.height
    self.width = size.width
    self.I_Map = [[0 for y in range(self.height)] for x in range(self.width)]
    #print(self.I_Map)
    
    #pdb.set_trace()
    #create axes
    self.ax1 = plt.subplot(111)

    #create image plot
    self.im1 = self.ax1.imshow(np.random.randint(0, high=256, size=(self.width,self.height)))

    plt.ion()


    self.im1.set_data(np.random.randint(0, high=256, size=(self.width,self.height)))
    #plt.pause(0.05)
    

  def update_map(self, enemy_array, unit_stats):

    # this embedded for loop iterates through the influence map
    # entries and checks whether each enemy is within the range
    # of damage, if it is then the entry gets added with this dps

    for x in range(self.width):
      for y in range(self.height):
        #print("Width:",self.width,"Height:",self.height,"X:",x,"Y:",y)
        self.I_Map[x][y] = 0
        for enemy in enemy_array: #[positon, d_max]
            distance = math.sqrt((enemy.x - x) ** 2 + (enemy.y - y) ** 2)
            if distance <= enemy.d_max:
                self.I_Map[x][y] += unit_stats.units[enemy.type]['DPS']
    #pdb.set_trace()
    self.im1.set_data(self.I_Map)
    #plt.pause(0.05)

  def get_secure_pos(self, actual_position):

    # this function returns a Point3 for the sc2 action to use indicating
    # where the secure closest position is

    r_x = actual_position.x #is conversion necessary?
    r_y = actual_position.y

    if self.I_Map[int(r_x)][int(r_y)] == 0:
      return actual_position

    distances_to_coords = {}
    for x in range(0,self.width):
      for y in range(0,self.height):
        if self.I_Map[x][y] == 0:
          distance = math.sqrt((r_x - x) ** 2 + (r_y - y) ** 2)
          distances_to_coords[distance] = (x,y)

    if len(distances_to_coords) == 0:
      #-1 will be the error code returned
      return -1

    map_pos = distances_to_coords[min(distances_to_coords.keys())]

    return Point2((map_pos[0], map_pos[1])) #FIXME: not sure if this works, we need to return a position that the game understands, but idk if you can make a new Point3 object
