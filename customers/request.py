CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "hHall@gmail.com"
    },
    {
        "id": 2,
        "name": "Darth Maul",
        "address": "7002 Dathomir Dr",
        "email": "Maul@DualSaber.net"
    },
    {
        "id": 3,
        "name": "Darth Vader",
        "address": "222 Deathstar Cir",
        "email": "LordVader@e-mpire.com"
    },
    {
        "id": 4,
        "name": "Moff Gideon",
        "address": "7002 Gideon Ct",
        "email": "DarkSaber@Mine.com"
    },
    {
        "email": "asdf@asdfa.com",
        "name": "asdf asdf",
        "address": "asdfa",
        "id": 7
    }
]

def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found location, if it exists
    requested_customer = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer