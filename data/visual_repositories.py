import  requests

from plotly.graph_objs import Bar
from plotly import offline

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

repo_links, rating, labels = [], [], []
for certain_item in all_items:
    repo_name = certain_item['name']
    repo_url = certain_item['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)



    rating.append(certain_item['stargazers_count'])

    belongs_to = certain_item['owner']['login']
    description = certain_item['description']
    label = f"{belongs_to}<br />{description}"
    labels.append(label)

#Display graph.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': rating,
    'hovertext': labels,
    'marker': {
        'color':'rgb(20,80,150)',
        'line': {'width': 2.0, 'color': 'rgb(60,60,60)'}
    },
    'opacity': 0.8,
}]

my_layout = {
    'title': 'Highly Rated Projects on Github',
    'titlefont': {'size': 24},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 22},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Rating',
        'titlefont': {'size': 22},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='highly_rate_graphed_projects.html')