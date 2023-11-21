# WeatherBit API Microsesrvice
This is a microservice that I have created for CS 361. This microservice will be implemented by my partner in their program. 

## Communication Contract
* Communication with this microservice will be done using REST API calls. 
* If I make changes to this code I will communicate the changes to my partner and update this ReadMe to reflect correct and current funcitonality.
* If my partner requests any part of this code to be changed to aid in the implementation of her program, I will update the code and update this ReadMe to reflect correct and current functionality. 

## Environment Set Up 

1. Open project terminal
2. Install dependencies:
```
pip install requests
pip install fastapi
pip install "uvicorn[standard]"
```

## REQUEST data 
### Current Weather Request
Pass in the name of a city into the ```get_current_weather``` function. 
```
def get_current_weather(city_current):
    # obtain url with desired city
    url = 'http://127.0.0.1:8001/current/' + city_current
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
```
For instance, if the city "Bellevue is passed into the function. The res.json output will look like this:
```
{'city_name': 'Bellevue', 'country_code': 'US', 'data': [{'app_max_temp': 48.3, 'app_min_temp': 34.9, 'clouds': 57, 'clouds_hi': 80, 'clouds_low': 6, 'clouds_mid': 22, 'datetime': '2023-11-20', 'dewpt': 37.3, 'high_temp': 49.2, 'low_temp': 38.8, 'max_dhi': None, 'max_temp': 49.2, 'min_temp': 35.8, 'moon_phase': 0.603872, 'moon_phase_lunation': 0.26, 'moonrise_ts': 1700516528, 'moonset_ts': 1700467892, 'ozone': 285.2, 'pop': 0, 'precip': 0, 'pres': 1026.1, 'rh': 81, 'slp': 1026.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700493580, 'sunset_ts': 1700526429, 'temp': 42.8, 'ts': 1700485260, 'uv': 0, 'valid_date': '2023-11-20', 'vis': 12.6, 'weather': ...
The output will be long, so I have shortened it for this example. 
```

