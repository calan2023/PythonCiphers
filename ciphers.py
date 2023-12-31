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
                if key > 0:
                    valid = True
                else:
                    print("Key needs to be a whole number greater than zero.")
                    key = input("Choose another value for the key: ")
            elif isinstance(key, str):
                if key.isnumeric():
                    key = int(key)
                else:
                    print("Key needs to be a whole number greater than zero.")
                    key = input("Choose another value for the key: ")
            elif isinstance(key, float):
                print("Key needs to be a whole number greater than zero.")
                key = input("Choose another value for the key: ")
            
        self.key = key

    def __str__(self):
        return f'Key = {self.key}'

    def __repr__(self):
        return f'Key = {self.key}'
        
    def encrypt(self, message):
        message = message.lower()
        encrypted_letter_values = []
        encrypted_message = ''
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = (LETTER_VALUES[letter] + self.key) % NUM_LETTERS
                encrypted_letter_values.append(encrypted_letter_value)
            else:
                encrypted_letter_values.append(letter)                
            
        for number in encrypted_letter_values:
            if isinstance(number, int):
                for key, value in LETTER_VALUES.items():
                    if number == value:
                        encrypted_message += key
            else:
                encrypted_message += number

        return encrypted_message

    def decrypt(self, message):
        message = message.lower()
        decrypted_letter_values = []
        decrypted_message = ''
        for letter in message:
            if letter.isalpha():
                decrypted_letter_value = (LETTER_VALUES[letter] - self.key) % NUM_LETTERS
                decrypted_letter_values.append(decrypted_letter_value)
            else:
                decrypted_letter_values.append(letter)
            
        for number in decrypted_letter_values:
            if isinstance(number, int):
                for key, value in LETTER_VALUES.items():
                    if number == value:
                        decrypted_message += key
            else:
                decrypted_message += number

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
        encrypted_letter_values = []
        encrypted_message = ''
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = ((self.a * LETTER_VALUES[letter]) +
                                          self.b) % NUM_LETTERS
                encrypted_letter_values.append(encrypted_letter_value)
            else:
                encrypted_letter_values.append(letter)                
                
        for number in encrypted_letter_values:
            if isinstance(number, int):
                for key, value in LETTER_VALUES.items():
                    if number == value:
                        encrypted_message += key
            else:
                encrypted_message += number

        return encrypted_message

    def decrypt(self, message):
        '''d(e(x)) = a^(-1)(e(x) - b)'''
        message = message.lower()
        decrypted_letter_values = []
        decrypted_message = ''
        for letter in message:
            if letter.isalpha():
                decrypted_letter_value = (VALUE_INVERSES[self.a] * (LETTER_VALUES[letter] - self.b)) % NUM_LETTERS
                decrypted_letter_values.append(decrypted_letter_value)
            else:
                decrypted_letter_values.append(letter)

        for number in decrypted_letter_values:
            if isinstance(number, int):
                for key, value in LETTER_VALUES.items():
                    if number == value:
                        decrypted_message += key
            else:
                decrypted_message += number

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
        encrypted_letter_values = []
        encrypted_message = ''
        for letter in message:
            if letter.isalpha():
                encrypted_letter_value = (LETTER_VALUES[letter] ** self.e) % self.n
                encrypted_letter_values.append(encrypted_letter_value)
            elif letter == ' ':
                encrypted_letter_values.append('_')
            else:
                encrypted_letter_values.append(letter)                
                
        for i in range(len(encrypted_letter_values)):
            if isinstance(encrypted_letter_values[i], int):
                encrypted_letter_values[i] = str(encrypted_letter_values[i])
                
        encrypted_message = ' '.join(encrypted_letter_values)
        return encrypted_message

    def decrypt(self, message):
        '''m = c^d (mod n)'''

        message = message.split(' ')
        decrypted_letter_values = []
        decrypted_message = ''
        for number in message:
            if number.isnumeric():
                decrypted_letter_value = (int(number) ** self.d) % self.n
                decrypted_letter_values.append(decrypted_letter_value)
            elif number == '_':
                decrypted_letter_values.append(' ')
            else:
                decrypted_letter_values.append(number)

        for number in decrypted_letter_values:
            if isinstance(number, int):
                for key, value in LETTER_VALUES.items():
                    if number == value:
                        decrypted_message += key
            else:
                decrypted_message += number

        return decrypted_message
        
def is_prime(num):
    '''Checks if number is prime. If number is less than 2, or if there exists a
    number 'i' between 2 and the number given where the number mod 'i' equals 0,
    then number is not prime. Otherwise, the number will be prime.

    Args:
        num (int): The number being checked to see if it's prime

    Returns:
        prime (bool): The result of whether number is prime
    '''
    
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    return prime

def is_invertible(num, phi_n):
    '''Checks if number has a multiplicative inverse in mod Φ(n). If there exists
    a number 'i' between 1 and Φ(n) where the number x 'i' mod Φ(n) equals 1,
    then number is invertible. Otherwise, the number will not be invertible.

    Args:
        num (int): The number being checked to see if it's invertible
        phi_n (int): Represents value for Φ(n)

    Returns:
        invertible (bool): The result of whether number is invertible
        d (int): The multiplicative inverse of the number in mod Φ(n)
    '''
    
    invertible = False
    d = None
    for i in range(1, phi_n):
        if (num * i) % phi_n == 1:
            invertible = True
            d = i
            break
    return invertible, d
