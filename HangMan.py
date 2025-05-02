import random
"""main"""
def main():
    """main"""
    print("Welcome to Hangman!")
    words = ["apple", "banana", "cherry", "orange", "strawberry"]
    vowels = {"a", "e", "i", "o", "u"}
    num = random.randint(0, len(words)-1)
    ans = ["_" if letter not in vowels else letter for letter in words[num]]
    print("Hint: " + " ".join(ans))
    while("_" in ans):
        word = input("Guess a letter: ")
        if word in words[num]:
            print(f"Correct guess: {word}")
            for idx in range(0,len(words[num])):
                if words[num][idx] == word:
                    ans[idx] = word
        else:
            print(f"Incorrect guess: {word}")
        print("Hint: " + " ".join(ans))
    print(f"Congratulations! You guessed the word {words[num]} correctly!")
main()