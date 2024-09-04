def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Satırları kontrol et
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Sütunları kontrol et
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Çaprazları kontrol et
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_tie(board):
    # Tahtada boş yer kalmadıysa ve kazanan yoksa oyun berabere
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Row and column must be 0, 1, or 2.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 2.")

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break

        # Oyuncuyu değiştir
        player = "O" if player == "X" else "X"

tic_tac_toe()
