import requests


def get_current_weather(city_current):
    url = 'http://127.0.0.1:8001/current/' + city_current
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
        return None


def daily_forecast(city_forecast):
    url = 'http://127.0.0.1:8001/forecast/' + city_forecast
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
        return None


if __name__ == '__main__':
    city = input("Enter the city you would like to get data from: ")
    current_weather = get_current_weather(city)
    current_weather_list = str(current_weather["data"])
    x = current_weather_list.split()
    return_weather = x[1].replace(",", "", )
    print("Current Temperature: ", return_weather)

    daily_weather = daily_forecast(city)
    daily_weather_list = str(daily_weather["data"])
    x = daily_weather_list.split("{'app_")
    day = 0
    for c in x:
        if day > 0:
            print("Day ", day, " : ", c)
        day = day + 1
