# Classe qui simule un chéquier simple
class Checkbook:
    def __init__(self):
        # Initialisation du solde à 0
        self.balance = 0.0

    def deposit(self, amount):
        # Ajoute le montant déposé au solde
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        # Retire le montant demandé si le solde est suffisant
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        # Affiche le solde actuel
        print("Current Balance: ${:.2f}".format(self.balance))

# Fonction principale du programme
def main():
    cb = Checkbook()  # Création d'une instance de Checkbook
    while True:
        # Demande à l'utilisateur ce qu'il veut faire
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()

        if action == 'exit':
            # Sortie de la boucle et fin du programme
            break
        elif action == 'deposit':
            # Essaye de convertir l'entrée utilisateur en float pour le dépôt
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif action == 'withdraw':
            # Essaye de convertir l'entrée utilisateur en float pour le retrait
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif action == 'balance':
            # Affiche le solde
            cb.get_balance()
        else:
            # Message d'erreur pour toute commande inconnue
            print("Invalid command. Please try again.")

# Point d'entrée du script
if __name__ == "__main__":
    main()
