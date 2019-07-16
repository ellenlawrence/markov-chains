"""Generate Markov text from text files."""

from random import choice
from collections import defaultdict

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_data = open(file_path).read()

    return file_data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = defaultdict(list)
    
    words = text_string.split()

    for index, word in enumerate(words):
        if index == len(words) - 2:
            break
        chains[(word, words[index + 1])].append(words[index + 2])

    # for chain, words in chains.items():
    #     print(f'{chain}: {words}')

    return chains


def make_text(chains):
    """Return text from chains.""" 

    words = []

    keys_chain = chains.keys() #makes a list of the keys in chains
    keys_chain = list(keys_chain) #made keys_chain into an iterable list
    bigrm = choice(keys_chain) #randomly chooses a tuple from keys
    
    words.append(bigrm[0]) 
    words.append(bigrm[1])

    while len(words) < 50 and bigrm in chains:
        new_word = choice(chains[bigrm])
        words.append(new_word)
        bigrm = (bigrm[1], new_word)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
