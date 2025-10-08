import base64

def symbol_frequency(file_name,codes_amount):
    with open(file_name, 'rb') as file:
        encoded_file = base64.b64encode(file.read()).decode('utf-8')
        all_symbols = base64.b64encode(file_name.encode('utf-8')).decode()+encoded_file
    symbols_list = [x for x in sorted(set(all_symbols))]
    symbols_frequency = dict()
    for i in range(0,len(symbols_list)):
        symbol = symbols_list[i]
        symbols_frequency[symbol] = all_symbols.count(symbol)
    frequency_relations = symbols_frequency.copy()
    for symbol in symbols_frequency.keys():
        frequency_relations[symbol] = int(((symbols_frequency[symbol]/sum(symbols_frequency.values()))*codes_amount))
        if not frequency_relations[symbol]:
            frequency_relations[symbol] += 1
    return frequency_relations