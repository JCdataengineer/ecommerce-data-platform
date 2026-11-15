# Import the library to make HTTP requests
import requests

# Import the library to save API data
import json


def fetch_rates(api_url):
    """Request the exchange rates from the API and return the response."""
    response = requests.get(api_url)
    return response


def save_rates(data, filename):
    """Save the data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Get the data from the API
response = fetch_rates("https://api.frankfurter.dev/v1/latest?from=USD&to=EUR,GBP,MXN")
# Stop and report the error unless the request succeeded.
status = response.status_code
if status != 200:
    print("Request failed with status code", status)
else:
    data = response.json()
    save_rates(data, "rates.json")
    for currency, rate in data["rates"].items():
        print(currency, ":", rate)