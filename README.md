INFLUENCE CLASS

The influence map class will act as a helper class to the agent. Think of the Influence class as an interface that receives data from the agent about the current state of the game and evaluates the influence of the cells around the reaper. Then, it tells the agent whether it is feasible to kite. If it is feasible to kite, the reaper will make another call to the Influence instance to perform perfect kiting. 

If you are writing the enemyDict data structure, I need it to give me the following information:

    name of the unit
    
    whether the unit is on creep
    
    the position of the unit in the map that is already converted to a 32x32 grid.
    
Thanks :)

