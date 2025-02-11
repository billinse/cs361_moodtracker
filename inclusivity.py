def display_welcome_message():
    """
    Welcome message that reflects the eight Inclusivity Heuristics:
    
    IH #1: Meaningful Purpose - Explains the benefits of mood tracking.
    IH #2: Clear Costs - Informs you that your data is stored locally with no hidden costs.
    IH #3: User Control - You can cancel actions at any time.
    IH #4: Familiar Interactions - Uses a standard CLI menu.
    IH #5: Easy Reversal - Offers clear cancellation options.
    IH #6: Clear Next Steps - Provides instructions at every step.
    IH #7: Multiple Input Modalities - Accepts both numeric and text commands.
    IH #8: Safe Actions - Confirms critical actions like deletion.
    """
    print("Welcome to Mood Tracker!")
    print("This app helps you track your mood and gain insights into your emotional states.")
    print("Your data is stored locally and is never shared, so there are no hidden costs.")
    print("You are in control. If you ever want to cancel an action, simply type 'cancel'.")
    print("Use the menu options displayed by typing the number or the command word ('log', 'view', 'delete', 'exit').")
    print("Important actions such as deleting a previously logged mood will always ask for confirmation.")
    print("Let's get started!\n")
