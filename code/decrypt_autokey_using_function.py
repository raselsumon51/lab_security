def decrypt(cipher_text, key):
    if cipher_text.islower() or key.islower():
        cipher_text = cipher_text.upper()
        key = key.upper()
    print(key)
    print(cipher_text)
    cipher_text_l = list(cipher_text)
    key_l = list(key)

    res = []

    for i in range(len(cipher_text_l)):
        y = (ord(cipher_text_l[i]) - ord(key_l[i]) + 26) % 26 + ord('A')
        res.append(chr(y))
        key_l.append(chr(y))  # Use the original key for decryption

    decrypted_text = "".join(res)
    return decrypted_text

# Example usage
cipher_text = 'PTPni'
key = 'n'
decrypted_text = decrypt(cipher_text, key)
print(decrypted_text)
