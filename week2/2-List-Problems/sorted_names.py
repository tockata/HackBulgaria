n = input("Enter count of names: ")
n = int(n)

count = 1
names = []

while count <= n:
    new_name = input("Enter new name: ")
    names += [new_name]

    count += 1

sorted_names = sorted(names)

print("Sorted names are:")
for name in sorted_names:
    print(name)

