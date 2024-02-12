cipher_text = 'PTPni'
key = 'n'

if(cipher_text.islower() or key.islower()):
    cipher_text= cipher_text.upper()
    key =  key.upper()
    

cipher_text_l = list(cipher_text)
key_l = list(key)

res= []
print(len(cipher_text_l))

for i in range(len(cipher_text_l)):
    y = (ord(cipher_text_l[i]) - ord(key_l[i]) + 26) % 26 + ord('A')
    res.append(chr(y))
    key_l.append(chr(y))
res = "".join(res)
print(res)