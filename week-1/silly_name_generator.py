"""Randomly generate funny sidekick names using Python code
that conforms to established style guidelines."""
import random
import sys

# Steps
#     : Load a list of first names
#     : Load a list of surnames
#     : Choose a first name at random
#     : Assign the name to a variable
#     : Choose surname at random
#     : Assign the name to a variable
#     : Print the name in order and in red front
#     : Ask the user to quit or play again

first = ["Big Burps", "Bill 'Beenie-Weenie'", "Bob 'Stinkbut'", "Boxelder",
         "Chad", "Bowel Noises", "Dennis Clawhammer", "Cleet", "Winston 'Jazz Hands"]

last = ["Appleyard", "Bigmeat", "Bloominshine", "Goodpasture",
        "Henderson", "Jingley-Schmidt", "Kingfish", "Wigglesworth", "Weewax"]

print("Welcome to the Psych 'Sidekick Name Picker'.\n")

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)

    print()
    print("{} {}".format(firstName, lastName), file=sys.stderr)  # convert name variables to string
    print()

    ask = input("Do you want to try again? (Press Enter else n to quit)\n")
    if ask.lower() == 'n':
        break

input("\nPress Enter to exit")

