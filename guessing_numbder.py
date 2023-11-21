import random

attempts_list = []


def show_score():
    if not attempts_list:
        print("There's currently no high score, start plaing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


attempt = 0
rand_number = random.randint(1, 10)

print("Hello player! Welcome to the guessing game!")
player_name = input("What's your name? ")
want_play = input(
    f"Hi, {player_name}, would you like to play the guessing game?"
    " (Enter yes/no): "
).lower()

if want_play == "no":
    print("That's cool, Thanks!")
    exit()
else:
    show_score()

while want_play == "yes":
    try:
        guess = int(input("Pick a number between 1 and 10: "))
        if (guess < 1 or guess > 10):
            raise ValueError("Please guess a number within the given range")

        attempt += 1

        if (guess == rand_number):
            print("Nice, you got it!")
            print(f"It took you {attempt} attempts!")
            want_play = input(
                "Would you like to play again (Enter Yes/No): ").lower()

            attempts_list.append(attempt)

            if want_play == "no":
                print("That's cool, have a good day.")
            else:
                attempt = 0
                rand_number = random.randint(1, 10)
                show_score()
                continue
        elif (guess > rand_number):
            print("It's lower!")
        else:
            print("It's higher!")
    except ValueError as err:
        print(err)
