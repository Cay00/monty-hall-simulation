import random
import sys


def simulate_game(change_choice: bool) -> bool:
    # Ilość drzwi - DOMYŚLNIE 3
    door_quantity = 3
    # Ukryta nagroda
    prize_door = random.randint(0, door_quantity - 1)
    # Gracz wybiera losowo drzwi
    player_choice = random.randint(0, door_quantity - 1)

    # Prowadzący otwierz drzwi, które:
    # - nie są wybrane przez gracza
    # - nie mają nagrody
    remaining_doors = []
    for door in range(door_quantity):
        if door != player_choice and door != prize_door:
            remaining_doors.append(door)
    door_opened = random.choice(remaining_doors)

    # Jeśli gracz zmienia wybór, wybiera inne drzwi niż wcześniej i niż te otwarte przez prowadzącego
    if change_choice:
        for door in range(door_quantity):
            if door != player_choice and door != door_opened:
                player_choice = door
                break

    # Czy gracz wygrał?
    return player_choice == prize_door


def simulate(n: int, change_choice: bool) -> float:
    wins = sum(simulate_game(change_choice) for _ in range(n))
    return wins / n


def user_game():
    print("Witaj w grze Monty Hall!")
    doors = [0, 1, 2]
    wins = 0
    losses = 0
    round_number = 1

    while True:
        print(f"\n--- Runda {round_number} ---")
        prize_door = random.randint(0, 2)

        while True:
            try:
                player_choice = int(input("Wybierz drzwi (1, 2 lub 3): ")) - 1
                if player_choice in doors:
                    break
                else:
                    print("Podaj liczbę 1, 2 lub 3.")
            except ValueError:
                print("Wprowadź liczbę!")

        # Prowadzący otwiera drzwi bez nagrody i nie wybrane przez gracza
        door_opened = None
        for door in doors:
            if door != player_choice and door != prize_door:
                door_opened = door
                break
        print(f"Prowadzący otwiera drzwi numer {door_opened + 1}. Znajduje się tam przegrana.")

        # Pozostałe zamknięte drzwi
        for door in doors:
            if door != player_choice and door != door_opened:
                remaining_door = door
                break

        # Pytanie o zmianę wyboru
        while True:
            decision = input(f"Czy chcesz zmienić wybór na drzwi numer {remaining_door + 1}? (t/n): ").strip().lower()
            if decision in ("t", "n"):
                break
            else:
                print("Wpisz 't' (tak) lub 'n' (nie).")

        if decision == "t":
            player_choice = remaining_door

        print(f"Twoje ostateczne drzwi to {player_choice + 1}.")
        if player_choice == prize_door:
            print("Gratulacje! Wygrałeś!")
            wins += 1
        else:
            print(f"Niestety, to przegrana. Nagroda była za drzwiami {prize_door + 1}.")
            losses += 1

        total = wins + losses
        percent = (wins / total) * 100 if total > 0 else 0
        print("\nStatystyki:")
        print(f"  - Wygrane: {wins}")
        print(f"  - Przegrane: {losses}")
        print(f"  - Skuteczność: {percent:.2f}%")

        again = input("\nCzy chcesz zagrać ponownie? (t/n): ").strip().lower()
        if again != "t":
            print("Dziękujemy za grę! Do zobaczenia!")
            sys.exit(0)

        round_number += 1


if __name__ == "__main__":
    print("Witaj! Wybierz tryb działania programu:")
    print("1 - Symulacja statystyczna")
    print("2 - Gra interaktywna")

    while True:
        mode = input("Twój wybór (1 lub 2): ").strip()
        if mode == "1":
            trials = 100000
            win_switch = simulate(trials, change_choice=True)
            win_stay = simulate(trials, change_choice=False)

            print(f"\nSymulacja na podstawie {trials} prób:")
            print(f"Wygrana przy zmianie wyboru: {win_switch * 100:.2f}%")
            print(f"Wygrana przy pozostaniu przy wyborze: {win_stay * 100:.2f}%")
            break

        elif mode == "2":
            user_game()

        else:
            print("Wybierz 1 lub 2.")
