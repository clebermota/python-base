#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10"""
__version__ = "0.1.0"
__authot__ = "Cleber"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
numeros = list(range(1, 11)) #utilizando o range 

# Iterable (percorríveis)

# para cada número em numeros:
for numero in numeros:
    print("Tabuada do : ", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("---------------")
