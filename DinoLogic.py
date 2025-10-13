import ProductionLogic
	

def next_move(x, y, width, height):

	if x == 1 and y == height-1:
		return West
		
	elif y % 2 == 0:
		if x < width -1:
			return East
		else:
			return North
			
	else:
		if x > 1:
			return West
		else:
			return North

		
		
def play_snake():
	set_world_size(12)
	n = get_world_size()   
	width = n
	height = n
	change_hat(Hats.Dinosaur_Hat)
	while True:
		x, y = get_pos_x(), get_pos_y()
		if x==0 and y==n-1 :
			while get_pos_y() != 0:
				move(South)
			d = East
		else:
			d = next_move(x, y, width, height)
		if d == None or not can_move(d):
			break
		moved = move(d)  
			



