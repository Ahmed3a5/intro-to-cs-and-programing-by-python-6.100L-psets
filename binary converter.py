printable_ascii ={
    ' ': 32, '!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47,
    '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61, '>': 62, '?': 63,
    '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79,
    'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95,
    '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111,
    'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126
}

# print(printable_ascii['a'])


Ascii_nums = {
    32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/',
    48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?',
    64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O',
    80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_',
    96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g', 104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o',
    112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w', 120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~'
}

def binary_convert(num):
    """
        take a number and return its binary version
    """
    binary = ''
    if num == 0:
        return '0'

    while num >= 1:
        if num%2 != 0:
            binary ='1' +binary
        else:
            binary ='0' +binary
        num = num//2
    
    return binary

# print(binary_convert(27))


def binary_to_decimel(binary):
    num = 0
    i = len(binary)-1
    j = 0
    while i >=0:
        num += (2**j) * int(binary[i])
        i-=1 
        j+=1

    return num

# binary = binary_convert(1112334444)
# print(binary)
# print(binary_to_decimel(binary))



def get_word_asccii(word):

    ascii_nums = []
    for char in word:
        if char in printable_ascii.keys():
            ascii_nums.append(printable_ascii[char])

    return ascii_nums

# print(get_word_asccii('ahmed'))

def convert_word_binary(word):
    word_list = get_word_asccii(word)
    word_binary =''

    for i in word_list:
        binary = binary_convert(i)
        word_binary+=binary
        word_binary+=' '
    
    return word_binary

def split_binary(binary):
    temp = ''
    binary_list = []
    for bi in binary:
        if bi != ' ':
            temp+=bi
        else:
            binary_list.append(temp)
            temp = ''

    return binary_list


def get_decimel_list(binary):
    deciml_list = []
    binary_list = split_binary(binary)
    for bi in binary_list:
        deciml_list.append(binary_to_decimel(bi))
    
    return deciml_list


def convert_binary_to_word(binary):
    word =''
    decimel_list = get_decimel_list(binary)

    for num in decimel_list:
        if num in Ascii_nums.keys():
            word += Ascii_nums[num]
    

    return word


# binary = convert_word_binary('ashrafasde')
# print(convert_binary_to_word(binary))


def main():
    while True:
        print(96*'=')
        print(30*'=' , 'WELCOME TO SIMPLE BINARY CONVERTER' , 30*'=')
        print(96*'=')
        print('1-convert number')
        print('2-converet string')
        print('3-convert binary to number')
        print('4-convert binary to string')
        print('5-EXIT')

        try:
            choose = int(input())

            if choose == 1:
                num = int(input('number: '))
                binary = binary_convert(num)
                print(f'your binary is: {binary}')
                
            elif choose == 2:

                sentence = input('enter your word: ')
                word_binary = convert_word_binary(sentence)

                print(f'your word binary is {word_binary} ')
            elif choose == 3:
                binary = input('enter your binary number: ')
                num = binary_to_decimel(binary)
                print(f'your decimel number is {num}')
            elif choose == 4:
                binary_str = input('enter your string binary: ')
                word = convert_binary_to_word(binary_str)
                print(f'your sentence is ==> {word}')

            elif choose == 5:
                break

        except:
            print('INVALID CHOOSE')
            print('TRY AGIAN')


main()
