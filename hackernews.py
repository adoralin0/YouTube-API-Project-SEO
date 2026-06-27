import requests

def get_latest_hn_story():
    # 1. Get the list of most recent story IDs
    live_data_url = "https://hacker-news.firebaseio.com/v0/newstories.json"
    
    try:
        response = requests.get(live_data_url)
        # Parse the JSON array of IDs
        story_ids = response.json()
        
        # 2. Iterate through recent IDs until we find a valid 'story'
        for story_id in story_ids:
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            item_response = requests.get(item_url)
            item_data = item_response.json()
            
            # Check if the item is valid and specifically a "story"
            if item_data and item_data.get("type") == "story":
                title = item_data.get("title", "No Title")
                author = item_data.get("by", "Unknown Author")
                link = item_data.get("url", "No Link Provided")
                
                # 3. Print out the story details
                print(f"Title: {title}")
                print(f"Author: {author}")
                print(f"Link: {link}")
                return  # Exit the function once the latest story is handled
                
        print("No recent item found that matches 'story' type.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_latest_hn_story()