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

## RECEIVE data

# UML sequence diagram 
