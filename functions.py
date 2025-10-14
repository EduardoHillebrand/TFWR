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

def CheckExpander():
	peso = 9999999999999999999999999999
	index = False
	necessario = False
	
	for thing in AllUnlocks.all:
		cost = get_cost(thing)
		if cost:
			somatorio = 0    
			for item in cost:
				total = num_items(item)
				custo = cost[item]        
				minimo = custo * 1.35
				somatorio += minimo - num_items(item)
				
			if somatorio < peso :
				peso = somatorio
				index = thing
				custoMaisAlto = 0
				for item2 in cost:
					custo = cost[item]
					minimo = custo * 1.35
					if custoMaisAlto < minimo:
						custoMaisAlto = minimo
						necessario = item2
				
	
	return [necessario,index,peso]	
		
def RandomTry(percent,func,what):
	rand = random() * 100 // 1
	if rand < percent:
		if what == False:
			func()
		else:
			func(what)
		return 1
	return 0
			

def ReturnHome(x=0,y=0):
	while get_pos_y() > y:
		move(South)
	while get_pos_x() > x:
		move(West)


def menor_item():
	itens = AllUnlocks.AllItems
	menor = None
	menor_qtd = 999999999999999
	for item in itens:
		qtd = num_items(item)
		if qtd < menor_qtd:
			menor = item
			menor_qtd = qtd
	return menor
		
		
		
		