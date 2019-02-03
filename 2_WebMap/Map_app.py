import folium
import pandas


data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list (data["ELEV"])


def color_prod(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[43.655702, 25.428406], zoom_start=2, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name='Volcanoes')

for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el), parse_html=True),
#                                icon=folium.Icon(color=color_prod(el))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(str(el), parse_html=True),
                                     fill_color=color_prod(el), fill_opacity=0.7, color = 'grey', radius=6))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor' : 'yellow' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")