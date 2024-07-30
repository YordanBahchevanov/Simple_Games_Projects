from flask import Flask, render_template, request, jsonify
from random import randint

app = Flask(__name__)

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
guesses_left = 3


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    global random_number, guesses_left
    data = request.get_json()
    user_guess = data.get("guess")

    if user_guess is None or not (lower_num <= user_guess <= higher_num):
        return jsonify({
            "message": "Please enter a valid number.",
            "guesses_left": guesses_left,
            "correct": False,
        })

    if user_guess > random_number:
        message = "The number is lower."
    elif user_guess < random_number:
        message = "The number is higher."
    else:
        message = "You guessed it!"
        guesses_left = 3  # Reset for a new game, if you guess it.
        random_number = randint(lower_num, higher_num)
        return jsonify({
            "message": message,
            "guesses_left": guesses_left,
            "correct": True,
        })

    guesses_left -= 1

    if guesses_left == 0:
        message = f"You have no more guesses! The number was {random_number}"
        guesses_left = 3  # Reset for a new game if you didn't guess it.
        random_number = randint(lower_num, higher_num)
        return jsonify({
            "message": message,
            "guesses_left": 0,
            "correct": False,
        })

    return jsonify({
        "message": message,
        "guesses_left": guesses_left,
        "correct": False,
    })


if __name__ == '__main__':
    app.run(debug=True)

# Old code.
# from random import randint
#
# lower_num, higher_num = 1, 10
# random_number: int = randint(lower_num, higher_num)
# print(f"Guess the number in the range from {lower_num} to {higher_num}")
#
# guesses_left = 3
#
# while guesses_left != 0:
#     try:
#         user_guess: int = int(input('Guess: '))
#     except ValueError as e:
#         print("Please enter a valid number.")
#         continue
#
#     if user_guess > random_number:
#         print("The number is lower.")
#     elif user_guess < random_number:
#         print("The number is higher.")
#     else:
#         print("You guessed it!")
#         break
#
#     guesses_left -= 1
#
#     if guesses_left != 0:
#         print(f"You have {guesses_left} guesses left.")
#
# else:
#     print(f"You have no more guesses! The number was {random_number}")
