def count_vowels_consonants(word):
    vowels = "aeiouyAEIOUY"
    result_dictionary = {"vowels": 0, "consonants": 0}
    for char in word:
        if char in vowels:
            result_dictionary["vowels"] += 1
        else:
            result_dictionary["consonants"] += 1

    return result_dictionary

print(count_vowels_consonants("aaaAcccD"))

