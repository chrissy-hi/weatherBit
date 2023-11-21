from json import JSONDecodeError
import requests
import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/current/{city_current}')
def current_weather(city_current):
    api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=732710630ccd492a9c1042a8b2fff513&units=I&days=10&' \
                  f'city={city_current}'
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


@app.get('/forecast/{city_forecast}')
def forecast_daily(city_forecast):
    api_url = f'http://api.weatherbit.io/v2.0/forecast/daily?key=732710630ccd492a9c1042a8b2fff513&units=I&days=7&' \
                f'city={city_forecast}'
    response = requests.get(api_url)
    try:
        data = json.loads(response.text)
        return data
    except Exception as e:
        return "error", 500


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)
