import random

# List of predefined words
words = ["python", "apple", "school", "computer", "banana"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

print("===== Welcome to Hangman Game =====")
print("Guess the word one letter at a time.")

while incorrect_guesses > 0:
    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is fully guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    print("Remaining incorrect guesses:", incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!")
    else:
        incorrect_guesses -= 1
        print("❌ Wrong guess!")

# Game over
if incorrect_guesses == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)