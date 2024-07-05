'''The module containing extra functions used in other modules for checking if
a number is prime, checking if a number is invertible, and doing fast
exponentiation calculations.
'''

import random

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
