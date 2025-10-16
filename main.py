import ProductionLogic
import MazeLogic
import DinoLogic
import functions

isFirst = True

while True:	
	if get_world_size()  != 32:
		set_world_size(32)

	functions.CheckExpand()
	if not isFirst:
		functions.ReturnHome()
		isFirst = False
		
	plans = functions.CheckExpander()
	if plans[0] != False:
		plan = plans[0]
	else:
		plan = functions.menor_item()
		
	if num_items(Items.Power) < 5000:
		plan = Items.Power
	
	print(plans[1],'>',plans[0],' - ',plans[2])
	
	if  plan == Items.Gold:
		if num_items(Items.Weird_Substance) > 50000 and num_items(Items.Power) > 5000 :
			change_hat(Hats.Gold_Hat)
			#MazeLogic.loop_mazes(6,10)
			MazeLogic.loop_mazes(12,1)
		else :
			change_hat(Hats.Gold_Hat)	
			harvest()
			map = ['S','S','']
			for item in map:
				functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
				functions.do_flips(14)
	elif plan == Items.Bone:
		if num_items(Items.Cactus) > 30000 and num_items(Items.Power) > 5000 :
			change_hat(Hats.Traffic_Cone)
			DinoLogic.play_snake(12)
		else :
			if get_world_size()  != 32:
				set_world_size(32)
			change_hat(Hats.Traffic_Cone)	
			harvest()
			map = ['K','K','K','K','']
			for item in map:
				functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
				functions.do_flips(14)
				do_flips()
	
	elif plan == Items.Cactus:
		change_hat(Hats.Cactus_Hat)	
		harvest()
		map = ['K','K','K','K','']
		for item in map:
			functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
			functions.do_flips(14)

	elif plan == Items.Pumpkin:
		change_hat(Hats.Wizard_Hat)	
		harvest()
		map = ['P','P','P','P','']
		for item in map:
			functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
			functions.do_flips(14)
	
	elif plan == Items.Carrot:
		change_hat(Hats.Carrot_Hat)	
		harvest()
		map = ['C','C','C','C','']
		for item in map:
			functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
			functions.do_flips(14)
		
	elif plan == Items.Wood :
		change_hat(Hats.Tree_Hat)	
		harvest()
		map = ['T','T','T','T','T']
		for item in map:
			functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
			functions.do_flips(14)
		
	elif plan == Items.Hay:
		change_hat(Hats.Green_Hat)	
		harvest()
		map = ['H','H','H','H','H']
		for item in map:
			functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
			functions.do_flips(14)
		
	elif plan == Items.Power:
		change_hat(Hats.Sunflower_Hat)	
		harvest()
		map = ['S','S','S','']
		for item in map:
			functions.harvest_farm_drone_function(ProductionLogic.loop_ProductionForClones,[item])
			functions.do_flips(14)

	else:
		print(plans[0],plans[1],plans[2])
		
	





	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		