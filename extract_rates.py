# Import the library to make HTTP requests
import requests

# Define the API URL
api_url = "https://api.frankfurter.dev/v1/latest?from=USD&to=EUR,GBP,MXN"

# Send a GET request to the API
response = requests.get(api_url)

# Validate that the status code is 200 and then, stop and report the error unless the request succeeded
status = response.status_code

if status != 200:
    print("Request failed with status code", status)
else:
    data = response.json()
    for currency, rate in data['rates'].items():
        print(currency, ':', rate)