import random

def choose_word():
    words = ["taskone","hangman","python", "internship", "codeaplha"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 5 
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("\nWelcome to Hangman Game!!!")
    print("\nMax Attempts is Five Times Guess  a Word.")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("\nYou've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts += 1
            print(f"\nIncorrect! Attempts left: {max_attempts - attempts}")
        
        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print("\nCongratulations!!! You guessed the word.")
    else:
        print(f"\nSorry, you ran out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
