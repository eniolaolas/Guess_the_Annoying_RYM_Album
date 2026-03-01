import random
#random module
from album_library import albums #key:value

#dictionary of key:();
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

def main(): #contains main body of code
    album_names = random.choice(list(albums.keys()))
    hint_text = albums[album_names]
    answer = album_names
    hint = ["_"] * len(answer) #provides hint for answer/multiply by number of integers
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    print(f"Hint: {hint_text}")


    while is_running:
        display_man(wrong_guesses) #display man after every wrong guess
        display_hint(hint)
        guess = input("Enter a letter:  ").lower()


        if len(guess)!=1:
            print("invalid input I said a letter")
            continue #skips loop
        if len(guess) != guess.isalpha(): # if a guess is a number
            print("never asked for numbers gang")
            continue  # skips loop
        if guess in answer:
            for i in range(len(answer)):
                if answer [i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            if wrong_guesses > 1:
                print ("you're running on thin ice buddy")
        if guess in guessed_letters:
            print("you alr typed "  f"{guess} in fn") #f string puts a function in the print statement
            continue #skips loop

        if "_" not in hint: # if you win
            display_man(wrong_guesses)
            display_answer(answer)
            print ("congrats fn")
            is_running = False
        elif wrong_guesses >= len(hangman_ascii_art) - 1: #too many wrong guesses
            display_man(wrong_guesses)
            display_answer(answer)
            print (f"{answer}" " was the album bro get back on reddit")
            is_running = False #closes function


        guessed_letters.add(guess)

if __name__ == "__main__":
    main()


