import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "player"
    else:
        return "computer"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    rounds = 3
    player_score = 0
    computer_score = 0

    for _ in range(rounds):
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        while player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)
        if winner == "player":
            player_score += 1
            print("You win this round!")
        elif winner == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")

        print(f"Score: Player {player_score} - {computer_score} Computer\n")

    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > player_score:
        print("Sorry, the computer won the game.")
    else:
        print("The game is a tie!")

if __name__ == "__main__":
    main()
