# Pedir al usuario que ingrese la cantidad de bloques
blocks = int(input("Ingresa la cantidad de bloques: "))

# Inicializar las variables
height = 0
current_layer_blocks = 1

# Construir la pirámide
while blocks >= current_layer_blocks:
    # Restar el número de bloques utilizados para la capa actual
    blocks -= current_layer_blocks
    # Incrementar la altura de la pirámide
    height += 1
    # Incrementar el número de bloques necesarios para la siguiente capa
    current_layer_blocks += 1

# Imprimir la altura de la pirámide
print("La altura de la pirámide es:", height)
