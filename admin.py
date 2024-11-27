import webbrowser
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


# Main menu
def main_menu():

    typing_effect("\n************************************", Fore.GREEN)
    typing_effect("***** Anbu Tools Admin Details *****", Fore.GREEN)
    typing_effect("*************************************", Fore.GREEN)

    # Options
    while True:
        typing_effect("\nChoose an option:", Fore.GREEN)
        typing_effect("\n1. Telegram", Fore.GREEN)
        typing_effect("\n2. What'sapp", Fore.GREEN)
        typing_effect("\n3. Facebook", Fore.GREEN)
        typing_effect("\n4. Messenger", Fore.GREEN)
        typing_effect("\n5. Exit", Fore.GREEN)
 
        
        choice = input(Fore.GREEN + "\nEnter your choice (1-5): ")

        if choice == "1":
            # Open Telegram
            
            webbrowser.open("https://t.me/")  # Replace with your actual Telegram ID or link
            
            typing_effect("Opening Telegram ID...", Fore.YELLOW)
            
        
        elif choice == "2":
            # Open What's app

            webbrowser.open("https://wa.me/")

            typing_effect("Opening Whatsapp...", Fore.YELLOW)
        
        elif choice == "3":
            # Open Facebook

            webbrowser.open("https://www.facebook.com/")

            typing_effect("Opening Facebook...", Fore.YELLOW)

        elif choice == "4":
            # Open Messenger

            webbrowser.open("https://www.messenger.com/t/")

            typing_effect("Opening Messenger...", Fore.YELLOW)
        

        elif choice == "5":
            # Exit

            typing_effect("Exiting... Goodbye!", Fore.GREEN)

            break

        else:
            typing_effect("Invalid choice. Please try again.", Fore.RED)

# Entry point
if __name__ == "__main__":
    main_menu()
