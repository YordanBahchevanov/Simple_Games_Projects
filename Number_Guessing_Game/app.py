from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f"Guess the number in the range from {lower_num} to {higher_num}")

guesses_left = 3

while guesses_left != 0:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print("Please enter a valid number.")
        continue

    if user_guess > random_number:
        print("The number is lower.")
    elif user_guess < random_number:
        print("The number is higher.")
    else:
        print("You guessed it!")
        break

    guesses_left -= 1

    if guesses_left != 0:
        print(f"You have {guesses_left} guesses left.")

else:
    print(f"You have no more guesses! The number was {random_number}")
