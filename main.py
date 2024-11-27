import os
import time
from colorama import Fore, init
import pyfiglet

# Colorama initialization (for Windows)
init(autoreset=True)

# Function to simulate typing effect
def typing_effect(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(color + char, end="", flush=True)
        time.sleep(delay)
    print()

# Function to play sound using termux-media-player
def play_sound(file_path):
    try:
        os.system(f"termux-media-player play {file_path}")
    except Exception as e:
        print(f"Error playing sound: {e}")

def main_menu():
    # Welcome Screen with ASCII Art and Typing Effect
    ascii_art = pyfiglet.figlet_format("ANBU TOOLS", font="slant", width=200)
    typing_effect(ascii_art, Fore.GREEN)

    # Play Welcome Sound
    typing_effect("Loading Please Wait ............", Fore.GREEN, delay=0.1)

    try:
        play_sound("welcome.wav")  # Replace with your audio file
    except Exception as e:
        print(f"Error playing sound: {e}")

    # Main Menu with Green Color and Typing Effect
    while True:
        typing_effect("\nChoose an option:", Fore.GREEN)

        typing_effect("\n1. SMS", Fore.GREEN)

        typing_effect("\n2. Call", Fore.GREEN)

        typing_effect("\n3. Custom SMS", Fore.GREEN)

        typing_effect("\n4. SMS & Call Mixed", Fore.GREEN)

        typing_effect("\n5. Admin Details", Fore.GREEN)

        typing_effect("\n6. Exit", Fore.GREEN)

        choice = input(Fore.GREEN + "\nEnter your choice (1-6): ")

        if choice == "1":
            os.system("python sms.py")

        elif choice == "2":
            os.system("python call.py")

        elif choice == "3":
            os.system("python custom_sms.py")

        elif choice == "4":
            os.system("python sms_call.py")

        elif choice == "5":
            os.system("python admin.py")

        elif choice == "6":
            typing_effect("\nExiting... Goodbye!", Fore.GREEN)
            break
        else:
            typing_effect("Invalid choice. Please try again.", Fore.RED)

if __name__ == "__main__":
    main_menu()
