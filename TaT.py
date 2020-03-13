
print("Bienvenido a TaTeTi")

matriz=[["1","2","3"],["4","5","6"],["7","8","9"]]
jueguito = 1

while jueguito == 1:
	print (matriz[0])
	print (matriz[1])
	print (matriz[2])
	
	if matriz[0][0]==matriz[0][1] and matriz[0][1]==matriz[0][2] or matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]:
		print ("GANASTE")
		jueguito=2
	if matriz[0][0]==matriz[1][0] and matriz[1][0]==matriz[2][0] or matriz[0][1]==matriz[1][1] and matriz[1][1]==matriz[2][1]: 
		print ("GANASTE")
	
	
	
	
	jugadas_1=(input("\nJugador 1, elija la posición\n"))
		
	if jugadas_1 == matriz[0][0]:
		matriz[0][0] = "O"
	if jugadas_1 == matriz[0][1]:
		matriz[0][1] = "O"
	if jugadas_1 == matriz[0][2]:
		matriz[0][2] = "O"
	if jugadas_1 == matriz[1][0]:
		matriz[1][0] = "O"
	if jugadas_1 == matriz[1][1]:
		matriz[1][1] = "O"
	if jugadas_1 == matriz[1][2]:
		matriz[1][2] = "O"
	if jugadas_1 == matriz[2][0]:
		matriz[2][0] = "O"
	if jugadas_1 == matriz[2][1]:
		matriz[2][1] = "O"
	if jugadas_1 == matriz[2][2]:
		matriz[2][2] = "O"
	
	print (matriz[0])
	print (matriz[1])
	print (matriz[2])

	if matriz[0][0]==matriz[0][1] and matriz[0][1]==matriz[0][2] or matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]:
		print ("GANASTE")
		jueguito=2
	if matriz[0][0]==matriz[1][0] and matriz[1][0]==matriz[2][0] or matriz[0][1]==matriz[1][1] and matriz[1][1]==matriz[2][1]: 
		print ("GANASTE")
			
	jugadas_2=(input("\nJugador 2, elija la posición\n"))
	if jugadas_2 == matriz[0][0]:
		matriz[0][0] = "X"
	if jugadas_2 == matriz[0][1]:
		matriz[0][1] = "X"
	if jugadas_2 == matriz[0][2]:
		matriz[0][2] = "X"
	if jugadas_2 == matriz[1][0]:
		matriz[1][0] = "X"
	if jugadas_2 == matriz[1][1]:
		matriz[1][1] = "X"
	if jugadas_2 == matriz[1][2]:
		matriz[1][2] = "X"
	if jugadas_2 == matriz[2][0]:
		matriz[2][0] = "X"
	if jugadas_2 == matriz[2][1]:
		matriz[2][1] = "X"
	if jugadas_2 == matriz[2][2]:
		matriz[2][2] = "X"



	
