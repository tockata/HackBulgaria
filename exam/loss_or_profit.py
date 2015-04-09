def loss_or_profit(income, outcome):
    total_income = 0
    total_outcome = 0

    for x in range(0, len(income)):
        total_income += income[x]

    for x in range(0, len(outcome)):
        total_outcome += outcome[x]

    result = total_income - total_outcome
    if result > 0:
        print("+" + str(result))
    elif result == 0:
        print("=0")
    else:
        print(result)

loss_or_profit([1, 2, 3], [3])
loss_or_profit([10], [20, 30])
loss_or_profit([10], [10])
