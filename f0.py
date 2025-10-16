import functions
import DinoLogic
import MazeLogic

import DroneControll


functions.ReturnHome()
pos = DroneControll.register(get_time()) #define o principal
while True:	
	do_a_flip()
	if num_drones() < max_drones() -1 :
		DroneControll.create_new_drone()
	
	


	#spawn_drone(drone_function)
	#max_drones()
	#num_drones()
	
	