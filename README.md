# 🗺️ Atlas Diário

Uma aplicação para análise e acompanhamento de eventos de interesse em notícias diárias globais, permitindo filtragem, visualização e exportação de dados de forma intuitiva.

## 📋 Funcionalidades

### Aba Timeline
- **Filtros globais:** Data inicial/final, seleção múltipla de países e tags
- **Tabela interativa:** Exibe notícias com data, país (com emoji), texto completo e tags
- **Paginação:** Navegação por páginas para melhor performance
- **Tag Cloud:** Visualização das tags mais frequentes no período selecionado
- **Exportação:** Download dos dados filtrados em formato CSV

### Aba Dataviz
- **Gráfico de linha:** Evolução do número de notícias por dia
- **Distribuição por país:** Top 15 países com mais notícias
- **Tags mais frequentes:** Ranking das tags mais utilizadas
- **Tag Cloud:** Visualização interativa das tags do período

## 🛠️ Tecnologias

- **Frontend & Backend:** Streamlit
- **Manipulação de dados:** Pandas
- **Visualizações:** Plotly
- **Word Cloud:** WordCloud + Matplotlib
- **Formato dos dados:** JSON

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
- `news_data.json` - Dataset com 90 dias de notícias (20-50 por dia)
- `country_emojis.json` - Mapeamento de países para emojis

### 3. Executar a aplicação
```bash
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`

## 📊 Características dos Dados

### Dataset de Teste
- **Período:** 90 dias consecutivos
- **Notícias por dia:** 20 a 50
- **Países:** 20 países diferentes (máximo 1 notícia por país/dia)
- **Tags:** 1 a 3 tags por notícia (tags de 1-2 palavras)
- **Hotspots:** Países e tags com maior concentração de notícias

### Continuidade de Eventos
- Eventos podem se estender por vários dias
- Notícias consecutivas para o mesmo país podem complementar eventos anteriores
- Cria narrativas sequenciais para simular investigações reais

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

## 🎯 Hotspots Implementados

### Países com Mais Atividade
- Estados Unidos 🇺🇸
- Brasil 🇧🇷
- Rússia 🇷🇺
- China 🇨🇳

### Tags Mais Frequentes
- ransomware
- ciberataque
- vazamento dados
- setor financeiro

## 📱 Interface

### Sidebar - Filtros Globais
- **Período:** Seleção de data inicial e final
- **Países:** Seleção múltipla de países
- **Tags:** Seleção múltipla de tags

### Aba Timeline
- Estatísticas resumidas
- Tabela paginada com notícias
- Tag cloud interativa
- Botão de exportação CSV

### Aba Dataviz
- Gráfico de linha temporal
- Gráfico de barras por país
- Gráfico de barras por tags
- Tag cloud do período

## 🔧 Personalização

### Adicionar Novos Países
Edite o arquivo `data_generator.py` e adicione países na lista `self.countries` e seus respectivos emojis em `self.country_emojis`.

### Adicionar Novas Tags
Adicione novas tags na lista `self.tags` do gerador de dados.

### Modificar Templates de Notícias
Edite os dicionários `templates` e `continuation_templates` na função `generate_news_text()`.

## 📈 Análise de Dados

A aplicação permite:
- Identificar picos de atividade por país
- Acompanhar evolução de eventos ao longo do tempo
- Analisar distribuição de tags e temas
- Exportar dados para análise externa
- Visualizar hotspots de atividade

## 🤝 Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Implemente as mudanças
4. Teste a aplicação
5. Envie um pull request

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ usando Streamlit, Pandas e Plotly** 