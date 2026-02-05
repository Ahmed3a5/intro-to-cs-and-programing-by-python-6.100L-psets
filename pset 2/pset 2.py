def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    count = 0  # counter to increment if letter in secret in list of letters 
    
    ## loop through the letters of the secret word to know if it in the letters we guessed

    for i in secret_word:
        
        if i in letters_guessed: 
            
            count+=1  ## increment the counter if the letter in secret is in the letters guesseued
    
    # if all letters in the list then the count will equal the lenght of secret word 
    if count == len(secret_word): 
        return True
    else:
        return False
          
           
    

#secret_word = 'apple'
#letters_guessed = ['a' ,'p', 'p' , 'l','e']
#letters_guessed = ['p' , 'l' , 'p', 'e' , 'a']
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#letters_guessed = ['e']
#print(has_player_won(secret_word, letters_guessed))
            


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word =''   

    ## loop throigh the secret word 

    for i in secret_word:

        ## if the letter not in the letters guessed list it will but an * in the new word  in the same position of the letter 

        if i not in letters_guessed:
            
            word += '*'
        
        ## if letter in the letters guessed list we add the letter of the secrete in the new word we retrun
        else: 
            
            word +=i

    return word

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# #print(get_word_progress(secret_word, letters_guessed))



def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word = ''

    ## loop through all letters 
    for i in letters:

    ## if the letter  not in the guessed we add it in the word that will be return this is the letters that will be allowed to enterd in the next guess
        if i not in letters_guessed:
            word+=i
    return word

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))
#   return  'abcdfghjlmnoqtuvwxyz'


def is_valid(char , letters_guessed):
    '''
    Docstring for is_valid
              
    :param char: is a string of len 1 and is already not guessed 
    return boolean of True if the char is represent the chasracteristics 
    false else
    '''
    ## the alll alphabets variabble
    letters = 'abcdefghijklmnopqrstuvwxyz'

    ## check if the char meet the criteria to make it valid as input 

    if len(char) == 1 and char not in letters_guessed and char in letters :
        return True
    else:
        return False
     

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# char = ''
#print(is_valid(char , letters_guessed))


def is_with_help(guess):
    '''
    Docstring for play_with_help
    take a string and return a boolean if it meet the criteria of a string !   
    :param guess: is a string of the criteria 
    '''
    if guess == '!':
        return True
    else:
        return False
    
# guess = '!'
# print(play_with_help(guess))

def play_with_help( with_help, secret_word , letters_guessed , num_guesses):
    '''
    function that return the new word after replace one letter from the secrete word with the hidden letter in guessed progress
    and return the new num_guessed after -3 

    :param with_help:  a bool 
    :param secret_word: the secret word we try to guess
    :param letters_guessed: list of the letters that player guess
    :param num_guesses: take an int of number gueses 
    '''

    if with_help:

        ## know which characters is known and wich is hidden to help the player with it 

        word_progress = get_word_progress(secret_word , letters_guessed)   

        ## make lis of word progrees string 
        word_progress = list(word_progress)

        ## iterate through the word progrees list 

        for i in range(len(word_progress)):

            ##  condition if the letter is hidden  by * 

            if word_progress[i] == '*':

            ## append the one letter of the secret word to the letters guessed and substract 3 from the nums guessed 
                letters_guessed.append(secret_word[i])
                revelead_letter = secret_word[i]
                num_guesses -=3
                  
            ## return the new word and num guessed 
                return  num_guesses , revelead_letter 
            
    return  num_guesses , None
     



# secret_word = 'ahmed hany'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# with_help = True
# num_guesses = 9

# num_guesses = play_with_help(with_help, secret_word , letters_guessed , num_guesses)
# print(num_guesses)


