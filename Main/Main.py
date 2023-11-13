#Primero llenamos la matriz:
#(Este paso todavía tiene que ser desarrollado)

#Evaluamos las condiciones, primo lo hacemos de manera horizontal
coindencia=0

for fila in Matriz: 
    for i in range(len(fila)-4): 
        if (fila[i]==fila[i+1] and fila[i+1]==fila[i+2] and fila[i+2]==fila[i+4]) or (fila[i+1]==fila[i+2] and fila[i+2]==fila[i+3] and fila[i+3]==fila[i+4]) or (fila[i+2]==fila[i+3] and fila[i+3]==fila[i+4] and fila[i+4]==fila[i+5]): 
            coindencia=coindencia+1
        

#Determinamos la condicion de la persona: 

if coindencia>=2: 
    print("La persona es: Mutante")
else: 
    print("La persona no es: Muntante")