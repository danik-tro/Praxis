import folium
import pandas as pd

data = pd.read_csv("maps/data/Volcanoes_USA.txt")

lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']
name = data['NAME']

maps = folium.Map(location=[50.4546600,30.5238000], zoom_start=8)

"""
!folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(maps) add marker
"""

for lat_, lon_, elv_, name_ in zip(lat, lon, elevation, name):
    folium.Marker(location=[lat_, lon_], popup=(name_ + "\n" + str(elv_) + " m"), icon=folium.Icon(color = 'gray')).add_to(maps)

maps.save('maps/maps1.html')