import os
from turtle import clear
from destinations import add_destination, list_destinations, remove_destination

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to return to the main menu...")

def main_menu():
    print("Travel Planner - Destination Manager\n")
    print("Please select an option (1 - 4):")
    print("1) Add a destination")
    print("2) View destination list")
    print("3) Remove a destination")
    print("4) Exit")

def main():

    while True:
        main_menu()
        user_input = input("\nEnter your choice (1 - 4): ").strip()

        if user_input == "1":
            clear_screen()
            add_destination()
            pause()
        elif user_input == "2":
            clear_screen()
            list_destinations()
            pause()
        elif user_input == "3":
            clear_screen()
            remove_destination()
            pause()
        elif user_input == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid selection")
            pause()

if __name__ == "__main__":
    main()
