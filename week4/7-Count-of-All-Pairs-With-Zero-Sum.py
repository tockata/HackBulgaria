def count_zero_pairs(numbers):
    count = 0

    for i1 in range(0, len(numbers)):
        for i2 in range(i1, len(numbers)):
            if numbers[i1] + numbers[i2] == 0:
                count += 1

    return count

print(count_zero_pairs([0, 2, -2, 5, 10]))
