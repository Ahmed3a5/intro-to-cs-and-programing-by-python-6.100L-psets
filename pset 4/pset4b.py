import random


## our asci letters in a list 
letters =[
  ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', 
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', 
  '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', 
  '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'
]
    
# print(letters)

## our dictionary of ascci letters and each value as a function 
def make_dict_ascii(letters):
    """
    return a dictionary of ascii letters and its number     
    :param letters: a list of letters 
    """
    ASCII = {}
    j=0
    ## iteration through the range of the values 
    for i in range(32 , 127 ,1):
        ASCII[letters[j]] = i
        j+=1
    return ASCII
ASCII = make_dict_ascii(letters)
# print(ASCII)

## helper functioin to get the character which is attached to its ascii value
def get_asscii(ASCII , num):
    """
    return a character from the dictionary 
    
    :param ASCII: dictionary of ascii 
    :param num: the number of ascii we want the letter attached to it 
    """
    for k , v in ASCII.items():
        if v == num:
            return k
        
# print(get_asscii(ASCII , 32))
        
## helper function to split a string 

def split_text(text):
    """
        return a list of every character in the string 
        text is a string 
    """
    letters = []
    for char in text:
        letters.append(char)
    return letters



class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            the message text
        '''
        self.input_text = input_text

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''Message('{self.get_text()}')'''

    def get_text(self):
        '''
        Used to access the message text outside of the class

        Returns: (string) the message text
        '''
        return self.input_text
    
    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char by

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        ## add the shift  to the char number in ascii 
        char_num = ASCII[char] + shift
        ## we subtract 32 from the char number to return the range to 0 so we can take the reminder from 95 character in 
        ## the range of 32 to 126 ascci so we then add 32 to return to the base whic it 32 
        ## modular of 95 is which if the added shift is above the 126 we reset the the number as a clock and add the reminder to 
        char_num = (char_num - 32) % 95 + 32
        ## return the new char after encrypt the original one 
        return get_asscii(ASCII , char_num)
            
    
    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to the message text.
        For each character in the text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt the message text
                        len(pad) == len(the message text)

        Returns: (string) The ciphertext produced using the one time pad
        '''

        ciphertext = ''
        i = 0
        ## iterate throght the original input text 
        for char in self.input_text:
            ## convert each letter to the crypted form use thr shift number in the pad 
            ## that is in the same position as the character 
            new_char = self.shift_char(char , pad[i])
            i+=1
            ## add thte encrypted character to the ciphertext 
            ciphertext+=new_char
        
        return ciphertext


# message = Message('ahmed')
# pad = [20 , 40 , 50 , 70 ,50]
# print(message.apply_pad(pad))


class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad is not None then len(pad) == len(self.input_text)

        A PlaintextMessage object inherits from Message. It has three attributes:
            the message text
            the pad (list of integers, determined by pad
                or generated randomly using self.generate_pad() if pad is None)
            the ciphertext (string, input_text encrypted using the pad)
        '''
        Message.__init__(self , input_text)
        ## if pad is none we generate one else we make acopy of it as list
        if pad == None:
            self.pad = self.generate_pad()
        else:
            self.pad = list(pad)

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt the message text.

        The pad should be generated by making a new list and for each character
            in the message chosing a random number in the range [0, 110) and
            adding that number to the list.

        Returns: (list of integers) the new one time pad
        '''
        self.pad = []
        ## itterate through the lenght of text
        for i in range(len(self.input_text)):
            ## choose a rondome numper for each character 
            num = random.randint(0 , 110)
            ## append this number at the same position of the character 
            self.pad.append(num)
            ## retrun a copy of the pad
        return self.pad.copy()

    def get_pad(self):
        '''
        Used to safely access your one time pad outside of the class

        Returns: (list of integers) a COPY of your pad
        '''
        return self.pad
    
    def get_ciphertext(self):
        '''
        Used to access the ciphertext produced by applying pad to the message text

        Returns: (string) the ciphertext
        '''
        ## if the self pad is none we generte one 
        if self.pad == None:
            self.generate_pad()
            ## then we make a ciphertext to the text use the original methode of the superclass Message
        ciphertext = self.apply_pad(self.pad)
        ## return the ciphertext
        return ciphertext

    def change_pad(self, new_pad):
        '''
        Changes the pad used to encrypt the message text and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(new_pad) == len(the message text)

        Returns: nothing
        '''
        ## se change the self pad with the new pad 
        self.pad = new_pad
        self.get_ciphertext()

# text = PlaintextMessage('ahmed')
# print(text.generate_pad())
# print(text.get_pad())
# print(text.get_ciphertext())

    
class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has one attribute:
            the message text (ciphertext)
        '''
        Message.__init__(self , input_text)

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        '''
        Decrypts the message text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(the message text)

        Returns: (PlaintextMessage) the decrypted message (containing the pad)
        '''

        message = ''
        ## we use our split method to split text to each character in it 
        letters = split_text(self.input_text)
        ## iterate through the lenght of the  new array of the chars 
        for i in range(len(letters)):
            ## get the ascci of the character from the dictionary 
            num = ASCII[letters[i]]
            ## we claculate the  number of the original text from the cipher one 
            new_num = ((num - 32-pad[i]) % 95) +32
            ## we get the original character 
            char = get_asscii(ASCII , new_num)
            ## we add the original character to the message 
            message +=char
            ## we retutn the message as plain text object 
        return PlaintextMessage(message , pad)


# text = PlaintextMessage('ahmed')
# text.generate_pad()
# print(text.get_pad())
# cipher = EncryptedMessage(text.get_ciphertext())
# print(cipher.decrypt_message(text.get_pad()))


