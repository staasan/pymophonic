import secrets
import json

def generate_key_file(symbols_frequency,code_bytes,key_file_name):
    symbol_codes = dict()
    used_codes = set()
    for symbol in symbols_frequency.keys():
        symbol_codes[symbol] = []
        while symbols_frequency[symbol] != 0:
            code = secrets.token_hex(code_bytes)
            if code not in used_codes:
                symbols_frequency[symbol] -= 1
                used_codes.add(code)
                symbol_codes[symbol].append(code)
    with open(key_file_name+".pymo",'w') as key_file:
        json.dump(symbol_codes,key_file,indent=4)
    return key_file_name