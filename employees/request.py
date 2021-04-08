EMPLOYEES = [
    {
        "id": 1,
        "name": "Emma Beaton",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Samual L. Jackson",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Hayden Christensen",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Ewan McGregor",
        "locationId": 1
    },
    {
        "name": "Carrie Fisher",
        "locationId": 3,
        "id": 5
    },
    {
        "name": "Natalie Portman",
        "location": 4,
        "id": 6
    },
    {
        "id": 7,
        "name": "George Lucas",
        "locationId": 3
    }
]

def get_all_employees():
    return EMPLOYEES

    # Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found location, if it exists
    requested_employee = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee