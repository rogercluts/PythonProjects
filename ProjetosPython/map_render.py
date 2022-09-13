import folium

mapa = folium.Map(
    location=[-23.550093493433984, -46.6341472592547],
    tiles='Stamen Terrain',
    zoom_start=16
)

folium.Marker(
    [-23.550093493433984, -46.6341472592547],
    popup='<i>Praça da Sé<i>',
    tooltip='Click Aqui'
).add_to(mapa)

mapa.save(r'.\mapa.html')