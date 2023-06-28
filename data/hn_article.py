import requests
import json

#Make APi call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
# url ='https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Explore status code.
response_dict = r.json()
readable_file = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\readable_hs_submitted.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)