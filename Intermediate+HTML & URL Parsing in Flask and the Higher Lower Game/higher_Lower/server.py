import random

from flask import Flask
from random import Random
app = Flask(__name__)

@app.route('/')
def generate_number():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'width= 400 height= 500/>")

@app.route('/<int:guess>')
def guess_the_number(guess):
    random_number = random.randint(0,10)
    if guess == random_number:
        return ("<h1 style ='color:green'>You found me!</h1>"
                "<img src= 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width = 400 height= 500/>")

    elif guess < random_number:
        return ("<h1 style = 'color:red'>Too Low, try again!</h1>"
                "<img src= 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width = 400 height= 500/>")
    else:
        return ("<h1 style = 'color:purple'>Too high, try again!</h1>"
                "<img src= 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width = 400 height= 500/>")


if __name__ == "__main__":
    app.run(debug=True)