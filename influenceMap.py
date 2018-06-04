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

    self.granularity = 10
    self.height = size.height * self.granularity
    self.width = size.width * self.granularity
    self.I_Map = [[0 for y in range(self.height)] for x in range(self.width)]
    #print(self.I_Map)
    self.distances_to_coords = {}
    #pdb.set_trace()
    #create axes
    self.ax1 = plt.subplot(111)

    #create image plot
    self.im1 = self.ax1.imshow(np.random.randint(0, high=256, size=(self.width,self.height)))

    plt.ion()


    self.im1.set_data(np.random.randint(0, high=256, size=(self.width,self.height)))
    #plt.pause(0.05)
    
  def get_secure_pos(self, actual_position, enemy_array, unit_stats):
    r_x = int(actual_position.x * self.granularity)
    r_y = int(actual_position.y * self.granularity)
    start = (r_x, r_y)
    min_dist = distance((0,0), (self.width, self.height))
    closest_0 = -1

    #check current position
    self.fill_cell(start, enemy_array, unit_stats)
    if self.I_Map[r_x][r_y] == 0:
      return actual_position

    for i in range(1, max(self.width, self.height)):
      left = r_x - i
      right = r_x + i
      bot = r_y - i
      top = r_y + i

      for y in range1(bot, top): #check left and right sides
        if 0 <= y < self.height: 
          if 0 <= left < self.width: #position is in bounds
            self.fill_cell((left, y), enemy_array, unit_stats)
            
            if self.I_Map[left][y] == 0:
              cur_dist = distance(start, (left, y))
              if cur_dist < min_dist: #new closest pos
                min_dist = cur_dist
                closest_0 = (left, y)
          if 0 <= right < self.width: #position is in bounds 
            self.fill_cell((right, y), enemy_array, unit_stats)

            if self.I_Map[right][y] == 0:
              cur_dist = distance(start, (right, y))
              if cur_dist < min_dist: #new closest pos
                min_dist = cur_dist
                closest_0 = (right, y)

      for x in range1(left + 1, right - 1): #check top and bottom sides
        if 0 <= x < self.width:
          if 0 <= bot < self.height: #position is in bounds 
            self.fill_cell((x, bot), enemy_array, unit_stats)

            if self.I_Map[x][bot] == 0:
              cur_dist = distance(start, (x, bot))
              if cur_dist < min_dist: #new closest pos
                min_dist = cur_dist
                closest_0 = (x, bot)
          if 0 <= top < self.height:
            self.fill_cell((x, top), enemy_array, unit_stats)

            if self.I_Map[x][top] == 0:
              cur_dist = distance(start, (x, top))
              if cur_dist < min_dist:
                min_dist = cur_dist
                closest_0 = (x, top)

      if closest_0 != -1:
        x = closest_0[0] / self.granularity
        y = closest_0[1] /self.granularity
        return Point2((x, y))

  def fill_cell(self,position, enemy_array, unit_stats):
    x = position[0]
    y = position[1]

    self.I_Map[x][y] = 0
    for enemy in enemy_array: #[positon, d_max]
        distance = math.sqrt((enemy.x - x/self.granularity) ** 2 + (enemy.y - y/self.granularity) ** 2)
        if distance <= enemy.d_max * self.granularity:
            self.I_Map[x][y] += unit_stats.units[enemy.type]['DPS']

def distance(p0, p1):
  return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

def range1(start,end):
  return range(start, end+1)

  '''def update_map(self, enemy_array, unit_stats, actual_position):

    # this embedded for loop iterates through the influence map
    # entries and checks whether each enemy is within the range
    # of damage, if it is then the entry gets added with this dps
    self.distances_to_coords = {}
    r_x = actual_position.x * self.granularity 
    r_y = actual_position.y * self.granularity

    for x in range(self.width):
      for y in range(self.height):
        #print("Width:",self.width,"Height:",self.height,"X:",x,"Y:",y)
        self.I_Map[x][y] = 0
        for enemy in enemy_array: #[positon, d_max]
            distance = math.sqrt((enemy.x - x/self.granularity) ** 2 + (enemy.y - y/self.granularity) ** 2)
            if distance <= enemy.d_max * self.granularity:
                self.I_Map[x][y] += unit_stats.units[enemy.type]['DPS']
        #check for distance 
        if self.I_Map[x][y] == 0:
          distance = math.sqrt((r_x - x) ** 2 + (r_y - y) ** 2)
          self.distances_to_coords[distance] = (x / self.granularity ,y /self.granularity)
    #pdb.set_trace()
    self.im1.set_data(self.I_Map)
    #plt.pause(0.05)

  def get_secure_pos(self, actual_position):

    # this function returns a Point3 for the sc2 action to use indicating
    # where the secure closest position is

    r_x = actual_position.x * self.granularity 
    r_y = actual_position.y * self.granularity

    if self.I_Map[int(r_x)][int(r_y)] == 0:
      return actual_position

    if len(self.distances_to_coords) == 0:
      #-1 will be the error code returned
      return -1

    map_pos = self.distances_to_coords[min(self.distances_to_coords.keys())]

    return Point2((map_pos[0], map_pos[1])) '''


