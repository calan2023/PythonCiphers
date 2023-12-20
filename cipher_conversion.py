from ciphers import *

def get_lines(file):
    infile = open(file)
    lines = infile.read().splitlines()
    infile.close()
    return lines

def get_cipher():
    print('''Available Ciphers:
1: Caesar
2: Affine''')
    cipher = input("Choose a cipher: ")
    while cipher not in ['1', '2']:
        print('Invalid. Try again')
        cipher = input("Choose a cipher: ")
        
    if cipher == '1':
        key = input("Choose a key for the Caesar cipher: ")
        while not key.isnumeric():
            print('Invalid. Try again')
            key = input("Choose a key for the Caesar cipher: ")
        key = int(key)
        cipher = Caesar(key)
        
    elif cipher == '2':
        a = input('Choose Key A for the Affine cipher: ')
        while not a.isnumeric():
            print('Invalid. Try again')
            a = input('Choose Key A for the Affine cipher: ')
        a = int(a)
        
        b = input('Choose Key B for the Affine cipher: ')
        while not b.isnumeric():
            print('Invalid. Try again')
            b = input('Choose Key B for the Affine cipher: ')
        b = int(b)
        
        cipher = Affine(a, b)
    return cipher
            
def plain_to_cipher():
    lines = get_lines('plain.txt')
    code = get_cipher()
    outfile = open('cipher.txt', 'a')
    for line in lines:
        cipher = code.encrypt(line)
        outfile.write(cipher + '\n')
    outfile.close()

def cipher_to_plain():
    lines = get_lines('cipher.txt')
    code = get_cipher()
    outfile = open('plain.txt', 'a')
    for line in lines:
        plain = code.decrypt(line)
        outfile.write(plain + '\n')
    outfile.close()
