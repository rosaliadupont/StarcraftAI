import math
import pdb

class Search:
	def __init__(self, func):
		self.width = 5
		self.height = 5
		self.array = [[func(x, y) for y in range(self.height)] for x in range(self.width)]

	def expanding_search(self, start):
		#min_dist = self.distance((0,0),(self.width, self.height))
		print(start)
		closest_0 = -1
		#if array[start[0]][start[1]] == 0:
		#	return start
		s_x = start[0]
		s_y = start[1]

		#pdb.set_trace()

		for i in range(1, max(self.width, self.height)):
			if 0 <= s_x - i < self.width: #left edge
				for y in range1(s_y - i, s_y + i): 
					if 0 <= y < self.height: #position is in bounds
						#cur_dist = self.distance(start, (x-i, y))
					 	self.array[s_x-i][y] += 1
					 	#if array[x -i][y] == 0 and cur_dist < min_distance: #new closest pos
					 	#	min_dist = cur_dist
					 	#	closest_0 = (x-i, y)
			if 0 <= s_x + i < self.width: #right edge
				for y in range1(s_y - i, s_y + i):
					if 0 <= y < self.height: #position is in bounds
						self.array[s_x+i][y] += 1
						#cur_dist = self.distance(start, (x+i, y))
					 	#if array[x +i][y] == 0 and cur_dist < min_distance: #new closest pos
					 	#	min_dist = cur_dist
					 	#	closest_0 = (x+i, y)
			if 0 <= s_y - i < self.height: #bottom edge
				for x in range1(s_x - i + 1, s_x + i - 1):
					if 0 <= x < self.width: #position is in bounds
						self.array[x][s_y-i] += 1
						#cur_dist = self.distance(start, (x, y-i))
						#if array[x][y - i] == 0 and cur_dist < min_distance:
						#	min_dist = cur_dist
						#	closest_0 = (x, y - i)
			if 0 <= s_y + i < self.height: #top edge
				for x in range1(s_x - i + 1, s_x+ i - 1):
					if 0 <= x < self.width: #position is in bounds
						self.array[x][s_y+i] += 1
						#cur_dist = self.distance(start, (x, y+i))
						#if array[x][y - i] == 0 and cur_dist < min_distance:
						#	min_dist = cur_dist
						#	closest_0 = (x, y+i)
			#if closest_0 != -1:
			#	return closest_0

	def other_search(self, start):
		#min_dist = self.distance((0,0),(self.width, self.height))
		closest_0 = -1
		#if array[start[0]][start[1]] == 0:
		#	return start
		s_x = start[0]
		s_y = start[1]

		for i in range(1, max(self.width, self.height)):
			for y in range1(s_y - i, s_y + i):
				if 0 <= y < self.height: 
					if 0 <= s_x - i < self.width: #position is in bounds
						self.array[s_x-i][y] += 1
						#if array[x -i][y] == 0:
						#	cur_dist = self.distance(start, (x-i, y))
						 #	if cur_dist < min_dist: #new closest pos
						 #		min_dist = cur_dist
						 #		closest_0 = (x-i, y)
					if 0 <= s_x + i < self.width: #position is in bounds 
						self.array[s_x+i][y] += 1
						#if array[x +i][y] == 0:
						#	cur_dist = self.distance(start, (x+i, y))
						 #	if cur_dist < min_dist: #new closest pos
						 #		min_dist = cur_dist
						 #		closest_0 = (x+i, y)

			for x in range1(start[0] - i + 1, start[0] + i - 1):
				if 0 <= x < self.width:
					if 0 <= s_y - i < self.height: #position is in bounds 
						self.array[x][s_y-i] += 1
						#if array[x][y - i] == 0:
						#	cur_dist = self.distance(start, (x, y-i))
						#	if cur_dist < min_dist: #new closest pos
						#		min_dist = cur_dist
						#		closest_0 = (x, y-i)
					if 0 <= s_y + i < self.height:
						self.array[x][s_y+i] += 1
						#if array[x][y+i] == 0:
						#	cur_dist = self.distance(start, (x, y+i))
						#	if cur_dist < min_dist:
						#		min_dist = cur_dist
						#		closest_0 = (x, y+i)

			#if closest_0 != -1:
			#	return closest_0
	
	#def distance(self, p0, p1):
	#	result = math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
    #	return result

def range1(start,end):
	return range(start, end+1)
def main():
	s = Search(lambda x, y: 0)
	s.expanding_search((2,2))

	print("Expanding Search")
	for x in range(s.width):
		print(s.array[x])

	s = Search(lambda x, y: 0)
	s.other_search((2,2))

	print("Other Search")
	for x in range(s.width):
		print(s.array[x])

if __name__ == '__main__':
    main()

