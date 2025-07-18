import random

# Predefined word list
words = ["apple", "tiger", "chair", "table", "piano"]
word = random.choice(words)
guessed = ["_"] * len(word)
tries = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))

while tries > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        tries -= 1
        print(f"Wrong guess. Tries left: {tries}")

    print(" ".join(guessed))

if "_" not in guessed:
    print("🎉 You won!")
else:
    print(f"😢 You lost! The word was: {word}")
