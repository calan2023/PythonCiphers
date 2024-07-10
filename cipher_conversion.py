'''The main module for running the cipher converter. Used for encrypting and
decrypting text in text documents.
'''

import subprocess
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
3: Vigenere
4: Playfair
5: RSA
6: Rabin''')
    cipher = input("Choose a cipher: ")
    while cipher not in ['1', '2', '3', '4', '5', '6']:
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
        key = input("Choose a key for the Vigenere cipher: ")
        cipher = Vigenere(key)
    elif cipher == '4':
        key = input("Choose a key for the Playfair cipher: ")
        cipher = Playfair(key)
    elif cipher == '5':
        p = input("Choose first prime number for the RSA Cryptosystem: ")
        q = input("Choose second prime number for the RSA Cryptosystem: ")
        cipher = RSA(p, q)
    elif cipher == '6':
        p = input("Choose first prime number for the Rabin cipher: ")
        q = input("Choose second prime number for the Rabin cipher: ")
        cipher = Rabin(p, q)
    return cipher

def get_frequency(lines):
    '''Gets the number of times each letter appears in a text string.

    Args:
        lines (str): The text string

    Returns:
        frequency (dict): Dictionary containing the frequency of each letter
        in the text string
    '''
    
    frequency = {}
    for line in lines:
        line = line.lower()
        for letter in line:
            if letter in frequency.keys():
                frequency[letter] += 1
            else:
                if letter in LETTER_VALUES.keys():
                    frequency[letter] = 1
    return frequency

def get_most_frequent(frequency):
    '''Gets the most frequency letter/s and the frequency value/s.

    Args:
        frequency (dict): Dictionary containing the frequency of each letter
        in a text string

    Returns:
        most_frequent (list): A list of tuples containing the most frequent
        letter/s and the corresponding frequency value/s
    '''
    
    most_frequent = [(' ', 0)]
    for key, value in frequency.items():
        if value > most_frequent[0][1]:
            most_frequent = [(key, value)]
        elif value == most_frequent[0][1]:
            most_frequent += [(key, value)]
    return most_frequent
            
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
    '''Gets lines in cipher.txt file. Asks user if they know the cipher to decrypt
    ciphertext. If yes, then it gets cipher user wants to use, opens
    plain.txt file and decrypts each line and writes the decrypted line into
    plain.txt file; if no, then it runs caesar_cipher_crack() and affine_cipher_crack()
    functions.
    '''

    lines = get_lines('cipher.txt')
    knows_cipher = input("\nDo you know the cipher and key that was used to encrypt "\
                         "this text? Enter 'Y' for yes or 'N' for no: ")
    while knows_cipher not in ['Y', 'y', 'N', 'n']:
            print('Invalid. Try again')
            knows_cipher = input("\nDo you know the cipher and key that was used to encrypt "\
                                 "this text? Enter 'Y' for yes or 'N' for no: ")
    if knows_cipher in ['Y', 'y']:
        code = get_cipher()
        outfile = open('plain.txt', 'a')
        for line in lines:
            plain = code.decrypt(line)
            outfile.write(plain + '\n')
        outfile.close()
    else:
        if '_' in lines[0]:
            print("\nRSA encrypted text cannot be cracked")
        else:
            caesar_cipher_crack(lines)
            affine_cipher_crack(lines)

def caesar_cipher_crack(lines):
    '''Gets lines in cipher.txt file, puts the frequency of each letter in a
    dictionary, finds which letters are the most common, and for each of those
    letters, calculates key for Caesar cipher and decrypts each line and writes
    the decrypted line into plain.txt file.

    Args:
        lines (list): List containing each line of text in cipher.txt file
    '''
    
    frequency = get_frequency(lines)
    most_frequent = get_most_frequent(frequency)
    outfile = open('plain.txt', 'a')
    for i in most_frequent:
        key = (LETTER_VALUES[i[0]] - LETTER_VALUES['e']) % NUM_LETTERS
        code = Caesar(key)
        for line in lines:
            plain = code.decrypt(line)
            outfile.write(plain + '\n')
        outfile.write(f'(Decrypted using Caesar({key}))' + '\n')
    outfile.close()

def affine_cipher_crack(lines):
    '''Gets lines in cipher.txt file, puts the frequency of each letter in a
    dictionary, finds which letters are the most common and second most common,
    and for each of those letters, calculates Key A and Key B for Affine cipher
    and decrypts each line and writes the decrypted line into plain.txt file.

    Args:
        lines (list): List containing each line of text in cipher.txt file
    '''
    
    frequency = get_frequency(lines)
    most_frequent = get_most_frequent(frequency)
    for i in most_frequent:
        del frequency[i[0]]
    next_frequent = get_most_frequent(frequency)
    outfile = open('plain.txt', 'a')
    for m in most_frequent:
        for n in next_frequent:
            key_a = VALUE_INVERSES[LETTER_VALUES['t'] - LETTER_VALUES['e']]\
                    * (LETTER_VALUES[n[0]] - LETTER_VALUES[m[0]])\
                    % NUM_LETTERS
            key_b = (LETTER_VALUES[m[0]] - (LETTER_VALUES['e'] * key_a))\
                    % NUM_LETTERS
            if (key_a in VALUE_INVERSES) and (0 <= key_b <= NUM_LETTERS-1):
                code = Affine(key_a, key_b)
                for line in lines:
                    plain = code.decrypt(line)
                    outfile.write(plain + '\n')
                outfile.write(f'(Decrypted using Affine({key_a}, {key_b}))' + '\n')
    outfile.close()

def main():
    '''Prints available conversions. Gets and validates users choice. If user
    chooses 'Plaintext -> Ciphertext', it opens plain.txt, instructs the user
    to enter plaintext, and after pressing ENTER, runs plain_to_cipher() and
    opens cipher.txt to show ciphertext. If user chooses
    'Ciphertext -> Plaintext', it opens cipher.txt, instructs the user to
    enter ciphertext, and after pressing ENTER, runs cipher_to_plain() and
    opens plain.txt to show plaintext. Gets and validates users choice to do
    another conversion, and closes plain.txt and cipher.txt. If user inputs 'Y',
    process repeats, and if user inputs 'N', program stops.
    '''

    running = True
    while running:
        print('''Available Conversions:
