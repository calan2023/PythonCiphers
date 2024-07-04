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

import random
import math

LETTER_VALUES = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
                 'w': 22, 'x': 23, 'y': 24, 'z': 25}
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
        
        valid = False
        while not valid:
            if isinstance(key, int):
                if key >= 0:
                    valid = True
                else:
                    print("Key needs to be a whole number that is not negative.")
                    key = input("Choose another value for the key: ")
            elif isinstance(key, str):
                if key.isnumeric():
                    key = int(key)
                else:
                    print("Key needs to be a whole number that is not negative.")
                    key = input("Choose another value for the key: ")
            elif isinstance(key, float):
                print("Key needs to be a whole number that is not negative.")
                key = input("Choose another value for the key: ")
            
        self.key = key

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
                for key, value in LETTER_VALUES.items():
                    if encrypted_letter_value == value:
                        encrypted_message += key
            else:
                encrypted_message += letter               
            
        return encrypted_message

    def decrypt(self, message):
        message = message.lower()
        decrypted_message = ''
        for letter in message:
            if letter.isalpha():
                decrypted_letter_value = (LETTER_VALUES[letter] - self.key) % NUM_LETTERS
                for key, value in LETTER_VALUES.items():
                    if decrypted_letter_value == value:
                        decrypted_message += key
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
        
        valid = False
        while not valid:
            if isinstance(a, int):
                if a in VALUE_INVERSES:
                    valid = True
                else:
                    print('Key A needs to be a whole number greater than zero '\
                          'with an inverse in mod 26.')
                    a = input('Choose another value for Key A: ')
            elif isinstance(a, str):
                if a.isnumeric():
                    a = int(a)
                else:
                    print('Key A needs to be a whole number greater than zero '\
                          'with an inverse in mod 26.')
                    a = input('Choose another value for Key A: ')
            elif isinstance(a, float):
                print('Key A needs to be a whole number greater than zero '\
                          'with an inverse in mod 26.')
                a = input('Choose another value for Key A: ')

        valid = False
        while not valid:
            if isinstance(b, int):
                if 0 <= b <= NUM_LETTERS-1:
                    valid = True
                else:
                    print('Key B needs to be a whole number between 0 and 25.')
                    b = input('Choose another value for Key B: ')
            elif isinstance(b, str):
                if b.isnumeric():
                    b = int(b)
                else:
                    print('Key B needs to be a whole number between 0 and 25.')
                    b = input('Choose another value for Key B: ')
            elif isinstance(b, float):
                print('Key B needs to be a whole number between 0 and 25.')
                b = input('Choose another value for Key B: ')

        self.a = a
        self.b = b

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
                for key, value in LETTER_VALUES.items():
                    if encrypted_letter_value == value:
                        encrypted_message += key
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
                for key, value in LETTER_VALUES.items():
                    if decrypted_letter_value == value:
                        decrypted_message += key
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
        
        valid = False
        while not valid:
            if not isinstance(key, str):
                print("Key needs to be a string with no spaces, numbers or other special characters.")
                key = input("Choose another value for the key: ")
            else:
                valid = True
                for letter in key:
                    if not letter.isalpha():
                        valid = False
                        print("Key needs to be a string with no spaces, numbers or other special characters.")
                        key = input("Choose another value for the key: ")
                        
        self.key = key.lower()
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
        
        valid = False
        while not valid:
            if not isinstance(key, str):
                print("Key needs to be a string with no spaces, numbers or other special characters.")
                key = input("Choose another value for the key: ")
            else:
                valid = True
                for letter in key:
                    if not letter.isalpha():
                        valid = False
                        print("Key needs to be a string with no spaces, numbers or other special characters.")
                        key = input("Choose another value for the key: ")
                        break
        
        self.key = key.replace('j', 'i')
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
        
        valid = False
        while not valid:
            if isinstance(p, int):
                if is_prime(p):
                    valid = True
                else:
                    print('p needs to be a prime number.')
                    p = input('Choose another value for p: ')
            elif isinstance(p, str):
                if p.isnumeric():
                    p = int(p)
                else:
                    print('p needs to be a prime number.')
                    p = input('Choose another value for p: ')
            elif isinstance(p, float):
                print('p needs to be a prime number.')
                p = input('Choose another value for p: ')
        self.p = p
        
        valid = False
        while not valid:
            if isinstance(q, int):
                if is_prime(q) and q != self.p:
                    valid = True
                else:
                    print("q needs to be a prime number that's different from p.")
                    q = input('Choose another value for q: ')
            elif isinstance(q, str):
                if q.isnumeric():
                    q = int(q)
                else:
                    print("q needs to be a prime number that's different from p.")
                    q = input('Choose another value for q: ')
            elif isinstance(q, float):
                print("q needs to be a prime number that's different from p.")
                q = input('Choose another value for q: ')
        self.q = q
        self.n = p * q
        self.phi_n = (p-1) * (q-1)
        
        e = input(f'Choose an invertible element in mod {self.phi_n}: ')
        valid = False
        while not valid:
            if isinstance(e, int):
                invertible, d = is_invertible(e, self.phi_n)
                if invertible:
                    valid = True
                else:
                    print('e needs to be a whole number that has a '\
                          f'multiplicative inverse in mod {self.phi_n}.')
                    e = input('Choose another value for e: ')
            elif isinstance(e, str):
                if e.isnumeric():
                    e = int(e)
                else:
                    print('e needs to be a whole number that has a '\
                          f'multiplicative inverse in mod {self.phi_n}.')
                    e = input('Choose another value for e: ')
            elif isinstance(e, float):
                print('e needs to be a whole number that has a '\
                        f'multiplicative inverse in mod {self.phi_n}.')
                e = input('Choose another value for e: ')
        self.e = e
        self.d = d
        self.public_key = (self.n, self.e)
        print(f'Public key: (n, e) = {self.public_key}')

    def __str__(self):
        return f'p = {self.p}\nq = {self.q}\nn = {self.n}\nΦ(n) = {self.phi_n}\ne = {self.e}\nd = {self.d}\nPublic key = {self.public_key}'

    def __repr__(self):
        return f'p = {self.p}\nq = {self.q}\nn = {self.n}\nΦ(n) = {self.phi_n}\ne = {self.e}\nd = {self.d}\nPublic key = {self.public_key}'
    
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
                for key, value in LETTER_VALUES.items():
                    if decrypted_letter_value == value:
                        decrypted_message += key
            elif number == '_':
                decrypted_message += ' '
            else:
                decrypted_message += number

        return decrypted_message
        
