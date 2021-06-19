# https://rapidapi.com/collection/list-of-free-apis
# https://rapidapi.com/warting/api/currency-converter/

import requests
from requests.exceptions import HTTPError
from pprint import pprint


def get_weather_api_data(lon, lat, units="metric", lang="en"):
    result = {}
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
    # Api uzklausos parametrai ishsaugojami dictionary tipo strukturoje,
    # kuria paduoda request funkcijai kaip params parametra
    querystring = {"lon": str(lon), "lat": str(lat), "units": units, "lang": lang}
    # Api raktas pridedamas i request headeri kaip x-rapidapi-key, tai specifiska pagal Api tiekeja
    # ir randama jo tinkalapio dokumentacijoje.
    headers = {
        'x-rapidapi-key': "f677aeeac1mshd2e756e85ff708dp1189dajsn297c80913788",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

    try:
        # Pats kreipimasis duomenu is interneto, naudojant requests.request funkcija,
        # requests - populiari pitono interneto biblioteka
        result = requests.request("GET", url, headers=headers, params=querystring)
        # If the response was successful, no Exception will be raised
        result.raise_for_status()
        # .json() pavercia atsakyma i dictionary tipo duomenu struktura
        result = result.json()

    # Jei bus klaidu, mums atspausdins pranesima, bet programa nenulus,
    # o funkcija grazins tuscia dictionary
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6

    return result


if __name__ == "__main__":
    # Vilniaus koordinates "lon": "25", "lat": "54" +-
    api_response = get_weather_api_data(25, 54)

    print(type(api_response))
    pprint(api_response, indent=4)

# Uzduotis:
# 1. Sukurti funkcija kuri is atsakymo duomenu strukturos istrauks city_name, temp ir weather - description - code
# bei datetime laukus ir grazins mazesni dictionary tik su reikalingais duomenimis.

# 2. Sukurti funkcija kuri pagal salyga (pvz temperatura maziau uz 15 arba weather code 500 (lyja)),
# Suformuotu perspejanti pranesima, isivaizduojamos oru aplikacijos klientams.

# Api atsakymo (api_response) pvz:
# <class 'dict'>
# {   'count': 1,
#     'data': [   {   'app_temp': 12.8,
#                     'aqi': 45,
#                     'city_name': 'Eišiškės',
#                     'clouds': 100,
#                     'country_code': 'LT',
#                     'datetime': '2021-06-12:21',
#                     'dewpt': 11.4,
#                     'dhi': 0,
#                     'dni': 0,
#                     'elev_angle': -12.78,
#                     'ghi': 0,
#                     'h_angle': -90,
#                     'lat': 54,
#                     'lon': 25,
#                     'ob_time': '2021-06-12 21:51',
#                     'pod': 'n',
#                     'precip': 1,
#                     'pres': 986.203,
#                     'rh': 90.6018,
#                     'slp': 1004.68,
#                     'snow': 0,
#                     'solar_rad': 0,
#                     'state_code': '65',
#                     'station': 'EYVI',
#                     'sunrise': '01:41',
#                     'sunset': '18:56',
#                     'temp': 12.8,
#                     'timezone': 'Europe/Vilnius',
#                     'ts': 1623534708,
#                     'uv': 0,
#                     'vis': 2,
#                     'weather': {   'code': 500,
#                                    'description': 'Light rain',
#                                    'icon': 'r01n'},
#                     'wind_cdir': 'W',
#                     'wind_cdir_full': 'west',
#                     'wind_dir': 280,
#                     'wind_spd': 1.75472}]}

