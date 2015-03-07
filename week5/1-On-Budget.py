def on_budget(books, budget):
    sorted_books = sorted(books)
    total_books_price = sum(books)
    current_sum = 0
    count = 0

    result = {}

    for price in sorted_books:
        if (current_sum + price) <= budget:
            current_sum += price
            count += 1
        else:
            break

    loan = total_books_price - current_sum - (budget - current_sum)

    result["books_on_budget"] = count

    if loan > 0:
        result["loan"] = loan
    else:
        result ["loan"] = 0

    return result

print(on_budget([0, 10, 100, 5, 3, 8, 25], 35))
print(on_budget([0, 0, 0], 10))
print(on_budget([50, 60, 100], 20))