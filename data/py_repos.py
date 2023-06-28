import requests

#Make an API and store responses.
url= 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3.json'}
req = requests.get(url, headers=headers)
print(f"Status code: {req.status_code}")

#Store API response in a variable.
response_dict = req.json()

#Process results.
print(f"All repositories: {response_dict['total_count']}")

#Inspect the information in all the repositories.
all_items = response_dict['items']
print(f"Repositories shown: {len(all_items)}")

#Examine only the first repository.
certain_item = all_items[0]
print(f"\nKeys: {len(all_items)}")
for key in sorted(response_dict.keys()):
    print(key)


print("\nInformation about each repository: ")
for certain_item in all_items:
    print(f"Name: {certain_item['name']}")
    print(f"Owners: {certain_item['owner']['login']}")
    print(f"Stars: {certain_item['stargazers_count']}")
    print(f"Repository: {certain_item['html_url']}")
    print(f"Created: {certain_item['created_at']}")
    print(f"Updated: {certain_item['updated_at']}")
    print(f"Description: {certain_item['description']}")