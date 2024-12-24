import os
from colorama import Fore, init
import time

# Initialize colorama
init(autoreset=True)

# Typing effect function
def typing_effect(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# Open link function for Termux
def open_link(url):
    os.system(f"termux-open-url {url}")

# Main menu
def main_menu():
    typing_effect("\n************************************", Fore.GREEN)
    typing_effect("***** Anbu Tools Admin Details *****", Fore.GREEN)
    typing_effect("*************************************", Fore.GREEN)

    while True:
        
        typing_effect("\nChoose an option:", Fore.GREEN)
        
        typing_effect("\n1. Telegram", Fore.GREEN)
        
        typing_effect("\n2. WhatsApp", Fore.GREEN)
        
        typing_effect("\n3. Facebook", Fore.GREEN)
        
        typing_effect("\n4. Messenger", Fore.GREEN)
        
        typing_effect("\n5. Exit", Fore.GREEN)

        choice = input(Fore.GREEN + "\nEnter your choice (1-5): ")

        if choice == "1":
            typing_effect("Opening Telegram ID...", Fore.YELLOW)
            open_link("https://t.me/KakashiByAnbu")

        elif choice == "2":
            typing_effect("Opening WhatsApp...", Fore.YELLOW)
            open_link("https://wa.me/")

        elif choice == "3":
            typing_effect("Opening Facebook...", Fore.YELLOW)
            open_link("https://www.facebook.com/")

        elif choice == "4":
            typing_effect("Opening Messenger...", Fore.YELLOW)
            open_link("https://www.messenger.com/t/")

        elif choice == "5":
            typing_effect("Exiting... Returning!", Fore.GREEN)
            break

        else:
            typing_effect("Invalid choice. Please try again.", Fore.RED)

if __name__ == "__main__":
    main_menu()