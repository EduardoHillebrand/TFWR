global farm_drone_control_var
farm_drone_control_var = [[]]


WS = get_world_size()
MD = max_drones()
MAX_SLOTS = min(MD,WS)

def _init_if_needed():
	global farm_drone_control_var
	if (not farm_drone_control_var) or (len(farm_drone_control_var) != MAX_SLOTS):
		farm_drone_control_var = []
		pos = 0
		while pos < MAX_SLOTS:
			farm_drone_control_var.append([None, pos])
			pos += 1


def get_farm_drone_control():
	global harvest_farm_drone_var
	_init_if_needed()
	return farm_drone_control_var


def set_farm_drone_control(new_value):
	global farm_drone_control_var

	i = 0
	while i < MAX_SLOTS-1:
		item = new_value[i]
		if  len(item) != 2:
			return False
		i += 1

	farm_drone_control_var = new_value
	return True
	
#################### END OF global farm_drone_control_var ####################