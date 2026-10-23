import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        if num_friends == 1:
            # Якщо один учасник, ділити на (1 - 1) не можна, тож він оплачує весь чек повністю
            friends[lucky_one] = round(total_amount, 2)
        else:
            share = round(total_amount / (num_friends - 1), 2)
            for friend in friends:
                if friend == lucky_one:
                    friends[friend] = 0
                else:
                    friends[friend] = share
    else:
        print("No one is going to be lucky")

        share = round(total_amount / num_friends, 2)
        for friend in friends:
            friends[friend] = share

    print(friends)