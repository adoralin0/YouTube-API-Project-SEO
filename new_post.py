
from googleapiclient.discovery import build
import json

API_KEY = "AIzaSyB3xTseZV4HULchrx8a2KFlTLgd-BHXWVA"

def test_youtube_api():
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
    test_youtube_api()