import os
from dotenv import load_dotenv
import openai

load_dotenv()

def carregar_regras_avancadas():
    regras = {
        "regras": [
            "Renda alta (maior que 3 vezes o valor do empréstimo solicitado) com dívidas baixas (<30% da renda): Risco Baixo.",
            "Renda média (1 a 3 vezes maior que o valor do empréstimo) com dívidas moderadas (30-50% da renda): Risco Moderado.",
            "Renda baixa (menor que o valor do empréstimo) com dívidas altas (>50% da renda): Risco Alto.",
            "Dívidas totais <30% da renda indicam gestão financeira saudável: Risco Baixo.",
            "Dívidas entre 30% e 50% da renda: Risco Moderado.",
            "Dívidas >50% da renda são preocupantes: Risco Alto.",
            "Histórico sem atrasos: Risco Baixo.",
            "Histórico com atrasos nos últimos 2 anos: Risco Moderado.",
            "Histórico com múltiplas inadimplências: Risco Alto.",
            "Investimento em educação ou saúde: Risco Baixo a Moderado.",
            "Compra de bens duráveis ou melhoria de casa: Risco Moderado.",
            "Gastos com estilo de vida não essencial: Risco Moderado a Alto."
        ]
    }
    return regras

def avaliar_risco_cliente(client_data, regras):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    regras_prompt = " ".join(regras['regras'])
    prompt_text = f"""
      {regras_prompt}
      Avalie o cliente com os seguintes dados:
      Valor do Empréstimo: {client_data['valor_emprestimo']}, Renda Mensal: {client_data['renda']}, 
      Dívidas: {client_data['dividas']}, Histórico de Crédito: {client_data['historico_credito']}, 
      Motivo da Solicitação: {client_data['motivo_emprestimo']}.
      Classifique o risco como Alto, Moderado ou Baixo e justifique sua decisão.
      """

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt_text,
        temperature=0.5,
        max_tokens=250
    )

    return response.choices[0].text.strip()

regras = carregar_regras_avancadas()
client_data = {
    "valor_emprestimo": "R$5000",
    "renda": "R$7000",
    "dividas": "R$2000",
    "historico_credito": "Excelente",
    "motivo_emprestimo": "Comprar um carro novo"
}

risco = avaliar_risco_cliente(client_data, regras)
print(risco)
