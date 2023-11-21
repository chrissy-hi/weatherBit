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
Pass in the name of a city into the ```get_current_weather``` function. 
```
def get_current_weather(city_current):
    url = 'http://127.0.0.1:8001/current/' + city_current
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        print("There was an error sending your request. Status Code: ", res.status_code)
        return None
```


## RECEIVE data

# UML sequence diagram 
