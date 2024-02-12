def generateKey(string,key):
    given_key = key
    key = list(key)
    if len(string)==len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i%len(given_key)])
    return "".join(key)  
   
def cipher_text(string, key):
    res = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i]))%26 + ord('A')
        res.append(chr(x))
    return "".join(res)

def plain_text(string, key):
    res = []
    for i in range(len(string)):
        x = (ord(string[i]) - ord(key[i])+26)%26 + ord('A')
        res.append(chr(x))
    return "".join(res)    
    
    
    
string = "SECRET MESSAGE"
keyword = "LEMON"

string = string.replace(" ","")
key = generateKey(string,keyword)
print(key)
cipher_text = cipher_text(string, key)
print(f'cipher text is {cipher_text}')

plain_text = plain_text(cipher_text, key)
print(f'plain text is {plain_text}')
