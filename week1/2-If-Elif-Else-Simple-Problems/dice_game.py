from random import randint

number = int(input("Enter dice side: "))
player1_name = input("Enter player1 name: ")
player2_name = input("Enter player2 name: ")

player1_rolls = randint(1, number)
print(player1_name + " rolls: " + str(player1_rolls))
player2_rolls = randint(1, number)
print(player2_name + " rolls: " + str(player2_rolls))

if player1_rolls == player2_rolls:
    print("Equals")
elif player1_rolls > player2_rolls:
    print(player1_name + " wins!")
elif player2_rolls > player1_rolls:
    print(player2_name + " wins!")