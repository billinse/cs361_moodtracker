import random

QUOTES = [
    "A ship is safe in harbor, but that's not what ships are for.",
    "Worrying is like paying interest on a debt you may never owe.",
    "Not all those who wander are lost.",
    "The mighty oak tree was once a nut that stood its ground.",
    "We all make choices in life, but in the end our choices make us."
    "You miss 100 percent of the shots you don't take."
    "Whatever you are, be a good one."
]

# Pulls a quote randomly for the mood logger file.
def get_random_quote():
    return random.choice(QUOTES)
