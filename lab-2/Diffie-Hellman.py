import random
import math

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

class DiffieHellman(object):
    
    def __init__(self, publicKeyOne, publicKeyTwo, privateKey):
        self.publicKeyOne = publicKeyOne
        self.publicKeyTwo = publicKeyTwo
        self.privateKey = privateKey
        self.fullKey = None
        
        
    def generatePartKey(self):
        return (self.publicKeyOne ** self.privateKey) % self.publicKeyTwo
    
    
    def generatFullKey(self, partKeyR):
        self.fullKey = (partKeyR ** self.privateKey) % self.publicKeyTwo
        
        return self.fullKey
    
    
    def encrypt(self, message):
        encrypted_message = ""
        key = self.fullKey
        
        for c in message:
            encrypted_message += chr(ord(c)+key)
            
        return encrypted_message
    
    
    def decrypt(self, message):
        decrypted_message = ""
        key = self.fullKey
        
        for c in message:
            decrypted_message += chr(ord(c)-key)
            
        return decrypted_message

message = "Поехали в Америку!!!"

m = 1000
a1 = 0
a2 = 0
a3 = 0
a4 = 0

while True:
    
    if(millerRabin(random.randint(2, m-1),m) and not a1):
        AlisaPublicKey = random.randint(2, m-1)
        print('AlisaPublicKey:', AlisaPublicKey)
        a1 = 1
        
    if(millerRabin(random.randint(2, m-1),m)and not a2):
        AlisePrivateKey = random.randint(2, m-1)
        print('AlisePrivateKey:', AlisePrivateKey)
        a2 = 1
        
    if(millerRabin(random.randint(2, m-1),m) and not a3):
        BobPublicKey = random.randint(2, m-1)
        print('BobPublicKey:', BobPublicKey)
        a3 = 1
        
    if(millerRabin(random.randint(2, m-1),m) and not a4):
        BobPrivateKey = random.randint(2, m-1)
        print('BobPrivateKey:', BobPrivateKey)
        a4 = 1
        
    if(a1 and a2 and a3 and a4): break

Alisa = DiffieHellman(AlisaPublicKey, BobPublicKey, AlisePrivateKey)
Bob = DiffieHellman(AlisaPublicKey, BobPublicKey, BobPrivateKey)

AlisaPartKey = Alisa.generatePartKey()
BobPartKey = Bob.generatePartKey()
AlisaFullKey = Alisa.generatFullKey(BobPartKey)
BobFullKey = Bob.generatFullKey(AlisaPartKey)
BobEncrypted = Bob.encrypt(message)
message = Alisa.decrypt(BobEncrypted)

print(AlisaPartKey)
print(BobPartKey)
print(AlisaFullKey)
print(BobFullKey)
print(BobEncrypted)
print(message)