# Mood Tracker CLI

This is a basic CLI-based mood tracking program written in Python. It allows users to log their mood, view past mood entries, delete entries, and receive motivational quotes.

## Features

- **Log Your Mood:**  
  Log your mood with optional details. You can cancel the logging process at any time.
  
- **View Past Moods:**  
  See all your saved mood entries stored in a JSON file.

- **Delete a Mood Entry:**  
  Safely delete an entry with a confirmation prompt to prevent accidental deletion.

- **Motivational Quotes:**  
  Receive a random motivational quote after logging your mood.

- **Inclusivity Design:**  
  This program explicitly reflects all eight Inclusivity Heuristics:
  - **IH #1 (Meaningful Purpose):** Explains why mood tracking is valuable.
  - **IH #2 (Clear Costs):** Informs you that your data is stored locally.
  - **IH #3 (User Control):** Allows you to cancel actions.
  - **IH #4 (Familiar Interactions):** Uses a standard CLI interface.
  - **IH #5 (Easy Reversal):** Offers options to cancel or reverse actions.
  - **IH #6 (Clear Next Steps):** Provides clear instructions at every step.
  - **IH #7 (Multiple Input Modalities):** Accepts both numbers and command words.
  - **IH #8 (Safe Actions):** Confirms critical actions like deletion.

- **Quality Attributes Demonstrated:**
  - **Usability:** Simple, clear, and familiar menu and prompts.
  - **Maintainability:** Modular code with functions kept concise and separated by responsibility.
  - **Reliability:** Robust error handling ensures safe file operations and user inputs.

## Files

- `main.py`: Entry point for the CLI program.
- `mood_logger.py`: Handles mood logging.
- `mood_storage.py`: Manages saving, viewing, and deleting mood entries.
- `mood_quotes.py`: Provides random motivational quotes.
- `inclusivity.py`: Displays inclusive messaging and instructions.
- `README.md`: This documentation.

## How to Run

1. Ensure you have Python 3 installed.
2. Open your terminal or command prompt.
3. Navigate to the project root folder.
4. Run the program using:
   ```bash
   python main.py
