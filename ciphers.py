'''The module containing the classes for three types of ciphers used for
encryption and decryption of text.

All classes have five methods:
    __init__():
        Initialises the class by validating user input before assigning
        attributes needed for the cipher.

    __str__() and __repr__():
        String representations of the class.

        Returns:
            String of all attributes assigned in the class

    encrypt(message):
        Encrypts text letter by letter through using the equation for the
        cipher and attributes of the class.

        Args:
            message (str): The plaintext that will be encrypted

        Returns:
            encrypted_message (str): The ciphertext version of message argument

    decrypt(message):
        Decrypts text letter by letter through using the equation for the
        cipher and attributes of the class.

        Args:
            message (str): The ciphertext that will be decrypted

        Returns:
            decrypted_message (str): The plaintext version of message argument

'''

from extra_functions import *

LETTER_VALUES = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
                 'w': 22, 'x': 23, 'y': 24, 'z': 25}
VALUE_LETTERS = {value: key for key, value in LETTER_VALUES.items()}
VALUE_INVERSES = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11,
                  21: 5, 23: 17, 25: 25}
NUM_LETTERS = 26

# Caesar Cipher ================================================================

class Caesar():
    '''Attributes:
        key (int): The key used for shifting letters in a Caesar cipher 
    '''
    
    def __init__(self, key):
        '''Args:
            key (int): The key chosen by the user for shifting letters in a
            Caesar cipher
        '''
        
        condition = lambda key: key >= 0
        self.key = valid_int_key(key, condition)

    def __str__(self):
        return f'Key = {self.key}'

    def __repr__(self):
        return f'Key = {self.key}'
        
    def encrypt(self, message):
        message = message.lower()
        encrypted_message = ''
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = (LETTER_VALUES[letter] + self.key) % NUM_LETTERS
                encrypted_message += VALUE_LETTERS[encrypted_letter_value]
            else:
                encrypted_message += letter               
            
        return encrypted_message

    def decrypt(self, message):
        message = message.lower()
        decrypted_message = ''
        for letter in message:
            if letter.isalpha():
                decrypted_letter_value = (LETTER_VALUES[letter] - self.key) % NUM_LETTERS
                decrypted_message += VALUE_LETTERS[decrypted_letter_value]
            else:
                decrypted_message += letter
            
        return decrypted_message

# Affine Cipher ================================================================

class Affine():
    '''Attributes:
        a (int): The value that's multiplied to value of letter in an Affine
        cipher
        b (int): The value that's added to the product of a and value of letter
        in an Affine cipher
    '''
    
    def __init__(self, a, b):
        '''Args:
            a (int): The value chosen by the user that's multiplied to value of
            letter in an Affine cipher
            b (int): The value chosen by the user that's added to the product of
            a and value of letter in an Affine cipher
        '''
        
        condition = lambda a: a in VALUE_INVERSES
        error_prompt = 'Key A needs to be a whole number greater than zero '\
                        'with an inverse in mod 26.'
        input_prompt = 'Choose another value for Key A: '
        self.a = valid_int_key(a, condition, error_prompt, input_prompt)

        condition = lambda b: 0 <= b <= NUM_LETTERS-1
        error_prompt = 'Key B needs to be a whole number between 0 and 25.'
        input_prompt = 'Choose another value for Key B: '
        self.b = valid_int_key(b, condition, error_prompt, input_prompt)

    def __str__(self):
        return f'a = {self.a}\nb = {self.b}'

    def __repr__(self):
        return f'a = {self.a}\nb = {self.b}'
        
    def encrypt(self, message):
        '''e(x) = ax + b'''
        message = message.lower()
        encrypted_message = ''
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = ((self.a * LETTER_VALUES[letter]) +
                                          self.b) % NUM_LETTERS
                encrypted_message += VALUE_LETTERS[encrypted_letter_value]
            else:
                encrypted_message += letter

        return encrypted_message

    def decrypt(self, message):
        '''d(e(x)) = a^(-1)(e(x) - b)'''
        message = message.lower()
        decrypted_message = ''
        for letter in message:
            if letter.isalpha():
                decrypted_letter_value = (VALUE_INVERSES[self.a] *
                                          (LETTER_VALUES[letter] - self.b)) % NUM_LETTERS
                decrypted_message += VALUE_LETTERS[decrypted_letter_value]
            else:
                decrypted_message += letter

        return decrypted_message

# Vigenere Cipher ==============================================================
    
