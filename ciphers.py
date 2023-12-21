LETTER_VALUES = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
                 'w': 22, 'x': 23, 'y': 24, 'z': 25}
VALUE_INVERSES = {1: 1, 3: 9, 5: 21, 7: 15, 9: 3, 11: 19, 15: 7, 17: 23, 19: 11,
                  21: 5, 23: 17, 25: 25}
NUM_LETTERS = 26

# Caesar Cipher
class Caesar():
    def __init__(self, key):
        valid = False
        while not valid:
            if isinstance(key, int):
                if CONDITION:
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

# Affine Cipher
class Affine():
    def __init__(self, a, b):
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

# RSA Cryptosystem
class RSA():
    def __init__(self, p, q):
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
                    q = input('Choose another value for p: ')
            elif isinstance(q, str):
                if q.isnumeric():
                    q = int(q)
                else:
                    print("q needs to be a prime number that's different from p.")
                    q = input('Choose another value for p: ')
            elif isinstance(q, float):
                print("q needs to be a prime number that's different from p.")
                q = input('Choose another value for p: ')
        self.q = q
        
        self.n = p * q
        self.phi_n = (p-1) * (q-1)
        e = int(input(f'Choose an invertible element in mod {self.phi_n}: '))
        invertible, d = is_invertible(e, self.phi_n)
        while not invertible:
            print(f'{e} is not invertible in mod {self.phi_n}.')
            e = int(input(f'Choose an invertible element in mod {self.phi_n}: '))
            invertible, d = is_invertible(e, self.phi_n)
        self.e = e
        self.d = d
        self.public_key = (self.n, self.e)
        print(f'Public key: (n, e) = {self.public_key}')

    def __str__(self):
        return f'p = {self.p}\nq = {self.q}\nn = {self.n}\nΦ(n) = {self.phi_n}\ne = {self.e}\nd = {self.d}\nPublic key = {self.public_key}'

    def __repr__(self):
        return f'p = {self.p}\nq = {self.q}\nn = {self.n}\nΦ(n) = {self.phi_n}\ne = {self.e}\nd = {self.d}\nPublic key = {self.public_key}'
    
    def encrypt(self, m):
        '''c = m^e (mod n)'''
        c = (m ** self.e) % self.n
        return c

    def decrypt(self, c):
        '''m = c^d (mod n)'''
        m = (c ** self.d) % self.n
        return m
        
def is_prime(num):
    prime = True
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    return prime

def is_invertible(num, phi_n):
    invertible = False
    d = None
    for i in range(1, phi_n):
        if (num * i) % phi_n == 1:
            invertible = True
            d = i
            break
    return invertible, d
