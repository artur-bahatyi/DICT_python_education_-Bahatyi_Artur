print("HANGMAN")
print("The game will be available soon.")

import random

def play_game():
    words = ["python", "java", "javascript", "php"]
    secret_word = random.choice(words)

    guessed_state = ["-" for _ in secret_word]
    attempts = 8
    guessed_letters = set()

    while attempts > 0:
        print("\n" + "".join(guessed_state))

        letter = input("Input a letter: > ")

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if not letter.islower() or not letter.isalpha():
            print("Please enter a lowercase English letter")
            continue

        if letter in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(letter)

        if letter in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    guessed_state[i] = letter

            if "-" not in guessed_state:
                print(f"You guessed the word {secret_word}!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

    if "-" in guessed_state and attempts == 0:
        print("You lost!")

def main():
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break

if __name__ == "__main__":
    main()