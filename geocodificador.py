import requests
from math import radians, sin, cos, sqrt, atan2

# ⚠️ ATENÇÃO: NÃO utilizar a chave abaixo para além desse projeto, por gentileza!

API_KEY = "AIzaSyAEQbTwSKwW8I8u73kHsmzKjQTz9_hbpVE" 

def obter_coordenadas(endereco):
    url = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": endereco,
        "key": API_KEY
    }

    resposta = requests.get(url, params=params, verify=False).json()

    if resposta["status"] == "OK":
        local = resposta["results"][0]["geometry"]["location"]
        return (local["lat"], local["lng"])
    else:
        print(f"Erro ao geocodificar: {resposta}")
        return None


def calcular_distancia_km(coord1, coord2):
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    raio = 6371  
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return raio * c