def unique_letters(word:str) -> int :
    '''
    this function take a string and retutn an int of the unique letters in te word
    
    :param word: is a string 
    '''
    letters = []   ## an empty list that will take the letters of the word
    count = 0      ## the counter that count unique letters
    ## iterate through the word 

    for i in word:

    ## see if the letter is in the list 
        if i not in letters:

        ## append letter in the list if not exist 
            letters.append(i)
        ## increment the count if the letter not in list 
            count += 1
    
    
    return count



# word = 'nnnenwpppdammmmdw;;;;;;;;;aw'
# print(unique_letters(word))



def hangman(secret_word , with_help):
    num_guesses = 10 
    letters_guessed = []
    vowels = 'aeiou'

    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is  {len(secret_word)} letters long')
    print(14*'-')

    
    ## looping till ther is no guesses are avaialble 

    while num_guesses > 0:


          ##   know the available letters after take the correct letter form all alphabet 

        available_letters = get_available_letters(letters_guessed)   

            # if he guess correct char know what its position in the word and 
            
        word_progress = get_word_progress(secret_word , letters_guessed) 



        ## messages 

        print(f'you have {num_guesses} guesses left')
        print(f'Available letters: {available_letters}')


        ## take the input from the user 

        guess = input('please guess a letter: ')
        

        ## know if the player want a help or not 

        with_help = is_with_help(guess)

        ## condition if player ask for help or not 

        if with_help:

            if num_guesses >= 3 :

            ## resign new guesse and letters_guessed 
                (num_guesses , letter_revealed ) = play_with_help(with_help , secret_word , letters_guessed , num_guesses)

                ##   know the available letters after take the correct letter form all alphabet 

                available_letters = get_available_letters(letters_guessed)   

                # if he guess correct char know what its position in the word and 
                
                word_progress = get_word_progress(secret_word , letters_guessed) 

                print(f'letter revealed: {letter_revealed}')
                print(word_progress)
                print(14*'-')

                if has_player_won(secret_word , letters_guessed): 

                    total_score = (num_guesses+ (4*unique_letters(secret_word)) + (3*len(secret_word)))
                
                    print('Congratulations, you won!')
                    print(f'Your total score for this game is: {total_score}')

                ##  break if the 2 word match an the player win  ## if the the player guess the word correct 

                    break


            else:
                
                print(f'Oops! Not enough guesses left: {word_progress}')
                print(14*'-')

            
        else:
        

            # know if the character entered by the user meet the criteria or not 

            if is_valid(guess , letters_guessed):


                ##  append input in letters that is guessed  

                letters_guessed.append(guess)

                # know if the character is in the word or not
                if guess in secret_word:  


                    word_progress = get_word_progress(secret_word , letters_guessed)


                    print(f'Good guess: {word_progress}')
                    print(14*'-')
        

                else:


                    print(f'Oops! That letter is not in my word: {word_progress}')
                    print(14*'-')
            

                    ## condition if the incorrect guess is voewls or not to decrease guesses by 1 or 2

                    if guess not in vowels:

                        ### decrement the number of guesses available by 1 if guess not vowel

                        num_guesses-=1

                    else:

                        ## decreease by 2 if guess is vowel

                        num_guesses -=2


            else:
                print('Oops! That is not a valid letter. Please input a letter from')
                print(f'the alphabet: {word_progress}')
                print(14*'-')


            #  to know if the player guess all the characters of all the word before finish all guesses numbers 
            if has_player_won(secret_word , letters_guessed): 

                total_score = (num_guesses+ (4*unique_letters(secret_word)) + (3*len(secret_word)))
                
                print('Congratulations, you won!')
                print(f'Your total score for this game is: {total_score}')

                ##  break if the 2 word match an the player win  ## if the the player guess the word correct 

                break

            elif not has_player_won(secret_word , letters_guessed) and num_guesses == 0:

                print(f'Sorry, you ran out of guesses. The word was {secret_word}')

                
                

            
        



secret_word = 'wildcard'
with_help = False
hangman(secret_word , with_help)

    
            








