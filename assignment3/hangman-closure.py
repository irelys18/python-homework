# Task 4
def make_hangman(secret_word):

    guesses =[]

    def hangman_closure(letter):

        guesses.append(letter)

        display = ""

        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"

        print(display)
        return "_" not in display
            
    return hangman_closure
        
secret_word = input("Enter the secret word: ")

game = make_hangman(secret_word)

finished = False

while not finished:

    guess = input("Guess a letter: ")

    finished = game(guess)

print("Congratulations! You guessed the word!")