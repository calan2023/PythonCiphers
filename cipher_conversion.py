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
        cipher = Caesar(key) 
    elif cipher == '2':
        a = input('Choose Key A for the Affine cipher: ')
        b = input('Choose Key B for the Affine cipher: ')
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

def main():
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
