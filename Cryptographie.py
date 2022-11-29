#coding:utf-8

def crypt_char(char, key):

    char = char.upper()
    key = key.upper()
    
    key_position = ord(key) - 65
    char_position = ord(char) - 65

    position = ( key_position + char_position ) % 26

    char_crypt = chr(position+65)
    return char_crypt

def crypt_string(string, key):
    
    i = 0
    crypt_texte = ""

    while( i < len(string) ):

        bloc = string[i:i+len(key)]

        j = 0
        for lettre in bloc:
            crypt_texte = crypt_texte + crypt_char(lettre, key[j])
            j+=1

        i+=len(key)

    return crypt_texte.lower()


texte = input("Entrer votre texte : ")
cle = input("Entrer votre cle : ")

print("La forme cryptée est : " + crypt_string(texte, cle))