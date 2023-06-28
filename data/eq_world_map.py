import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)
filename = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\significant_month.geojson'

# filename = 'C:\\Users\\vfuen\\Documentsments\\Resume\\pythonProject\\data\\1.0_month_eq.geojson'
# filename = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\1.0_day_eq.geojson'
with open(filename, encoding='utf8') as f:
    whole_eq_data = json.load(f)

readable_file = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\readable_eq_significant_.geojson'
with open(readable_file, 'w') as f:
    json.dump(whole_eq_data, f, indent=4)


all_eq_dicts = whole_eq_data['features']
# print(len(all_eq_dicts))


eq_mags, lngtds, lttds, hover_texts = [], [], [], []

for a_dict in all_eq_dicts:
    mag = a_dict['properties']['mag']
    lngtd = a_dict['geometry']['coordinates'][0]
    lttd = a_dict['geometry']['coordinates'][1]
    title= a_dict['properties']['title']
    eq_mags.append(mag)
    lngtds.append(lngtd)
    lttds.append(lttd)
    hover_texts.append(title)

#Map earthquakes from 10/14/2021.
# data= [Scattergeo(lon=lngtds, lat=lttds)]

data = [{
          'type': 'scattergeo',
          'lon': lngtds,
          'lat': lttds,
        'text': hover_texts,

        'marker': {
              'size': [5*mag for mag in eq_mags],
          'color':eq_mags,
          'colorscale': 'RdBu',
          'reversescale': True,
          'colorbar':{'title':'Magnitude'},
          },

      }]




graph_layout = Layout(title='Significant Earthquakes World-Wide')

fig = {'data': data, 'layout': graph_layout}
offline.plot(fig, filename='Significant_worldwide_earthquakes.html')