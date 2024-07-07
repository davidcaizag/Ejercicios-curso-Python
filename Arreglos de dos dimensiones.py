# Definir los símbolos para las piezas y el campo vacío
EMPTY = "."
ROOK = "R"
KNIGHT = "N"
PAWN = "P"

# Crear el tablero de ajedrez de 8x8 con todos los campos vacíos
board = [[EMPTY for i in range(8)] for j in range(8)]

# Colocar las torres en el tablero
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

# Colocar un caballo en C4 (índices de fila y columna son 4 y 2 respectivamente)
board[4][2] = KNIGHT

# Colocar un peón en E5 (índices de fila y columna son 3 y 4 respectivamente)
board[3][4] = PAWN

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Imprimir el tablero después de colocar las piezas
print_board(board)
