import ProductionLogic
import MazeLogic
import DinoLogic
import functions

while True:	
	set_world_size(32)
	functions.ReturnHome()
	plans = functions.CheckExpander()
	plan = plans[0]
	
	#CheckExpander
	#
	
	if  plan == Items.Gold:
		if num_items(Items.Weird_Substance) > 50000 and num_items(Items.Power) > 5000 :
			change_hat(Hats.Gold_Hat)
			MazeLogic.loop_mazes(6)
		else :
			change_hat(Hats.Wizard_Hat)	
			harvest()
			ProductionLogic.loop_Production(['S','S',''])
	elif plan == Items.Bone:
		if num_items(Items.Cactus) > 30000 and num_items(Items.Power) > 5000 :
			change_hat(Hats.Traffic_Cone)
			DinoLogic.play_snake()
		else :
			change_hat(Hats.Wizard_Hat)	
			harvest()
			ProductionLogic.loop_Production(['K','K','K','K','S','S',''])
	
	elif plan == Items.Cactus:
		change_hat(Hats.Wizard_Hat)	
		harvest()
		ProductionLogic.loop_Production(['K','K','K','K','S',''])
	
	elif plan == Items.Pumpkin:
		change_hat(Hats.Wizard_Hat)	
		harvest()
		ProductionLogic.loop_Production(['P','P','P','P','S',''])
	
	elif plan == Items.Carrot:
		change_hat(Hats.Wizard_Hat)	
		harvest()
		ProductionLogic.loop_Production(['C','C','C','C','S',''])
		
	elif plan == Items.Wood :
		change_hat(Hats.Wizard_Hat)	
		harvest()
		ProductionLogic.loop_Production(['H','T','H','T','S',''])
		
	elif plan == Items.Hay:
		change_hat(Hats.Wizard_Hat)	
		harvest()
		ProductionLogic.loop_Production(['H','T','H','T','S',''])
		
	
	functions.CheckExpand()




	
		