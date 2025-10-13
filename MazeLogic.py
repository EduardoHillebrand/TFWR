
def make_maze(size=6):
	plant(Entities.Bush)
	substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)


DIRS = [North, East, South, West]
RIGHT = {North: East, East: South, South: West, West: North}
LEFT  = {North: West, West: South, South: East, East: North}
BACK  = {North: South, South: North, East: West, West: East}

def find_and_harvest():
	d = East
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True
		r = RIGHT[d]
		if can_move(r):
			move(r)
			d = r
			continue
		if can_move(d):
			move(d)
			continue
		l = LEFT[d]
		if can_move(l):
			move(l)
			d = l
			continue
		move(BACK[d])
		d = BACK[d]

def loop_mazes(size=6):	
	make_maze(size)
	find_and_harvest()


