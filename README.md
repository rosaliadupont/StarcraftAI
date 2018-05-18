Reaper Agent

See team drive for code outline of how this fits into everyone elses code. 

This code is the main class that interfaces with the api and the game itself directly. It has high level funtions that use the influence map, unit stats, and any other classes. 

Most functionality is implimented in the step function, which updates observations from the obs array, checks kiting, and determines an action for the reaper that is then sent to the game. 


