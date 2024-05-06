import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_decision(valor, credito, renda, motivo):

    credito = credito.lower()
    motivo = motivo.lower()

    valor = float(valor)
    renda = float(renda)

    prompt = f"Cliente solicitou empréstimo de {valor}. Seu histórico de crédito é {credito}, sua renda mensal é de {renda} e o motivo é {motivo}. Classifique qual o risco do empréstimo, se é Alto ou Médio ou Baixo e justifique o motivo.\n"

    response = openai.Completion.create(
      engine="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=250
    )

    return response.choices[0].text.strip()

def run_decision_system():
    print("Testando o Sistema de Decisão de Empréstimos:")
    print("==============================================\n")

    valor = input("Informe o valor do empréstimo desejado: ")
    credito = input("Informe o nível do histórico de crédito (bom/medio/ruim): ")
    renda = input("Informe o valor da sua renda mensal: ")
    motivo = input("Informe o motivo do empréstimo: ")

    decision = generate_decision(valor, credito, renda, motivo)

    print("\nDecisão:")
    print(decision)
    print("\n==============================================\n")

run_decision_system()