import farmer_recipies
import myMap
import functions

def loop_Production():
	WS = get_world_size()
	LenPP = len(myMap.PlotTerms)
	counter = -1
	#set_farm_size(SIZE)
	
	while get_pos_y() > 0:
		move(South)
	while get_pos_x() > 0:
		move(West)
	
	#do_a_flip()
	
	while True:
	
		y =  get_pos_y()
		x =  get_pos_x()
		
		
		if x == 0 and y == 0:
			counter +=1
			if counter >  LenPP-1 :
				return 
			plotList = farmer_recipies.getPlotPlans(counter)
			SIZE = len(plotList) -1
			#print(functions.GetLabel(myMap.PlotTerms[counter]))
		
		if can_harvest():
			harvest()
		
	
		if(x > SIZE or y > SIZE):
			if get_ground_type() != Grounds.Grassland:
				till()
			
		elif plotList[x][y] == "C" :
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
	
		elif plotList[x][y] == "B" :
			if get_ground_type() != Grounds.Grassland:
				till()
			plant(Entities.Bush)
	
		elif plotList[x][y] == "T" :
			if get_ground_type() != Grounds.Grassland:
				till()
			plant(Entities.Tree)
	
	
		elif plotList[x][y] == "P" :
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Pumpkin)
	
	
		elif plotList[x][y] == "S" :
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Sunflower)
	
	
		elif plotList[x][y] == "K" :
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Cactus)
		else:
			if get_ground_type() != Grounds.Grassland:
				till()
		test = num_items(Items.Fertilizer) > 1000 and get_entity_type() != Entities.Grass
		if test:
			functions.RandomTry(25,use_item,Items.Fertilizer)
		
		if y < WS-1:
			move(North)
		else:
			move(North)
			move(East)

		