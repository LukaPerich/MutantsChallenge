># MutantsChallenge
Nombre y Apellido: Luka Perich

Legajo: 51618

Email personal: lperich29@gmail.com

Email estudiantil: luka.perich@alumnos.frm.utn.edu.ar

>## Introduccion:  
El presente trabajo corresponde al proyecto final integrador realizado para la materia Programacion I de la Tecnicatura Superior en Programación de la Universidad Tecnológica
Regional con sede en Mendoza. A todos los grupos el profesor: Ing. Nicolas Quiros les
dio un desafio desarrollado por Mercado Libre, el cual busca integrar conocimientos sobre, matrices, funciones, metodos , bucles y condicionales. 

La introduccion del desafio es la siguiente: 
Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.

Te ha contratado a ti para que desarrolles un proyecto que detecte si un humano es mutante basándose en su secuencia de ADN.

Para eso te ha pedido crear un programa con un método o función con la siguiente firma:

boolean isMutant(String[] dna);

En donde recibirás como parámetro un array de Strings que representan cada fila de una tabla de (6x6) con la secuencia del ADN. Las letras de los Strings solo pueden ser: (A,T,C,G), las cuales representa cada base nitrogenada del ADN.

Este proyecto corresponnde a la resolucion del mismo, la cual resulto exitosa y de manera eficiente.

>## Como fue resulto: 
Lo primero que hice fue hacer una funcion para llenar la matriz, la cual llena cada espacio de una matriz de la dimension que le pase el usuario en este caso 6x6, una vez que se van cargado los datos la misma funcion va corroborando si los datos ingresados son correctos, en caso de ser correcto sigue interarndo hasta llenar la matriz, en caso de que no sea correcto le vuelve a pedir al usuario un tipo de dato valido, una vez ingresado el dato valido la funcion llena la matriz.
    
Uuna vez la matriz estaba completa creee otra funcion que evalua y recorre  de forma vertical, horizontal o diagonal si hay alguna coincidencia de 4 letras consecutivas, esto se realizo con (set.) para verificar si hay solo un elemento único, una vez hallada la coincidencia use un contador para llevar un registro de la cantidad de coincidencia que la funcion encontraba, por ultimo use una condicion para ver si había más de una coincidencia, esta funcion retorna la condicion de la persona que, en caso de tener más de dos coincidencias retorna "Mutante" y en caso de tener 1 o menos retorna "No mutante".

>## Casos de Prueba:

```bash
Muestra por pantalla: es Mutante
ATGCGA
CAGTGC
TTATGT
AGAAGG
CCCCTA
TCACTG
```
```bash
Muestra por pantalla: no es Mutante
TGCGA
CAGTGC
TTATTT
AGACGG
GCGTCA
TCACTG
```

>## Como correrlo: 
   
   Clona el repositorio desde este enlace: 
       https://github.com/LukaPerich/MutantsChallenge.git
       
   Ingresa al directorio del proyecto y ejecuta VS code (Asegurate de tener Python instaldo en tu computadora)
   
   Una vez dentro del programa corre el siguiente comando: 
   ```bash
python main.py
```
En caso de querer correr el codigo directamente: 

Copia y pega el siguiente codigo en Vs code en un archivo con la extencion .py

(Recuerda tener intaladas las extenciones correspondientes)

```python
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
        return print("La persona es Mutante")
    else:
        return print("La persona no es Mutante")

#Llamamos a las funciones
Matriz= llenarMatriz()
Condicon=AnalizarCondcion(Matriz)
```


       
