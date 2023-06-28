import json

#Identify what is in the eq file.

filename = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\1.0_day_eq.geojson'
with open(filename, encoding='utf8') as f:
    whole_eq_data = json.load(f)

readable_file = 'C:\\Users\\vfuen\\Documents\\Resume\\pythonProject\\data\\readable1_eq_1.0_day.geojson'
with open(readable_file, 'w') as f:
    json.dump(whole_eq_data, f, indent=4)


all_eq_dicts = whole_eq_data['features']
print(len(all_eq_dicts))


eq_mags, lngtds, lttds = [],[],[]

for a_dict in all_eq_dicts:
    mag = a_dict['properties']['mag']
    lngtd = a_dict['geometry']['coordinates'][0]
    lttd = a_dict['geometry']['coordinates'][1]
    eq_mags.append(mag)
    lngtds.append(lngtd)
    lttds.append(lttd)

print(eq_mags[:10])
print(lngtds[:6])
print(lttds[:3])