import string
from words import choose_word
from images import IMAGES



def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word,letters_guessed):
      return True
    return False
  
def ifvalid(user_input):

    if len(user_input) !=1:
        return False
    if not user_input.isalpha():
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    index=0
    guessed_word = ""
    while(index <len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+="_"
        index +=1
    return guessed_word
    

def get_available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left = ""
    for letter in all_letters:
      if letter not in letters_guessed:
        letters_left +=letter
    return letters_left

def get_hint(secret_word,letters_guessed):
    import random
    letters_not_guessed = []
    index=0
    while(index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index+=1
    return random.choice(letters_not_guessed)   

def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print(" ")
    letters_guessed = []
    user_difficulty_choice=input("enter the level in which you want play""\n""a easy""\n""b medium""\n""c hard\n" "a,b,c which level you want: ").lower()
    if user_difficulty_choice=="a":
        remaining_lives = 8
        images = [0,1,2,3,4,5,6,7]
    elif user_difficulty_choice == "b":
        remaining_lives = 6
        images = [0,2,4,5,6,7]

    elif user_difficulty_choice == "c":
        remaining_lives = 4
        images = [1,3,5,7]
    else:
        print('you did not chose any level thats why we will play on easy level: ')
        remaining_lives = 8
    i = 0
    while(remaining_lives > 0):
        user_input_hint = input('do you want hint or not say yes ya no: ')
        if user_input_hint =="yes":
            gussed_letter = get_hint(secret_word,letters_guessed)
            print(gussed_letter)
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: " + available_letters)
            guess_a_letter = input('please guess a letter: ').lower()
            letter = guess_a_letter
            if (not ifvalid(letter)):
                continue

            if letter in secret_word:
                letters_guessed.append(letter)
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                print(" ")
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print(" * * Congratulations, yo`u won! * * ")
                    print("")
                    break

            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                letters_guessed.append(letter)
                pic = IMAGES[i]
                print(IMAGES[pic])
                remaining_lives-=1
                print('You have only',remaining_lives,'Remaining lives')
                i=i+1
        else:
            user_input_hint =="no"
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: " + available_letters)
            guess_a_letter = input('please guess a letter: ').lower()
            letter = guess_a_letter
            if (not ifvalid(letter)):
                continue

            if letter in secret_word:
                letters_guessed.append(letter)
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                print(" ")
                if is_word_guessed(secret_word, letters_guessed) == True:
                    print(" * * Congratulations, you are won! * * ")
                    print("")
                    break

            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                letters_guessed.append(letter)
                pic = images[i]
                print(IMAGES[pic])
                remaining_lives-=1
                print('You have only',remaining_lives,'Remaining lives')
                i=i+1
    
    else:
        print("sorry, you ran out of guesses. The word was" +str(secret_word) + " . ")

secret_word = choose_word()
hangman(secret_word)

