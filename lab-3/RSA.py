import random
import math

def RSA(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    e = 0
    for i in range(2, z):
        if math.gcd(i, z) == 1:
            e = i
            break
    d = 0
    for i in range(z):
        x = 1+(i*z)
        if x % e == 0:
            d = int(x / e)
            break
    return [e, n], [d, n]



def primeNumber():
    while True:
        num = random.randint(11, 999)
        if  millerRabin(num, 10000) is True: 
            return num



def millerRabin(n, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    
    while s % 2 == 0:
        r += 1
        s //= 2
        
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
        
    return True


def encrypt(text, key):
    encryptText = []
    for m in text:
        encryptText.append(pow(ord(m), key[0]) % key[1])
    return encryptText

def decrypt(text, key):
    decryptText = ''
    for m in text:
        decryptText += chr(pow(m, key[0]) % key[1])
    return decryptText

text = "Поехали в Америку!!!" 

publicKey, privateKey = RSA(primeNumber(), primeNumber())
encryptedText = encrypt(text, publicKey)
decryptedText = decrypt(encryptedText, privateKey)



print('Public Key:', publicKey)
print('Private Key:', privateKey)
print("Encrypted text: ", encryptedText)
print('Decrypted text:', decryptedText)