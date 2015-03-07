def sublist(list1, list2):
    if len(list1) == 0:
        return True

    is_sublist = False

    for i in range(0, len(list2) - len(list1)):
        is_sublist = True
        for j in range(0, len(list1)):
            if list1[j] != list2[j + i]:
                is_sublist = False

        if is_sublist == True:
            return True

    return False

print(sublist([], [0, 0, 1, 2, 3, 5, 6]))
print(sublist([1, 2, 3], [0, 0, 1, 2, 3, 5, 6]))
print(sublist(["Python"], ["Python", "Django"]))
print(sublist(["Python", "Django"], ["Django", "Python"]))
print(sublist([1,2], [1, 0, 1, 2, 2]))
