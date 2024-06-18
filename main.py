from text_processing import count_words, unique_words, count_characters, unique_characters, reverse_string

import text_processing as tp

from tp import count_words as cw
from tp import unique_words as uw
from tp import count_characters as cc
from tp import unique_characters as uc
from tp import reverse_string as rs

# Test string define
test_string = "Hello world hello"

# Using word_count module
print("Word count is:", count_words(test_string))
print("Unique words:", unique_words(test_string))

# Using charcter count module
print("Character count:", count_characters(test_string))
print("Unique Character count:", unique_characters(test_string))

# Using reverse Module
print("Reveresed String:", reverse_string(test_string))

