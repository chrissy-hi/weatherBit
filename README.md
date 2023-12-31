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

## REQUEST and RECEIVE data 
### Current Weather Request
Pass in the name of a city into the ```get_current_weather``` function. 
```
def get_current_weather(city_current):
    # obtain url with desired city
    url = 'http://localhost:8001/current/' + city_current
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
```
For instance, if the city "Clyde" or zip code "98004" is passed into the function. The received data is the ```current_weather_info``` output and will look like this:
```
{"count":1,"data":[{"app_temp":40.2,"aqi":98,"city_name":"Clyde","clouds":93,"country_code":"US","datetime":"2023-11-29:05","dewpt":35.3,"dhi":0,"dni":0,"elev_angle":-46,"ghi":0,"gust":2.9,"h_angle":-90,"lat":47.6155,"lon":-122.2072,"ob_time":"2023-11-29 05:05","pod":"n","precip":0,"pres":1018,"rh":92,"slp":1018.12616,"snow":0,"solar_rad":0,"sources":["rtma","radar","satellite"],"state_code":"WA","station":"D4490","sunrise":"15:33","sunset":"00:20","temp":37,"timezone":"America/Los_Angeles","ts":1701234354,"uv":0,"vis":3.1,"weather":{"icon":"c04n","description":"Overcast clouds","code":804},"wind_cdir":"E","wind_cdir_full":"east","wind_dir":93,"wind_spd":0.6}]}

```

Pass in the longitude and latitude into the ```get_current_weather_lon_lat(lon, lat)``` function. 
```
def get_current_weather_lon_lat(lon, lat):
    # obtain url with desired city
    url = 'http://localhost:8001/current/' + lon + "/" + lat
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        print(f'{lon} and {lat} current weather ')
        print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
```
For instance, if the longitude -122.162520842 and the latitude 47.535997856 is passed into the function. The received data is the ```lat_lon_current ``` output and will look like this:
```
{"count":1,"data":[{"app_temp":32.3,"aqi":98,"city_name":"Newcastle","clouds":90,"country_code":"US","datetime":"2023-11-29:05","dewpt":31.7,"dhi":0,"dni":0,"elev_angle":-46.1,"ghi":0,"gust":3.8,"h_angle":-90,"lat":47.536,"lon":-122.1625,"ob_time":"2023-11-29 05:04","pod":"n","precip":0,"pres":1009,"rh":92,"slp":1027.9633,"snow":0,"solar_rad":0,"sources":["rtma","radar","satellite"],"state_code":"WA","station":"G1943","sunrise":"15:32","sunset":"00:21","temp":33,"timezone":"America/Los_Angeles","ts":1701234285,"uv":0,"vis":2.5,"weather":{"icon":"c03n","description":"Broken clouds","code":803},"wind_cdir":"ESE","wind_cdir_full":"east-southeast","wind_dir":110,"wind_spd":1.9}]}

```

This is the weather data for that day and this will include the max temperature for that day, minimum temperature, cloud information, ozone, snow, etc. 

