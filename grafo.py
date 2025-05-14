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
    import heapq

    pontos = [origem] + entregas
    grafo = {}
    for i in range(len(pontos)):
        for j in range(len(pontos)):
            if i != j:
                p1, p2 = pontos[i], pontos[j]
                d = calcular_distancia_km(p1["coordenadas"], p2["coordenadas"])
                grafo.setdefault(p1["nome"], {})[p2["nome"]] = d

    visitados = set()
    caminho = [origem["nome"]]
    atual = origem["nome"]
    distancia_total = 0

    while len(visitados) < len(pontos) - 1:
        visitados.add(atual)
        vizinhos = grafo[atual]
        proximo = min((n for n in vizinhos if n not in visitados), key=lambda n: vizinhos[n])
        distancia_total += vizinhos[proximo]
        caminho.append(proximo)
        atual = proximo

    nome_para_coord = {p["nome"]: p["coordenadas"] for p in pontos}
    rota_com_coords = [(nome, nome_para_coord[nome]) for nome in caminho]

    return rota_com_coords, round(distancia_total, 2)
