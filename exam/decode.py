def decode_word(encrypted_word, cipher):
    result = ""

    for x in range(0, len(encrypted_word)):
        for k, v in cipher.items():
            if encrypted_word[x] == v or isinstance(v, list) and encrypted_word[x] in v:
                result += k

    print(result)

decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'})
decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'})
decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'})
decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'})
