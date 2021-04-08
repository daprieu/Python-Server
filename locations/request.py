LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North Galactic Base",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "name": "Nashville Kennels East",
        "address": "615 East Nasty Street",
        "id": 3
    },
    {   
        "name": "Nashville Kennels West",
        "address": "999 Western side ct",
        "id": 4
    },
    {
        "name": "Alderaan",
        "address": "0 and gone street",
        "id": 5
    }
]


def get_all_locations():
    return LOCATIONS

    # Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_locations = location

    return requested_location