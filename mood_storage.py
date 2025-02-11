import json
import os

MOODS_FILE = "moods.json"

def load_moods():
    if os.path.exists(MOODS_FILE):
        with open(MOODS_FILE, "r") as file:
            try:
                moods = json.load(file)
                return moods
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_all_moods(moods):
    try:
        with open(MOODS_FILE, "w") as file:
            json.dump(moods, file, indent=4)
        return True
    except Exception as e:
        print("Error when saving mood:", e)
        return False

def save_mood(mood_entry):
    moods = load_moods()
    moods.append(mood_entry)
    return save_all_moods(moods)

def view_moods():
    print("\n--- Previous Moods ---")
    moods = load_moods()
    if not moods:
        print("No moods have been logged, yet.")
    else:
        for idx, entry in enumerate(moods, start=1):
            date = entry.get("date", "Unknown Date")
            mood = entry.get("mood", "No Mood")
            details = entry.get("details", "")
            print(f"{idx}. {date} | {mood} | {details}")
    print("\nPress Enter to return to the main menu.")
    input()

def delete_mood():
    print("\n--- Delete a Mood Entry ---")
    moods = load_moods()
    if not moods:
        print("No moods available for deletion.")
        input("Press Enter to return to the main menu.")
        return
    
    # Display moods with index numbers
    for idx, entry in enumerate(moods, start=1):
        date = entry.get("date", "Unknown Date")
        mood = entry.get("mood", "No Mood")
        details = entry.get("details", "")
        print(f"{idx}. {date} | {mood} | {details}")
    
    choice = input("Enter the number of the mood entry you want to delete (or type 'cancel' to abort): ").strip()
    if choice.lower() == "cancel":
        print("Deletion canceled! Returning to the main menu.")
        input("Press Enter to continue.")
        return
    
    try:
        index = int(choice) - 1
        if index < 0 or index >= len(moods):
            print("Invalid entry number! Returning to the main menu.")
            input("Press Enter to continue.")
            return
    except ValueError:
        print("Invalid input! Returning to the main menu.")
        input("Press Enter to continue.")
        return
    
    # Confirm deletion (safe action: confirmation prompt)
    confirm = input(f"Are you sure you want to delete entry #{choice}? (yes/no): ").strip().lower()
    if confirm == "yes":
        moods.pop(index)
        if save_all_moods(moods):
            print("Mood entry deleted successfully.")
        else:
            print("An error occurred while deleting the mood entry.")
    else:
        print("Deletion canceled.")
    input("Press Enter to return to the main menu.")
