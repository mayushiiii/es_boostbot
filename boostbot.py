import requests
import time

# api url for everskies
BASE_URL = "https://api.everskies.com"

# authentication token, can be found by going on your everskies account.
# open dev tools with f12, go to the network section, and you should search for an xhr get request(make sure your filters for them are on)
# click on the request, go to the headers tab, and you should find the token in the reasponse headers section! 
# content type never changes though
HEADERS = {
    "Authorization": "Bearer <<your token>>",
    "Content-Type": "application/json; charset=utf-8"
}

# you can probably find the post id on the url, it should be the number at the end of it
POST_ID = "<<your post id>>"  # replace with your post ID

# start commenting
counter = 0
while counter <= 10000:  # change this number as needed
    comment_text = str(counter)
    
    # API endpoint for posting comments
    COMMENT_URL = f"{BASE_URL}/discussion/{POST_ID}/reply"

    payload = {
        "parent_reply_id": None,
        "attachments":[],
        "content": comment_text
    }

    response = requests.post(COMMENT_URL, headers=HEADERS, json=payload)
    
    # this checks whether the post went through. maybe check the terminal once in a while
    if response.status_code == 201 or response.status_code == 200: 
        print(f"Posted comment: {comment_text}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

    counter += 1
    time.sleep(2)  # this is in seconds so adjust as needed
print(f"Finished posting {counter} comments")
