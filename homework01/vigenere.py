def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    count = 0
    while len(keyword) < len(plaintext):
        keyword += keyword
    keyword = keyword.upper()
    for el in plaintext:
        if not el.isalpha():                                    #проверка, сост ли строка только из букв симв
            ciphertext += el
        else:
            k1 = ord(keyword[count])
            k2 = ord(el)
            k3 = k2 + (k1 - ord('A'))
            if el.isupper():
                if k3 > ord('Z'):
                    k3 -= 26
            else:
                if k3 > ord('z'):
                    k3 -= 26
            ciphertext += chr(k3)
        count += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    count=0
    while len(keyword)<len(ciphertext):
            keyword+=keyword
    keyword = keyword.upper()
    for el in ciphertext:
        if not el.isalpha():
            plaintext+=el
        else:
            k1=ord(keyword[count])
            k2=ord(el)
            k3=k2-(k1-ord('A'))
            if el.isupper():
                if k3 < ord('A'):
                    k3 += 26
            else:
                if k3 < ord('a'):
                    k3 += 26
            plaintext+=chr(k3)
        count+=1
    return plaintext
