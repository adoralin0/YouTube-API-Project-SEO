# Import the requests library
import requests

# Define the URL for the POST request
url = 'https://jsonplaceholder.typicode.com/posts'

# Define the data payload to include in the request
data = {
    'title': 'Special Agent',
    'body': 'Leroy Jethro Gibbs',
    'userId': '1'
}

# Send the POST request with the data
response = requests.post(url, json=data)

# Print out the status code of the response
print(response.status_code)

# Print out the response content as JSON
print(response.json())