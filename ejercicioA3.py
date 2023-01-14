# 3. Crea un array o arreglo unidimensiona ...
print('________________________________________')
print('____________Ejercicio N°3_______________')
print('________________________________________')

a_unidimensional = []


def rellenar(n):
    tamaño = int(input("¿Que tamaño es el array?: "))
    for i in range(tamaño):
        a_unidimensional.append((i+1)*n)
    presentar(n)


def presentar(n):
    print("Multiplos del número ingresado: ", n)
    print(a_unidimensional)


rellenar(int(input("Escoja un número del cual desee ver la lista de múltiplos:")))
