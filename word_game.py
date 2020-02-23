#This is Dane's Word Guessing Game. You can either guess one word, or just the letter to make the full word. You have 8 tries to guess. 
import random


def play_again():
    answer = input('Would you like to play again? yes or no').lower()
    if answer == 'y' or answer =='yes':
        play_game()
    else:
        pass
#This will help get the word from the choices created below.
def get_word():
# I've defined 5 simple words that the user can guess from. 
# These words are not shown as choices during the game, so the user will have to choose randomly one of those 5 words.
    words = ['cat', 'dog', 'python', 'monkey', 'snake']
#This will return the random words, written as a return statement. 
    return random.choice(words)

#This will define get the game going with the play_game function.
def play_game():
#I define the alphabet as a string, so the user has choices only in the alphabet to guess the word.
# There's more sophisticated ways of doing this, but this made the most sense for me on this project.    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    word = get_word()
    letters_guessed = []
    tries = 8
    guessed = False
#This gives the player a clue of how many letters will be in the given word that they need to guess.
#It also gives the player a welcome prompt to begin playing the game.
#To start the game simply type in 'python3 word_game.py' into the terminal.
    print('Welcome to Dane\'s Word Guessing Game.\n')
    print('The word contains', len(word), 'letters.')
    print(len(word) * '_')

#Creating a while loop that will help player input one letter at a time for the game.
    while guessed == False and tries > 0:
#This will tell the player how many tries they have, written as a print statement.       
        print('You have ' + str(tries) + ' tries')
#This tells the player to input either a letter or a full word. This will automatically convert it to lowercase.        
        guess = input('Please enter one letter or the full word.').lower()
#Player inputs a letter. This if statement creates that ability to do so.
        if len(guess) == 1:
#Defined above in the alphabet string, this will tell the player to only enter a letter value, not any other character.           
            if guess not in alphabet:
                print('Please enter a letter only. No other values will work for this game.')
#In this case, if the player has already guessed a letter, this will tell tell the player to guess another letter they have not guessed yet.                
            elif guess in letters_guessed:
                print('You have already guessed that letter before. Try again.')
#This is a statement that will tell the player if the letter they have guessed is not in the word.
            elif guess not in word:
                print('Sorry, that letter is not part of the word :(')
#The append string below will make sure that if there's more than one of the same letter in the words being guessed that it will not penalize the player. 
#Thus making sure they don't loose a try for doing so.              
                letters_guessed.append(guess)
                tries -=1
#This makes sure that only one letter is guessed at a time, even if it's the same letter twice. 
            elif guess in word:
                print('Well done, that letter exists in the word!')
                letters_guessed.append(guess)
            else:
                print('')


#This function defines if the Player guesses the full word.
#If the length of the guess is equal to the word, the player attempted to guess the full word.
        elif len(guess) == len(word):
            if guess == word:
                print('You are amazing! Great job!')
                guessed = True
            else:
                print('Sorry, that is not the word we were looking for.')
                tries -= 1

#This is if the player puts in more or less characters than the full word itslef.   
        else:
            print('Your guess is not the same length as the word the game is looking for. Sorry, try again.')

#This defines the current status of where the player stands in the game, defind below in this string. 
        status = ''
        if guessed == False:
#If the user has not guessed every letter in the word, the letters guessed will still be prited on the screen.            
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '_'
#The remaining space where the letter has not been guessed will have a _ shown where the letter has not been guesed.                    
            print(status)

#If the player has guessed all the letters in the word, or simply the word itself, the player is given a positive prompt on the screen. 
        if status == word:
            print('You are amazing! Great job!')
            guessed = True
#Otherwise if the player has not guessed the word in 8 tries, the player's turn is now over and will need to start over.             
        elif tries == 0:
            print('Sorry you have run out of tries. Better luck next time.')

    play_again()
#This gives the offical green light for the game to begin. 
play_game()