def count_words(text):
    words = text.split()
    return len(words)

def unique_words(text):
    words = text.lower().split()
    return set(words)

# print(unique_words("Good morning everyone, and welcome to the session. This session is good."))
# print(count_words("Good morning everyone, and welcome to the session. This session is good."))

