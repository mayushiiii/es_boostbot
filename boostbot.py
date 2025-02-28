import requests
import time

# Set up API URL
BASE_URL = "https://api.everskies.com"

# Your authentication token (found in DevTools > Headers > Authorization)
HEADERS = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInVzZXJfaWQiOjEzOTQ3MTAwfQ.eyJpc3MiOiJldmVyc2tpZXMuY29tIiwiYXVkIjoiYXV0aCIsImp0aSI6IjJoMnNSRU5iQ0h6N1hGQ05hYzh2d09rbmhleWxsUjJqIiwiaWF0IjoxNzM5NDgxNDM5LjgxNTYwNiwibmJmIjoxNzM5NDgxMTM5LjgxNTYwNywiZXhwIjoxNzM5NTY3ODM5fQ.frr1XdXVF-X7aeKUg5gZKEzZ7ybf13D-w7y6t5f1E4Y",
    "Content-Type": "application/json; charset=utf-8"
}

# The post you want to boost
POST_ID = "58594342"  # Replace with the actual post ID

# Start commenting
counter = 0
while counter <= 10000:  # Change this number as needed
    comment_text = str(counter)
    
    # API endpoint for posting comments (adjust if necessary)
    COMMENT_URL = f"{BASE_URL}/discussion/{POST_ID}/reply"

    payload = {
        "parent_reply_id": None,
        "attachments":[],
        "content": comment_text
    }

    response = requests.post(COMMENT_URL, headers=HEADERS, json=payload)

    if response.status_code == 201 or response.status_code == 200:
        print(f"Posted comment: {comment_text}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

    counter += 1
    time.sleep(2)  # Delay to avoid spam detection
print(f"Finished posting {counter} comments")
