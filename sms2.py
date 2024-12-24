import os
import time
from colorama import Fore, init

# Colorama initialization (for Windows)
init(autoreset=True)

# Function to simulate typing effect
def typing_effect(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

def main_menu():

    # Main Menu with Green Color and Typing Effect
    while True:
        typing_effect("\nChoose an option:", Fore.GREEN, delay=0.1)

        typing_effect("\n1. Custom SMS", Fore.GREEN, delay=0.1)

        typing_effect("\n2. Balance", Fore.GREEN, delay=0.1)

        typing_effect("\n3. Exit", Fore.GREEN, delay=0.1)

        choice = input(Fore.GREEN + "\nEnter your choice (1-3): ")

        if choice == "1":
            os.system("python custom_sms.py")

        elif choice == "2":
            os.system("python balance.py")

        elif choice == "3":
            typing_effect("\nExiting... Goodbye!", Fore.GREEN)
            
            
            break
        else:
            typing_effect("Invalid choice. Please try again.", Fore.RED)

if __name__ == "__main__":
    main_menu()
