def win_indexes(n):
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]


def is_winner(board, decorator):
    board_state = [board[0:3], board[3:6], board[6::]]
    n = len(board_state)
    for indexes in win_indexes(n):
        if all(board_state[r][c] == decorator for r, c in indexes):
            return True
    return False


def space_check(board, position):
    return board[position] == '-'


def is_full(board):
    for i in range(len(board)):
        if space_check(board, i):
            return False
    return True


def move_location(move_string):
    if move_string == '1 1':
        slot = 0
    elif move_string == '1 2':
        slot = 1
    elif move_string == '1 3':
        slot = 2
    elif move_string == '2 1':
        slot = 3
    elif move_string == '2 2':
        slot = 4
    elif move_string == '2 3':
        slot = 5
    elif move_string == '3 1':
        slot = 6
    elif move_string == '3 2':
        slot = 7
    else:
        slot = 8
    return slot


def print_board(board):
    b1 = board[0:3]
    b2 = board[3:6]
    b3 = board[6:9]
    b1 = ' '.join(b1)
    b2 = ' '.join(b2)
    b3 = ' '.join(b3)
    border_top = '    1 2 3\n  ---------'
    border_bot = '  ---------'
    print(f'{border_top}\n1 | {b1} |\n2 | {b2} |\n3 | {b3} |\n{border_bot}')


def again():
    return input('Play again? (y/n)\n').startswith('y')


board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
valid_moves = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']

print(f'Welcome to Tic-Tac-Toe')
# Players
player_1 = input('Enter player 1 name:\n')
player_2 = input('Enter player 2 name:\n')
print('\nEnter moves with row first, then column.\nExample: 1 3 will make a move on the top right corner of the board\n')

# Game
while True:
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    turn = 'Player 1'
    game = True

    while game:
        if turn == 'Player 1':
            print_board(board)
            valid_move = 0

            while valid_move == 0:
                player_move = input(f'Make a move {player_1}:\n')
                if player_move not in valid_moves:
                    print('Please enter a valid move!')
                elif player_move in valid_moves:
                    move = move_location(player_move)
                    if board[move] == 'X' or board[move] == 'O':
                        print('This space is occupied! Choose another one!')
                    else:
                        move = move_location(player_move)
                        board[move] = 'X'
                        valid_move += 1

            if is_winner(board, 'X'):
                print_board(board)
                print('Player 1 wins!')
                game = False
            else:
                if is_full(board):
                    print_board(board)
                    print('Draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            print_board(board)
            valid_move = 0

            while valid_move == 0:
                player_move = input(f'Make a move {player_2}:\n')
                if player_move not in valid_moves:
                    print('Please enter a valid move!')
                elif player_move in valid_moves:
                    move = move_location(player_move)
                    if board[move] == 'X' or board[move] == 'O':
                        print('This space is occupied! Choose another one!')
                    else:
                        move = move_location(player_move)
                        board[move] = 'O'
                        valid_move += 1

            if is_winner(board, 'O'):
                print_board(board)
                print('Player 2 wins!')
                game = False
            else:
                if is_full(board):
                    print_board(board)
                    print('Draw')
                    break
                else:
                    turn = 'Player 1'

    if not again():
        break

