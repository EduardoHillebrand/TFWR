while get_pos_y() > 0:
	move(South)
while get_pos_x() > 0:
	move(West)

costGrid = [0,0,0,0]
	
Kcost = get_cost(Entities.Cactus)
for item in Kcost:
		Kcusto = Kcost[item]

print(list(Kcost)[0],Kcusto)
costGrid[3] = Kcusto

move(North)
move(North)
	
	
Pcost = get_cost(Entities.Pumpkin)
for item in Pcost:
		Pcusto = Pcost[item]

print(list(Pcost)[0],Pcusto)
costGrid[2] = Pcusto

move(North)
move(North)

Ccost = get_cost(Entities.Carrot)
Ccouter = 0

for item in Ccost:
		Ccusto = Ccost[item]
		print(list(Ccost)[Ccouter],Ccusto)
		costGrid[Ccouter] = Ccusto
		move(North)
		Ccouter +=1
move(North) 
move(East)
move(North) 
move(East)
move(North) 
move(East)

Kcost = get_cost(Entities.Sunflower)
for item in Kcost:
		Kcusto = Kcost[item]

print(list(Kcost)[0],Kcusto)
costGrid[3] = Kcusto

move(North)
move(North)

move(North)	
move(East)	
move(East)
move(North) 
move(East)
move(North)	
move(East)	
		
print("Hay:",costGrid[0]*costGrid[2]*costGrid[3])
move(North)
print("Hay:",costGrid[1]*costGrid[2]*costGrid[3])