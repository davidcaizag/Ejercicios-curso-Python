# Pedir al usuario que ingrese un número natural
c0 = int(input("Ingresa un número natural: "))

# Inicializar el contador de pasos
steps = 0

# Ejecutar el bucle de Collatz mientras c0 no sea 1
while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1

# Imprimir el último valor de c0 que será 1
print(c0)
# Imprimir el número total de pasos
print("pasos =", steps)
