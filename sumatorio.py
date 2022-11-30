from functools import reduce

entrada = "0"
numeros = []

def suma(a,b):
    return a + b

while entrada.isdigit():
    entrada = input("Introduzca un número o teclee una letra para salir:")
    if entrada.isdigit():
        numero = int(entrada)
        numeros.append(numero)

pares = list(filter(lambda x: x%2 == 0, numeros))
impares = list(filter(lambda x: x%2 == 1, numeros))

suma_pares = reduce(suma, pares)
suma_impares = reduce(suma,impares)
print(f'Números pares introducidos:  {pares} Suman un total de {suma_pares}')
print(f'Números impares introducidos:  {impares} Suman un total de {suma_impares}')

