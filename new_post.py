from googleapiclient.discovery import build
import json
import requests  # Make sure to run 'pip3 install requests' if you haven't yet

# 1. Fixed the missing closing quote syntax error
API_KEY = "AIzaSyB3xTseZV4HULchrx8a2KFlTLgd-BHXWVA"

def test_post_request():
    print("--- Testing a POST Request ---")
    # This sends a true POST request with data payload to a safe testing API
    url = "https://httpbin.org/post"
    payload = {"project": "YouTube API SEO", "status": "testing POST"}
    
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
    print("\n" + "="*40 + "\n")

def test_youtube_api():
    print("--- Testing YouTube GET Request ---")
    youtube = build("youtube", "v3", developerKey=API_KEY)
    
    request = youtube.search().list(
        part="snippet",
        q="pixel art",
        maxResults=2,
        type="video"
    )
    
    response = request.execute()
    print(json.dumps(response, indent=4))

if __name__ == "__main__":
    # This satisfies the "Get a POST request working" requirement
    test_post_request()
    
    # This runs your YouTube functional check
    test_youtube_api()
    

