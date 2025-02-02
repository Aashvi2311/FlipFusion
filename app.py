import random
import time

def shuffle_board():
    values = ["🍎", "🍉", "🍌", "🍒", "🍇", "🍓", "🍍", "🍊", "🥝", "🍐", "🫐", "🍑"] * 2
    random.shuffle(values)
    return [[values.pop() for _ in range(4)] for _ in range(6)]

def display_board(board, revealed):
    print("   0  1  2  3")
    print("  ------------")
    for i, row in enumerate(board):
        print(i, "|", " ".join(row[j] if revealed[i][j] else "#" for j in range(4)))

def play_game():
    board = shuffle_board()
    revealed = [[False] * 4 for _ in range(6)]
    matched_pairs = 0
    attempts = 0
    
    while matched_pairs < 12:
        display_board(board, revealed)
        
        try:
            row1, col1 = map(int, input("Enter first card (row col): ").split())
            if revealed[row1][col1]:
                print("Already revealed! Try again.")
                continue
        except:
            print("Invalid input! Try again.")
            continue
        
        revealed[row1][col1] = True
        display_board(board, revealed)
        
        try:
            row2, col2 = map(int, input("Enter second card (row col): ").split())
            if revealed[row2][col2] or (row1 == row2 and col1 == col2):
                print("Invalid choice! Try again.")
                revealed[row1][col1] = False
                continue
        except:
            print("Invalid input! Try again.")
            revealed[row1][col1] = False
            continue
        
        revealed[row2][col2] = True
        display_board(board, revealed)
        
        if board[row1][col1] == board[row2][col2]:
            print("It's a match!")
            matched_pairs += 1
        else:
            print("Not a match! Flipping back...")
            time.sleep(1)
            revealed[row1][col1] = revealed[row2][col2] = False
        
        attempts += 1
    
    print("Congratulations, you matched all pairs in", attempts, "attempts!")

if __name__ == "__main__":
    play_game()
