from string import ascii_letters
a= input("Please enter your text:")
c=int(input("Enter you operation ( 1-encrypt , 2-decrypt):"))
b=int(input("Please enter the number key:"))

def encrypt(string,key):
    scu = ascii_letters
    result = ''
    
    for i in string:
        if i not in scu:
            result += i
        else:
            new_key = (scu.index(i) + key) % len(scu)
            result += scu[new_key]
    return (result)   
def decrypt(string,key):
    key *= -1
    return encrypt(string,key)
if c == 1:
    print (encrypt(a ,b))
else:
    print(decrypt(a,b))








