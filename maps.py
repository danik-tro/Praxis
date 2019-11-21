"""
!folium.Marker(location=[37.4074687,-122.086669], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(maps) add marker
"""

import folium
import pandas as pd
from folium.plugins import MarkerCluster
import sys


def color_change(evl):
    if (evl < 1000):
        return 'green'
    elif 1000 <= evl < 3000:
        return 'orange'
    else:
        return 'red'

if __name__ == "__main__":
    data = pd.read_csv("maps/data/Volcanoes_USA.txt")

    lat = data['LAT']
    lon = data['LON']
    elevation = data['ELEV']
    name = data['NAME']

    maps = folium.Map(location=[37.4074687,-122.086669], zoom_start=5, tiles= 'CartoDB dark_matter')


    marker_cluster = MarkerCluster().add_to(maps)
    for lat_, lon_, elv_, name_ in zip(lat, lon, elevation, name):
        folium.CircleMarker(location=[lat_, lon_],radius=9,  popup=(name_ + "\n" + str(elv_) + " m"), fill_color = color_change(elv_), color="gray", fill_opacity = 0.9).add_to(marker_cluster)

    maps.save('maps/maps1.html')