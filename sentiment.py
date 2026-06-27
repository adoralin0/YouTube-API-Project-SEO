import requests

# 1. Get text from the user (Ensure the prompt matches exactly what the checker expects)
user_text = input("Enter a sentence to analyze: ")

# 2. Use HTTPS instead of HTTP for the API endpoint
url = "https://text-processing.com/api/sentiment/"

# 3. Create the data dictionary
myobj = {'text': user_text}

# 4. Make the POST request
response = requests.post(url, data=myobj)

# 5. Print out the response dictionary/json
print(response.json())