1: Plaintext -> Ciphertext
2: Ciphertext -> Plaintext''')
        conversion = input("Choose a cipher conversion: ")
        while conversion not in ['1', '2']:
            print('Invalid. Try again')
            conversion = input("Choose a cipher conversion: ")
        print()
        if conversion == '1':
            first_file = subprocess.Popen('notepad plain.txt')
            input("Input your plaintext into the plain.txt file, save it, "\
                  "and press ENTER in terminal to continue.")
            plain_to_cipher()
            print("\nYou can now see the ciphertext in cipher.txt.")
            second_file = subprocess.Popen('notepad cipher.txt')
        elif conversion == '2':
            first_file = subprocess.Popen('notepad cipher.txt')
            input("Input your ciphertext into the cipher.txt file, save it, "\
                  "and press ENTER in terminal to continue.")
            cipher_to_plain()
            print("\nYou can now see the plaintext in plain.txt.")
            second_file = subprocess.Popen('notepad plain.txt')

        again = input("\nWould you like to do another conversion? Enter 'Y' for yes "\
                      "or 'N' for no: ")
        while again not in ['Y', 'y', 'N', 'n']:
            print('Invalid. Try again')
            again = input("Would you like to do another conversion? Enter 'Y' for yes "\
                          "or 'N' for no: ")
        if again in ['Y', 'y']:
            running = True
        else:
            running = False
        first_file.kill()
        second_file.kill()
        
if __name__ == '__main__':
    main()
