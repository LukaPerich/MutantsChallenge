#Creando la matriz: 
Matriz1=[
    ["F","A","A","A","A","A"],
    ["C","A","G","T","G","C"],
    ["T","T","A","T","G","T"],
    ["A","A","A","A","G","G"],
    ["C","C","C","C","T","A"],
    ["T","C","A","C","T","G"]
]
#for fila in Matriz1:
#print (Matriz1[0][0])
fila1=Matriz1[0]
fila2=Matriz1[1]
fila3=Matriz1[2]
fila4=Matriz1[3]
fila5=Matriz1[4]
fila6=Matriz1[5]




coindencia=0
for fila in Matriz1: 
    for i in range(len(fila)-4): 
        if (fila[i]==fila[i+1] and fila1[i+1]==fila1[i+2] and fila[i+2]==fila[i+4]) or (fila[i+1]==fila[i+2] and fila1[i+2]==fila1[i+3] and fila[i+3]==fila[i+4]) or (fila[i+2]==fila[i+3] and fila1[i+3]==fila1[i+4] and fila[i+4]==fila[i+5]): 
            coindencia=coindencia+1
        

if coindencia>=2: 
    print("Mutante")
else: 
    print("No muntante")
    
#Opcion 1 para ver en horizontal
#if (fila1[0]==fila1[1] and fila1[1]==fila1[2] and fila1[2]==fila1[3] ) or (fila1[1]==fila1[2] and fila1[2]==fila1[3] and fila1[3]==fila1[4]) or(fila1[2]==fila1[3] and fila1[3]==fila1[4] and fila1[4]==fila1[5]): 
#    print(1)
#else:
#    print(0)

#Opcion 2 usamos un bucle: 

