# Import the library to make HTTP requests
import requests


def fetch_rates(api_url):
    """Request the exchange rates from the API and return the response."""
    response = requests.get(api_url)
    return response


response = fetch_rates("https://api.frankfurter.dev/v1/latest?from=USD&to=EUR,GBP,MXN")

# Stop and report the error unless the request succeeded.
status = response.status_code
if status != 200:
    print("Request failed with status code", status)
else:
    data = response.json()
    for currency, rate in data["rates"].items():
        print(currency, ":", rate)