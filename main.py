import ProductionLogic
import MazeLogic
import functions


while True:
	
	if num_items(Items.Weird_Substance) > 50000 and num_items(Items.Power) > 5000 :
		MazeLogic.loop_mazes(6)
	else :
		harvest()
		ProductionLogic.loop_Production()

	functions.CheckExpand()




	
		