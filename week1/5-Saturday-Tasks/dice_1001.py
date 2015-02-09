from random import randint

maria_score = 1001
ivan_score = 1001
winner_found = False

while not winner_found:
    tempSumMaria = 0
    tempSumIvan = 0
    diceCountMaria = 5
    diceCountIvan = 5

    while diceCountMaria > 0:
        roll = randint(1, 6)
        tempSumMaria += roll
        diceCountMaria -= 1
    if maria_score > 0:
        maria_score -= tempSumMaria
        print("Maria: current roll sum = {}, current score = {}".format(tempSumMaria, maria_score))
    elif maria_score < 0:
        maria_score += tempSumMaria
        print("Maria: current roll sum = {}, current score = {}".format(tempSumMaria, maria_score))
    if maria_score == 0:
        print("Maria wins!")
        winner_found = True
        break

    while diceCountIvan > 0:
        roll = randint(1, 6)
        tempSumIvan += roll
        diceCountIvan -= 1
    if ivan_score > 0:
        ivan_score -= tempSumIvan
        print("Ivan: current roll sum = {}, current score = {}".format(tempSumIvan, ivan_score))
    elif ivan_score < 0:
        ivan_score += tempSumIvan
        print("Ivan: current roll sum = {}, current score = {}".format(tempSumIvan, ivan_score))
    if ivan_score == 0:
        print("Ivan wins!")
        winner_found = True
        break