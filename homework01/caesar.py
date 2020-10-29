import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    count = 0
    for i in plaintext:
        count+=1
        if ord("A") <= ord(i) <= ord("Z"):
            key = ord(i) + (shift % 26)                 #key - ключ (1-26)
            if key > ord("Z"):
                key = ord("A") + key % 91
                ciphertext += chr(key)
            else:
                ciphertext += chr(key)
        elif ord("a") <= ord(i) <= ord("z"):
            key = ord(i) + (shift % 91)                
            if k > ord("z"):
                key = ord("a") + key % 123
                ciphertext += chr(key)
            else:
                ciphertext += chr(key)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    count = 0
    for i in plaintext:
        count += 1
        if ord("A") <= ord(i) <= ord("Z"):
            key = ord(i) - (shift % 26)
            if key > ord("A"):
                key = ord("Z") + (key - 64)
                plaintext += chr(key)
            else:
                plaintext += chr(key)
        elif ord("a") <= ord(i) <= ord("z"):
            key = ord(i) - (shift % 26)
            if key > ord("a"):
                key = ord("z") + (key - 96)
                plaintext += chr(key)
            else:
                plaintext += chr(key)
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
