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

def main():
    """Choose names at random from 2 lists of name and print to screen"""
    first = ["Big Burps", "Bill 'Beenie-Weenie'", "Bob 'Stinkbut'", "Boxelder",
             "Chad", "Bowel Noises", "Dennis Clawhammer", "Cleet", "Winston 'Jazz Hands"]

    last = ["Appleyard", "Bigmeat", "Bloominshine", "Goodpasture",
            "Henderson", "Jingley-Schmidt", "Kingfish", "Wigglesworth", "Weewax"]

    print("Welcome to the Psych 'Sidekick Name Picker'.\n")

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print()
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print()

        ask = input("Do you want to try again? (Press Enter else n to quit)\n")
        if ask.lower() == 'n':
            break

    input("\nPress Enter to exit")


if __name__ == "__main__":
    main()
