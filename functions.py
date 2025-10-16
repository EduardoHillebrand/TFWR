import AllUnlocks
import ProductionLogic

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
	peso = 9999
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
				if total > minimo:
					continue
				faltam = minimo - num_items(item)
				somatorio += faltam / minimo * 100
				
			if somatorio < peso :
				peso = somatorio
				index = thing
				custoMaisAlto = 0
				for item2 in cost:
					custo = cost[item2]
					minimo = custo * 1.35
					total = num_items(item2)
					if total > minimo:
						continue
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
	while get_pos_y() != y:
		if(get_pos_y() > y):
			move(South)
		elif(get_pos_y() < y):
			move(North)
			
	while get_pos_x() != x:
		if(get_pos_x() > x):
			move(West)
		elif(get_pos_x() < x):
			move(East)



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
		
def do_flips(qtd):
	counter = 0
	while counter < qtd:
		do_a_flip()
		counter+=1
	return "Happy now?"

def harvest_farm_drone_function(function,params,pre_delay=0,pos_delay=0):
	do_flips(pre_delay)
	ProductionLogic.set_harvest_farm_drone_var(params)
	spawn_drone(function)
	ProductionLogic.set_harvest_farm_drone_var(None)
	do_flips(1)
		
		