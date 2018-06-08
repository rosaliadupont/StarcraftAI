# StarcraftAI

This bot controls a single reaper unit and kites against a zergling. Theoretically, this 
program is capable of handling different unit types so long as those unit types are encoded.

Required to run:
  Python 3, can be downloaded from their website.
  Starcraft II, can be downloaded from Battle.net
  The maps in maps-folder need to be copied to the Starcraft II Maps folder, and must be stored in a subdirectory of the Maps folder.
  To run the bot for a given map the command line should read: $python3 reaper-agent mapname

What follows is a summary of what each file does:
    reaper_agent.py starts the actual game and contains the logic for when the reaper moves and when the reaper attacks.
    enemy.py is a simple class for storing relevant data for an enemy.
    Unit_Stats.py is a class storing the statistics for reaper and zerglings. If additional unit types are to be added, their 
information should be added here
    influenceMap.py is a class that reaper_agent uses to find a safe place on the map to move to.
