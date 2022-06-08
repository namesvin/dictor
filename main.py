# Main python file
import json
import os
import time

# Define clear function
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Define lookup function
def lookup(wordin):
    dict = json.load(open('dict.json'))
    for word, definition in dict.items():
        if word == wordin:
            clear()
            print("Definition found!")
            time.sleep(0.5)
            clear()
            print("Word: " + word)
            print("Definition:\n" + definition)
            input("Press enter to continue!")
            return
    print("Word not found!")
    time.sleep(1)

# Main menu
while True:
    clear()
    menu = input("Welcome to Dictor!\n1. L for word lookup\n2. Q to quit\nSelection: ")
    if menu == "L":
        clear()
        wordin = input("Enter the word you want me to search: ")
        lookup(wordin)
    elif menu == "Q":
        break
    else:
        print("Invalid selection!")