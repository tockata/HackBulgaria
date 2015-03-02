# from test_data import generate_test

def get_people_count(activity):
    result_dictionary = {}
    for name in activity:
        result_dictionary[name] = None

    return len(result_dictionary)

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))