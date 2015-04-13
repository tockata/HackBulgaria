def decode_word(encrypted_word, cipher):
    result = ""

    for x in range(0, len(encrypted_word)):
        for key, value in cipher.items():
            if encrypted_word[x] == value:
                result += key

    return result

print(decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))
print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}))
print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))
print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))
