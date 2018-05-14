

High level notes:
Global 2D 32x32 matrix, with each unit = ~1 pixel
Lookup table for unit types and their attributes
Global reaper values
Collect enemy units into some sort of list/hashtable/array
In main, loop through the enemy units in our enemy collection
Compute influence of each enemy unit and update the corresponding cell 
Slay

Pseudocode

// structures
Hashtable class?

//globals
w , h = 32, 32
influence_map = [[0 for x in range(w)] for y in range(h)]
Enemy_collection = Hashtable()

Fn main() {
	...
	// Collect enemy units into enemy_collection
	
	// iterate over the collection 
	/* For enemy_unit in enemy_collection {
		// get enemy speed value
		// get enemy attack range
		// get enemy cell position
		// eq 1 - If reaper speed > enemy speed then set bool true
		// eq 2 - if reaper range > enemy range +enemy speed x kitingTime(reaper) + 1 
then  set bool2 true
		//eq_dmax - dmax(reaper, enemy) = enemy attackRange + k + enemy speed x 
kitingTime(reaper)
// eq 4 - if an enemy is within range determined by DPS, then DPS of target added to the cell:
	EnemyInfluence(reaper, enemy, d) =
		enemy.DPS if d  ≤ dmax(reaper, enemy)
		0 	        if d > dmax(reaper, enemy)
			// update the enemy cell position in the matrix
	} */
	...
}
