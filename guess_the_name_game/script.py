import random 

# creating word_bank 
word_bank = ["app","tiktok","whatsapp","instagram","facebook","twitter"] 
random_word = random.choice(word_bank) 


# creating underscore as placeholder 
guessedWord = ['_'] * len(random_word) 

attempts = 5 
print("Welcome to the Word Guessing Game!")
# loop for the user continously 
while attempts > 0: 
    print("The current word : "+' '.join(guessedWord)) 
    userGuess = input("Guess a letter: ") 
    if userGuess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == userGuess:
                  guessedWord[i] = userGuess
                  print("Great Guess✔!")
                
    else:   
                attempts -= 1
                print("Wrong guess! Attempt left:" ,str(attempts))



    if '_' not in guessedWord: 
            print("\nCongratulation🎉 you guess the word "+random_word ) 
            break

else: 
        print("\n You \'ve run out of the attemps👀! The word was "+random_word)

    