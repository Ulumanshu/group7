api_response = {'a': 1, 'b': 2, 'c': 3, 'weather': {'temp': None, 'sky': 'clear'}}
weather = api_response.get('weather', {}) or {}
temp = weather.get('temp', 0) or 0
sky = weather.get('sky', 0) or 0
print(weather, temp, sky)