# 1. Crea dos arrays ...
print('________________________________________')
print('____________Ejercicio N°1_______________')
print('________________________________________')

tamaño = int(input('Ingrese la cantidad de arrays: '))
array1 = []
array2 = []

for i in range(tamaño):
    array1.append(input(str('Ingrese un nombre: ')))
print(array1)
for x in range(tamaño):
    array2.append(len(array1[x]))
print(array2)
