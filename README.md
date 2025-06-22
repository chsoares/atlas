# 🗺️ Atlas

Uma aplicação interativa para análise e visualização de notícias globais de segurança cibernética, desenvolvida com Streamlit e Plotly. Permite acompanhar eventos em tempo real, filtrar dados por período, países e tags, e gerar insights através de visualizações dinâmicas.

## 📋 Funcionalidades

### Aba Timeline
- **Filtros avançados:** Data inicial/final, seleção múltipla de países e tags
- **Métricas em tempo real:** Contadores de notícias, países, tags e período
- **Timeline interativa:** Visualização cronológica agrupada por data com países ordenados alfabeticamente
- **Tags estilizadas:** Ribbons coloridos para melhor identificação visual
- **Evolução temporal das tags:** Gráfico de linha com filtro múltiplo de tags selecionadas
- **Tag Cloud:** Visualização das tags mais frequentes no período
- **Exportação:** Download dos dados filtrados em formato CSV

### Aba Dataviz
- **Métricas gerais:** Estatísticas do dataset completo
- **Gráfico de linha temporal:** Evolução do número de notícias por dia com design otimizado
- **Mapa de calor geográfico:** Distribuição de notícias por país usando choropleth
- **Análise de tags:** Word cloud e tabela de frequências com filtros de data
- **Design consistente:** Visualizações com tema unificado e cores do Streamlit

## 🛠️ Tecnologias

- **Frontend & Backend:** Streamlit
- **Manipulação de dados:** Pandas
- **Visualizações:** Plotly (go.Figure, px.line, px.choropleth)
- **Word Cloud:** WordCloud + Matplotlib
- **Formato dos dados:** JSON
- **Estilização:** CSS customizado

## 🚀 Instalação e Uso

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Gerar dados de teste
```bash
python data_generator.py
```

Este comando irá gerar:
- `news_data.json` - Dataset com 90 dias de notícias (10-50 por dia)
- `country_emojis.json` - Mapeamento de 80 países para emojis e códigos ISO

### 3. Executar a aplicação
```bash
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`

## 📊 Características dos Dados

### Dataset de Teste
- **Período:** 90 dias consecutivos (1º de janeiro a 31 de março de 2025)
- **Notícias por dia:** 10 a 50 (com variação realística)
- **Países:** 80 países diferentes (máximo 1 notícia por país/dia)
- **Tags:** 1 a 3 tags por notícia (25 tags diferentes)
- **Variação temporal:** Fins de semana com menos atividade, crises e picos aleatórios

### Padrões Realísticos
- **Fins de semana:** 30% menos notícias
- **Crises:** 150% mais notícias (10% de chance)
- **Picos aleatórios:** 80% mais notícias (5% de chance)
- **Continuidade de eventos:** Notícias consecutivas para o mesmo país

### Hotspots Implementados
- **Países prioritários:** Estados Unidos, Brasil, Rússia, China (80% de chance)
- **Tags prioritárias:** ransomware, ciberataque, vazamento dados, setor financeiro (70% de chance)

### Estrutura dos Dados
```json
[
  {
    "data": "2025-01-01",
    "pais": "Brasil",
    "texto": "Ataque de ransomware afeta setor financeiro brasileiro, causando interrupção em serviços bancários.",
    "tags": ["ransomware", "setor financeiro"]
  }
]
```



## 🔧 Personalização

### Adicionar Novos Países
Edite o arquivo `data_generator.py`:
```python
self.countries = ["Novo País", ...]
self.country_emojis = {
    "Novo País": {"emoji": "🏳️", "iso": "XXX"},
    ...
}
```

### Adicionar Novas Tags
```python
self.tags = ["nova tag", ...]
```

### Modificar Templates de Notícias
Edite os dicionários `templates` e `continuation_templates` na função `generate_news_text()`.

### Ajustar Variação Temporal
Modifique os parâmetros na função `generate_dataset()`:
- Probabilidade de crise: `random.random() < 0.1`
- Probabilidade de pico: `random.random() < 0.05`
- Redução em fins de semana: `base_news * 0.7`
