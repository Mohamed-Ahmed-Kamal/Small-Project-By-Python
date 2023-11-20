
import random


while True:

    user = input(
        "Plese Enter your choic / 'r' for rock & 'p' for paper & 's' for scissors => ")

    pc = random.choice(["r", "p", "s"])

    if pc == user:
        print(pc)
        print("tie !!")
    elif (user == "p" and pc == "r") or (user == "r" and pc == "s") or (user == "s" and pc == "p"):
        print(f"Pc Choic :  {pc}")
        print("You Win")
    else:
        print(f"Pc Choic :  {pc}")
        print("You Lost")
