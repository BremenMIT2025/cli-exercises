import random

print(
    "Welcome to the game! This is a number guessing game, and you have 10 chances to guess the number. Let's start!"
)

num = random.randrange(100)

for i in range(10):
    while True:
        guess = input("Please enter your guess. Press Enter to submit: ")
        try:
            guess_num = int(guess)
            break
        except:
            print("User input was not a valid number (must be an integer).")
            continue
    if guess_num == num:
        print(f"You were correct! Guessing game won using {i+1} attempts.")
        break
    if guess_num < num:
        print("Your guess is too low. Try again.")
    elif guess_num > num:
        print("Your guess is too high. Try again.")
