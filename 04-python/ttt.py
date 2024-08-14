board = {
    '00' : {'value': ' '},
    '10' : {'value': ' '},
    '20' : {'value': ' '},
    '01' : {'value': ' '},
    '11' : {'value': ' '},
    '21' : {'value': ' '},
    '02' : {'value': ' '},
    '12' : {'value': ' '},
    '22' : {'value': ' '}
}

def display_board():
    print("    0   1   2")
    print("")
    print(f"0   {board['00']['value']} | {board['10']['value']} | {board['20']['value']} ")
    print("   -----------")
    print(f"1   {board['01']['value']} | {board['11']['value']} | {board['21']['value']} ")
    print("   -----------")
    print(f"2   {board['02']['value']} | {board['12']['value']} | {board['22']['value']} ")
    print("")


def player_input(char):
    while True:
        x = input("Choose an X value: ")
        y = input("Choose a Y value: ")
        index = x + y
        
        if index not in board:
            print("Invalid position!")
            continue
        
        if board[index]['value'] == ' ':
            board[index]['value'] = char
            break
        else:
            print('Space taken!')


def check_win():
    rows = [[],[],[]]
    columns = [[],[],[]]

    for cell in board.keys():
        rows[int(cell[0])].append(board[cell]['value'])
        columns[int(cell[1])].append(board[cell]['value'])

    if rows[0][0] == rows[1][1] == rows[2][2] != ' ':
        return True
    
    if rows[0][2] == rows[1][1] == rows[2][0] != ' ':
        return True

    for row in rows:
        if row[0] == row[1] == row[2] != ' ':
            return True
    
    for column in columns:
        if column[0] == column[1] == column[2] != ' ':
            return True
        
    
def play():
    print("welcom to tic-tac-toe")
    print("X will go first")

    plays = 0
    while True:
        if plays %2 == 0:
            display_board()
            print("X's Turn")
            player_input('X')
            win = check_win()
            if win:
                display_board()
                print("Player X wins!")
                break
        else:
            display_board()
            print("O's Turn")
            player_input('O')
            win = check_win()
            if win:
                display_board()
                print("Player O wins!")
                break
        plays += 1

        if plays == 9:
            print("It's a tie")
            display_board()
            break

play()