import folium
import json

# Charger les arrondissements de Paris
with open("arrondissements.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

# Créer une carte
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Ajouter les arrondissements avec une couleur aléatoire
folium.GeoJson(
    geojson_data,
    style_function=lambda feature: {
        'fillColor': 'blue',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.6
    },
    highlight_function=lambda feature: {'weight': 3, 'fillOpacity': 0.8},
    tooltip=folium.GeoJsonTooltip(fields=["c_ar"]),  # Numéro de l'arrondissement
).add_to(m)

# Sauvegarde en HTML
m.save("carte_paris.html")
