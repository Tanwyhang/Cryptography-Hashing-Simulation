import string
import json
import os

unhashed, hashed = 0, 1
chars = string.printable
# fix a hashingn system
hashed_chars = ['C', 'M', '0', '7', '+', 'F', 'e', 'U', 'P', '_', '/', '=',
                ')', 'f', '9', '{', 'r', 't', ':', '[', 'z', 'x', 'X', 'o',
                '&', 'T', 'y', ' ', '8', '\x0b', '6', 'n', '#', 'W', 'd',
                '\t', '\n', '1', '$', 'p', 'h', 'N', '4', ',', '2', 'j', 
                'a', 'K', 'E', 'Y', 'A', '\\', 'R', 'i', '^', '*', 'g', 'c',
                '3', 'G', '?', '>', 'I', 'u', 's', ';', 'k', '\r', '"', '%',
                '<', '-', 'B', '.', '@', '5', 'b', "'", '`', 'Q', 'v', 'Z',
                'm', 'D', '}', ']', 'w', 'L', 'O', 'V', '~', '\x0c', '!',
                '|', 'S', 'l', 'H', 'J', 'q', '(']

keys = list(zip(chars, hashed_chars))

def out(s):
    return s + '>>> '

def encrypt(password):
    encrypted_password = ''
    for i in password:
        current_key = keys[chars.index(i)]
        encrypted_password += current_key[hashed]
    return encrypted_password

def decrypt(password):
    decrypted_password = ''
    for i in password:
        current_key = keys[hashed_chars.index(i)]
        decrypted_password += current_key[unhashed]
    return decrypted_password

def add_user(username:str, password:str):

    with open('data.json', 'r') as data: #load users
        userdat = json.load(data)

    # encrypt password + update user data
    encrypted_password = encrypt(password)
    new_userinfo = {username:encrypted_password}
    userdat.update(new_userinfo)  # update() adds elements from new_info to {old_info}
    userdat = json.dumps(userdat) # format python -> json

    # write user data
    with open('data.json', 'w') as data:
        data.write(userdat)

def show_info(username):
    with open('data.json', 'r') as data: #load users
        userdat = json.load(data)
    return userdat[username]
    

add_user('wyhang', 'wyhang1234')
print(show_info('wyhang'))