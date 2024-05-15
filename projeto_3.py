import os
from dotenv import load_dotenv
import openai

load_dotenv()

def get_knowledge():
    return {
        "diseases": [
            {
                "name": "Gripe Comum",
                "symptoms": [
                    "febre alta", "dores musculares severas", "cansaço extremo", "dor de cabeça severa", 
                    "tosse seca", "dor de garganta", "espirros"
                ],
                "description": "A gripe comum é uma infecção viral que ataca o sistema respiratório."
            },
            {
                "name": "Resfriado",
                "symptoms": [
                    "coriza", "congestão nasal", "dor de garganta leve", "espirros", 
                    "tosse leve", "dor de cabeça leve"
                ],
                "description": "O resfriado é uma infecção viral do trato respiratório superior."
            },
            {
                "name": "Zika",
                "symptoms": [
                    "febre baixa", "erupções cutâneas com pontos brancos ou vermelhos", "dores nas articulações", 
                    "conjuntivite", "dor de cabeça"
                ],
                "description": "A Zika é uma infecção viral transmitida principalmente por mosquitos Aedes."
            },
            {
                "name": "Chikungunya",
                "symptoms": [
                    "febre alta", "dores intensas nas articulações", "erupções cutâneas", 
                    "dores musculares", "dor de cabeça", "fadiga"
                ],
                "description": "Chikungunya é uma infecção viral transmitida por mosquitos, causando febre e dor intensa nas articulações."
            },
            {
                "name": "COVID-19",
                "symptoms": [
                    "febre", "tosse seca", "cansaço", "perda de olfato e paladar", 
                    "dificuldade respiratória", "dor de cabeça", "dores no corpo"
                ],
                "description": "COVID-19 é uma doença respiratória causada pelo coronavírus SARS-CoV-2."
            }
        ]
    }

def build_prompt(symptoms, knowledge_base):
    prompt = f"Paciente apresenta os seguintes sintomas: {', '.join(symptoms)}.\n\n"
    prompt += "Base de conhecimento sobre doenças:\n"

    for disease in knowledge_base['diseases']:
        prompt += f"\n{disease['name']}:\n"
        prompt += f"Descrição: {disease['description']}\n"
        prompt += f"Sintomas: {', '.join(disease['symptoms'])}\n"

    prompt += "\nCom base nos sintomas fornecidos e na base de conhecimento, qual é o diagnóstico mais provável? "
    prompt += "Inclua recomendações de tratamento e justifique cada decisão com base nos sintomas fornecidos."
    
    return prompt

def diagnose_viral_infections(symptoms):
    knowledge_base = get_knowledge()
    prompt = build_prompt(symptoms, knowledge_base)

    openai.api_key = os.getenv('OPENAI_API_KEY')

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=600,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Erro ao acessar a API da OpenAI: {str(e)}"


symptoms = ["febre baixa", "dor de cabeça", "conjuntivite", "dor nas articulações"]
result = diagnose_viral_infections(symptoms)
print(result)
