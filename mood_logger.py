from datetime import datetime
import mood_quotes
import mood_storage

def log_mood():
    print("\n--- Log a Mood ---")
    print("You can type 'cancel' at any prompt to cancel logging a mood!")
    
    mood = input("How are you feeling today? ")
    if mood.strip().lower() == "cancel":
        print("Mood logging canceled! Returning to the main menu.\n")
        return

    details = input("Would you like to add more details? (Press Enter to skip or type 'cancel' to abort): ")
    if details.strip().lower() == "cancel":
        print("Mood logging canceled! Returning to the main menu.\n")
        return
    
    # Gets the current date in month/day/year format.
    date_str = datetime.now().strftime("%m/%d/%Y")
    entry = {
        "date": date_str,
        "mood": mood,
        "details": details
    }
    
    # Savew the mood entry (the data is stored locally, with no hidden costs)
    if mood_storage.save_mood(entry):
        print("Your mood has been saved locally. Thank you!")
    else:
        print("There was an error when saving your mood.")
    
    # Displays a random motivational quote
    quote = mood_quotes.get_random_quote()
    print("\nHere's a motivational quote for you:")
    print(f"\"{quote}\"\n")
    input("Press Enter to return to the main menu.")
