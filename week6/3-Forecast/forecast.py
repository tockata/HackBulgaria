def forecast(days):
    weather = { "sunshine": 0, "rain": 0, "snow": 0 }

    for i in range(0, len(days)):
        if days[i] == "sunshine":
            weather["sunshine"] += 1
        if days[i] == "rain":
            weather["rain"] += 1
        if days[i] == "snow":
            weather["snow"] += 1

    if weather["sunshine"] > weather["rain"] and weather["sunshine"] > weather["snow"]:
        return "sunshine"
    if weather["rain"] > weather["sunshine"] and weather["rain"] > weather["snow"]:
        return "rain"
    if weather["snow"] > weather["sunshine"] and weather["snow"] > weather["rain"]:
        return "snow"
    if weather["sunshine"] == weather["rain"] and weather["rain"] == weather["snow"]:
        return days[len(days) - 1]
    if weather["sunshine"] == weather["rain"]:
        return "snow"
    if weather["rain"] == weather["snow"]:
        return "sunshine"
    if weather["sunshine"] == weather["snow"]:
        return "rain"

print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))