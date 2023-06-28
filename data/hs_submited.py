from operator import itemgetter

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

#Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:16]:
    #Different API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id {submission_id}\status: {r.status_code}")
    response_dict = r.json()

    #Create dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_links': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_links']}")
    print(f"Comments: {submission_dict['comments']}")



