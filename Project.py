import requests
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:Java&sort=stars'
header = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=header)

if r.status_code == 200:
    print('Хорошо')
else:
    print('Плохо')

r_dict = r.json()
r_dicts = r_dict['items']
labels, stars, r_links = [], [], []
for r_dict in r_dicts:
    r_name = r_dict['name']
    r_url = r_dict['html_url']
    r_link = f'<a href="{r_url}">{r_name}</a>'
    r_links.append(r_link)

    stars.append(r_dict['stargazers_count'])

    descr = r_dict['description']
    own = r_dict['owner']['login']
    lab = f'{own} {descr}'
    labels.append(lab)

data = [{'type': 'bar',
         'x': r_links,
         'y': stars,
         'hovertext': labels,
         'marker': {
             'color': 'rgb(80,120,160)',
             'line': {'width': 1.7, 'color': 'rgb(50, 50, 50)'}
         },
         'opacity': 0.7
         }]
m_lout = {
    'title': 'Java проекты с наибольшим количеством звезд на Github',
    'titlefont': {'size': 30},
    'xaxis': {
        'title': 'Репозитории',
        'titlefont': {'size': 26},
        'tickfont': {'size': 16}
    },
    'yaxis': {
        'title': 'Звезды',
        'titlefont': {'size': 26},
        'tickfont': {'size': 16}

    }
}

fig = {'data': data, 'layout': m_lout}
offline.plot(fig, filename='Java.html')

