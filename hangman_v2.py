#Written in Python 2.7.9
import random 
import sys

#Welcome message
print ("Welcome to Hangman! Guess the word before time's out!") 

#Hangman Word List
wordList = ["pig", "basketball", "cherry", "light", "inchworm", "cheese", "candle", "chair", "eyes", "back", "address", "blowfish",
            "computer", "tissue", "trumpet", "watch", "family", "lemon", "house", "dream", "assassin", "school"]

#Hangman Graphics 
def hangman(guesses):
    if guesses == 0: 
        print "_________         "
        print "|        |        "
        print "|                 "
        print "|                 "
        print "|                 "
        print "|                 "
        print "|____             "
    elif guesses == 1:
        print "_________         "
        print "|        |        "
        print "|        O        "
        print "|                 "
        print "|                 "
        print "|                 "
        print "|____             "
    elif guesses == 2: 
        print "_________         "
        print "|        |        "
        print "|        O        "
        print "|       /         "
        print "|                 "
        print "|                 "
        print "|____             "
    elif guesses == 3:
        print "_________         "
        print "|        |        "
        print "|        O        "
        print "|       /|        "
        print "|                 "
        print "|                 "
        print "|____             "
    elif guesses == 4:
        print "_________         "
        print "|        |        "
        print "|        O        "
        print "|       /|\       "
        print "|                 "
        print "|                 "
        print "|____             "
    elif guesses == 5: 
        print "_________         "
        print "|        |        "
        print "|        O        "
        print "|       /|\       "
        print "|       /         "
        print "|                 "
        print "|____             "
    else:
        print "_________         "
        print "|        |        "
        print "|        O        "
        print "|       /|\       "
        print "|       / \       "
        print "|                 "
        print "|____             "



def main():
    #Choose a random word 
    chooseWord = random.choice(wordList)
    
    blanks = '_' * (len(chooseWord))
    print ("Your word is:" + blanks) #display number of blanks 
    #Storing input information
    attempts = 0 
    alreadyGuessed = []
    correctGuess = []
    while attempts < 7:
        #ask for user input 
        guess = raw_input("Enter a letter: ").lower()
    
    
        #Setting input criteria
        if len(guess) > 1: 
            print ("Only one letter allowed")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz': 
            print ("Please enter letters only")
        elif guess in alreadyGuessed:
            print ("You have already guessed that letter")
        else: 
            pass
        
        #results of a correct guess
        if guess in chooseWord:
            alreadyGuessed.append(guess)
            correctGuess.append(guess)
            for i in range(len(chooseWord)):
                if chooseWord[i] in correctGuess:
                    blanks = blanks[:i] + chooseWord[i] + blanks[i+1:]                
            print hangman(attempts)
            print ('You have guessed: ' + ' '.join(set(alreadyGuessed))) 
            print ('Correct letters: ' + ' '.join(correctGuess))
            print blanks
        
        #results of a wrong guess
        if guess not in chooseWord:
            alreadyGuessed.append(guess)
            attempts += 1 
            print hangman(attempts) 
            print ('You have guessed: ' + ' '.join(set(alreadyGuessed)))
            print ('Correct letters: ' + ' '.join(set(correctGuess))) 
            print blanks
            
        #overall results
        if  blanks == chooseWord:       
            print ("Congratulations! You have won the game. The word is: " + ''.join(chooseWord))
            break
                
        elif attempts >= 6 and blanks != chooseWord: 
            print ("Uh oh! You have run out of chances. The word is: " + ''.join(chooseWord))
            break
            

    #Replay option! 
    print('Do you wish to play again? Y/N')
    response = raw_input().lower().startswith('y')
    
    
    if response == True:
        attempts = 0 
        alreadyGuessed = []
        correctGuess = []
        chooseWord = random.choice(wordList)
        main()
    else: 
        sys.exit()
        
if __name__ == "__main__": #run game
    main()
