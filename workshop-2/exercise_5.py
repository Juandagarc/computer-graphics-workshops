# Exercise 5: Word Frequency Counter
# Objective: Create a function that counts the frequency of each word in a text string

def count_words(text):
    """Counts the frequency of each word in a text"""
    text_lower = text.lower()

    punctuation_marks = ".,;:!?¿¡\"'()[]{}+-*/=<>@#$%^&"
    for mark in punctuation_marks:
        text_lower = text_lower.replace(mark, "")

    words = text_lower.split()

    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies

def frequency_exercise():
    """Word frequency counter demonstration exercise"""
    text = "Python is a programming language. Python is easy to learn and Python is powerful."
    print(f"Text: {text}")
    word_frequencies = count_words(text)
    print(f"\nWord frequency:")
    for word, frequency in word_frequencies.items():
        print(f"'{word}': {frequency}")
