book1_name = "Pragmatic Thinking and Learning"
book1_price = 30
book2_name = "Learn You a Haskell"
book2_price = 0
book3_name = "The Healthy Programmer"
book3_price = 50
book4_name = "Code Complete"
book4_price = 60
book5_name = "The Pragmatic Programmer"
book5_price = 20
book6_name = "Pro Git"
book6_price = 0
book7_name = "Introduction to Algorithms"
book7_price = 80
book8_name = "Concrete Mathematics"
book8_price = 100

book_dictionary = {book1_name: book1_price,
                  book2_name: book2_price,
                  book3_name: book3_price,
                  book4_name: book4_price,
                  book5_name: book5_price,
                  book6_name: book6_price,
                  book7_name: book7_price,
                  book8_name: book8_price}

# print every available book with its price:
for book_name, book_price in book_dictionary.items():
    print("Book name: {}, price: {}".format(book_name, book_price))

print("")

# what is total price of all books:
sum = 0
for book_price in book_dictionary.values():
    sum = sum + book_price
print("Total price: {}\n".format(sum))

# what is total books count:
print("Total books count: {}\n".format(len(book_dictionary)))

# if a one byus Introduction to Algoritims and Concrete Mathematics he gets 25% discount.
# What will be the price?
price_after_discount = book7_price * 0.75 + book8_price * 0.75
print("Price after discount: {}\n".format(price_after_discount))

# With a budget of 150, how many books can be bought, which are these books?
print("With 150 BGN one can bought a maximum of 5 books and there are four variants:")
print("1. {}, {}, {}, {}, {}.".format(book1_name, book2_name, book3_name, book4_name, book6_name))
print("2. {}, {}, {}, {}, {}.".format(book1_name, book2_name, book3_name, book5_name, book6_name))
print("3. {}, {}, {}, {}, {}.".format(book2_name, book3_name, book5_name, book6_name, book7_name))
print("4. {}, {}, {}, {}, {}.".format(book1_name, book2_name, book5_name, book6_name, book8_name))
