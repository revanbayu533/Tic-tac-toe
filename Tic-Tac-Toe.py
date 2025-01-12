board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
current_player = "X"
winner = None
game_running = True

# Mencetak papan
def print_board(board):
    for row in [board[i:i+3] for i in range(0, len(board), 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Mengambil input pemain
def player_input(board):
    while True:
        try:
            inp = int(input(f"Masukkan angka 1-9 untuk pemain {current_player}: ")) - 1
            if 0 <= inp < 9 and board[inp] == '-':
                board[inp] = current_player
                break
            else:
                print("Posisi tidak valid atau sudah terisi. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan angka antara 1-9.")

# Memeriksa pemenang atau seri
def check_win_tie(board):
    global winner, game_running
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != '-':
            winner = current_player
            print_board(board)
            print(f"Pemenangnya adalah {winner}!")
            game_running = False
            return
    if '-' not in board:
        print_board(board)
        print("Permainan seri!")
        game_running = False

# Mengganti pemain
def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

# Loop utama permainan
while game_running:
    print_board(board)
    player_input(board)
    check_win_tie(board)
    if game_running:
        switch_player()
