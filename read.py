import base64

def symbol_frequency(file_name,codes_amount):
    with open(file_name, 'rb') as file:
        encoded_file = base64.b32encode(file.read()).decode('utf-8')
        all_symbols = base64.b32encode(file_name.encode('utf-8')).decode()+encoded_file
    symbols_list = [x for x in sorted(set(all_symbols))]
    symbols_frequency = dict()
    for i in range(0,len(symbols_list)):
        symbol = symbols_list[i]
        symbols_frequency[symbol] = all_symbols.count(symbol)
    codes_frequency = symbols_frequency.copy()
    for symbol in symbols_list:
        codes_frequency[symbol] = int((symbols_frequency[symbol]/sum(symbols_frequency.values()))*codes_amount)
        if codes_frequency[symbol] < 2: codes_frequency[symbol] = 2
    for i in range(0,sum(codes_frequency.values())-codes_amount):
        codes_frequency[max(codes_frequency, key=codes_frequency.get)] -= 1
    for i in range(0,codes_amount-sum(codes_frequency.values())):
        codes_frequency[min(codes_frequency, key=codes_frequency.get)] += 1
    return codes_frequency