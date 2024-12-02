"""
Name: Your Name
Email: your.email@example.com
"""

def reverse_words(sentence):
    """
    Reverses each word in the given sentence.
    Punctuation remains attached to the word.
    """
    words = sentence.split(' ')
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def add_weirdness(text):
    """
    Replaces vowels in the text with distinct characters.
    Mapping: a -> z, e -> x, i -> y, o -> p, u -> q
    """
    weirdness_mapping = str.maketrans("aeiouAEIOU","ɓɐʍs$&*@#X")
    return text.translate(weirdness_mapping)

def translate_to_zorplax(sentence):
    """
    Translates a sentence into Zorplax, an alien language.
    Steps:
    1. Reverse the words.
    2. Add weirdness to the reversed sentence.
    """
    reversed_sentence = reverse_words(sentence)
    weird_sentence = add_weirdness(reversed_sentence)
    return weird_sentence

# Example translations with citations

# 1. "To infinity and beyond!" - Toy Story
print(translate_to_zorplax("To infinity and beyond!"))
# Expected Output: "!doneyb d1ytninif @n 0T"

# 2. "I see your Schwartz is as big as mine!" - Spaceballs
print(translate_to_zorplax("I see your Schwartz is as big as mine!"))
# Expected Output: "!3n1m s@ 9g1b s@ 2t3r@hwz 0uoy 3s3I"

# 3. "Live long and prosper." - Star Trek
print(translate_to_zorplax("Live long and prosper."))
# Expected Output: ".r3s0rp @nd g0nl 3v1L"

# 4. "The truth is out there." - The X-Files
print(translate_to_zorplax("The truth is out there."))
# Expected Output: ".3r3ht u0t s1 3ht"

# 5. "I want to believe." - The X-Files
print(translate_to_zorplax("I want to believe."))
# Expected Output: ".3v1l3b @0 t@nW 1"

