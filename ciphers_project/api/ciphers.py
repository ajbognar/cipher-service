def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        c_encoded = ""
        if(c == " "):
            c_encoded = " "
        elif(c.isupper()):
            c_encoded = ((ord(c) + shift - 65) % 26 + 65)
            c_encoded = chr(c_encoded)
        else:
            c_encoded = ((ord(c) + shift - 97) % 26 + 97)
            c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text