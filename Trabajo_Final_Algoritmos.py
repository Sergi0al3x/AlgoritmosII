# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 10:15:39 2025

@author: Sergio
"""

#Explicacion Tecnica 

# Funcional: elevar al cuadrado usando map y lambda
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# Procedural: elevar al cuadrado con bucle
numeros = [1, 2, 3, 4]
cuadrados = []
for n in numeros:
    cuadrados.append(n**2)
print(cuadrados)

#Desarrollo en vivo 

# Problema: filtrar pares, elevar al cuadrado y mostrar resultado

#Programación Funcional
numeros = [1, 2, 3, 4, 5, 6]

pares_al_cuadrado = list(
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros))
)
print("Resultado funcional:", pares_al_cuadrado)

#Programación Procedural:
numeros = [1, 2, 3, 4, 5, 6]

def procesar_lista(lista):
    resultado = []
    for num in lista:
        if num % 2 == 0:
            resultado.append(num ** 2)
    return resultado

print("Resultado procedural:", procesar_lista(numeros))

#idea de proyecto 

# --- Procesador de Texto: Lectura Procedural + Limpieza Funcional ---

def leer_archivo(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.readlines()

# Función pura para limpiar líneas de texto
def limpiar_linea(linea):
    return linea.strip().lower().replace('.', '').replace(',', '')

# Procesamiento funcional de todo el texto
def procesar_texto(lineas):
    lineas_limpias = list(map(limpiar_linea, lineas))
    lineas_no_vacias = list(filter(lambda l: l != '', lineas_limpias))
    return lineas_no_vacias

# Flujo procedural
if __name__ == "__main__":
    lineas = leer_archivo("texto_ejemplo.txt")
    resultado = procesar_texto(lineas)
    print("Texto procesado:")
    for linea in resultado:
        print(linea)