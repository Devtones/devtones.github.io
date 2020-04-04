#%%
import folium

# initialisation de la carte
coord_init = [48.85, 2.33] #Paris
myMap = folium.Map(location=coord_init,
    zoom_start=12, 
    tiles='cartodbpositron', 
    prefer_canvas=True
    )

# Fichier contenant le tracé des communes (format topojson)
shapefile_communes = "DATA/communes-IdF.geojson"

# Affichage du contour des communes
folium.GeoJson(shapefile_communes).add_to(myMap)

# Export en html
myMap.save('SimpleCoroplethe.html')

