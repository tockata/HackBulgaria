def calculate_coins(sum):
    sum = round(sum * 100)
    coins = [100, 50, 20, 10, 5, 2, 1]
    result_dictionary = {}

    for coin in coins:
        count = sum // coin
        result_dictionary[coin] = count
        sum -= count * coin

    return result_dictionary

print(calculate_coins(8.94))
print(calculate_coins(0.53))