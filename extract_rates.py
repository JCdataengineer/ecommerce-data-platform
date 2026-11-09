# Import the library to make HTTP requests
import requests

# Define the API URL
api_url = "https://api.frankfurter.dev/v1/latest?from=USD&to=EUR,GBP,MXN"

# Send a GET request to the API
response = requests.get(api_url)

# Print the status code
print(response.status_code)

# Convert the response into a dictionary
data = response.json()

# Print Data
print(data)

# Extract euro rate from the dictionary
print(data['rates']['EUR'])

# Create a loop to print each rate
for currency, rate in data['rates'].items():
    print(currency, ':', rate)