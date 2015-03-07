def status_count(students):
    result = {
        "finalized": [],
        "not-finalized": []
    }

    for student in students:
        if student["status"] == "finalized":
            result["finalized"] += [student["name"]]
        else:
            result["not-finalized"] += [student["name"]]

    return result

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }]

print(status_count(students))