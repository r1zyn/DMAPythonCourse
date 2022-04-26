from random import choice

options: dict[str, str] = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

choices: list[str] = ["R", "P", "S"]

user: str = input("Enter your choice (R for Rock, P for Paper or S for Scissors): ")
computer: str = options[choice(choices)]

while user.upper() not in options:
    user = input("Please enter a valid choice (R for Rock, P for Paper or S for Scissors): ")
else:
    if options[user.upper()] == "Rock" and computer == "Paper": 
        print("You lost! Paper (computer) beats Rock (you)")
    elif options[user.upper()] == "Rock" and computer == "Scissors":
        print("You won! Rock (you) beats Scissors (computer)")
    elif options[user.upper()] == "Paper" and computer == "Scissors":
        print("You lost! Scissors (computer) beats Paper (you)")
    elif options[user.upper()] == "Paper" and computer == "Rock":
        print("You won! Paper (you) beats Rock (computer)")
    elif options[user.upper()] == "Scissors" and computer == "Rock":
        print("You lost! Rock (computer) beats Scissors (you)")
    elif options[user.upper()] == "Scissors" and computer == "Paper":
        print("You won! Scissors (you) beats Paper (computer)")
    else:
        print("It's a tie! You both chose {}".format(options[user.upper()]))