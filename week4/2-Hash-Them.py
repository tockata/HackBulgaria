def hash_them(keys, values):
    countValues = len(values)
    indexValues = 0
    result_dictionary = {}
    for index in keys:
        if indexValues <= countValues - 1:
            result_dictionary[index] = values[indexValues]
            indexValues += 1
        else:
            result_dictionary[index] = None

    return result_dictionary

print(hash_them(["Ivan", "Maria"], [1, 2]))
print(hash_them(["Ivan", "Maria"], [1]))