### Daily Forecast Request
Pass in the name of a city into the ```get_daily_forecast``` function. 
```
def daily_forecast(city_forecast):
    # obtain url with desired city
    url = 'http://127.0.0.1:8001/forecast/' + city_forecast
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
```
For instance, if the city "Bellevue is passed into the function. The res.json output will look like this:
```
{'city_name': 'Bellevue', 'country_code': 'US', 'data': [{'app_max_temp': 48.3, 'app_min_temp': 34.9, 'clouds': 57, 'clouds_hi': 80, 'clouds_low': 6, 'clouds_mid': 22, 'datetime': '2023-11-20', 'dewpt': 37.3, 'high_temp': 49.2, 'low_temp': 38.8, 'max_dhi': None, 'max_temp': 49.2, 'min_temp': 35.8, 'moon_phase': 0.603872, 'moon_phase_lunation': 0.26, 'moonrise_ts': 1700516528, 'moonset_ts': 1700467892, 'ozone': 285.2, 'pop': 0, 'precip': 0, 'pres': 1026.1, 'rh': 81, 'slp': 1026.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700493580, 'sunset_ts': 1700526429, 'temp': 42.8, 'ts': 1700485260, 'uv': 0, 'valid_date': '2023-11-20', 'vis': 12.6, 'weather': {'description': 'Broken clouds', 'code': 803, 'icon': 'c03d'}, 'wind_cdir': 'ENE', 'wind_cdir_full': 'east-northeast', 'wind_dir': 78, 'wind_gust_spd': 4.9, 'wind_spd': 3.4}, {'app_max_temp': 53.1, 'app_min_temp': 36.6, 'clouds': 84, 'clouds_hi': 98, 'clouds_low': 26, 'clouds_mid': 96, 'datetime': '2023-11-21', 'dewpt': 37.8, 'high_temp': 54.2, 'low_temp': 44.7, 'max_dhi': None, 'max_temp': 54.2, 'min_temp': 38.8, 'moon_phase': 0.718257, 'moon_phase_lunation': 0.29, 'moonrise_ts': 1700604068, 'moonset_ts': 1700559118, 'ozone': 295.7, 'pop': 85, 'precip': 0.399, 'pres': 1020.3, 'rh': 73, 'slp': 1020.5, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700580065, 'sunset_ts': 1700612774, 'temp': 46.2, 'ts': 1700553660, 'uv': 1.3, 'valid_date': '2023-11-21', 'vis': 12.3, 'weather': {'description': 'Moderate rain', 'code': 501, 'icon': 'r02d'}, 'wind_cdir': 'SSE', 'wind_cdir_full': 'south-southeast', 'wind_dir': 164, 'wind_gust_spd': 8.3, 'wind_spd': 5.6}, {'app_max_temp': 48.2, 'app_min_temp': 38.9, 'clouds': 77, 'clouds_hi': 71, 'clouds_low': 45, 'clouds_mid': 73, 'datetime': '2023-11-22', 'dewpt': 43.9, 'high_temp': 49, 'low_temp': 40.8, 'max_dhi': None, 'max_temp': 49, 'min_temp': 41.3, 'moon_phase': 0.819552, 'moon_phase_lunation': 0.32, 'moonrise_ts': 1700691503, 'moonset_ts': 1700650290, 'ozone': 323.4, 'pop': 80, 'precip': 0.307, 'pres': 1022.1, 'rh': 93, 'slp': 1022.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700666549, 'sunset_ts': 1700699121, 'temp': 45.7, 'ts': 1700640060, 'uv': 1.2, 'valid_date': '2023-11-22', 'vis': 10.5, 'weather': {'description': 'Light rain', 'code': 500, 'icon': 'r01d'}, 'wind_cdir': 'SW', 'wind_cdir_full': 'southwest', 'wind_dir': 227, 'wind_gust_spd': 7.8, 'wind_spd': 5.1}, {'app_max_temp': 46.4, 'app_min_temp': 33.4, 'clouds': 43, 'clouds_hi': 0, 'clouds_low': 63, 'clouds_mid': 0, 'datetime': '2023-11-23', 'dewpt': 38.8, 'high_temp': 47.2, 'low_temp': 33.5, 'max_dhi': None, 'max_temp': 47.2, 'min_temp': 36.7, 'moon_phase': 0.901745, 'moon_phase_lunation': 0.36, 'moonrise_ts': 1700778928, 'moonset_ts': 1700741477, 'ozone': 322.5, 'pop': 0, 'precip': 0, 'pres': 1015.3, 'rh': 87, 'slp': 1015.4, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700753033, 'sunset_ts': 1700785471, 'temp': 42.4, 'ts': 1700726460, 'uv': 1.6, 'valid_date': '2023-11-23', 'vis': 15, 'weather': {'description': 'Broken clouds', 'code': 803, 'icon': 'c03d'}, 'wind_cdir': 'E', 'wind_cdir_full': 'east', 'wind_dir': 97, 'wind_gust_spd': 8.5, 'wind_spd': 5.6}, {'app_max_temp': 38.1, 'app_min_temp': 30.3, 'clouds': 14, 'clouds_hi': 0, 'clouds_low': 0, 'clouds_mid': 0, 'datetime': '2023-11-24', 'dewpt': 33.1, 'high_temp': 43.5, 'low_temp': 31.6, 'max_dhi': None, 'max_temp': 43.5, 'min_temp': 33.5, 'moon_phase': 0.9603, 'moon_phase_lunation': 0.39, 'moonrise_ts': 1700866435, 'moonset_ts': 1700832722, 'ozone': 287.3, 'pop': 0, 'precip': 0, 'pres': 1016.1, 'rh': 83, 'slp': 1016.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700839515, 'sunset_ts': 1700871824, 'temp': 37.9, 'ts': 1700812860, 'uv': 2, 'valid_date': '2023-11-24', 'vis': 15, 'weather': {'description': 'Few clouds', 'code': 801, 'icon': 'c02d'}, 'wind_cdir': 'ESE', 'wind_cdir_full': 'east-southeast', 'wind_dir': 118, 'wind_gust_spd': 8.1, 'wind_spd': 5.4}, {'app_max_temp': 40.1, 'app_min_temp': 29.8, 'clouds': 28, 'clouds_hi': 24, 'clouds_low': 0, 'clouds_mid': 18, 'datetime': '2023-11-25', 'dewpt': 32.1, 'high_temp': 44, 'low_temp': 34, 'max_dhi': None, 'max_temp': 44, 'min_temp': 31.6, 'moon_phase': 0.992561, 'moon_phase_lunation': 0.43, 'moonrise_ts': 1700954128, 'moonset_ts': 1700923990, 'ozone': 276.8, 'pop': 0, 'precip': 0, 'pres': 1015.3, 'rh': 81, 'slp': 1015.5, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700925997, 'sunset_ts': 1700958179, 'temp': 37.3, 'ts': 1700899260, 'uv': 1.9, 'valid_date': '2023-11-25', 'vis': 15, 'weather': {'description': 'Scattered clouds', 'code': 802, 'icon': 'c02d'}, 'wind_cdir': 'NE', 'wind_cdir_full': 'northeast', 'wind_dir': 42, 'wind_gust_spd': 6.3, 'wind_spd': 4}, {'app_max_temp': 45.1, 'app_min_temp': 33, 'clouds': 37, 'clouds_hi': 52, 'clouds_low': 0, 'clouds_mid': 34, 'datetime': '2023-11-26', 'dewpt': 26.7, 'high_temp': 45.1, 'low_temp': 37.3, 'max_dhi': None, 'max_temp': 45.1, 'min_temp': 34, 'moon_phase': 0.997987, 'moon_phase_lunation': 0.46, 'moonrise_ts': 1701042136, 'moonset_ts': 1701015127, 'ozone': 299, 'pop': 0, 'precip': 0, 'pres': 1011.4, 'rh': 63, 'slp': 1011.6, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1701012477, 'sunset_ts': 1701044536, 'temp': 38.6, 'ts': 1700985660, 'uv': 2.4, 'valid_date': '2023-11-26', 'vis': 15, 'weather': {'description': 'Scattered clouds', 'code': 802, 'icon': 'c02d'}, 'wind_cdir': 'NE', 'wind_cdir_full': 'northeast', 'wind_dir': 56, 'wind_gust_spd': 2, 'wind_spd': 1.8}], 'lat': '47.61038', 'lon': '-122.20068', 'state_code': 'WA', 'timezone': 'America/Los_Angeles'} 
```
## RECEIVE data

# UML sequence diagram 
