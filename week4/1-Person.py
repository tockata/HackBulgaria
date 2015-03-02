person = {}

first_name = input("Enter first name: ")
person["first_name"] = first_name
second_name = input("Enter second name: ")
person["second_name"] = second_name
third_name = input("Enter third name: ")
person["third_name"] = third_name
birth_year = input("Enter birth year: ")
person["birth_year"] = int(birth_year)
person["current_age"] = 2015 - person["birth_year"]

print(person)