### Daily Forecast Request
Pass in the name of a city into the ```get_daily_forecast``` function. 
```
def get_daily_forecast(city_forecast):
    # obtain url with desired city
    url = 'http://127.0.0.1:8001/forecast/' + city_forecast
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        daily_forecast_info = res.json()
        return daily_forecast_info
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
```
For instance, if the city "Bellevue" or the zip code of Bellevue is passed into the function. The received data is the ```daily_forecast_info``` output and will look like this:
```
{'city_name': 'Bellevue', 'country_code': 'US', 'data': [{'app_max_temp': 48.3, 'app_min_temp': 34.9, 'clouds': 57, 'clouds_hi': 80, 'clouds_low': 6, 'clouds_mid': 22, 'datetime': '2023-11-20', 'dewpt': 37.3, 'high_temp': 49.2, 'low_temp': 38.8, 'max_dhi': None, 'max_temp': 49.2, 'min_temp': 35.8, 'moon_phase': 0.603872, 'moon_phase_lunation': 0.26, 'moonrise_ts': 1700516528, 'moonset_ts': 1700467892, 'ozone': 285.2, 'pop': 0, 'precip': 0, 'pres': 1026.1, 'rh': 81, 'slp': 1026.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700493580, 'sunset_ts': 1700526429, 'temp': 42.8, 'ts': 1700485260, 'uv': 0, 'valid_date': '2023-11-20', 'vis': 12.6, 'weather': {'description': 'Broken clouds', 'code': 803, 'icon': 'c03d'}, 'wind_cdir': 'ENE', 'wind_cdir_full': 'east-northeast', 'wind_dir': 78, 'wind_gust_spd': 4.9, 'wind_spd': 3.4}, {'app_max_temp': 53.1, 'app_min_temp': 36.6, 'clouds': 84, 'clouds_hi': 98, 'clouds_low': 26, 'clouds_mid': 96, 'datetime': '2023-11-21', 'dewpt': 37.8, 'high_temp': 54.2, 'low_temp': 44.7, 'max_dhi': None, 'max_temp': 54.2, 'min_temp': 38.8, 'moon_phase': 0.718257, 'moon_phase_lunation': 0.29, 'moonrise_ts': 1700604068, 'moonset_ts': 1700559118, 'ozone': 295.7, 'pop': 85, 'precip': 0.399, 'pres': 1020.3, 'rh': 73, 'slp': 1020.5, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700580065, 'sunset_ts': 1700612774, 'temp': 46.2, 'ts': 1700553660, 'uv': 1.3, 'valid_date': '2023-11-21', 'vis': 12.3, 'weather': {'description': 'Moderate rain', 'code': 501, 'icon': 'r02d'}, 'wind_cdir': 'SSE', 'wind_cdir_full': 'south-southeast', 'wind_dir': 164, 'wind_gust_spd': 8.3, 'wind_spd': 5.6}, {'app_max_temp': 48.2, 'app_min_temp': 38.9, 'clouds': 77, 'clouds_hi': 71, 'clouds_low': 45, 'clouds_mid': 73, 'datetime': '2023-11-22', 'dewpt': 43.9, 'high_temp': 49, 'low_temp': 40.8, 'max_dhi': None, 'max_temp': 49, 'min_temp': 41.3, 'moon_phase': 0.819552, 'moon_phase_lunation': 0.32, 'moonrise_ts': 1700691503, 'moonset_ts': 1700650290, 'ozone': 323.4, 'pop': 80, 'precip': 0.307, 'pres': 1022.1, 'rh': 93, 'slp': 1022.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700666549, 'sunset_ts': 1700699121, 'temp': 45.7, 'ts': 1700640060, 'uv': 1.2, 'valid_date': '2023-11-22', 'vis': 10.5, 'weather': {'description': 'Light rain', 'code': 500, 'icon': 'r01d'}, 'wind_cdir': 'SW', 'wind_cdir_full': 'southwest', 'wind_dir': 227, 'wind_gust_spd': 7.8, 'wind_spd': 5.1}, {'app_max_temp': 46.4, 'app_min_temp': 33.4, 'clouds': 43, 'clouds_hi': 0, 'clouds_low': 63, 'clouds_mid': 0, 'datetime': '2023-11-23', 'dewpt': 38.8, 'high_temp': 47.2, 'low_temp': 33.5, 'max_dhi': None, 'max_temp': 47.2, 'min_temp': 36.7, 'moon_phase': 0.901745, 'moon_phase_lunation': 0.36, 'moonrise_ts': 1700778928, 'moonset_ts': 1700741477, 'ozone': 322.5, 'pop': 0, 'precip': 0, 'pres': 1015.3, 'rh': 87, 'slp': 1015.4, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700753033, 'sunset_ts': 1700785471, 'temp': 42.4, 'ts': 1700726460, 'uv': 1.6, 'valid_date': '2023-11-23', 'vis': 15, 'weather': {'description': 'Broken clouds', 'code': 803, 'icon': 'c03d'}, 'wind_cdir': 'E', 'wind_cdir_full': 'east', 'wind_dir': 97, 'wind_gust_spd': 8.5, 'wind_spd': 5.6}, {'app_max_temp': 38.1, 'app_min_temp': 30.3, 'clouds': 14, 'clouds_hi': 0, 'clouds_low': 0, 'clouds_mid': 0, 'datetime': '2023-11-24', 'dewpt': 33.1, 'high_temp': 43.5, 'low_temp': 31.6, 'max_dhi': None, 'max_temp': 43.5, 'min_temp': 33.5, 'moon_phase': 0.9603, 'moon_phase_lunation': 0.39, 'moonrise_ts': 1700866435, 'moonset_ts': 1700832722, 'ozone': 287.3, 'pop': 0, 'precip': 0, 'pres': 1016.1, 'rh': 83, 'slp': 1016.2, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700839515, 'sunset_ts': 1700871824, 'temp': 37.9, 'ts': 1700812860, 'uv': 2, 'valid_date': '2023-11-24', 'vis': 15, 'weather': {'description': 'Few clouds', 'code': 801, 'icon': 'c02d'}, 'wind_cdir': 'ESE', 'wind_cdir_full': 'east-southeast', 'wind_dir': 118, 'wind_gust_spd': 8.1, 'wind_spd': 5.4}, {'app_max_temp': 40.1, 'app_min_temp': 29.8, 'clouds': 28, 'clouds_hi': 24, 'clouds_low': 0, 'clouds_mid': 18, 'datetime': '2023-11-25', 'dewpt': 32.1, 'high_temp': 44, 'low_temp': 34, 'max_dhi': None, 'max_temp': 44, 'min_temp': 31.6, 'moon_phase': 0.992561, 'moon_phase_lunation': 0.43, 'moonrise_ts': 1700954128, 'moonset_ts': 1700923990, 'ozone': 276.8, 'pop': 0, 'precip': 0, 'pres': 1015.3, 'rh': 81, 'slp': 1015.5, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1700925997, 'sunset_ts': 1700958179, 'temp': 37.3, 'ts': 1700899260, 'uv': 1.9, 'valid_date': '2023-11-25', 'vis': 15, 'weather': {'description': 'Scattered clouds', 'code': 802, 'icon': 'c02d'}, 'wind_cdir': 'NE', 'wind_cdir_full': 'northeast', 'wind_dir': 42, 'wind_gust_spd': 6.3, 'wind_spd': 4}, {'app_max_temp': 45.1, 'app_min_temp': 33, 'clouds': 37, 'clouds_hi': 52, 'clouds_low': 0, 'clouds_mid': 34, 'datetime': '2023-11-26', 'dewpt': 26.7, 'high_temp': 45.1, 'low_temp': 37.3, 'max_dhi': None, 'max_temp': 45.1, 'min_temp': 34, 'moon_phase': 0.997987, 'moon_phase_lunation': 0.46, 'moonrise_ts': 1701042136, 'moonset_ts': 1701015127, 'ozone': 299, 'pop': 0, 'precip': 0, 'pres': 1011.4, 'rh': 63, 'slp': 1011.6, 'snow': 0, 'snow_depth': 0, 'sunrise_ts': 1701012477, 'sunset_ts': 1701044536, 'temp': 38.6, 'ts': 1700985660, 'uv': 2.4, 'valid_date': '2023-11-26', 'vis': 15, 'weather': {'description': 'Scattered clouds', 'code': 802, 'icon': 'c02d'}, 'wind_cdir': 'NE', 'wind_cdir_full': 'northeast', 'wind_dir': 56, 'wind_gust_spd': 2, 'wind_spd': 1.8}], 'lat': '47.61038', 'lon': '-122.20068', 'state_code': 'WA', 'timezone': 'America/Los_Angeles'} 
```

