#Usamos esta funcion para darle dimension y llenar la matriz 
def llenarMatriz():
    dimension=int(input("Ingrese la dimesion de la matriz: "))
    matriz = [[0] * dimension for _ in range(dimension)]

    for fila in range(dimension):
        for columna in range(dimension):
            while True: 
                letra = input(f"Ingrese la letra de la cadena numero: [{columna}]:").upper()
                if (letra=="A" or letra=="T" or letra=="C" or letra=="G" ):
                    matriz[fila][columna] = letra
                    break
                else:
                        print("El valor ingresado no es correcto intente nuevamente")
    return matriz

def AnalizarCondcion(matriz1):
    coincidencia = 0
    # Empezamos a recorrer la matriz y evaluarla
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0]) - 3):
            # Horizontal
            if len(set(matriz1[i][j : j + 4])) == 1:
                coincidencia += 1

            # Vertical
            if len(set(matriz1[i][j] for i in range(i, i + 4))) == 1:
                coincidencia += 1

    for i in range(len(matriz1) - 3):
        for j in range(len(matriz1[0]) - 3):
            
            if len(set(matriz1[i + k][j + k] for k in range(4))) == 1:
                coincidencia += 1

            
            if len(set(matriz1[i + k][j + 3 - k] for k in range(4))) == 1:
                coincidencia += 1
    #Retornamos la condicion de la persona: 
    if coincidencia >= 2:
        return print("La persona es: Mutante")
    else:
        return print("La persona no es: Mutante")

#Llamamos a las funciones
Matriz= llenarMatriz()
Condicon=AnalizarCondcion(Matriz)
