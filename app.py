from flask import Flask, render_template, request, redirect, url_for, session
from grafo import construir_grafo_lojas, otimizar_rota_dijkstra
from geocodificador import obter_coordenadas, calcular_distancia_km
from maps import gerar_links_rota_google

app = Flask(__name__)
app.secret_key = "segredo"

lojas = [
    {"nome": "Loja A", "endereco": "Rua Vergueiro, 1000 - São Paulo, SP"},
    {"nome": "Loja B", "endereco": "Rua Frei Caneca, 520 - Consolação, São Paulo - SP"},
    {"nome": "Loja C", "endereco": "Av. Faria Lima, 1156 - Jardim Paulistano, São Paulo - SP"},
    {"nome": "Loja D", "endereco": "Rua Afonso Brás, 200 - Vila Nova Conceição, São Paulo - SP"},
    {"nome": "Loja E", "endereco": "Rua Pedroso Alvarenga, 460 - Vila Olímpia, São Paulo - SP"},
    {"nome": "Loja F", "endereco": "Av. Dr. Arnaldo, 1234 - Cerqueira César, São Paulo - SP"},
    {"nome": "Loja G", "endereco": "Rua Clodomiro Amazonas, 950 - Itaim Bibi, São Paulo - SP"},
    {"nome": "Loja H", "endereco": "Rua Teodoro Sampaio, 1450 - Pinheiros, São Paulo - SP"},
    {"nome": "Loja I", "endereco": "Av. Paulista, 1313 - Bela Vista, São Paulo - SP"},
    {"nome": "Loja J", "endereco": "Av. Sapopemba, 7890 - Sapopemba, São Paulo - SP"},
    {"nome": "Loja K", "endereco": "Rua Amador Bueno, 456 - Santo Amaro, São Paulo - SP"},
    {"nome": "Loja L", "endereco": "Av. Cupecê, 1020 - Jardim Miriam, São Paulo - SP"},
    {"nome": "Loja M", "endereco": "Rua Maria Cândida, 630 - Vila Guilherme, São Paulo - SP"},
    {"nome": "Loja N", "endereco": "Av. Itaquera, 2100 - Itaquera, São Paulo - SP"},
    {"nome": "Loja O", "endereco": "Rua Voluntários da Pátria, 1345 - Santana, São Paulo - SP"},
    {"nome": "Loja P", "endereco": "Av. Washington Luís, 3500 - Campo Belo, São Paulo - SP"},
    {"nome": "Loja Q", "endereco": "Rua Nossa Senhora das Graças, 87 - Osasco, SP"},
    {"nome": "Loja R", "endereco": "Av. Dom Pedro I, 190 - Vila São José, São Bernardo do Campo - SP"},
    {"nome": "Loja S", "endereco": "Rua Dona Primitiva Vianco, 400 - Centro, Barueri - SP"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/construir_grafo', methods=['GET', 'POST'])
def construir_grafo():
    if request.method == 'POST':
        endereco = request.form.get('endereco')
        coord = obter_coordenadas(endereco)
        if coord:
            comprador = {"nome": "Comprador", "endereco": endereco, "coordenadas": coord}
            
            for loja in lojas:
                loja["coordenadas"] = obter_coordenadas(loja["endereco"])
            
            # Construir o grafo
            grafo = construir_grafo_lojas(lojas, comprador)

            # Estruturar o grafo para facilitar a exibição
            grafo_completo = {'comprador': {}}
            for loja in lojas:
                nome_loja = loja['nome']
                grafo_completo['comprador'][nome_loja] = calcular_distancia_km(comprador['coordenadas'], loja['coordenadas'])
            
            for loja in lojas:
                nome_loja = loja['nome']
                grafo_completo[nome_loja] = {}
                for outra_loja in lojas:
                    if loja != outra_loja:
                        grafo_completo[nome_loja][outra_loja['nome']] = calcular_distancia_km(loja['coordenadas'], outra_loja['coordenadas'])

            session['grafo'] = grafo_completo
            session['comprador'] = comprador
            return render_template('construir_grafo.html', sucesso=True)
        else:
            return render_template('construir_grafo.html', erro=True)
        
    return render_template('construir_grafo.html')



@app.route('/exibir_grafo')
def exibir_grafo():
    grafo = session.get('grafo')
    if not grafo:
        return render_template('exibir_grafo.html', erro=True)

    # Organizar as distâncias para facilitar a exibição no template
    distancias_comprador_lojas = []
    for destino, distancia in grafo.get('comprador', {}).items():
        distancias_comprador_lojas.append(f"Comprador → {destino}: {distancia} km")

    distancias_lojas_lojas = []
    for origem, destinos in grafo.items():
        if origem != 'comprador':  # Evitar mostrar o comprador nas distâncias das lojas
            for destino, distancia in destinos.items():
                distancias_lojas_lojas.append(f"{origem} → {destino}: {distancia} km")

    return render_template(
        'exibir_grafo.html',
        grafo=grafo,
        erro=False
    )

@app.route('/calcular_rota', methods=['POST', 'GET'])
def calcular_rota():
    if request.method == 'POST':
        loja_index = request.form.get('loja_index')

        if not loja_index:
            erro = "Por favor, selecione uma loja de origem."
            return render_template('calcular_rota.html', erro=erro, lojas=lojas)

        try:
            loja_index = int(loja_index)
            loja_origem = lojas[loja_index]
        except (ValueError, IndexError):
            erro = "Loja selecionada inválida."
            return render_template('calcular_rota.html', erro=erro, lojas=lojas)

        loja_origem['coordenadas'] = obter_coordenadas(loja_origem['endereco'])

        num_entregas_str = request.form.get('num_entregas')
        if num_entregas_str == 'outro':
            num_entregas_digitar = request.form.get('num_entregas_digitar')
            if not num_entregas_digitar or not num_entregas_digitar.isdigit():
                erro = "Por favor, selecione a quantidade de entregas."
                return render_template('calcular_rota.html', erro=erro, lojas=lojas)
            num_entregas = int(num_entregas_digitar)
        elif num_entregas_str and num_entregas_str.isdigit():
            num_entregas = int(num_entregas_str)
        else:
            erro = "Por favor, selecione a quantidade de entregas."
            return render_template('calcular_rota.html', erro=erro, lojas=lojas)

        entregas = []
        for i in range(1, num_entregas + 1):
            endereco_key = f'endereco_entrega_{i}'
            endereco = request.form.get(endereco_key)
            if not endereco:
                erro = f"Por favor, preencha todos os endereços de entrega."
                return render_template('calcular_rota.html', erro=erro, lojas=lojas)

            coord = obter_coordenadas(endereco)
            if coord:
                entregas.append({
                    "nome": f"Entrega {i}",
                    "endereco": endereco,
                    "coordenadas": coord
                })

        if not entregas:
            erro = "Endereço de entrega inválido."
            return render_template('calcular_rota.html', erro=erro, lojas=lojas)

        # Calcular rota otimizada
        rota, distancia_total = otimizar_rota_dijkstra(loja_origem, entregas)
        tempo_estimado = (distancia_total / 40) * 60  # 40 km/h média

        # Dicionários auxiliares
        coordenadas_por_nome = {}
        nomes_por_coordenada = {}

        # Loja de origem
        coordenadas_por_nome[loja_origem['nome']] = loja_origem['coordenadas']
        nomes_por_coordenada[loja_origem['coordenadas']] = loja_origem['nome']

        # Entregas
        for entrega in entregas:
            coordenadas_por_nome[entrega['nome']] = entrega['coordenadas']
            nomes_por_coordenada[entrega['coordenadas']] = entrega['nome']

        # Links e distâncias
        links = []
        distancias = []
        for origem, destino in rota:
            coord_origem = coordenadas_por_nome[origem]
            coord_destino = coordenadas_por_nome[destino]
            links.append(gerar_links_rota_google(coord_origem, coord_destino))
            distancias.append(round(calcular_distancia_km(coord_origem, coord_destino), 2))

        return render_template(
            'calcular_rota.html',
            rota=rota,
            distancia=round(distancia_total, 2),
            tempo=tempo_estimado,
            links=links,
            coordenadas=coordenadas_por_nome,
            distancias=distancias
        )

    return render_template('calcular_rota.html', lojas=lojas)

if __name__ == '__main__':
    app.run(debug=True)
