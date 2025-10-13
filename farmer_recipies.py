import functions
import myMap
import Grids



PlotPlans = {
	'P':Grids.plotList_Pumpkin,
	'S':Grids.plotList_Sunflower,
	'H':Grids.plotList_HT,
	'T':Grids.plotList_HT
}


def grid_fill(valor):
	grid = []
	i = 0
	while i < get_world_size():
		linha = []
		j = 0
		while j < get_world_size():
			linha.append(valor)
			j += 1
		grid.append(linha)
		i += 1
	return grid


def getPlotPlans(int):
	return functions.rotacionar(
		getRightPlotPlans(myMap.PlotTerms[int])
	)

def getRightPlotPlans(str):
	if str in PlotPlans:
		grid = PlotPlans[str]
		return grid
	return grid_fill(str)
	
	
