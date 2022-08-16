import os

# board = [
#     ["!", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_"], 
#     ["8", "|", "_", "|", "o", "|", "_", "|", "o", "|", "_", "|", "o", "|", "_", "|", "o", "|"],
#     ["7", "|", "o", "|", "x", "|", "o", "|", "_", "|", "o", "|", "_", "|", "o", "|", "_", "|"],
#     ["6", "|", "o", "|", "o", "|", "_", "|", "o", "|", "_", "|", "o", "|", "_", "|", "o", "|"],
#     ["5", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
#     ["4", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
#     ["3", "|", "x", "|", "_", "|", "x", "|", "_", "|", "x", "|", "_", "|", "x", "|", "_", "|"],
#     ["2", "|", "_", "|", "x", "|", "_", "|", "x", "|", "_", "|", "x", "|", "_", "|", "x", "|"],
#     ["1", "|", "x", "|", "_", "|", "x", "|", "_", "|", "x", "|", "_", "|", "x", "|", "_", "|"],
#     ["!", "!", "A", "!", "B", "!", "C", "!", "D", "!", "E", "!", "F", "!", "G", "!", "H", "!"],
#     ]

board = [
    ["!", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_"], 
    ["8", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["7", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["6", "|", "_", "|", "_", "|", "x", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["5", "|", "_", "|", "_", "|", "_", "|", "o", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["4", "|", "_", "|", "_", "|", "x", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["3", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["2", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["1", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["!", "!", "A", "!", "B", "!", "C", "!", "D", "!", "E", "!", "F", "!", "G", "!", "H", "!"],
    ]

def draw():
    global first_iteration
    first_iteration = True

    def draw_board(square, i):
        if square == "!":
            print(" ", end="")
        elif square == "_":
            if first_iteration and i == 17:
                print("_")
            else:
                print("_", end="")
        elif square == "|":
            if i != 18:
                print("|", end="")
            else:
                print("|")
        else:
            print(square, end="")

    for row in board:
        i = 1
        for square in row:
            draw_board(square, i)
            i += 1
        first_iteration = False
      


    def move_player(letterfrom, numberfrom, letterto, numberto):
        board_to_list = {
            "8": 1,
            "7": 2, 
            "6": 3,
            "5": 4,
            "4": 5,
            "3": 6,
            "2": 7,
            "1": 8,
            "A": 2,
            "B": 4,
            "C": 6,
            "D": 8,
            "E": 10,
            "F": 12,
            "G": 14,
            "H": 16,
        }
        
        def valid_piece():
            print("Escolha uma peça valida!")
            get_pos()
            
        def backwards_move():
            print("Você não pode mover sua peça para trás")
            get_pos()

        def hori_vert_move():
            print("Você não pode andar na vertical ou horizontal")
            get_pos()

        def capturing_move(num_direction, letter_direction, enemy_num_direction, enemy_letter_direction):
            print(board_to_list[numberfrom] + num_direction, "oii")
            if board[board_to_list[numberfrom] + num_direction][board_to_list[letterfrom] + letter_direction] == "_":
                if board_to_list[numberto] != (board_to_list[numberfrom] + num_direction) or board_to_list[letterto] != (board_to_list[letterfrom] + letter_direction):
                    print("Você é obrigado a comer uma peça")
                    get_pos()
                else:
                    board[board_to_list[numberfrom] + enemy_num_direction][board_to_list[letterfrom] + enemy_letter_direction] = "_"
                    board[board_to_list[numberfrom]][board_to_list[letterfrom]] = "_"
                    board[board_to_list[numberto]][board_to_list[letterto]] = "o"


        if board[board_to_list[numberfrom]][board_to_list[letterfrom]] == "_":
            valid_piece()
        elif board_to_list[numberfrom] < 7 and board_to_list[letterfrom] < 14 and board[board_to_list[numberfrom] - 1][board_to_list[letterfrom] + 2] == "x":
            capturing_move(-2, +4, -1, +2)
        elif board_to_list[numberfrom] > 2 and board_to_list[letterfrom] < 14 and board[board_to_list[numberfrom] + 1][board_to_list[letterfrom] + 2] == "x":
            capturing_move(2, 4, 1, 2)
        elif board_to_list[numberfrom] < 7 and board_to_list[letterfrom] > 4 and board[board_to_list[numberfrom] - 1][board_to_list[letterfrom] - 2] == "x":
            capturing_move(-2, -4, -1, -2)
        elif board_to_list[numberfrom] > 2 and board_to_list[letterfrom] > 4 and board[board_to_list[numberfrom] +1][board_to_list[letterfrom] -2] == "x":
            capturing_move(2, -4, +1, -2)
        elif board[board_to_list[numberfrom]][board_to_list[letterfrom]] == "o" and numberfrom < numberto:
            backwards_move()
        elif numberfrom == numberto or letterfrom == letterto:
            hori_vert_move()
        else:    
            board[board_to_list[numberfrom]][board_to_list[letterfrom]] = "_"
            board[board_to_list[numberto]][board_to_list[letterto]] = "o"
        
    def get_pos():
        letterfrom = input(f'\nDa letra: ').upper()
        while letterfrom.isalpha() == False:
            letterfrom = input("Insira a LETRA de partida: ").upper()
        
        numberfrom = input(f'Do número: ')
        while numberfrom.isnumeric() == False:
            numberfrom = input(f'Insira o número de partida: ')

        letterto = input(f'Para a letra: ').upper()
        while letterfrom.isalpha() == False:
            letterto = input(f'Para a letra: ').upper()

        numberto = input(f'Para o número: ')
        while numberto.isnumeric() == False:
            numberto = input(f'Para o número: ')

        move_player(letterfrom, numberfrom, letterto, numberto)

    get_pos()

while True:
    cls = lambda: os.system('cls')
    cls()
    draw()
    