def is_prime(num):
    '''Checks if number is prime. If number is 2, then it is prime. Otherwise,
    if number is less than or equal to 1 or number is even, then it is not prime.
    Otherwise, the Miller-Rabin test is run up to 100 times with a random base.
    If one of the tests comes back negative, then number is not prime.
    Otherwise, the number will be prime.

    Args:
        num (int): The number being checked to see if it's prime

    Returns:
        True/False (bool): The result of whether number is prime
    '''
    
    if num == 2:
        return True
    elif num <= 1 or num % 2 == 0:
        return False
    else:
        for i in range(100):
            base = random.randint(1, num-1)
            if miller_rabin_test(num, base) is False:
                return False
    return True

def miller_rabin_test(num, base):
    '''Runs a Miller-Rabin primality test. Gets positive integer 's' and odd
    positive integer 'd' where num - 1 = 2**s * d. If base**d is congruent to
    1 mod num, num is prime. Otherwise, for each integer 'r' from 0 to s - 1,
    if base**(2**r * d) is congruent to -1 mod num, num is prime. Otherwise,
    num is not prime.

    Args:
        num (int): The number being checked to see if it's prime
        base (int): The base number used for checking the primality
        of the number

    Returns:
        True/False (bool): The result of whether the number is prime
    '''
    
    s = 1
    d = None
    while d is None:
        if ((num-1) // 2**s) % 2 == 1:
            d = (num - 1) // 2**s
        else:
            s += 1

    if fast_exponentiation(base, d, num) == 1:
        return True

    for r in range(s):
        if fast_exponentiation(base, 2**r * d, num) == num-1:
            return True
    return False

def fast_exponentiation(base, exponent, modulus):
    '''Calculates the equation a**m mod n, where m and n can be large,
    by using exponentiation by squaring.
    
    Args:
        base (int): The base number 'a' in the calculation
        exponent (int): The exponent number 'm' in the calculation
        modulus (int): The modulus 'n' the calculation is computed in

    Returns:
        final_result (int): The result of the calculation
    '''
    
    binary_exponent = format(exponent, 'b')
    reverse_binary = binary_exponent[::-1]
    
    exponents_list = []
    for i in range(len(reverse_binary)):
        if reverse_binary[i] == '1':
            exponents_list.append(i)

    exponents_list.reverse()
    max_exponent = exponents_list[0]
    final_result = 1
    if exponents_list[-1] == 0:
        final_result *= base
        final_result %= modulus
        exponents_list.pop()
        
    squared = base   
    for k in range(1, max_exponent+1):
        squared = squared**2 % modulus
        if k == exponents_list[-1]:
            final_result *= squared
            final_result %= modulus
            exponents_list.pop()
    return final_result

def is_invertible(num, phi_n):
    '''Checks if number has a multiplicative inverse in mod Φ(n) by running
    the extended Euclidean algorithm. If the greatest common divisor of the
    number and Φ(n) equals 1, then the number is invertible and returns the
    multiplicative inverse mod Φ(n). Otehrwise, the number isn't invertible.

    Args:
        num (int): The number being checked to see if it's invertible
        phi_n (int): Represents value for Φ(n)

    Returns:
        invertible (bool): The result of whether number is invertible
        d (int): The multiplicative inverse of the number in mod Φ(n)
    '''

    gcd, x, _ = extended_gcd(num, phi_n)
    if gcd == 1:
        invertible = True
        d = x % phi_n
    else:
        invertible = False
        d = None
    return invertible, d

def extended_gcd(a, n):
    '''Finds the greatest common divisor of two numbers 'a' and 'n' and finds
    the two numbers 'x' and 'y' in the equation 'gcd = ax + ny'

    Args:
        a, n (int): The two numbers used to find the greatest common divisor

    Returns:
        gcd (int): The greatest common divisor of the two numbers
        x, y (int): The two numbers in the equation 'gcd = ax + ny'
    '''
    if a == 0 : 
        return n, 0, 1
    
    gcd, x1, y1 = extended_gcd(n%a, a) 

    x = y1 - (n//a) * x1 
    y = x1
    return gcd, x, y
