def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Cek baris dan kolom
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True

    # Cek diagonal
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Giliran {current_player}")
        try:
            row = int(input("Pilih baris (0-2): "))
            col = int(input("Pilih kolom (0-2): "))
        except ValueError:
            print("Masukkan angka valid!")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Pemain {current_player} menang!")
                break
            elif is_full(board):
                print_board(board)
                print("⚖️ Permainan seri!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Langkah tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
