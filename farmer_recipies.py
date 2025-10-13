import functions
import myMap
import Grids



PlotPlans = {
	'T':Grids.plotList_T, 
	'O':Grids.plotList_O,
	'Z':Grids.plotList_z,
	'X':Grids.plotList_gpt,
	'S':Grids.plotList_sunflower
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
	
	
