import math

##  problem 0 get list from text  ##

def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
 
    word_list = input_text.split()
    return word_list
    
# text = 'hello world, hello'
# print(text_to_list(text))


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """

    
    frequent_dict = {}      ## define the dictionary we return 

    ## if the formar parameter is str 

    if type(input_iterable) == str:

        ## convert this string into list
        word_list = text_to_list(input_iterable)

        ## recurrsion through our function 
        return get_frequencies(word_list) 
    
    ## if the paramter is list 
    else:

        ## iteration is the list 
        for i in input_iterable:

            ## i is the item of the list itself
            ## condition if the items in list not in the dictionary
            if i not in frequent_dict:

                ## add the item in the list with the value of occurence 
                frequent_dict[i] = 1

            ## if the item is in dict
            else:

                ## increment the value of the item in the dict 
                frequent_dict[i] +=1
    
    ## return the dict 
    return frequent_dict

## unit test of the function 

# text = 'hello world hello world'
# text_list = ['hello' , 'world' , 'hello' ]
# print(get_frequencies(text)) 
# print(get_frequencies(text_list)) 


### Problem 2: Letter Frequencies ###

def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    letters_dict = {}
    
    ## iterate through the word

    for i in range(len(word)):
        ## see if the letter not in the dict
        if word[i] not in letters_dict:
            ## add the letter to the dict with its value 1
            letters_dict[word[i]] = 1
        ## the letter already in the dict 
        else:
            ## incremnt the value of the letter in the dict
            letters_dict[word[i]] +=1

    ## return the dict 
    return letters_dict

## unit test of funtion 

# word = 'helllllllllooooooooooo'
# print(get_letter_frequencies(word))

# Tests Problem 2: Get Letter Frequencies

# freq1 = get_letter_frequencies('hello')
# freq2 = get_letter_frequencies('that')
# print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}



def count_word(word , words_list):
    """
    word is string the
    words_list is list of words

    return 
    how many times of word in words_list count
    0 if word not in words_list  
    """
    ## get word frequences in the words_list if words is text 
    if type(words_list) == str:

        words_dict = get_frequencies(words_list) 
  
    ## if word in list return the count of it 
    else: 
        if word in words_dict:
            ## return the the count of word in the dict 
            return words_dict[word]
        ## if word not in the list 
        else:
            return 0

## unit test of the function 

# words = 'i want to be happy in in programing and medicine the 2 together just happen i do not want to be ' \
#         'fauileer'
# word = 'in'
# print(count_word( word,words))


def unique_elements(L1 , L2):
    """ L1 is list of words or letters 
        L2 is other list of words or letters 

        return 
        a new list of the unique words of the 2 lists 

    """

    unique_list = []   ## empty list of uniques 
    ## iterate through the first list 
    for i in L1:
        ## if the element not in the unique we add it 
        if i not in unique_list:
           unique_list.append(i)
    ## iterate through the second list 
    for i in L2:
        ## if elemnent not in unique we add it 
        if i not in unique_list:
            unique_list.append(i)

    ## return unique list 
    return unique_list

##    \\\\\\\\\\ another solution  recursion    \\\\\\  

# def unique_list_mod(L ,unique_list):
#     if len(L)==1:
#         if L[0] not in unique_list:
#             unique_list.append(L[0])
#     else:
#         if L[0]  in unique_list:
#             return unique_list_mod(L[1:], unique_list)   
#         else:
#             unique_list.append(L[0])
#             return  unique_list_mod(L[1:] , unique_list)
#     return unique_list
            

# L1 = ['hello' , 'hello' , 'world' , 'in' , 'me' , 'world' , 'ahmed']
# L2 = ['hello' , 'hello' , 'world' , 'in' , 'me' , 'world' , 'mohamed' ]
# unique_list = []
# print(unique_list_mod(L1 , unique_list))
# print(unique_list_mod(L2 , unique_list))
# print(unique_elements(L1 , L2))


## find frequent difference 

def freq_differ(word,dict_1 ,dict_2):
    """ word is the word we calc difference of it in w dictionaries 
        dict1 is a dict of elements
        dict2 is a list of elements 
        
        return 
        an absoulte value of the difference between the frequencies of word in the 2 dictionaries 

    """
    ## if word only in dict 1 we take the frequency from it 
    if word in dict_1 and word not in dict_2:
        count = dict_1[word]
    ## if word only in dict 2 take the frequency from it 
    elif word in dict_2 and word not in dict_1:
        count = dict_2[word]
    ## if count in the 2 dict take the absolute value of the differnce 
    else:
        count = abs((dict_1[word] -dict_2[word]))
    ## return count 
    return count

        

## unit test 

# dict_1 = {'ahmed':2 , 'ashraf': 3 , 'ammer': 4 , 'samir':9}
# dict_2 = {'ahmed': 5 , 'ameeer':6 , 'ashraf':5 , 'mohamed':4}
# print(freq_differ('samir' , dict_1 ,dict_2))
    


def freq_totals(word , dict_1 ,dict_2):
    """
        word is string 
        dict_1 is dictionary of words and its frequencies 
        dict_2 is dictionary of words and its frequencies

        return the totals of word frequencies in the 2 dictionaries 
    """
    ## if the word only in the dict_1 take the frequency from it 
    if word in dict_1 and word not in dict_2:
        count = dict_1[word]
    ## if the word only in the dict 2 take the frequency from it 
    elif word in dict_2 and word not in dict_1:
        count = dict_2[word]
    ## if the word in the 2 dictionaries we add the 2 frequencies 
    else:
        count = dict_1[word] + dict_2[word]
    ## return the count 
    return count 


## unit test of the function 

# dict_1 = {'ahmed':2 , 'ashraf': 3 , 'ammer': 4 , 'samir':9}
# dict_2 = {'ahmed': 5 , 'ameeer':6 , 'ashraf':5 , 'mohamed':4}
# print(freq_totals('ahmed' , dict_1 ,dict_2))
    




### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    ## our variables 

    sum_all_diferences = 0
    sum_all_totals = 0

    ## define the unique list of the words in the 2 dictionaries 

    unique_list = unique_elements(freq_dict1, freq_dict2)

    ## iterate through the unique list to take the  difference frequency and totals frequencies  of all elements 

    for i in unique_list:
        ## i is the element itself in the list 
        ## calculate the sum of all differnces and increment the summof all by it 
        
        sum_all_diferences += freq_differ(i , freq_dict1 , freq_dict2)

        ## calcualte the frequent totals of all elements and increment the summ all totals by it 
        sum_all_totals += freq_totals(i , freq_dict1 , freq_dict2)

    ## calculate the similarity score

    similarity_score = 1 - (sum_all_diferences/sum_all_totals)
    ## round the similarity score to 2 decimle places 
    similarity_score = round(similarity_score , 2)

    return similarity_score


## unint test of function 

# dict_1 = {'ahmed':2 , 'ashraf': 3 , 'ammer': 4 , 'samir':9 , 'saad':2}
# dict_2 = {'ahmed': 5 , 'ameeer':6 , 'ashraf':5 , 'mohamed':4 , 'serum': 3}
# print(calculate_similarity_score(dict_1 ,dict_2))

# word1_freq = get_letter_frequencies('toes')
# word2_freq = get_letter_frequencies('that')
# word3_freq = get_frequencies('nah')
# word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
# word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
# word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
# print(word_similarity1)  # should print 1.0
# print(word_similarity2)  # should print 0.25
# print(word_similarity3)  # should print 0.0



def get_most_frequent_words(freq1 , freq2):
    """
        freq 1 : is a dictionary of frequent words 
        freq 2 : is the second dictionary of frequent words 

        return 
        a list of most frequent word in the two dictionaries 
        if the word in the two dictionaries the frequency of the word is combined of the two dictionaries 
        if two words have same greater freqency return them alphabitically 
    """
    
    ## take the unique elements ogf the 2 dictionaries 
    unique_list = unique_elements(freq1 , freq2)

    ## temporary variables for hold most word 
    temp_freq = 0
    word = ''

    ## the most frequent list 

    most_frequent_list = []

    ## temp dictionary for equal words 

    temp_dict = {}

    ## iterate through the unique list

    for elem in unique_list:

        ## count the frequency of the elem in the 2 dictonary if in them  or if in one dict  
        count = freq_totals(elem , freq1 , freq2)

        ## if the count greater than the temp _freq assign the it to it 
        if count > temp_freq:

            temp_freq = count
            word = elem
        ## if two words have the same freqency we add to the dictionary 
        elif count == temp_freq:

            temp_dict[elem] = count
    
    most_frequent_list.append(word)

    ## final comparison of the words 
        
    if temp_dict != {}:  ## if the temp dict not empty 
        ## itereae through the dictionary 
        for elem in temp_dict:
            ## if the frequency of the word in it equall to the larger frequency in the two dictionaries 
            if temp_dict[elem] == temp_freq:
                ## append the elemnt of the dictionary in the list 
                most_frequent_list.append(elem)      
    
    most_frequent_list.sort()

    ## return the list 
    return most_frequent_list


# Tests Problem 4: Most Frequent Word(s)
# freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
# most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
# print(most_frequent)      # should print ["hello", "world"]

# dict_1 = {'ahmed':2 , 'ashraf': 3 , 'ammer': 4 , 'samir':9 , 'saad':2}
# dict_2 = {'ahmed': 5 , 'ameeer':9 , 'ashraf':5 , 'mohamed':9 , 'serum': 3}
# most_frequent = get_most_frequent_words(dict_1, dict_2)
# print(most_frequent)



## Problem 5: Finding TF-IDF ###

def get_tf(file_paths):
    """
    file paths is file contain of text of strings 
    return a dictionary of word mapping to its tf 
            tf(word) = number of time words occur in file path / the total words in the path     
    """

    ## get words frequences from the file path 

    word_freq = get_frequencies(file_paths)

    ## text to list to calculate the number of words in the text 
    all_words_sum = len(text_to_list(file_paths))

    ## the new dictionary we retrun for each word and its tf 

    tf_dict = {}

    ## iterate through the word freq dictionary 

    for elem in word_freq:
        ## calculate the 
        tf_dict[elem] = word_freq[elem]/all_words_sum
    

    return tf_dict

## unit test 

# file_paths = " The sun was bright, bright in the sky"
# "The wind was soft, soft on my face."
# "I walked and walked, thinking and thinking"
# "about dreams, dreams that never fade" 

# print(get_tf(file_paths))

# tf_text_file = 'hello world hello'
# tf = get_tf(tf_text_file)
# print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}


def extend_list(L):
    """
    return the list extended with elements of sublists
    
    :param L: is alist of sublists
    """

    if len(L)==1:
        if type(L[0]) == list:
            return extend_list(L[0])
        else:
            return [L[0]]
    else:
        if type(L[0]) == list:
            return extend_list(L[1:]) + extend_list(L[0])
        else:
            return extend_list(L[1:]) + [L[0]]
        
## unit test

# L = [['ahmed' , 'ameer'] , ['ashraf' , 'samir'] , ['mohamed']]
# print(extend_list(L))


def find_word_count(word , L):
    """
    return how many times the word appear in the sublists without the repeated element in the same sublist 

    :param word: is a string that we should find 
    :param L: is a list of sublists or list of multiple element string 
    """
    ## if the L is str we convert it to list of words
    if type(L) == str:
        L = text_to_list(L)
    ## if the len list is one element 
    if len(L)==1:
        ## if we find this word in this sublist  we return 1 the count of word
        if word in L[0]:
            return 1
        else:   ## if not found return 0 
            return 0
    ## if more than one element in the list
    else:
        ## if the word in the first element 
        if word in L[0]:
            ## we add 1 and return the function for the rest of the list
            return 1+find_word_count( word,L[1:])
        ## if the word not found in the first element 
        else:
            ## we retrun the function to the rest of list only 
            return find_word_count( word ,L[1:])


# file_paths = ['hello world, hello' , 'hello friends']
# print(find_word_count( 'hello',file_paths))



def get_idf(file_paths):
    """
        file paths : is a list of file names which conatain strings in it 

        return 
        a dictionary mapping each word to its idf calculated 
        idf(word) = log_10(total number of documents / number of documents word in it )

    """
    ## new list of the all words of the file paths 
    new_list = []

    ## idf_dict make 

    idf_dict = {}

    ## iterate through the file path and append the items in the new list after convert to list
    for i in file_paths:
        new_list.append(text_to_list(i))
       

    ## extend the new list make a one large list
    new_list = extend_list(new_list)
    
    #print(new_list)

    ## iterate through the new list 

    for word in new_list:
        ## if the word not in the idf dictionary
        if word not in idf_dict:

            #print(word , find_word_count(word,file_paths))

            ## find word count in the file paths and find the idf and add it to idf dictionary  
            idf_dict[word] = math.log10(len(file_paths) / find_word_count(word,file_paths))


    
    return idf_dict


## unit test 

# file_paths = ['hello world, hello' , 'hello friends']
# idf_text_files = ['hello world, hello', 'hello friends']
# idf = get_idf(idf_text_files)
# print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
# print(get_idf(file_paths))



def get_tfidf(tf_file_path , idf_file_path):
    """
        Returns:
        a sorted list of tuples (in increasing TF-IDF score), where each tuple is
        of the form (word, TF-IDF). In case of words with the same TF-IDF, the
        words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)  

    :param tf_file_path: is a list of strings that will give us the word tf 
    :param idf_file_path:  this is the file which we will calculate the idf of words in it 
    """
    TF_IDF_list = []
    TF = get_tf(tf_file_path)
    IDF = get_idf(idf_file_path)
    # print(IDF)
    # print(TF)
 
    for elem in TF:
        if elem in IDF:
            TF_IDF = TF[elem] * IDF[elem]
            TF_IDF_list.append((elem ,TF_IDF )) 
            # print(TF_IDF_list)
    
    return TF_IDF_list



# tf_text_file = 'hello world hello'
# idf_text_files = ['hello world hello', 'hello friends']
# print(get_tfidf(tf_text_file ,idf_text_files ))




