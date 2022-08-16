import os

board = [
    ["!", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_", "!", "_"], 
    ["8", "|", "_", "|", "o", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["7", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["6", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["5", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["4", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["3", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["2", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["1", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|", "_", "|"],
    ["!", "!", "A", "!", "B", "!", "C", "!", "D", "!", "E", "!", "F", "!", "G", "!", "H", "!"],
    ]

def draw():
    global first_iteration
    first_iteration = True

    def checking_piece(square, i):
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
            checking_piece(square, i)
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
        
        # condições de erro
        board[board_to_list[numberfrom]][board_to_list[letterfrom]] = "_"
        board[board_to_list[numberto]][board_to_list[letterto]] = "o"
        

    letterfrom = input(f'\nDe letra: ')
    numberfrom = input(f' de número: ')
    letterto = input(f'Para letra: ')
    numberto = input(f'Para número: ')

    move_player(letterfrom, numberfrom, letterto, numberto)


while True:
    cls = lambda: os.system('cls')
    cls()
    draw()
    