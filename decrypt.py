import json
import base64
import os


def decrypt(encrypted_file_name,key_file):
    with open(key_file, 'r') as file:
        key = json.load(file)
        inverse_key = {code: symbol for symbol, codes in key.items() for code in codes}
        code_length = len(list(inverse_key.keys())[0])
    encrypted_file_name = encrypted_file_name.split('/')[-1].replace(".\\","")

    decrypted_file_name = ''
    for symbol_number in range(0,len(encrypted_file_name)-(code_length-1),code_length):
        code = encrypted_file_name[symbol_number:symbol_number + code_length]
        decrypted_file_name += inverse_key[code]
    decrypted_file_name = base64.b32decode(decrypted_file_name)

    extension = b'.tmp'
    decrypted_file = open(decrypted_file_name+extension,'w')
    with open(encrypted_file_name, 'r') as encrypted_file:
        encrypted_file = encrypted_file.read()
        for symbol_number in range(0,len(encrypted_file) - (code_length - 1), code_length):
            code = encrypted_file[symbol_number:symbol_number+code_length]
            decrypted_file.write(inverse_key[code])
    decrypted_file.close()
    with open(decrypted_file_name, 'wb') as decoded_file:
        content = open(decrypted_file_name+extension,'rb').read()
        decoded_file.write(base64.b32decode(content))
        os.remove(decrypted_file_name+extension)
    return decrypted_file_name.decode()
