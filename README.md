# MutantsChallenge
    Nombre y Apellido: Luka Perich

    Legajo: 51618

    Email:lperich29@gmail.com


## Introduccion:  
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

## Como fue resulto: 
    Lo primero que hice fue hacer una funcion para llenar la matriz, la cual llena cada espacio de una matriz de la dimension que le pase el usuario en este caso 6x6, una vez que se van cargado los datos la misma funcion va corroborando si los datos ingresados son correctos, en caso de ser correcto sigue interarndo hasta llenar la matriz, en caso de que no sea correcto le vuelve a pedir al usuario un tipo de dato valido, una vez ingresado el dato valido la funcion llena la matriz.
    
    Uuna vez la matriz estaba completa creee otra funcion que evalua y recorre  de forma vertical, horizontal o diagonal si hay alguna coincidencia de 4 letras consecutivas, esto se realizo con (set.) para verificar si hay solo un elemento único, una vez hallada la coincidencia use un contador para llevar un registro de la cantidad de coincidencia que la funcion encontraba, por ultimo use una condicion para ver si había más de una coincidencia, esta funcion retorna la condicion de la persona que, en caso de tener más de dos coincidencias retorna "Mutante" y en caso de tener 1 o menos retorna "No mutante"

## Como correrlo: 

   Clona el repositorio desde este enlace:
  ```bash
    https://github.com/LukaPerich/MutantsChallenge.git
```
   Ingresa al directorio del proyecto y ejecuta VS code
   Una vez dentro del programa corre el siguiente comando:
   ```bash
    python main.py
```