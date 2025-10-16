import functions
import farmer_recipies
import myMap
import Grids
import GlobalVars

WS = get_world_size()
MD = max_drones()
MAX_SLOTS = min(MD,WS)

#LenPP = len(PlotTerms)

def _find_first_free_position():
	pos = 0
	total = len(GlobalVars.get_farm_drone_control())
	while pos < total:
		# Slot livre se o ID naquele slot é None
		if GlobalVars.get_farm_drone_control()[pos][0] == None:
			return pos
		pos += 1
	return None 

def _find_position_by_id(drone_id):
	pos = 0
	while pos < len(GlobalVars.get_farm_drone_control()):
		pair = GlobalVars.get_farm_drone_control()[pos]
		if pair and (pair[0] != False) and (pair[0] == drone_id):
			return pos
		pos += 1
	return None


def register(drone_id):

	# Já existe?
	existing_pos = _find_position_by_id(drone_id)
	if existing_pos != None:
		quick_print("id",drone_id,"já está na posição",existing_pos)
		return existing_pos

	# Menor posição livre
	free_pos = _find_first_free_position()
	if free_pos == None:
		quick_print("não há posições livres para alocar")
		return None
		
	farm_drone_control_var = GlobalVars.get_farm_drone_control()
	farm_drone_control_var[free_pos] = [drone_id, free_pos]
	GlobalVars.set_farm_drone_control(farm_drone_control_var)
	
	quick_print("registrado id ",drone_id," na posição ",free_pos)
	return free_pos

def die(drone_id):
	_init_if_needed()

	pos = _find_position_by_id(drone_id)
	if pos == None:
		quick_print("id",drone_id,"não encontrado para encerrar")
		return False
	
	farm_drone_control_var = GlobalVars.get_farm_drone_control()
	farm_drone_control_var[free_pos] = [None, pos]
	GlobalVars.set_farm_drone_control(farm_drone_control_var)
	quick_print("id ",drone_id," encerrado, posição ",pos," liberada")
	return True

def create_new_drone():
	spawn_drone(function_of_new_drone)
	
	
def function_of_new_drone():
	drone_id = get_time()
	pos = register(drone_id)
	if pos == None:
		return
	
	functions.ReturnHome(pos)
	while True:
		if can_harvest() or get_entity_type() == None:
			harvest()
			plant("S")
			move(North)
			
	ended = die(drone_id)
	
	
def plant(seed):
	y =  get_pos_y()
	x =  get_pos_x()
	
	if(x > MAX_SLOTS or y > MAX_SLOTS):
		if get_ground_type() != Grounds.Grassland:
				till()
			
	elif seed == "C" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)

	elif seed == "B" :
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Bush)
	
	elif seed == "T" :
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Tree)
		
	elif seed == "P" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Pumpkin)
	
	elif seed == "S" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Sunflower)
		
	elif seed == "K" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
	else:
		if get_ground_type() != Grounds.Grassland:
			till()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	