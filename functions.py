import AllUnlocks
def rotacionar(matriz):
	if not matriz or not matriz[0]:
		return []

	altura = len(matriz)
	largura = len(matriz[0])

	nova = []
	y_linha = 0
	while y_linha < largura:
		linha = []
		x_coluna = 0
		while x_coluna < altura:
			linha.append(matriz[altura - 1 - x_coluna][y_linha])
			x_coluna += 1
		nova.append(linha)
		y_linha += 1

	return nova
	
	
def CheckExpand():
	things = AllUnlocks.all
	
	for thing in things:
		tryExpand(thing)

def tryExpand(that):
	cost = get_cost(that)  
	if not cost:
		return

	for item in cost:
		custo = cost[item]            
		total = num_items(item)
		minimo = custo * 1.35
		if total <= minimo:     
			return  
			
	print("!")
	unlock(that)

def GetLabel(str):
	if str == "C" :
		return "Carrot"
	elif str == "B" :
		return "Bush"
	elif str == "T" :
		return "Wood" 
	elif str == "P" :
		return "Pumpkin"
	elif str == "S" :
		return "Sunflower"
	elif str == "K" :
		return "Cactus"
	elif str == "O" :
		return "Optimized"
	elif str == "Z" :
		return "Love"
	elif str == "X" :
		return "IA Generated"
	else:
		return "Hay"
		
		
def RandomTry(percent,func,what):
	rand = random() * 100 // 1
	if rand < percent:
		if what == False:
			func()
		else:
			func(what)
		return 1
	return 0
			
		
		
		
		
		