import random


class Game:
    def __init__(self):
        self.player = ("Dane")

    def play_game(self):
        #started with a shorter list to get the game going. Now I am using the list that came with the homework.
        with open('words.txt', 'r') as file:
            data = file.read()
        print("")
        print('Welcome to "Dane Guesses Mystery Words!')
        print("")
        print("Guess one letter at a time until you have guessed the entire word. You have 8 tries to guess the correct word. Good luck. ""/n")
        word_list = [word for word in data.split()]
        game_word = random.choice(word_list)
        game_word = str(game_word)
        game_word = game_word.lower()
        print(game_word)
        game_word_len = len(game_word)
        game_word_letters = list(game_word)
        print("This will eventually be hidden:")
        print (game_word_letters)
        underscore_list = ["_"] * game_word_len
        print("")
        print(f"Your word has {game_word_len} some letters:")
        print("")
        print (self.list)to_string(underscore.list))
        print("")
        while "_" in underscore_list:
            playing = True
            while playing:
                choice = input("Guess a letter:")
                choice.lower()
                if choice.isalpha() and len(choice)==1:
                if choice in underscore_list:
                    print("You've already chosen a letter, please continue.")
                elif choice in game_word_letters:
                    index_position_list = self.get_index_positions(game_word_letters,choice)
                    choice_list = len(index_posotion_list)*[choice,]
                    for (index, choice) in zip(index_position_list, choice_list):
                        underscore_list[index] = choice
                    print(self.list_to_string(underscore_list))
                    print("Great job!")
                else:
                    self.player.number_of_turns_remaining -=1
                    print(f"That's incorrect. You have {slef.player.number_of_turns_remaining} turns")
                
              else:
                  print("Please enter characters A-Z, and only one letter at a time.")  
                if self.player.number_of_turns == 0:
                    self.start_over()
                break
            playing = False
            self.start_over_win()

    def get_index_positions(self, game_word_letters, choice):
        index_pos_list = []
        index_pos = 0
        while True: 
            try:
                index_pos = game_word_letters.index(choice, index_pos)
                index_pos_list.append(index_pos)
                index_pos += 1
            except:
                break
            return index_pos_list



    def list_to_string(self, underscore_list):
        str1 = " "
        return (str1.join(underscore_list))
    
    
    def start_over(self):
        print ("Sorry, you're are out of guesses.")
        play_again = input ("Press R to (R)estart. Press anything to exit. ")
        play_again.lower()
        if play_again == "r"
                Game().play_game()
            else:
                exit()

    def start_over_win(self):
        print("Great job! You win!")
        play_again = input ("Press R to (R)estart"). Press anything to exit. ")
        play_again.lower()
        if play_again == "r"
                Game().play_game()
            else:
                exit()


class Player:
    def __init__(self, name):
        self.name = name 
        self.number_of_turns_remaining = 8




game = Game()
Game().play_game()











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
