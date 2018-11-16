import pandas as pd
import folium

shilin_bin = pd.read_csv('.\\data\\data89_shilin.csv',
                         sep=",")
print shilin_bin.shape
print shilin_bin.columns
shilin_bin.columns = ['section', 'road', 'road_detail',
                      'lon', 'lat', 'extra']
print shilin_bin[['road', 'road_detail',
                  'lon', 'lat']].head()
# pip install folium

shilin_center = [25.085201, 121.524982]
zoom = 12
map_osm = folium.Map(location=shilin_center,
                     zoom_start=zoom)
ucom_center = [25.052028, 121.543974]
for i in range(len(shilin_bin)):
    coordinate = [shilin_bin.iloc[i, 4], shilin_bin.iloc[i, 3]]
    sample_icon = folium.Icon(color='green', icon='info-sign')
    message1 = "[%s]%s" % (shilin_bin.iloc[i, 1], shilin_bin.iloc[i, 2])
    umessage1 = unicode(message1, "utf-8")
    folium.Marker(coordinate, icon=sample_icon, popup=umessage1) \
        .add_to(map_osm)

folium.CircleMarker(ucom_center, radius=30, popup='ucom training center',
                    fill_color='#C0FFEE').add_to(map_osm)

map_osm.save('.\\map\\map89.html')
