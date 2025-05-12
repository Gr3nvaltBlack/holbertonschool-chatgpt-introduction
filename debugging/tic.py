def print_board(board):
    """Affiche le plateau de jeu dans la console"""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Vérifie si un joueur a gagné"""
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie les diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """Vérifie si toutes les cases sont remplies (match nul)"""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Initialise une grille vide
    player = "X"

    while True:
        print_board(board)

        # Saisie sécurisée de la position
        try:
            row = int(input(f"Joueur {player}, entrez la ligne (0-2) : "))
            col = int(input(f"Joueur {player}, entrez la colonne (0-2) : "))

            if row not in range(3) or col not in range(3):
                print("Coordonnées hors limites. Réessaie.")
                continue

            if board[row][col] != " ":
                print("Cette case est déjà occupée ! Réessaie.")
                continue

            board[row][col] = player  # Place le symbole du joueur

            if check_winner(board):
                print_board(board)
                print(f"🎉 Le joueur {player} a gagné !")
                break

            if is_board_full(board):
                print_board(board)
                print("Match nul !")
                break

            # Change de joueur
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Entrée invalide. Tu dois entrer un nombre entier.")
        except IndexError:
            print("Coordonnées invalides. Réessaie.")

# Lancer le jeu
tic_tac_toe()
