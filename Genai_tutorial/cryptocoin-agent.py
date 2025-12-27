import os
from google import genai
from google.genai import types
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
load_dotenv()
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

def get_crypto_coin_price(coin: str) -> int:
    # url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    # parameters = {
    #     'start': '1',
    #     'limit': '5000',
    #     'convert': 'USD'
    # }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.getenv('COINMARKETCAP_API_KEY'),
    }
    params = {
        "symbol": "DOGE",  # Change this: ETH, SOL, DOGE, etc.
        "convert": "USD"
    }
    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(url, params=params,headers=headers)
        data = json.loads(response.text)
        print(data["data"][coin]["quote"])
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

# Configure the client and model
# get_crypto_coin_price("DOGE")
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature, get_crypto_coin_price]
)

# Make the request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="DOGECOIN coin price.",
    config=config,
)

# Print the final, user-facing response
print(response.text)