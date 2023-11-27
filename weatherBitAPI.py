from json import JSONDecodeError
from typing import Optional

import requests
import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/current/{city_current}')
def current_weather(city_current):
    print(city_current)
    if city_current.isdigit():
        api_url = f'http://api.weatherbit.io/v2.0/current?key=732710630ccd492a9c1042a8b2fff513&units=I' \
                  f'&postal_code={city_current}'
    else:
        api_url = f'http://api.weatherbit.io/v2.0/current?key=732710630ccd492a9c1042a8b2fff513&units=I' \
                  f'&city={city_current}'
    print(api_url)
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/current/{lon}/{lat}')
def current_weather(lon: str = "", lat: str = ""):
    api_url = f'http://api.weatherbit.io/v2.0/current?key=732710630ccd492a9c1042a8b2fff513&units=I' \
              f'&lat={lat}' \
              f'&lon={lon}'
    print(api_url)
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/forecast/{city_forecast}')
def forecast_daily(city_forecast):
    if city_forecast.isdigit():
        api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=732710630ccd492a9c1042a8b2fff513&units=I&days=7&' \
                  f'postal_code={city_forecast}'
    else:
        api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=732710630ccd492a9c1042a8b2fff513&units=I&days=7&' \
                  f'city={city_forecast}'
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/forecast/{lon}/{lat}')
def forecast_daily(lon, lat):
    api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=732710630ccd492a9c1042a8b2fff513&units=I&days=7&' \
              f'&lat={lat}' \
              f'&lon={lon}'
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8001)
