import random
from album_library import albums


hangman_ascii_art = {0:("    "
                        "    "
                        "    "), #making the hangman
                     1:(" o ",
                        "   ",
                        "   "),
                     2:(" o ",
                        " | ",
                        "   "),
                     3:(" o ",
                        " |-",
                        "   "),
                     4:(" o ",
                        "-|-",
                        "   "),
                     5:(" o ",
                        "-|-",
                        "// "),
                     6:(" o ",
                        "-|-",
                        "/ \\")
                     }
for line in hangman_ascii_art [6]:
    pass

def display_man(wrong_guesses): #function to show hangman
    for line in hangman_ascii_art[wrong_guesses]:
        print(line)

def display_hint(hint): #function to show hint
    print("".join(hint))


def display_answer(answer): #function to show answer
    print("".join(answer))


def main():
    album_names = random.choice(list(albums.keys()))
    hint_text = albums[album_names]
    answer = album_names
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    hint = []
    for char in answer:
        if char == " ":
            hint.append(" ")  # Show spaces as spaces
        else:
            hint.append("_")  # Show letters as blanks
    print(f"Hint: {hint_text}")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter:  ").lower()


        #rules for which characters could be valid inputs
        # Input validation FIRST
        if len(guess) != 1:
            print("invalid input I said a letter")
            continue

        if len(guess) != guess.isalpha(): # if a guess is a number
            print("never asked for numbers gang")
            continue

        # Check if already guessed BEFORE processing
        if guess in guessed_letters:
            print("you alr typed "  f"{guess} in fn")
            continue

        # Add to guessed letters RIGHT AFTER validation
        guessed_letters.add(guess)

        # Now process the guess
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            if wrong_guesses > 1:
                print("you're running on thin ice buddy")

        # Check win/lose conditions (this was being skipped before!)
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("congrats bro")
            is_running = False
        elif wrong_guesses >= len(hangman_ascii_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"{answer} was the album bro get back on reddit")
            is_running = False




if __name__ == "__main__":
    main()