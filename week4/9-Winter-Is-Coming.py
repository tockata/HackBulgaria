def winter_is_coming(seasons):
    counter = 0

    for season in seasons:
        if season == "winter":
            counter = 0
        else:
            counter += 1

    if counter >= 5:
        return True
    else:
        return False

print(winter_is_coming(["winter", "summer", "summer", "summer", "spring", "spring"]))
print(winter_is_coming(["winter", "summer", "summer", "winter", "spring", "spring"]))