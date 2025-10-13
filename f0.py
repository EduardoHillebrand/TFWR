import AllUnlocks

def CheckExpand():
	peso = 9999999999999999999999999999
	index = AllUnlocks.all[0]
	necessário = AllUnlocks.all[0]
	
	for thing in AllUnlocks.all:
		cost = get_cost(thing)
		if cost:
			somatorio = 0    
			for item in cost:
				total = num_items(item)
				custo = cost[item]        
				minimo = custo * 1.35
				somatorio += minimo
				quick_print(thing,item,peso)
				
			if somatorio < peso :
				peso = somatorio
				index = thing
				custoMaisAlto = 0
				for item2 in cost:
					custo = cost[item]
					minimo = custo * 1.35
					if custoMaisAlto < minimo:
						custoMaisAlto = minimo
						necessário = item2
				
	
	quick_print(index,necessário,peso)
	
	
CheckExpand()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	