def max_score(beers, fries):
    sorted_beers = sorted(beers)
    sorted_fries = sorted(fries)
    score = 0

    for index in range(0, len(beers)):
        score += sorted_beers[index] * sorted_fries[index]

    return score

print(max_score([10, 11], [1, 5]))
print(max_score([5], [5]))
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))