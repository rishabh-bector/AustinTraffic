from folium.plugins import HeatMap
from tqdm import *
import pandas
import folium
import math

austin = pandas.read_csv("austin.csv", header=None)
austin.columns = ["id", "date", "issue", "location", "lat", "long", "address", "status", "status_date"]

map1 = folium.Map(location=[30.2653464,-97.7421536], zoom_start=13)

locations = []
for index, row in austin[["lat", "long"]].iterrows():
	try:
		if not math.isnan(float(row[0])):
			locations.append([float(row[0]), float(row[1])])
	except Exception as e:
		print(e)
HeatMap(locations, radius=15, blur=20, min_opacity=0.2).add_to(map1) 

map1.save("map.html")
print('DONE')

