import random

WORDFILE = "dictionary/countries.txt"

def get_random_word():
    """Get a random word from the wordlist using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open(WORDFILE, 'r') as f:
        words = f.readlines()
        random_index = random.randint(0,len(words)-1)
        curr_word = words[random_index].strip().lower()
    f.close()
    return curr_word