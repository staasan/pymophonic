import json
import base64


def encrypt(file_name,key_file):
    with open(key_file, 'rb') as file:
        key = json.load(file)
    required_codes = key.copy()
    for symbol in key:
        required_codes[symbol] = 0

    not_encrypted_file_name = base64.b32encode(file_name.split('/')[-1].split('\\')[-1].encode()).decode()
    encrypted_file_name = ''
    for symbol in not_encrypted_file_name:
        encrypted_file_name += key[symbol][required_codes[symbol]]
        required_codes[symbol] = (required_codes[symbol] + 1) % len(key[symbol])

    with open(encrypted_file_name,'w') as encrypted_file:
        not_encrypted_file = base64.b32encode(open(file_name, "rb").read()).decode("utf-8")
        for symbol in key:
            required_codes[symbol] = 0
        for symbol in not_encrypted_file:
            encrypting_letter = key[symbol][required_codes[symbol]]
            required_codes[symbol] = (required_codes[symbol] + 1)%len(key[symbol])
            encrypted_file.write(encrypting_letter)
    return encrypted_file_name
