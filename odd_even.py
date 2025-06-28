import random


def get_player_choice():
    while True:
        try:
            num = int(input("Choose a number between 1 and 10: "))
            if 1 <= num <= 10:
                return num
            else:
                print("Invalid input. Please choose between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")


def play_innings(batter, bowler, target=None):
    score = 0
    print(f"\n{batter} is batting...")
    while True:
        player_num = get_player_choice()
        comp_num = random.randint(1, 10)

        print(
            f"{batter} chose: {player_num if batter == 'Player' else comp_num}"
        )
        print(
            f"{bowler} chose: {comp_num if batter == 'Player' else player_num}"
        )

        if player_num == comp_num:
            print(f"{batter} is OUT!")
            break
        else:
            runs = player_num if batter == "Player" else comp_num
            score += runs
            print(f"Runs scored: {runs} | Total Score: {score}\n")

            if target is not None and score >= target:
                print(f"{batter} has chased the target!")
                break

    return score


# 🎮 Game loop starts
print("🏏 Welcome to Odd-Even Cricket Game!")

first_game = True
last_winner = None  # To store winner of previous game

while True:
    if first_game:
        # Toss setup
        first = input("Do you want to take odd or even? (odd/even): ").lower()

        if first == "odd":
            computer_choice = "even"
            print("You chose Odd! Computer will choose Even.")
        else:
            computer_choice = "odd"
            print("You chose Even! Computer will choose Odd.")

        toss = int(input("Choose a number between 1 and 10 for the toss: "))
        toss_num = random.randint(1, 10)
        print(f"Computer chose: {toss_num}")
        toss_sum = toss + toss_num
        print(f"Toss Sum: {toss_sum}")

        result = "odd" if toss_sum % 2 != 0 else "even"
        toss_winner = "Player" if result == first else "Computer"
        print(f"\n🎲 Toss Result: {toss_winner} wins the toss!")

        if toss_winner == "Player":
            print("You won the toss!")
            choice = input("Choose to bat or bowl first? (bat/bowl): ").lower()
        else:
            print("Computer won the toss and will bat first.")
            choice = "bowl"
        first_game = False

    else:
        print("\nNew Match Starting...")
        if last_winner == "Player":
            print("You won the last match! You get to choose to bat or bowl.")
            choice = input("Choose to bat or bowl first? (bat/bowl): ").lower()
        else:
            print("Computer won the last match and will bat first.")
            choice = "bowl"

    # Match gameplay
    if choice == "bat":
        player_score = play_innings("Player", "Computer")
        print(f"\n💻 Computer needs {player_score + 1} runs to win!")
        comp_score = play_innings("Computer",
                                  "Player",
                                  target=player_score + 1)
    else:
        comp_score = play_innings("Computer", "Player")
        print(f"\n🧍 You need {comp_score + 1} runs to win!")
        player_score = play_innings("Player",
                                    "Computer",
                                    target=comp_score + 1)

    # Final result
    print("\n📊 Final Scores:")
    print(f"Player: {player_score}")
    print(f"Computer: {comp_score}")

    if player_score > comp_score:
        print("🎉 You Win!")
        last_winner = "Player"
    elif player_score < comp_score:
        print("💻 Computer Wins!")
        last_winner = "Computer"
    else:
        print("🤝 It's a tie!")
        last_winner = "tie"

    play_more = input(
        "\nDo you want to play another match? (yes/no): ").lower()
    if play_more != "yes":
        print("🏆 Game Over!")
        print("Thanks for playing!")
        break
