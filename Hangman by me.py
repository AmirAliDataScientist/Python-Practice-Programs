import random
import os

print ('Welcome to Hangman Game! ')

words_list = ['Apple', 'Orange', 'Banana', "aardvark", "baboon", "camel"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 1 

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(words_list).lower() #Select a random word
print(random_word)

length = len(random_word) #length of the random word for future use
display = [] # An empty list for future use
for _ in range(length): #for loop to print block equal to choosen word length
    display += '_' 
print(display)

lives = 6 #variable to track lives
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False #varibale where while loop will depend
while not end_of_game: #itteration statement
    user_guess = input ('Enter a letter to guess the word: ')
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for letter in range (len(random_word)): #for loop to check if the guessed letter is matched with choosen letter
        #print(letter)
        if user_guess == random_word[letter]:
             display [letter] = user_guess #change the right letter at right position in the blank list
    print(display)
    
    if user_guess not in random_word: # reduce life if the guessed word is not matched 
        lives -=1
        if lives ==0:
            end_of_game = True # end game if user use all six lifes
        print (stages[lives])
        #Put live stages
    if '_' not in display:
        end_of_game = True
        print('You Win!')




    