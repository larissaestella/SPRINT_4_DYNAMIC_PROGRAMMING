   MATHEUS FARIAS DE LIMA - RM554254    
   MIGUEL MAURICIO PARRADO PATARROYO – RM554007   
   LARISSA ESTELLA GONÇALVES DOS SANTOS – RM552695  
   VITOR PINHEIRO NASCIMENTO – RM553693    
   PEDRO HENRIQUE CHAVES - RM553988  

# CHALLENGE FIAP - SPRINT 4: OTIMIZAÇÃO DE ROTAS COM GRAFOS E DIJKSTRA

## Descrição

Este projeto visa implementar funcionalidades de **grafos** e o **algoritmo de Dijkstra** para otimizar rotas de entrega de peças automotivas da Rede Âncora, utilizando coordenadas geográficas para calcular as distâncias entre lojas e o ponto de origem (comprador).

---

## 📚 Funcionalidades

### 1. ⚙️ Aplicação de Grafos

* Representa lojas e comprador como nós de um grafo.
* Distâncias geográficas são utilizadas como pesos nas conexões (arestas) entre os nós.

### 2. 🛣️ Cálculo do Menor Caminho

* Utiliza o **algoritmo de Dijkstra** para encontrar a **rota mais eficiente** entre o ponto de origem (comprador) e as lojas.
* Baseado nas distâncias entre os nós (lojas e comprador), representadas por um grafo ponderado.

### 3. 🌍 Geocodificação de Endereços

* Converte endereços em **coordenadas geográficas (latitude e longitude)** com a **API do Google Maps**, com margem de erro mínima (1–5%).
* Facilita a integração de dados geográficos no cálculo de rotas.

### 4. 🗺️ Geração de Links para Google Maps

* Gera **links para visualização das rotas** no Google Maps, facilitando a visualização das entregas.
* Suporta **rotas de múltiplos destinos**, com base nas lojas a serem visitadas.

---

### 📁 Estrutura de Arquivos

```
SPRINT_4_DYNAMIC_PROGRAMMING/
├── app.py
├── geocodificador.py
├── grafo.py
├── maps.py
├── templates/
│   ├── calcular_rota.html
│   ├── construir_grafo.html
│   ├── exibir_grafo.html
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```
---

## ▶️ Como Rodar o Projeto

1. **Clone esse repositório ou baixe os arquivos** para sua máquina.
2. Verifique se você tem o Python 3 instalado.
3. No terminal, navegue até a pasta do projeto:

   ```bash
   cd caminho/para/SPRINT_4_DYNAMIC_PROGRAMMING
   ```
4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```
5. Execute a aplicação:

   ```bash
   python app.py
   ```
6. Acesse o sistema no navegador via:

   ```bash
   http://localhost:5000
   ```

---

### 📦 Dependências

Certifique-se de instalar as dependências listadas no arquivo requirements.txt para rodar o projeto corretamente:

   ```
    Flask #framework web usado para construir a aplicação e interface HTML.
    requests
   ```

---

### 📅 Instruções de Uso

Ao acessar o sistema, você encontrará as seguintes opções:

    Construir grafo (Inserir endereço para construir os grafos)

    Exibir grafo com distâncias em Km

    Calcular rota (cálculo do menor caminho e exibição da rota otimizada com links do Google Maps)

O sistema permite criar o grafo a partir do endereço do comprador e das lojas fixas e então calcular e exibir a melhor rota de entrega.

---

### 🎨 Tela Inicial e Navegação

Navegação simples via HTML/CSS com layout responsivo.

---

### 🗃️ Detalhes dos Arquivos

* **app.py:**
  Roteador principal da aplicação Flask.

* **grafo.py:**
  Contém funções para calcular distâncias, construir o grafo e implementar o algoritmo de Dijkstra.

* **geocodificador.py:**
  Interface com a API do Google Maps para conversão de endereços. O valor será coerente com o Google Maps com margem de erro mínima (1–5%).

* **maps.py:**
  Gera links para rotas no Google Maps. É usado para visualizar as rotas calculadas.

---

### ✅ Status de Integração

* **NOTA IMPORTANTE:** Este módulo **AINDA não está completamente integrado ao sistema principal do projeto** (catalogação, pedidos, login, etc.). Ele funciona de forma isolada para testes e validações de conceitos de grafos e otimização de rotas.

* **Problema de Conexão com a API:** Se você estiver em uma rede com firewall ou proxy, pode ocorrer um problema de conexão ao acessar a API do Google Maps, pois essas configurações podem bloquear a comunicação com os servidores dela. Caso isso aconteça, recomendamos testar o código fora da rede corporativa para garantir que as requisições possam ser feitas sem bloqueios, permitindo o acesso correto à API.

---

## 🧠 Aprendizados Aplicados

* **Algoritmos de Grafos**: Implementação de grafos e utilização do algoritmo de Dijkstra para otimização de rotas.
* **Geocodificação**: Uso de API para conversão de endereços em coordenadas geográficas (latitude/longitude).
* **Integração com Google Maps**: Geração de links para visualização de rotas de múltiplos destinos.
* **Estrutura de Dados**: Implementação eficiente de estruturas de dados para cálculos de distâncias e otimização de rotas.
* **Interface**: Criação de interface web simples com Flask + HTML/CSS.

---

## 🎓 Desenvolvido para

**Challenge FIAP - Sprint 04
Engenharia de Software**

