# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 01:27:12 2020

@author: Harsh
"""
import pandas as pd
import folium

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58, -99.09],zoom_start=6,title="Stamen Terrain")
fgv=folium.FeatureGroup(name="Volcanoes")
def color_producer(elev):
    if elev<1000:
        return "green"
    elif 1000<elev<3000:
        return "orange"
    else:
        return "red"
    
for i ,j,k in zip(lat,lon,elev):

    fgv.add_child(folium.CircleMarker(location=[i,j],radius=6,popup=folium.Popup(str(k)+"m",parse_html=True)
                                     ,fill_color=color_producer(k),color='grey',fill_opacity=0.7))
fgp=folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)  
map.add_child(fgp) 
map.add_child(folium.LayerControl())               
map.save("map1.html")
