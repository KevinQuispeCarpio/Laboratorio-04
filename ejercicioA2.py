# 2. Dada las siguientes notas ...
print('________________________________________')
print('____________Ejercicio N°2_______________')
print('________________________________________')

notas = [20, 15, 12, 11, 8, 4, 1]
print("Esta son las notas originales:", notas)
minimo = notas[0]
for i in range(len(notas)):
    if minimo > notas[i]:
        minimo = notas[i]
print('Esta es la mínima nota:', minimo)

for j in range(len(notas)):
    if minimo == notas[j]:
        notas.remove(minimo)
print('Estan son las notas actuales', notas)

for i in range(len(notas)):
    print(notas[i]+notas[i+1])
