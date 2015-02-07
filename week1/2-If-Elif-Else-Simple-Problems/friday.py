import time

today = time.strftime("%A")
print(today)

if today == "Friday":
    print("It is friday.")
else:
    print("It is not friday ;( Today is {}".format(today))