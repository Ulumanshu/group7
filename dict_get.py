api_response = {'a': 1, 'b': 2, 'c': 3, 'weather': {'temp': '', 'sky': 'clear'}}
weather = api_response.get('weather', {}) or {}
temp = weather.get('temp', 0) or 0
sky = weather.get('sky', 0) or 0
print(weather, temp, sky)


# Tuples can be dictionary keys, sometimes it is very usefull if object properties are only unique together
product_dict = {}
tuple1 = (1234, 'Super Product XM-4450MX')

product_dict[tuple1] = [
    "Alpha Metal",
    'Beta Electronics',
    "Omega Nuclear",
]
print(product_dict)

a = product_dict.get(tuple1)
print(a)

# Rasti pagal dali rakto
for k, v in product_dict.items():
    id_ = k[0]
    name_ = k[1]
    if id_ == 222:
        pass
    if name_ == 'asdf':
        pass
    print(id_, name_, v)

# list comp
tavo_elmentas = [v for k, v in product_dict.items() if k[0] == 1234]
tavo_elmentas = len(tavo_elmentas) > 0 and tavo_elmentas[0] or False
print(tavo_elmentas)
