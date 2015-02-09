while True:
    points = int(input("Enter test points in range [0...100]: "))
    while points < 0 or points > 100:
        points = int(input("Points must be in range [0...100], try again: "))
    if 0 <= points <= 50:
        print("Слаб 2")
    elif 51 <= points <= 60:
        print("Среден 3")
    elif 61 <= points <= 70:
        print("Добър 4")
    elif 71 <= points <= 80:
        print("Много добър 5")
    elif 81 <= points <= 99:
        print("Отличен 6")
    else:
        print("Много отличен 7")
