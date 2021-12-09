# dictionary of name/number pairs
rolodex = {
    "Aaron": 5556069,
    "Abby": 5556070,
    "Adam": 5556071,
    "Adrian": 5556072,
    "Aidan": 5556073,
    "Aiden": 5556074,
    "Ainsley": 5556075,
    "Alastair": 5556076,
    "Alistair": 5556077,
}

# Retrieve value based on key
rolodex["Verne"]
hash("Verne")

# Add new key and value
rolodex["Verne"] = 5556078
rolodex["Adam"] = (5556071, 5556072)
rolodex["David (Amanda)"] = 5556079


def caller_id(lookup_number):
    for name, number in rolodex.items():
        if number == lookup_number:
            return name
