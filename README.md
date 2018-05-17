INFLUENCE CLASS

The influence map class will act as a helper class to the agent. Think of the Influence class as an interface that receives data from the agent about the current state of the game and evaluates the influence of the cells around the reaper. Then, it tells the agent whether it is feasible to kite. If it is feasible to kite, the reaper will make another call to the Influence instance to perform perfect kiting. 

If you are writing the enemyDict data structure that will be used to call the InfluenceMap.updateMap(), I need it to give me the following information:

    dmax of the enemy unit (either on-creep dmax or off-creep dmax) as a double.
    
    the position as a instance of a coordinate class
    
    the dps of the enemy unit as a double
    
The position of the unit in the map should already be in agreement to the scale of the 32x32 map that the InfluenceMap class uses.
    
Thanks :)

