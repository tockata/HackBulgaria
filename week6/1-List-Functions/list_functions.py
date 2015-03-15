def head(list):
    return list[0]

print(head([1,2,3]))
print(head(["Python"]))

def last(list):
    return list[len(list) - 1]

print(last([1,2,3]))
print(last(["Python"]))

def tail(list):
    del list[0]
    return list

print(tail([1, 2, 3]))
print(tail(["Python"]))

def equal_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(0, len(list1)):
        if list1[i] != list2[i]:
            return False

    return True

print(equal_lists([1, 2], [1, 2]))
print(equal_lists([1, 2], [2, 1]))
print(equal_lists([], []))
print(equal_lists([1, 2], [1, 2, 3]))

def count_item(element, list):
    count = 0

    for i in range(0, len(list)):
        if list[i] == element:
            count += 1

    return count

print(count_item(5, [1, 2, 3, 4, 5]))
print(count_item("winter", ["winter", "winter"]))
print(count_item(False, [True, True]))

def take(n, list):
    if n > len(list):
        return list

    result_list = []
    for i in range(0, n):
        result_list.append(list[i])

    return result_list

print(take(2, [1, 2, 3, 4, 5]))
print(take(3, [3, 4, 5, 6, 7, 8]))
print(take(10, [1]))

def drop(n, list):
    if n > len(list):
        return []

    result_list = []
    for i in range(n, len(list)):
        result_list.append(list[i])

    return result_list

print(drop(1, [1, 2, 3]))
print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
print(drop(10, [1]))

def reverse(list):
    result_list = []

    for i in range(len(list) - 1, -1, -1):
        result_list.append(list[i])

    return result_list

print(reverse(["Speak", "in", "reverse", "you", "must!"]))
print(reverse([1, 2, 3]))
print(reverse([]))