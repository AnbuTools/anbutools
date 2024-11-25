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
            
            telegram_link = "https://t.me/YourID"  # Replace with your actual Telegram ID or link
            
            typing_effect("Opening Telegram ID...", Fore.YELLOW)
            
            webbrowser.open(telegram_link)
        
        elif choice == "2":
            # Open What's app

            Whatsapp_link ="https://wa.me/number"

            typing_effect("Opening Whatsapp...", Fore.YELLOW)

            webbrowser.open(Whatsapp_link)
        
        elif choice == "3":
            # Open Facebook

            Facebook_link ="https://www.facebook.com/"

            typing_effect("Opening Facebook...", Fore.YELLOW)

            webbrowser.open(Facebook_link)

        elif choice == "4":
            # Open Messenger

            Messenger_link ="https://www.messenger.com/t/"

            typing_effect("Opening Messenger...", Fore.YELLOW)

            webbrowser.open(Messenger_link)
        

        elif choice == "5":
            # Exit

            typing_effect("Exiting... Goodbye!", Fore.GREEN)

            break

        else:
            typing_effect("Invalid choice. Please try again.", Fore.RED)

# Entry point
if __name__ == "__main__":
    main_menu()
