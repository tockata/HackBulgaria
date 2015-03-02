def count_words(words):
    result_dictionary = {}
    for wordToCheck in words:
        count = 0
        for word in words:
            if wordToCheck == word:
                count += 1

        if wordToCheck not in result_dictionary:
            result_dictionary[wordToCheck] = count

    return result_dictionary

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))