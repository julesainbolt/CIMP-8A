#! /usr/bin/env python3

from player import Player, Bart, Lisa


def display_title():
    print("Roshambo Game\n")


def get_name():
    return input("Enter your name: ")


def choose_bart_or_lisa(computer_player_choice):
    if computer_player_choice == "b":
        return Bart()
    elif computer_player_choice == "l":
        return Lisa()


def check_winner(current_player, computer_player):
    # If user (player) is rock
    if current_player.roshambo_value == "rock":
        if computer_player.roshambo_value == "paper":
            return computer_player
        elif computer_player.roshambo_value == "scissors":
            return current_player

    # If user (player) is paper
    if current_player.roshambo_value == "paper":
        if computer_player.roshambo_value == "rock":
            return current_player
        elif computer_player.roshambo_value == "scissors":
            return computer_player

    # If user (player) is scissors
    if current_player.roshambo_value == "scissors":
        if computer_player.roshambo_value == "rock":
            return computer_player
        elif computer_player.roshambo_value == "paper":
            return current_player

    return None


def main():

    display_title()

    # Create a player object from the player's name
    current_player = Player(get_name())

    computer_player_choice = input("\nWould you like to play Bart or Lisa? (b/l): ").lower()

    # Create a Bart or Lisa object from the prompt
    computer_player = choose_bart_or_lisa(computer_player_choice)

    print()

    continue_program = "y"
    while continue_program.lower() == "y":

        choice = input("Rock, paper, or scissors? (r/p/s): ").lower()

        if choice == "r":
            current_player.roshambo_value = "rock"
        elif choice == "p":
            current_player.roshambo_value = "paper"
        elif choice == "s":
            current_player.roshambo_value = "scissors"

        computer_player.generate_roshambo()

        print(f"\n{current_player.name}: {current_player.roshambo_value}")
        print(f"{computer_player.name}: {computer_player.roshambo_value}")

        winner = check_winner(current_player, computer_player)

        # If there's a tie
        if winner is None:
            print("Draw!")
        else:
            print(f"{winner.name} wins!")

        continue_program = input("\nPlay again? (y/n): ")

        print()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
