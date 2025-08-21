import random
import string
from typing import List, Optional

import nltk

nltk.download('words')




def random_password_generator(lenght = 8, include_numbers = True, include_symbols = True):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation()

    return ''.join(random.choice(characters)for _ in range(lenght))     

random_password_generator(8, True, False) 




def generate_pin(lenght = 8):
    characters = string.digits

    return ''.join(random.choice(characters)for _ in range(lenght))

generate_pin(8)





from nltk.corpus import words
def generate_memorable_password(lenght = 4, seperator = '_', capitalize = False):
    words_list = words.words()    
    password = '_'.join (random.choice(words_list)for _ in range (lenght))
    return password

generate_memorable_password(5)