import sys
from mood_logger import log_mood
from mood_storage import view_moods, delete_mood
from inclusivity import display_welcome_message

def main_menu():

    print("\n=== Mood Tracker ===")


    # Displays a detailed welcome message that clearly explains the purpose, function, and safety features for the user
    display_welcome_message()
    print("Please choose an option:")
    print("1. Log a Mood (or type 'log')")
    print("2. View Past Moods (or type 'view')")
    print("3. Delete a Mood Entry (or type 'delete')")
    print("4. Exit (or type 'exit')")
    
    choice = input("Enter your choice: ").strip().lower()
    return choice

def main():
    while True:
        choice = main_menu()
        if choice in ["1", "log"]:
            log_mood()
        elif choice in ["2", "view"]:
            view_moods()
        elif choice in ["3", "delete"]:
            delete_mood()
        elif choice in ["4", "exit"]:
            print("Exiting the program. Thank you for using Mood Tracker!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to return to the menu.")

if __name__ == "__main__":
    main()
