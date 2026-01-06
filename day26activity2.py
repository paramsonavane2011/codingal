board = {
    7: " ", 8: " ", 9: " ",
    4: " ", 5: " ", 6: " ",
    1: " ", 2: " ", 3: " "
}

turns = 0
turn = ""

def printBoard():
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("--+---+--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--+---+--")
    print(f"{board[1]} | {board[2]} | {board[3]}")

while turns < 10:
    turns += 1
    printBoard()
    if turns % 2 != 0:
        turn = "X"
    else:
        turn = "O"
    move = int(input(f"Player {turn}, enter your move (1-9): "))
    if move in board and board[move] == " ":
        board[move] = turn
    else:
        print("Invalid move. Try again.")
        turns -= 1
    if turns > 5:
        winningCombinations = [
            (7, 8, 9), (4, 5, 6), (1, 2, 3),
            (7, 4, 1), (8, 5, 2), (9, 6, 3),
            (7, 5, 3), (9, 5, 1)
        ]
        for combo in winningCombinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
                printBoard()
                print(f"Player {turn} wins!")
                exit()