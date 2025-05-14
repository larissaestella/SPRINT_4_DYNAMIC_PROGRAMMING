from geocodificador import calcular_distancia_km

def construir_grafo_lojas(lojas, comprador):
    grafo = {}
    pontos = lojas + [comprador]
    for origem in pontos:
        grafo[origem["nome"]] = {}
        for destino in pontos:
            if origem["nome"] != destino["nome"]:
                dist = calcular_distancia_km(origem["coordenadas"], destino["coordenadas"])
                grafo[origem["nome"]][destino["nome"]] = round(dist, 2)
    return grafo

def otimizar_rota_dijkstra(origem, entregas):
    pontos = [origem] + entregas
    grafo = {}
    for i in range(len(pontos)):
        for j in range(len(pontos)):
            if i != j:
                p1, p2 = pontos[i], pontos[j]
                d = calcular_distancia_km(p1["coordenadas"], p2["coordenadas"])
                grafo.setdefault(p1["nome"], {})[p2["nome"]] = d

    visitados = set()
    caminho = []
    atual = origem["nome"]
    visitados.add(atual)
    distancia_total = 0

    while len(visitados) < len(pontos):
        vizinhos = grafo[atual]
        nao_visitados = [(dest, dist) for dest, dist in vizinhos.items() if dest not in visitados]
        if not nao_visitados:
            break
        proximo, dist = min(nao_visitados, key=lambda x: x[1])
        caminho.append((atual, proximo))  
        distancia_total += dist
        visitados.add(proximo)
        atual = proximo

    return caminho, round(distancia_total, 2)
