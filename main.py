import ProductionLogic
import MazeLogic
import DinoLogic
import functions

while True:	
	set_farm_size(32)
	functions.ReturnHome()
	
	#CheckExpander
	#
	
	if False:
		if num_items(Items.Weird_Substance) > 50000 and num_items(Items.Power) > 5000 :
			change_hat(Hats.Gold_Hat)
			MazeLogic.loop_mazes(6)
		else :
			change_hat(Hats.Wizard_Hat)	
			harvest()
			ProductionLogic.loop_Production(['S','S',''])
	elif False:
		if num_items(Items.Cactus) > 30000 and num_items(Items.Power) > 5000 :
			change_hat(Hats.Traffic_Cone)
			DinoLogic.play_snake()
		else :
			change_hat(Hats.Wizard_Hat)	
			harvest()
			ProductionLogic.loop_Production(['S','S',''])
		

	
	
	
	functions.CheckExpand()




	
		