class Vigenere():
    '''Attributes:
        key (str): The key used for shifting letters in a Vigenere cipher
        caesar_ciphers (list): List of Caesar ciphers used in a Vigenere cipher based
        on the letters in the key
    '''
    
    def __init__(self, key):
        '''Args:
            key (str): The key chosen by the user for shifting letters in a Vigenere cipher
        '''
        
        self.key = valid_str_key(key).lower()
        self.caesar_ciphers = []
        key_length = len(self.key)
        for i in range(key_length):
            cipher = Caesar(LETTER_VALUES[self.key[i]])
            self.caesar_ciphers.append(cipher)

    def __str__(self):
        return f"Key = '{self.key}'"

    def __repr__(self):
        return f"Key = '{self.key}'"
    
    def encrypt(self, message):
        message = message.lower()
        encrypted_message = ''
        cipher_index = 0
        for letter in message:
            if letter.isalpha():
                letter_cipher = self.caesar_ciphers[cipher_index]
                encrypted_letter = letter_cipher.encrypt(letter)
                encrypted_message += encrypted_letter
                cipher_index = (cipher_index + 1) % len(self.caesar_ciphers)
            else:
                encrypted_message += letter

        return encrypted_message

    def decrypt(self, message):
        message = message.lower()
        decrypted_message = ''
        cipher_index = 0
        for letter in message:
            if letter.isalpha():
                letter_cipher = self.caesar_ciphers[cipher_index]
                decrypted_letter = letter_cipher.decrypt(letter)
                decrypted_message += decrypted_letter
                cipher_index = (cipher_index + 1) % len(self.caesar_ciphers)
            else:
                decrypted_message += letter

        return decrypted_message

# Playfair Cipher ==============================================================

class Playfair():
    '''Attributes:
        ALPHABET (list): All letters in the English alphabet (except 'j')
        key (str): The key used for creating a matrix of letters in a Playfair
        cipher
        matrix (list): 5x5 matrix used in a Playfair cipher
    '''
    
    ALPHABET = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'k',
                'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    
    def __init__(self, key):
        '''Args:
            key (str): The key chosen by the user for creating a matrix of letters
            in a Playfair cipher
        '''
        
        self.key = valid_str_key(key).lower().replace('j', 'i')
        new_alphabet = list(dict.fromkeys(list(self.key) + Playfair.ALPHABET))
        self.matrix = []
        for i in range(5, len(new_alphabet)+1, 5):
            self.matrix.append(new_alphabet[i-5:i])

    def __str__(self):
        string = f"Key = '{self.key}'"
        for row in self.matrix:
            string += f'\n{row}'
        return string

    def __repr__(self):
        string = f"Key = '{self.key}'"
        for row in self.matrix:
            string += f'\n{row}'
        return string

    def encrypt(self, message):
        message = message.lower().replace('j', 'i')
        split_message = []
        i, j = 0, 1
        while i < len(message) and j < len(message)+1:
            if not message[i:j].isalpha():
                split_message.append(message[i:j-1])
                i = j-1
            j += 1
        split_message.append(message[i:j-1])
        
        encrypted_message = ''
        for word in split_message:
            if word.isalpha():
                digrams = []
                i = 0
                while i < len(word):
                    digram = word[i:i+2]
                    if len(digram) == 1:
                        digram += 'x'
                    if digram[0] == digram[1]:
                        word = word[:i+1] + 'x' + word[i+1:]
                        digram = word[i:i+2]
                    digrams.append(digram)
                    i += 2
        
                for digram in digrams:
                    letter_indices = []
                    for letter in digram:
                        for row in range(len(self.matrix)):
                            if letter in self.matrix[row]:
                                col = self.matrix[row].index(letter)
                                letter_indices.append((row, col))
                                break
                        
                    letter1, letter2 = letter_indices[0], letter_indices[1]
                    if letter1[0] == letter2[0]:
                        col_size = len(self.matrix)
                        new_letter1 = self.matrix[letter1[0]][(letter1[1]+1)%col_size]
                        new_letter2 = self.matrix[letter2[0]][(letter2[1]+1)%col_size]
                    elif letter1[1] == letter2[1]:
                        row_size = len(self.matrix)
                        new_letter1 = self.matrix[(letter1[0]+1)%row_size][letter1[1]]
                        new_letter2 = self.matrix[(letter2[0]+1)%row_size][letter2[1]]
                    else:
                        new_letter1 = self.matrix[letter1[0]][letter2[1]]
                        new_letter2 = self.matrix[letter2[0]][letter1[1]]
                    encrypted_digram = new_letter1 + new_letter2
                    encrypted_message += encrypted_digram
            else:
                encrypted_message += word
        return encrypted_message

    def decrypt(self, message):
        message = message.lower()
        split_message = []
        i, j = 0, 1
        while i < len(message) and j < len(message)+1:
            if not message[i:j].isalpha():
                split_message.append(message[i:j-1])
                i = j-1
            j += 1
        split_message.append(message[i:j-1])
        
        decrypted_message = ''
        for word in split_message:
            if word.isalpha():
                digrams = []
                for i in range(0, len(word)-1, 2):
                    digram = word[i:i+2]
                    digrams.append(digram)

                for digram in digrams:
                    letter_indices = []
                    for letter in digram:
                        for row in range(len(self.matrix)):
                            if letter in self.matrix[row]:
                                col = self.matrix[row].index(letter)
                                letter_indices.append((row, col))
                                break

                    letter1, letter2 = letter_indices[0], letter_indices[1]
                    if letter1[0] == letter2[0]:
                        col_size = len(self.matrix)
                        new_letter1 = self.matrix[letter1[0]][(letter1[1]-1)%col_size]
                        new_letter2 = self.matrix[letter2[0]][(letter2[1]-1)%col_size]
                    elif letter1[1] == letter2[1]:
                        row_size = len(self.matrix)
                        new_letter1 = self.matrix[(letter1[0]-1)%row_size][letter1[1]]
                        new_letter2 = self.matrix[(letter2[0]-1)%row_size][letter2[1]]
                    else:
                        new_letter1 = self.matrix[letter1[0]][letter2[1]]
                        new_letter2 = self.matrix[letter2[0]][letter1[1]]
                    decrypted_digram = new_letter1 + new_letter2
                    decrypted_message += decrypted_digram
            else:
                decrypted_message += word
        return decrypted_message
        
