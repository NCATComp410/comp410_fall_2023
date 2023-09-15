import random

# Random data generators
def random_street_name():
    streets = ['Maple', 'Oak', 'Pine', 'Elm', 'Cedar', 'Birch', 'Cherry', 'Walnut', 'Willow', 'Spruce']
    types = ['St.', 'Ave.', 'Rd.', 'Blvd.', 'Ln.', 'Dr.']
    return f"{random.choice(streets)} {random.choice(types)}"

def random_city_name():
    cities = ['Springfield', 'Rivertown', 'Laketown', 'Hillside', 'Greenville', 'Fairview', 'Eldertown', 'Daleville', 'Crestwood', 'Bridgeton']
    return random.choice(cities)

def random_state_code():
    states = ['CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'GA', 'NC', 'MI', 'OH']
    return random.choice(states)

def random_zip_code():
    return ''.join(random.choices('0123456789', k=5))


def random_nsew():
    return random.choice(['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW', '', '', '', '', '', '', ''])

# Generate 1000 random addresses
with open('addresses.txt', 'w') as f:
    for _ in range(1000):
        address = f"{random.randint(1, 9999)} {random_nsew()} {random_street_name()}, {random_city_name()}, {random_state_code()} {random_zip_code()}"
        address = address.replace('  ', ' ')
        f.write(address + '\n')
