import time
import random

# List of sentences for typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The only thing we have to fear is fear itself.",
    "I think, therefore I am.",
    "Time and tide wait for no man.",
    "Knowledge is power."
]

def choose_sentence():
    return random.choice(sentences)

def typing_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter to start...")

    sentence = choose_sentence()
    print("\nType the following sentence as quickly and accurately as you can:")
    print(f"\n{sentence}\n")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    time_in_minutes = elapsed_time / 60
    word_count = len(sentence.split())
    wpm = word_count / time_in_minutes

    accuracy = sum(1 for a, b in zip(sentence, user_input) if a == b) / len(sentence) * 100

    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Your typing speed: {wpm:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

    if wpm >= 60:
        print("\nBeautiful, you are fast.")
    elif 30 <= wpm < 60:
        print("\nGood, but you can do better.")
    else:
        print("\nGot to improve!")

if __name__ == "__main__":
    typing_test()
