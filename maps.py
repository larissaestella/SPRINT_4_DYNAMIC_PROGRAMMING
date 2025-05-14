def gerar_links_rota_google(origem_coord, destino_coord):
    origem = f"{origem_coord[0]},{origem_coord[1]}"
    destino = f"{destino_coord[0]},{destino_coord[1]}"
    return f"https://www.google.com/maps/dir/?api=1&origin={origem}&destination={destino}&travelmode=driving"
