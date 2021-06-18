# (control + '/' for comments)

def print_board(board:dict[str,str]):
    print("\n")
    print("[ Current board ]:")
    print(f"7      |8      |9")
    print(f"   {board['7']}   |   {board['8']}   |   {board['9']}")
    print(f"_______|_______|_______")
    print(f"4      |5      |6")
    print(f"   {board['4']}   |   {board['5']}   |   {board['6']}")
    print(f"_______|_______|_______")
    print(f"1      |2      |3")
    print(f"   {board['1']}   |   {board['2']}   |   {board['3']}")
    print(f"       |       |")
    print("\n")

def check_win(board:dict[str,str]):
    if board['1'] != " " and board['1'] == board['2'] == board['3']:
        return board['1']
    elif board['4'] != " " and board['4'] == board['5'] == board['6']:
        return board['4']
    elif board['7'] != " " and board['7'] == board['8'] == board['9']:
        return board['7']
    elif board['1'] != " " and board['1'] == board['4'] == board['7']:
        return board['1']
    elif board['2'] != " " and board['2'] == board['5'] == board['8']:
        return board['2']
    elif board['3'] != " " and board['3'] == board['6'] == board['9']:
        return board['3']
    elif board['1'] != " " and board['1'] == board['5'] == board['9']:
        return board['1']
    elif board['3'] != " " and board['3'] == board['5'] == board['7']:
        return board['3']
    else:
        return ""


def get_user_input(available_choices:list[str], input_msg:str, error_msg:str = "Invalid input! Please try again."):
    choice = ""
    while(choice =="" or choice not in available_choices):
        choice = input(input_msg).upper()
        if(choice not in available_choices):
            print(error_msg)
    return choice



def play_game(board_default:dict[str,str]):
    play_new_game = "Y"
    while(play_new_game=="Y"):
        player:int = 0
        win_symbol:str = ""
        board  = board_default.copy()
        game_end = False
        available_choices = [str(x) for x in range(1,10)]
        user_input:str = ""

        print(f"New game started.")
        while not game_end:
            print_board(board)
            print(f"Player {(player +1 )}'s turn. ('O' for player 1, 'X' for player 2)")
            user_input = get_user_input(available_choices, "Select a tile to place: ")
            if player == 0:
                board[user_input] = "O"
            else:
                board[user_input] = "X"
            available_choices.remove(user_input)
            win_symbol = check_win(board)
            if win_symbol != "" or len(available_choices) == 0:
                game_end = True
            player = (player + 1) % 2
        
        print_board(board)
        if win_symbol == 'O':
            print("Player 1 wins!")
        elif win_symbol == 'X':
            print("Player 2 wins!")
        else:
            print("It is a tie!")
        
        play_new_game = get_user_input(['Y','N'], "Start new game? (Y or N): ")


board_default = {str(k):" " for k in range(1,10)}
play_game(board_default)