# RSA Cryptosystem =============================================================

class RSA():
    '''Attributes:
        p (int): The first prime number used in an RSA Cryptosystem
        q (int): The second prime number, different from p, used in an RSA
        Cryptosystem
        n (int): The product of p and q used in an RSA Cryptosystem
        phi_n (int): The number of positive integers less than n that are
        co-prime to n, used in an RSA Cryptosystem
        e (int): The number which has a multiplicative inverse in modulo phi_n
        used in an RSA Cryptosystem
        d (int): The multiplicative inverse of e in modulo phi_n used in an RSA
        Cryptosystem
        public_key (tuple): The numbers used in an RSA Cryptosystem that can be
        shown to anyone. Contains n and e
    '''

    def __init__(self, p, q):
        '''Args:
            p (int): The first prime number chosen by the user to be used in an
            RSA Cryptosystem
            q (int): The second prime number, different from p, chosen by the
            user to be used in an RSA Cryptosystem
        '''
        
        condition = lambda p: is_prime(p)
        error_prompt = 'p needs to be a prime number.'
        input_prompt = 'Choose another value for p: '
        self.p = valid_int_key(p, condition, error_prompt, input_prompt)
        
        condition = lambda q: is_prime(q) and q != self.p
        error_prompt = "q needs to be a prime number that's different from p."
        input_prompt = 'Choose another value for q: '
        self.q = valid_int_key(q, condition, error_prompt, input_prompt)
        self.n = self.p * self.q
        self.phi_n = (self.p-1) * (self.q-1)
        
        e = input(f'Choose an invertible element in mod {self.phi_n}: ')
        condition = lambda e: is_invertible(e, self.phi_n)[0]
        error_prompt = 'e needs to be a whole number that has a '\
                        f'multiplicative inverse in mod {self.phi_n}.'
        input_prompt = 'Choose another value for e: '
        self.e = valid_int_key(e, condition, error_prompt, input_prompt)
        self.d = is_invertible(self.e, self.phi_n)[1]
        self.public_key = (self.n, self.e)
        print(f'Public key: (n, e) = {self.public_key}')

    def __str__(self):
        return f'''p = {self.p}
q = {self.q}
n = {self.n}
Φ(n) = {self.phi_n}
e = {self.e}
d = {self.d}
Public key = {self.public_key}'''

    def __repr__(self):
        return f'''p = {self.p}
q = {self.q}
n = {self.n}
Φ(n) = {self.phi_n}
e = {self.e}
d = {self.d}
Public key = {self.public_key}'''
    
    def encrypt(self, message):
        '''c = m^e (mod n)'''

        message = message.lower()
        encrypted_message = []
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = fast_exponentiation(LETTER_VALUES[letter], self.e, self.n)
                encrypted_message.append(str(encrypted_letter_value))
            elif letter == ' ':
                encrypted_message.append('_')
            else:
                encrypted_message.append(letter)
                
        encrypted_message = ' '.join(encrypted_message)                
        return encrypted_message

    def decrypt(self, message):
        '''m = c^d (mod n)'''

        message = message.split(' ')
        decrypted_message = ''
        for number in message:
            if number.isnumeric():
                decrypted_letter_value = fast_exponentiation(int(number), self.d, self.n)
                decrypted_message += VALUE_LETTERS[decrypted_letter_value]
            elif number == '_':
                decrypted_message += ' '
            else:
                decrypted_message += number

        return decrypted_message

# Rabin Cipher =============================================================

