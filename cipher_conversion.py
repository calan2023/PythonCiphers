'''The main module for running the cipher converter. Used for encrypting and
decrypting text in text documents.
'''

from ciphers import *

def get_lines(file):
    '''Reads lines in a file and returns them in a list.

    Args:
        file (str): The file location of text

    Returns:
        lines (list): List containing each line of text in the file
    '''
    
    infile = open(file)
    lines = infile.read().splitlines()
    infile.close()
    return lines

def get_cipher():
    '''Prints available ciphers. Gets and validates users choice. If user chooses
    Caesar cipher, user is asked to enter a key and Caesar class is created. If
    user chooses Affine cipher, user is asked to enter Key A and Key B and Affine
    class is created. If user chooses RSA, user is asked to enter to prime numbers
    and RSA Cryptosystem is created.

    Returns:
        cipher (class): The cipher chosen by the user
    '''
    
    print('''Available Ciphers:
1: Caesar
2: Affine
3: RSA''')
    cipher = input("Choose a cipher: ")
    while cipher not in ['1', '2', '3']:
        print('Invalid. Try again')
        cipher = input("Choose a cipher: ")
        
    if cipher == '1':
        key = input("Choose a key for the Caesar cipher: ")
        cipher = Caesar(key) 
    elif cipher == '2':
        a = input('Choose Key A for the Affine cipher: ')
        b = input('Choose Key B for the Affine cipher: ')
        cipher = Affine(a, b)
    elif cipher == '3':
        p = input("Choose first prime number for the RSA Cryptosystem: ")
        q = input("Choose second prime number for the RSA Cryptosystem: ")
        cipher = RSA(p, q)
    return cipher
            
def plain_to_cipher():
    '''Gets lines in plain.txt file and gets cipher user wants to use. Opens
    cipher.txt file and encrypts each line and writes the encrypted line into
    cipher.txt file.
    '''
    
    lines = get_lines('plain.txt')
    code = get_cipher()
    outfile = open('cipher.txt', 'a')
    for line in lines:
        cipher = code.encrypt(line)
        outfile.write(cipher + '\n')
    outfile.close()

def cipher_to_plain():
    '''Gets lines in cipher.txt file and gets cipher user wants to use. Opens
    plain.txt file and decrypts each line and writes the decrypted line into
    plain.txt file.
    '''
    
    lines = get_lines('cipher.txt')
    code = get_cipher()
    outfile = open('plain.txt', 'a')
    for line in lines:
        plain = code.decrypt(line)
        outfile.write(plain + '\n')
    outfile.close()

def main():
    '''Prints available conversions. Gets and validates users choice. If user
    chooses 'Plaintext -> Ciphertext', it instructs the user to enter plaintext
    into plain.txt file, and after pressing ENTER, runs plain_to_cipher() and
    tells user to open cipher.txt to see ciphertext. If user chooses
    'Ciphertext -> Plaintext', it instructs the user to enter ciphertext
    into cipher.txt file, and after pressing ENTER, runs cipher_to_plain() and
    tells user to open plain.txt to see plaintext.
    '''
    
    print('''Available Conversions:
1: Plaintext -> Ciphertext
2: Ciphertext -> Plaintext''')
    conversion = input("Choose a cipher conversion: ")
    while conversion not in ['1', '2']:
        print('Invalid. Try again')
        conversion = input("Choose a cipher conversion: ")
    print()
    if conversion == '1':
        input("Input your plaintext into the plain.txt file and press ENTER to continue.")
        plain_to_cipher()
        print("\nOpen the cipher.txt file to see the ciphertext")
    elif conversion == '2':
        input("Input your ciphertext into the cipher.txt file and press ENTER to continue.")
        cipher_to_plain()
        print("\nOpen the plain.txt file to see the plaintext")

if __name__ == '__main__':
    main()
