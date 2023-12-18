lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key=int(input("Enter a Key"))
plain=input("Enter a plaintext")

def encrypt():
    global cp
    cp=""
    for c in plain:
        if c.isalpha() and c.islower():
            cp+=lower[(lower.index(c)+key)%26]
        elif c.isalpha() and c.isupper():
            cp+=upper[(upper.index(c)+key )%26 ]
        else:
            cp+=c
    print("ciphertext",cp)

def decrypt():
    global p
    p=""
    for c in cp:
        if c.isalpha() and c.islower():
            p+=lower[(lower.index(c)-key)%26]
        elif c.isalpha() and c.isupper():
            p+=upper[(upper.index(c)-key)%26]
        else:
            p+=c
    print("ciphertext",p)
encrypt()
decrypt()
