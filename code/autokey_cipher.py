def generate_autokey(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()

    if len(key) >= len(plaintext):
        return key + key[:-len(key)] 

    generated_key = ""
    for i in range(len(plaintext) - len(key)):
        generated_key += plaintext[i]
    return key + generated_key


def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def decrypt(cipher_text, key):
    if cipher_text.islower() or key.islower():
        cipher_text = cipher_text.upper()
        key = key.upper()
    cipher_text_l = list(cipher_text)
    key_l = list(key)
    res = []

    for i in range(len(cipher_text_l)):
        y = (ord(cipher_text_l[i]) - ord(key_l[i]) + 26) % 26 + ord('A')
        res.append(chr(y))
        key_l.append(chr(y))

    decrypted_text = "".join(res)
    return decrypted_text


plaintext = "HELLO"
autokey = "N"

    
key = generate_autokey(plaintext, autokey)
cipher_t = cipherText(plaintext,key)

print("Original text: ", plaintext)

print("Cipher text: ",cipher_t)
decrypted_text = decrypt(cipher_t, autokey)
print("Decrypted text: ",decrypted_text)

