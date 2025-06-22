import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple


class NewsDataGenerator:
    def __init__(self):
        self.countries = [
            "Brasil", "Estados Unidos", "Rússia", "China", "Índia", 
            "Japão", "Alemanha", "França", "Reino Unido", "Itália",
            "Canadá", "Austrália", "Coreia do Sul", "México", "Turquia",
            "Arábia Saudita", "Irã", "Egito", "Nigéria", "África do Sul",
            "Argentina", "Chile", "Colômbia", "Peru", "Venezuela",
            "Espanha", "Países Baixos", "Suécia", "Noruega", "Dinamarca",
            "Suíça", "Áustria", "Bélgica", "Polônia", "Ucrânia",
            "República Tcheca", "Hungria", "Romênia", "Bulgária", "Grécia",
            "Portugal", "Irlanda", "Finlândia", "Islândia", "Nova Zelândia",
            "Singapura", "Malásia", "Tailândia", "Vietnã", "Indonésia",
            "Filipinas", "Paquistão", "Bangladesh", "Sri Lanka", "Myanmar",
            "Camboja", "Laos", "Mongólia", "Cazaquistão", "Uzbequistão",
            "Quirguistão", "Tajiquistão", "Turcomenistão", "Azerbaijão", "Geórgia",
            "Armênia", "Moldávia", "Bielorrússia", "Lituânia", "Letônia",
            "Estônia", "Eslováquia", "Eslovênia", "Croácia", "Sérvia",
            "Bósnia e Herzegovina", "Montenegro", "Macedônia do Norte", "Albânia", "Kosovo"
        ]
        
        self.country_emojis = {
            "Brasil": {"emoji": "🇧🇷", "iso": "BRA"},
            "Estados Unidos": {"emoji": "🇺🇸", "iso": "USA"},
            "Rússia": {"emoji": "🇷🇺", "iso": "RUS"},
            "China": {"emoji": "🇨🇳", "iso": "CHN"},
            "Índia": {"emoji": "🇮🇳", "iso": "IND"},
            "Japão": {"emoji": "🇯🇵", "iso": "JPN"},
            "Alemanha": {"emoji": "🇩🇪", "iso": "DEU"},
            "França": {"emoji": "🇫🇷", "iso": "FRA"},
            "Reino Unido": {"emoji": "🇬🇧", "iso": "GBR"},
            "Itália": {"emoji": "🇮🇹", "iso": "ITA"},
            "Canadá": {"emoji": "🇨🇦", "iso": "CAN"},
            "Austrália": {"emoji": "🇦🇺", "iso": "AUS"},
            "Coreia do Sul": {"emoji": "🇰🇷", "iso": "KOR"},
            "México": {"emoji": "🇲🇽", "iso": "MEX"},
            "Turquia": {"emoji": "🇹🇷", "iso": "TUR"},
            "Arábia Saudita": {"emoji": "🇸🇦", "iso": "SAU"},
            "Irã": {"emoji": "🇮🇷", "iso": "IRN"},
            "Egito": {"emoji": "🇪🇬", "iso": "EGY"},
            "Nigéria": {"emoji": "🇳🇬", "iso": "NGA"},
            "África do Sul": {"emoji": "🇿🇦", "iso": "ZAF"},
            "Argentina": {"emoji": "🇦🇷", "iso": "ARG"},
            "Chile": {"emoji": "🇨🇱", "iso": "CHL"},
            "Colômbia": {"emoji": "🇨🇴", "iso": "COL"},
            "Peru": {"emoji": "🇵🇪", "iso": "PER"},
            "Venezuela": {"emoji": "🇻🇪", "iso": "VEN"},
            "Espanha": {"emoji": "🇪🇸", "iso": "ESP"},
            "Países Baixos": {"emoji": "🇳🇱", "iso": "NLD"},
            "Suécia": {"emoji": "🇸🇪", "iso": "SWE"},
            "Noruega": {"emoji": "🇳🇴", "iso": "NOR"},
            "Dinamarca": {"emoji": "🇩🇰", "iso": "DNK"},
            "Suíça": {"emoji": "🇨🇭", "iso": "CHE"},
            "Áustria": {"emoji": "🇦🇹", "iso": "AUT"},
            "Bélgica": {"emoji": "🇧🇪", "iso": "BEL"},
            "Polônia": {"emoji": "🇵🇱", "iso": "POL"},
            "Ucrânia": {"emoji": "🇺🇦", "iso": "UKR"},
            "República Tcheca": {"emoji": "🇨🇿", "iso": "CZE"},
            "Hungria": {"emoji": "🇭🇺", "iso": "HUN"},
            "Romênia": {"emoji": "🇷🇴", "iso": "ROU"},
            "Bulgária": {"emoji": "🇧🇬", "iso": "BGR"},
            "Grécia": {"emoji": "🇬🇷", "iso": "GRC"},
            "Portugal": {"emoji": "🇵🇹", "iso": "PRT"},
            "Irlanda": {"emoji": "🇮🇪", "iso": "IRL"},
            "Finlândia": {"emoji": "🇫🇮", "iso": "FIN"},
            "Islândia": {"emoji": "🇮🇸", "iso": "ISL"},
            "Nova Zelândia": {"emoji": "🇳🇿", "iso": "NZL"},
            "Singapura": {"emoji": "🇸🇬", "iso": "SGP"},
            "Malásia": {"emoji": "🇲🇾", "iso": "MYS"},
            "Tailândia": {"emoji": "🇹🇭", "iso": "THA"},
            "Vietnã": {"emoji": "🇻🇳", "iso": "VNM"},
            "Indonésia": {"emoji": "🇮🇩", "iso": "IDN"},
            "Filipinas": {"emoji": "🇵🇭", "iso": "PHL"},
            "Paquistão": {"emoji": "🇵🇰", "iso": "PAK"},
            "Bangladesh": {"emoji": "🇧🇩", "iso": "BGD"},
            "Sri Lanka": {"emoji": "🇱🇰", "iso": "LKA"},
            "Myanmar": {"emoji": "🇲🇲", "iso": "MMR"},
            "Camboja": {"emoji": "🇰🇭", "iso": "KHM"},
            "Laos": {"emoji": "🇱🇦", "iso": "LAO"},
            "Mongólia": {"emoji": "🇲🇳", "iso": "MNG"},
            "Cazaquistão": {"emoji": "🇰🇿", "iso": "KAZ"},
            "Uzbequistão": {"emoji": "🇺🇿", "iso": "UZB"},
            "Quirguistão": {"emoji": "🇰🇬", "iso": "KGZ"},
            "Tajiquistão": {"emoji": "🇹🇯", "iso": "TJK"},
            "Turcomenistão": {"emoji": "🇹🇲", "iso": "TKM"},
            "Azerbaijão": {"emoji": "🇦🇿", "iso": "AZE"},
            "Geórgia": {"emoji": "🇬🇪", "iso": "GEO"},
            "Armênia": {"emoji": "🇦🇲", "iso": "ARM"},
            "Moldávia": {"emoji": "🇲🇩", "iso": "MDA"},
            "Bielorrússia": {"emoji": "🇧🇾", "iso": "BLR"},
            "Lituânia": {"emoji": "🇱🇹", "iso": "LTU"},
            "Letônia": {"emoji": "🇱🇻", "iso": "LVA"},
            "Estônia": {"emoji": "🇪🇪", "iso": "EST"},
            "Eslováquia": {"emoji": "🇸🇰", "iso": "SVK"},
            "Eslovênia": {"emoji": "🇸🇮", "iso": "SVN"},
            "Croácia": {"emoji": "🇭🇷", "iso": "HRV"},
            "Sérvia": {"emoji": "🇷🇸", "iso": "SRB"},
            "Bósnia e Herzegovina": {"emoji": "🇧🇦", "iso": "BIH"},
            "Montenegro": {"emoji": "🇲🇪", "iso": "MNE"},
            "Macedônia do Norte": {"emoji": "🇲🇰", "iso": "MKD"},
            "Albânia": {"emoji": "🇦🇱", "iso": "ALB"},
            "Kosovo": {"emoji": "🇽🇰", "iso": "XKX"}
        }
        
        self.tags = [
            "ransomware", "setor financeiro", "ciberataque", "vazamento dados",
            "malware", "phishing", "infraestrutura crítica", "governo",
            "saúde", "educação", "energia", "transporte", "comércio",
            "tecnologia", "redes sociais", "inteligência artificial",
            "blockchain", "cryptocurrency", "IoT", "cloud computing",
            "zero-day", "APT", "espionagem", "hacktivismo", "terrorismo digital"
        ]
        
        # Hotspots - países e tags que terão mais notícias
        self.hotspot_countries = ["Estados Unidos", "Brasil", "Rússia", "China"]
        self.hotspot_tags = ["ransomware", "ciberataque", "vazamento dados", "setor financeiro"]
        
        # Eventos em andamento para criar continuidade
        self.ongoing_events = {}
        
    def generate_news_text(self, country: str, tags: List[str], day: int, is_continuation: bool = False) -> str:
        """Gera texto de notícia com base no país, tags e se é continuação de evento"""
        
        templates = {
            "ransomware": [
                f"Ataque de ransomware afeta setor financeiro em {country}, causando interrupção em serviços bancários.",
                f"Novo ransomware se espalha rapidamente por empresas de {country}, afetando milhares de sistemas.",
                f"Especialistas em segurança alertam sobre nova variante de ransomware circulando em {country}."
            ],
            "setor financeiro": [
                f"Instituições financeiras de {country} reportam tentativas de fraude em alta.",
                f"Banco central de {country} anuncia novas medidas de segurança cibernética.",
                f"Vazamento de dados afeta clientes de bancos em {country}."
            ],
            "ciberataque": [
                f"Grande ciberataque atinge infraestrutura crítica de {country}.",
                f"Grupo hacker internacional ataca sistemas governamentais de {country}.",
                f"Empresas de {country} sofrem ataques coordenados simultâneos."
            ],
            "vazamento dados": [
                f"Vazamento massivo de dados pessoais expõe milhões de cidadãos de {country}.",
                f"Empresa de tecnologia de {country} confirma vazamento de informações sensíveis.",
                f"Investigadores descobrem novo vazamento de dados em {country}."
            ],
            "malware": [
                f"Novo malware se propaga rapidamente em redes corporativas de {country}.",
                f"Especialistas detectam campanha de malware direcionada a {country}.",
                f"Malware bancário afeta usuários de internet banking em {country}."
            ],
            "phishing": [
                f"Campanha de phishing em massa atinge usuários de {country}.",
                f"Golpistas se passam por instituições oficiais de {country}.",
                f"Aumento significativo em tentativas de phishing em {country}."
            ],
            "infraestrutura crítica": [
                f"Ataque cibernético afeta infraestrutura energética de {country}.",
                f"Sistemas de transporte de {country} sofrem interferência cibernética.",
                f"Redes de comunicação de {country} são alvo de ataque coordenado."
            ],
            "governo": [
                f"Agencias governamentais de {country} reportam tentativas de invasão.",
                f"Vazamento de documentos confidenciais do governo de {country}.",
                f"Sistemas de defesa cibernética de {country} são testados."
            ]
        }
        
        # Se é continuação de evento, usar templates de atualização
        if is_continuation:
            continuation_templates = {
                "ransomware": [
                    f"No {day}º dia do ataque, bancos de {country} continuam com instabilidade nos sistemas.",
                    f"Especialistas trabalham para conter o ransomware que afeta {country} há {day} dias.",
                    f"Novas variantes do malware são detectadas em {country}, complicando a resposta."
                ],
                "setor financeiro": [
                    f"Instituições financeiras de {country} implementam medidas emergenciais após {day} dias de crise.",
                    f"Reguladores de {country} investigam falhas de segurança que persistem há {day} dias.",
                    f"Impacto financeiro do incidente em {country} ultrapassa estimativas iniciais."
                ],
                "ciberataque": [
                    f"Investigadores de {country} identificam origem do ataque após {day} dias de análise.",
                    f"Cooperação internacional é estabelecida para combater ataque em {country}.",
                    f"Novos alvos são identificados na campanha de ataques contra {country}."
                ]
            }
            
            for tag in tags:
                if tag in continuation_templates:
                    return random.choice(continuation_templates[tag])
        
        # Templates normais
        for tag in tags:
            if tag in templates:
                return random.choice(templates[tag])
        
        # Template genérico se nenhuma tag específica for encontrada
        generic_templates = [
            f"Incidente de segurança cibernética afeta {country}.",
            f"Especialistas em segurança alertam sobre novas ameaças em {country}.",
            f"Empresas de {country} reforçam medidas de proteção digital."
        ]
        
        return random.choice(generic_templates)
    
    def should_continue_event(self, country: str, tags: List[str]) -> bool:
        """Decide se deve continuar um evento existente"""
        if country in self.ongoing_events:
            event = self.ongoing_events[country]
            # 30% de chance de continuar evento existente
            if random.random() < 0.3 and event['days'] < 7:  # Máximo 7 dias
                return True
        return False
    
    def start_new_event(self, country: str, tags: List[str]):
        """Inicia um novo evento"""
        self.ongoing_events[country] = {
            'tags': tags,
            'days': 1,
            'start_date': datetime.now()
        }
    
    def continue_event(self, country: str):
        """Continua um evento existente"""
        if country in self.ongoing_events:
            self.ongoing_events[country]['days'] += 1
    
    def generate_dataset(self, start_date: str = "2025-01-01", days: int = 90) -> Tuple[List[Dict], Dict]:
        """Gera dataset completo de notícias"""
        news_data = []
        start = datetime.strptime(start_date, "%Y-%m-%d")
        
        for day in range(days):
            current_date = start + timedelta(days=day)
            date_str = current_date.strftime("%Y-%m-%d")
            
            # Número de notícias por dia (10-50) com variação baseada em eventos
            base_news = random.randint(10, 30)
            
            # Adicionar variação baseada em eventos especiais
            # Fins de semana tendem a ter menos notícias
            if current_date.weekday() >= 5:  # Sábado ou domingo
                base_news = int(base_news * 0.7)
            
            # Eventos especiais (crises) que aumentam o número de notícias
            if random.random() < 0.1:  # 10% de chance de crise
                base_news = int(base_news * 2.5)
            
            # Picos aleatórios de atividade
            if random.random() < 0.05:  # 5% de chance de pico
                base_news = int(base_news * 1.8)
            
            # Garantir que está dentro dos limites
            num_news = max(10, min(50, base_news))
            
            # Selecionar países para o dia (exatamente num_news países, um por país)
            available_countries = self.countries.copy()
            selected_countries = []
            
            # Priorizar hotspots com mais frequência
            for hotspot in self.hotspot_countries:
                if hotspot in available_countries and random.random() < 0.8:  # 80% chance
                    selected_countries.append(hotspot)
                    available_countries.remove(hotspot)
            
            # Adicionar países restantes até atingir num_news
            while len(selected_countries) < num_news:
                if available_countries:
                    country = random.choice(available_countries)
                    selected_countries.append(country)
                    available_countries.remove(country)
                else:
                    # Se acabaram os países, recomeçar a lista
                    available_countries = self.countries.copy()
                    # Remover países já selecionados
                    for selected in selected_countries:
                        if selected in available_countries:
                            available_countries.remove(selected)
            
            # Gerar notícias para cada país selecionado
            for country in selected_countries:
                # Decidir se continua evento existente ou inicia novo
                is_continuation = self.should_continue_event(country, [])
                
                if is_continuation:
                    event_tags = self.ongoing_events[country]['tags']
                    tags = random.sample(event_tags, min(len(event_tags), random.randint(1, 2)))
                    self.continue_event(country)
                else:
                    # Selecionar tags (priorizar hotspots)
                    available_tags = self.tags.copy()
                    selected_tags = []
                    
                    # Priorizar tags hotspot com mais frequência
                    for hotspot_tag in self.hotspot_tags:
                        if hotspot_tag in available_tags and random.random() < 0.7:  # 70% chance
                            selected_tags.append(hotspot_tag)
                            available_tags.remove(hotspot_tag)
                    
                    # Adicionar tags restantes
                    num_tags = random.randint(1, 3)
                    while len(selected_tags) < num_tags and available_tags:
                        tag = random.choice(available_tags)
                        selected_tags.append(tag)
                        available_tags.remove(tag)
                    
                    tags = selected_tags
                    self.start_new_event(country, tags)
                
                # Gerar texto da notícia
                text = self.generate_news_text(country, tags, 
                                             self.ongoing_events[country]['days'] if country in self.ongoing_events else 1,
                                             is_continuation)
                
                news_item = {
                    "data": date_str,
                    "pais": country,
                    "texto": text,
                    "tags": tags
                }
                
                news_data.append(news_item)
        
        return news_data, self.country_emojis
    
    def save_data(self, filename: str = "news_data.json", emoji_filename: str = "country_emojis.json"):
        """Salva os dados gerados em arquivos JSON"""
        news_data, emojis = self.generate_dataset()
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        
        with open(emoji_filename, 'w', encoding='utf-8') as f:
            json.dump(emojis, f, ensure_ascii=False, indent=2)
        
        print(f"Dataset gerado com {len(news_data)} notícias")
        print(f"Dados salvos em {filename} e {emoji_filename}")

if __name__ == "__main__":
    generator = NewsDataGenerator()
    generator.save_data() 