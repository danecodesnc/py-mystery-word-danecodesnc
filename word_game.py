import random

LIST = []


class Game:
    def __init__(self):
        with open('words.txt', 'r') as file:
            data = file.read()
        print('Welcome to Mystery Words!')
        word_list = [word for word in data.split()]
        game_word = random.choice(word_list)
        game_word_len = len(game_word)
        print("")
        

class Player:
    def __init__(self, name)
    self.name = name
    self.number_of_turns_remaining = 



game = Game()











# print("Word will have 5 charactersEnjoy the game ! ", name)

# words = ['apple', 'bananna', 'orange', 'grape', 'mango', 'berry']
    
# # Function will choose one random 
# # word from this list of words 
# word = random.choice(words) 

# guesses = '' 
# # any number of turns can be used here 
# turns = 8

# while turns > 0:
#      # counts the number of times a user fails
#     failed: 0

#     # all characters from the input 
#     # word taking one at a time. 
#     for character in word:

#     # comparing that character with 
#     # the character in guesses 
#     if char in guesses:  
#         print(char) 

# else:  
#     print("_") 
#     # for every failure 1 will be 
#     # incremented in failure 
#     failed += 1 
#  if failed == 0: 
   
#     # user will win the game if failure is 0 
#     # and 'You Win' will be given as output 
#     print("You Win")  
    
#     # this print the correct word 
#     print("The word is: ", word)  
#     break                  
            
   
# class Player
#     pass