Pass in the longitude and latitude into the ```get_daily_forecast_lon_lat(lon, lat)``` function. 
```
def get_daily_forecast_lon_lat(lon, lat):
    # obtain url with desired city
    url = 'http://localhost:8001/forecast/daily/' + lon + "/" + lat
    # send get request
    res = requests.get(url)
    if res.status_code == 200:
        print(f'{lon} and {lat} daily forecast ')
        print(res.json())
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
```
For instance, if the longitude -122.162520842 and the latitude 47.535997856 is passed into the function. The received data is the ```lat_lon_forecast``` output and will look like this:
```
{"city_name":"Newcastle","country_code":"US","data":[{"app_max_temp":40,"app_min_temp":28.4,"clouds":52,"clouds_hi":0,"clouds_low":52,"clouds_mid":47,"datetime":"2023-11-28","dewpt":30.3,"high_temp":42.4,"low_temp":29,"max_dhi":null,"max_temp":42.4,"min_temp":29.2,"moon_phase":0.93624,"moon_phase_lunation":0.53,"moonrise_ts":1701217015,"moonset_ts":1701195905,"ozone":336.1,"pop":0,"precip":0,"pres":1009.9,"rh":80,"slp":1028.8,"snow":0,"snow_depth":0,"sunrise_ts":1701185435,"sunset_ts":1701217259,"temp":35.9,"ts":1701176460,"uv":0,"valid_date":"2023-11-28","vis":7.1,"weather":{"description":"Broken clouds","code":803,"icon":"c03d"},"wind_cdir":"S","wind_cdir_full":"south","wind_dir":181,"wind_gust_spd":4,"wind_spd":2.9},{"app_max_temp":39,"app_min_temp":27.6,"clouds":55,"clouds_hi":8,"clouds_low":4,"clouds_mid":20,"datetime":"2023-11-29","dewpt":29.9,"high_temp":41.8,"low_temp":33.1,"max_dhi":null,"max_temp":41.8,"min_temp":29,"moon_phase":0.876434,"moon_phase_lunation":0.56,"moonrise_ts":1701306113,"moonset_ts":1701285154,"ozone":325.1,"pop":0,"precip":0,"pres":1006,"rh":82,"slp":1024.9,"snow":0,"snow_depth":0,"sunrise_ts":1701271911,"sunset_ts":1701303625,"temp":34.8,"ts":1701244860,"uv":2,"valid_date":"2023-11-29","vis":13.9,"weather":{"description":"Broken clouds","code":803,"icon":"c03d"},"wind_cdir":"SSE","wind_cdir_full":"south-southeast","wind_dir":159,"wind_gust_spd":4,"wind_spd":2.7},{"app_max_temp":37.6,"app_min_temp":31.5,"clouds":88,"clouds_hi":47,"clouds_low":79,"clouds_mid":95,"datetime":"2023-11-30","dewpt":34.2,"high_temp":42.7,"low_temp":38.8,"max_dhi":null,"max_temp":42.7,"min_temp":33.3,"moon_phase":0.802912,"moon_phase_lunation":0.6,"moonrise_ts":1701395868,"moonset_ts":1701373691,"ozone":364.6,"pop":70,"precip":0.206,"pres":998.5,"rh":85,"slp":1017.1,"snow":0,"snow_depth":0,"sunrise_ts":1701358387,"sunset_ts":1701389993,"temp":38.3,"ts":1701331260,"uv":0.6,"valid_date":"2023-11-30","vis":12.4,"weather":{"description":"Light rain","code":500,"icon":"r01d"},"wind_cdir":"SSE","wind_cdir_full":"south-southeast","wind_dir":160,"wind_gust_spd":8.7,"wind_spd":5.8},{"app_max_temp":36.8,"app_min_temp":32,"clouds":89,"clouds_hi":17,"clouds_low":86,"clouds_mid":95,"datetime":"2023-12-01","dewpt":38.9,"high_temp":45.2,"low_temp":42.4,"max_dhi":null,"max_temp":45.2,"min_temp":39.2,"moon_phase":0.719487,"moon_phase_lunation":0.63,"moonrise_ts":1701486142,"moonset_ts":1701461695,"ozone":381,"pop":90,"precip":0.566,"pres":997,"rh":88,"slp":1015.5,"snow":0,"snow_depth":0,"sunrise_ts":1701444861,"sunset_ts":1701476364,"temp":42.3,"ts":1701417660,"uv":0.8,"valid_date":"2023-12-01","vis":13.6,"weather":{"description":"Moderate rain","code":501,"icon":"r02d"},"wind_cdir":"S","wind_cdir_full":"south","wind_dir":185,"wind_gust_spd":22.1,"wind_spd":14.8},{"app_max_temp":45.3,"app_min_temp":36.1,"clouds":82,"clouds_hi":38,"clouds_low":86,"clouds_mid":77,"datetime":"2023-12-02","dewpt":40.3,"high_temp":46.3,"low_temp":42.6,"max_dhi":null,"max_temp":45.9,"min_temp":42.1,"moon_phase":0.629475,"moon_phase_lunation":0.66,"moonrise_ts":1701576679,"moonset_ts":1701549339,"ozone":355.5,"pop":90,"precip":0.656,"pres":996.8,"rh":87,"slp":1015.2,"snow":0,"snow_depth":0,"sunrise_ts":1701531334,"sunset_ts":1701562738,"temp":43.9,"ts":1701504060,"uv":0.9,"valid_date":"2023-12-02","vis":12.7,"weather":{"description":"Heavy rain","code":502,"icon":"r03d"},"wind_cdir":"S","wind_cdir_full":"south","wind_dir":191,"wind_gust_spd":20.4,"wind_spd":13.4},{"app_max_temp":49.4,"app_min_temp":38.4,"clouds":85,"clouds_hi":82,"clouds_low":93,"clouds_mid":79,"datetime":"2023-12-03","dewpt":42.8,"high_temp":51.5,"low_temp":43.6,"max_dhi":null,"max_temp":51.1,"min_temp":42.7,"moon_phase":0.535749,"moon_phase_lunation":0.7,"moonrise_ts":1701667255,"moonset_ts":1701636756,"ozone":326.6,"pop":90,"precip":0.905,"pres":999,"rh":87,"slp":1017.4,"snow":0,"snow_depth":0,"sunrise_ts":1701617805,"sunset_ts":1701649114,"temp":46.4,"ts":1701590460,"uv":1,"valid_date":"2023-12-03","vis":13.9,"weather":{"description":"Heavy rain","code":502,"icon":"r03d"},"wind_cdir":"S","wind_cdir_full":"south","wind_dir":178,"wind_gust_spd":17.9,"wind_spd":11.9},{"app_max_temp":50.9,"app_min_temp":43.9,"clouds":100,"clouds_hi":76,"clouds_low":59,"clouds_mid":100,"datetime":"2023-12-04","dewpt":42.8,"high_temp":50.9,"low_temp":46.3,"max_dhi":null,"max_temp":50.9,"min_temp":43.6,"moon_phase":0.440897,"moon_phase_lunation":0.73,"moonrise_ts":1701757753,"moonset_ts":1701724043,"ozone":320.1,"pop":75,"precip":0.226,"pres":1009.6,"rh":86,"slp":1028.1,"snow":0,"snow_depth":0,"sunrise_ts":1701704275,"sunset_ts":1701735493,"temp":46.8,"ts":1701676860,"uv":2.3,"valid_date":"2023-12-04","vis":12.6,"weather":{"description":"Light rain","code":500,"icon":"r01d"},"wind_cdir":"SE","wind_cdir_full":"southeast","wind_dir":143,"wind_gust_spd":8.7,"wind_spd":3.1}],"lat":47.536,"lon":-122.1625,"state_code":"WA","timezone":"America/Los_Angeles"}
```

This will be a 7 day forecast of the weather that will include daily maximum temperature, minimum temperature, dew point, uv index, etc.

# UML sequence diagram 

![image](https://github.com/chrissy-hi/weatherBit/assets/77197824/0b452428-6ca3-4515-a69b-f8012a895ab2)
