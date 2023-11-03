# Hangman game
# Objective: based on a blank state of a word the user needs to input letters and based on if the letter is in the word 
# reveal the location of the letter/s or put the letter in a string of Tried_letters and count up the Fails variable till 5
# The game ends once all letters are found (blank_word == original_word) or when Fails=5
#step1: put the words in an array and then based on random(0,len(a)) put in in the variable original_word
#step2: once the program has the original_word tranform it so each character is put in an array
#step3: if the user tries to guess an already guessed letter it would give a simple warning to try again 
# step4: insert multiple words separated by difficulty name in a file called as Category_name
# step5: based on the category and difficulty picked at the start by the user through a method find the sequence of words in that
#difficulty range and choose 1 word at random
# (will compare the input to the Tried_letters var, if the letter is there it would send the user back)

import re as regex
import random as RNG

print("Welcome to Hangman")
#Select the category
print("Select the category: 1.Countries, 2.Foods, 3.Games")
check_category_name = True
while check_category_name == True:
        category_name = input("Insert the number of category: ")
        if(category_name == str(1)):
            category_name = "Countries"
            print("Chose: Countries")
            check_category_name = False
        elif (category_name == str(2)):    
            category_name = "Foods"
            print("Chose: Foods")
            check_category_name = False
        elif (category_name == str(3)):    
            category_name = "Games"
            print("Chose: Games")
            check_category_name = False
        else: 
            print("Wrong number inserted. Try again")
            check_category_name = True

#Select the difficulty
print("Select the Difficulty: 1.Easy, 2.Medium, 3.Hard")
check_difficulty_name = True
while check_difficulty_name == True:
        difficulty_start = input("Insert the number of the difficulty: ")
        if(difficulty_start == str(1)):
            difficulty_start = "EASY"
            difficulty_end = "MEDIUM"
            print("Chose: Easy")
            check_difficulty_name = False
        elif (difficulty_start == str(2)):    
            difficulty_start = "MEDIUM"
            difficulty_end = "HARD"
            print("Chose: Medium")
            check_difficulty_name = False
        elif (difficulty_start == str(3)):    
            difficulty_start = "HARD"
            difficulty_end = ""
            print("Chose: Hard")
            check_difficulty_name = False
        else: 
            print("Wrong number inserted. Try again")
            check_difficulty_name= True
#print("Difficulty name is: " ,difficulty_start, difficulty_end)

#create a list with all possible words of a specified difficulty
#and then choose at random one of the words to be used in the game as Original_word
def ChooseTopicAndDifficulty (topic, difficulty_start, difficulty_end):  
    filename_coversion = topic + ".txt"
    #needed to reformat the name of the file outside of the open() method because {topic} is seen as string {topic} in '{topic}.txt'
    with open(filename_coversion,'r') as filename: 
        possible_words=[]
        copy = True   
        for line in filename:
            if line.strip() == difficulty_start:
                copy = False
                continue
            elif line.strip() == difficulty_end:
                break
            elif copy == False:
                #remove the new line from the end of the line in order to be inserted into the Possible_words list
                possible_words.append(line.replace("\n",""))
    filename.close()
    #choose which word will be used for the game by choosing it at random from the List
    random_number= RNG.randint(0,len(possible_words)-1)
    original_word = possible_words[random_number]
    # print("the random number is " + str(random_number))
    # print("the list of possible words is " + str(possible_words))
    # print("the original word is " + str(original_word))
    return original_word


original_word = str.lower(ChooseTopicAndDifficulty(category_name,difficulty_start,difficulty_end))
# need to insert a starting blank character into the list or the game cant start on the 1st loop because its stuck trying
#to compare X to NULL value
tried_letters =['']
fails = 5

# have the characters in a list so its easier to compare the inserted letter from the user to the words chars
separated_letters = list(original_word)
#print(separated_letters)

# intializing the blank_word as blank list and will append _ for each letter in original word
# or append - or blank for the corresponding values
blank_word= []
for letter in range(0,len(original_word)):
    if(original_word[letter] == ' ' ):
        blank_word.append(' ')
    elif (original_word[letter] == '-'):
        blank_word.append('-')
    else:
        blank_word.append('_')
    
print(blank_word)
print("Number of blank letters " + str(blank_word.count("_")))

while ((separated_letters != blank_word) and (fails !=0)):
    # fix incorrect x input to only accept 1 character
    check_x = True
    while check_x:
        x = (input("Insert a character ")) 
        for i in range(0,len(tried_letters)):
            if(str.lower(x) == tried_letters[i]):
                print("Letter already tried")
            else:    
                if len(x)>1:
                    print("Only 1 character allowed")
                elif regex.search("[^a-zA-Z]",x):
                    print("Only characters allowed")
                else: 
                    x = str.lower(x)
                    check_x = False

    # check if the inserted letter is inside the solution word
    found = 0
    for i in range(0,len(separated_letters)):
        if(x == str.lower(separated_letters[i])):
            blank_word[i] = x
            found =  1
    # if the Found flag didnt turned into 1 then the inserted letter will be added to the tried_letters 
    # list and the decrease the remaining attempts available
    if found == 0:
        tried_letters.append(x)
        fails = fails-1
    # if there are no more attempts the a game over message is displayed and it will show all the details and progress
    if(fails ==0):
        print("GAME OVER. no more attempts remaining")
        print("Final score")
        print(blank_word)
        print(tried_letters)
        print("Word was " + str(original_word))
        break
    # shows the current progress after each letter inserted
    print(blank_word)
    print("Tried letters " +str(tried_letters))
    print('Remaining attempts ' + str(fails))
# If the word was found the Game won message is displayed and it will show all the details and progress
else:
    print("GAME WON")
    print("Word was " + str(original_word))
    print("Tried letters " +str(tried_letters))