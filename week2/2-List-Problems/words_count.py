word = input("Enter word: ")
n = input("Enter count of words: ")
n = int(n)

count = 1
words = []

while count <= n:
    new_word = input("Enter new word: ")
    words += [new_word]

    count += 1

count_of_word = 0
for w in words:
    if w == word:
        count_of_word += 1

print("Word \"{}\" is found {} times in {}".format(word, count_of_word, words))
