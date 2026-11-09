import random

player1 = "John"
bot = "Jack"


while True:
    input_pencils = input("How many pencils would you like to use:\n")
    if not input_pencils.isdigit():
        print("The number of pencils should be numeric")
    elif int(input_pencils) == 0:
        print("The number of pencils should be positive")
    else:
        num_pencils = int(input_pencils)
        break


while True:
    current_player = input(f"Who will be the first ({player1}, {bot}):\n")
    if current_player in (player1, bot):
        break
    print(f"Choose between '{player1}' and '{bot}'")


while num_pencils > 0:
    print("|" * num_pencils)

    if current_player == player1:

        print(f"{player1}'s turn!")
        while True:
            taken_input = input()
            if taken_input not in ('1', '2', '3'):
                print("Possible values: '1', '2' or '3'")
            elif int(taken_input) > num_pencils:
                print("Too many pencils were taken")
            else:
                taken = int(taken_input)
                break
    else:

        print(f"{bot}'s turn:")
        if num_pencils == 1:
            taken = 1
        elif num_pencils % 4 == 1:

            taken = random.randint(1, 3)
        else:

            taken = (num_pencils - 1) % 4

        print(taken)

    num_pencils -= taken


    if num_pencils > 0:
        current_player = bot if current_player == player1 else player1


winner = bot if current_player == player1 else player1
print(f"{winner} won!")