class Rabin():
    '''Attributes:
        p (int): The first prime number used in a Rabin cipher
        q (int): The second prime number, different from p, used in a Rabin Cipher
        n (int): The product of p and q used in a Rabin cipher
    '''
    
    def __init__(self, p, q):
        '''Args:
            p (int): The first prime number chosen by the user to be used in an
            RSA Cryptosystem
            q (int): The second prime number, different from p, chosen by the
            user to be used in an RSA Cryptosystem
        '''
        
        condition = lambda p: is_prime(p)
        error_prompt = 'p needs to be a prime number.'
        input_prompt = 'Choose another value for p: '
        self.p = valid_int_key(p, condition, error_prompt, input_prompt)
        
        condition = lambda q: is_prime(q) and q != self.p
        error_prompt = "q needs to be a prime number that's different from p."
        input_prompt = 'Choose another value for q: '
        self.q = valid_int_key(q, condition, error_prompt, input_prompt)
        self.n = self.p * self.q

    def __str__(self):
        return f'p = {self.p}\nq = {self.q}\nn = {self.n}'

    def __repr__(self):
        return f'p = {self.p}\nq = {self.q}\nn = {self.n}'

    def encrypt(self, message):
        message = message.lower()
        encrypted_message = []
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = fast_exponentiation(LETTER_VALUES[letter], 2, self.n)
                encrypted_message.append(str(encrypted_letter_value))
            elif letter == ' ':
                encrypted_message.append('_')
            else:
                encrypted_message.append(letter)
                
        encrypted_message = ' '.join(encrypted_message)
        return encrypted_message

    def decrypt(self, message):
        message = message.split(' ')
        decrypted_messages = ['']
        for number in message:
            if number.isnumeric():
                a_squared = int(number) % self.p
                b_squared = int(number) % self.q
                a = 1
                while fast_exponentiation(a, 2, self.p) != a_squared:
                    a += 1
                b = 1
                while fast_exponentiation(b, 2, self.q) != b_squared:
                    b += 1
                gcd, u, v = extended_gcd(self.p, self.q)
                x1 = (b*self.p*u + a*self.q*v) % self.n
                x2 = (b*self.p*u - a*self.q*v) % self.n
                x3 = (-b*self.p*u + a*self.q*v) % self.n
                x4 = (-b*self.p*u - a*self.q*v) % self.n
                solutions = [x1, x2, x3, x4]
                valid_solutions = list({solution for solution in solutions\
                                        if solution < NUM_LETTERS})
                        
                if len(valid_solutions) == 1:
                    for i in range(len(decrypted_messages)):
                        decrypted_messages[i] += VALUE_LETTERS[valid_solutions[0]]
                                
                elif len(valid_solutions) == 2:
                    decrypted_messages_copy = decrypted_messages[:]
                    for i in range(len(decrypted_messages)):
                        decrypted_messages[i] += VALUE_LETTERS[valid_solutions[0]]
                        decrypted_messages_copy[i] += VALUE_LETTERS[valid_solutions[1]]
                    decrypted_messages += decrypted_messages_copy
                    
                elif len(valid_solutions) == 3:
                    decrypted_messages_copy1 = decrypted_messages[:]
                    decrypted_messages_copy2 = decrypted_messages[:]
                    for i in range(len(decrypted_messages)):
                        decrypted_messages[i] += VALUE_LETTERS[valid_solutions[0]]
                        decrypted_messages_copy1[i] += VALUE_LETTERS[valid_solutions[1]]
                        decrypted_messages_copy2[i] += VALUE_LETTERS[valid_solutions[2]]
                    decrypted_messages += decrypted_messages_copy1\
                                          + decrypted_messages_copy2

                elif len(valid_solutions) == 4:
                    decrypted_messages_copy1 = decrypted_messages[:]
                    decrypted_messages_copy2 = decrypted_messages[:]
                    decrypted_messages_copy3 = decrypted_messages[:]
                    for i in range(len(decrypted_messages)):
                        decrypted_messages[i] += VALUE_LETTERS[valid_solutions[0]]
                        decrypted_messages_copy1[i] += VALUE_LETTERS[valid_solutions[1]]
                        decrypted_messages_copy2[i] += VALUE_LETTERS[valid_solutions[2]]
                        decrypted_messages_copy3[i] += VALUE_LETTERS[valid_solutions[3]]           
                    decrypted_messages += decrypted_messages_copy1\
                                          + decrypted_messages_copy2\
                                          + decrypted_messages_copy3
            elif number == '_':
                for i in range(len(decrypted_messages)):
                    decrypted_messages[i] += ' '
            else:
                for i in range(len(decrypted_messages)):
                    decrypted_messages[i] += number
        decrypted_messages = '/'.join(decrypted_messages)
        return decrypted_messages
