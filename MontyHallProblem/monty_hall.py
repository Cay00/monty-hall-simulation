import random
import sys


def simulate_game(change_choice: bool) -> bool:
    # Number of doors - DEFAULT 3
    door_quantity = 3
    # Door hiding the prize
    prize_door = random.randint(0, door_quantity - 1)
    # Player randomly chooses a door
    player_choice = random.randint(0, door_quantity - 1)

    # Host opens a door that:
    # - is not chosen by the player
    # - does not have the prize
    remaining_doors = []
    for door in range(door_quantity):
        if door != player_choice and door != prize_door:
            remaining_doors.append(door)
    door_opened = random.choice(remaining_doors)

    # If player switches, change choice to the other unopened door
    if change_choice:
        for door in range(door_quantity):
            if door != player_choice and door != door_opened:
                player_choice = door
                break

    # Did the player win?
    return player_choice == prize_door


def simulate(n: int, change_choice: bool) -> float:
    wins = sum(simulate_game(change_choice) for _ in range(n))
    return wins / n


def user_game():
    print("Welcome to the Monty Hall Game!")
    doors = [0, 1, 2]
    wins = 0
    losses = 0
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        prize_door = random.randint(0, 2)

        while True:
            try:
                player_choice = int(input("Choose a door (1, 2, or 3): ")) - 1
                if player_choice in doors:
                    break
                else:
                    print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a number!")

        # Host opens a door that:
        # - is not the player's choice
        # - does not have the prize
        door_opened = None
        for door in doors:
            if door != player_choice and door != prize_door:
                door_opened = door
                break
        print(f"The host opens door number {door_opened + 1}. It has no prize.")

        # Remaining unopened door
        for door in doors:
            if door != player_choice and door != door_opened:
                remaining_door = door
                break

        # Ask player if they want to switch
        while True:
            decision = input(f"Do you want to switch to door number {remaining_door + 1}? (y/n): ").strip().lower()
            if decision in ("y", "n"):
                break
            else:
                print("Please enter 'y' (yes) or 'n' (no).")

        if decision == "y":
            player_choice = remaining_door

        print(f"Your final choice is door number {player_choice + 1}.")
        if player_choice == prize_door:
            print("Congratulations! You won!")
            wins += 1
        else:
            print(f"Sorry, you lost. The prize was behind door number {prize_door + 1}.")
            losses += 1

        total = wins + losses
        percent = (wins / total) * 100 if total > 0 else 0
        print("\nStatistics:")
        print(f"  - Wins: {wins}")
        print(f"  - Losses: {losses}")
        print(f"  - Win rate: {percent:.2f}%")

        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye!")
            sys.exit(0)

        round_number += 1


if __name__ == "__main__":
    print("Welcome! Choose program mode:")
    print("1 - Statistical simulation")
    print("2 - Interactive game")

    while True:
        mode = input("Your choice (1 or 2): ").strip()
        if mode == "1":
            trials = 100000
            win_switch = simulate(trials, change_choice=True)
            win_stay = simulate(trials, change_choice=False)

            print(f"\nSimulation based on {trials} trials:")
            print(f"Winning when switching: {win_switch * 100:.2f}%")
            print(f"Winning when staying: {win_stay * 100:.2f}%")
            break

        elif mode == "2":
            user_game()

        else:
            print("Please choose 1 or 2.")
