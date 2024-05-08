import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

class MiniAkinatorGPT:
    def __init__(self):

        self.characters = {
            "Homem de Ferro": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "não",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "É um bilionário?": "sim",
                "Consegue voar com o traje?": "sim",
            },
            "Thor": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "não",
                "Faz parte de um grupo?": "sim",
                "Vive em Asgard?": "sim",
            },
            "Coringa": {
                "É um herói?": "não",
                "Usa um traje especial?": "não",
                "Tem superpoderes?": "não",
                "É humano?": "sim",
                "Faz parte de um grupo?": "não",
                "É um vilão do Batman?": "sim",
            },
            "Loki": {
                "É um herói?": "não",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "não",
                "Faz parte de um grupo?": "não",
                "É irmão de Thor?": "sim",
            },
            "Batman": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "não",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "É um bilionário?": "sim",
                "Ele se veste como um morcego?": "sim",
            },
            "Mulher Maravilha": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "não",
                "Faz parte de um grupo?": "sim",
                "Vem da Ilha de Themyscira?": "sim",
            },
            "Superman": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "não",
                "Faz parte de um grupo?": "sim",
                "Vem de Krypton?": "sim",
            },
            "Flash": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "Corre muito rápido?": "sim",
            },
            "Homem-Aranha": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "Foi picado por uma aranha radioativa?": "sim",
            },
            "Capitão América": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "Ele foi um soldado héroi de guerra?": "sim",
            },
            "Hulk": {
                "É um herói?": "sim",
                "Usa um traje especial?": "não",
                "Tem superpoderes?": "sim",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "Fica muito grande e verde quando está bravo?": "sim",
            },
            "Aquaman": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "não",
                "Faz parte de um grupo?": "sim",
                "Vive na Atlântida?": "sim",
            },
            "Pantera Negra": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "É o rei de Wakanda?": "sim",
            },
            "Doutor Estranho": {
                "É um herói?": "sim",
                "Usa um traje especial?": "sim",
                "Tem superpoderes?": "sim",
                "É humano?": "sim",
                "Faz parte de um grupo?": "sim",
                "É um cirurgião convertido em feiticeiro?": "sim",
            },
        }

        self.questions = [
            "É um herói?",
            "Usa um traje especial?",
            "Tem superpoderes?",
            "É humano?",
            "Faz parte de um grupo?",
            "É um bilionário?",
            "Foi picado por uma aranha radioativa?",
            "Fica muito grande e verde quando está bravo?",
            "Corre muito rápido?",
            "Vive em Asgard?",
            "Vem da Ilha de Themyscira?",
            "Vem de Krypton?",
            "Vive na Atlântida?",
            "É um vilão do Batman?",
            "É irmão de Thor?",
            "É o rei de Wakanda?",
            "Consegue voar com o traje?",
            "Ele se veste como um morcego?",
            "Ele foi um soldado héroi de guerra?"
        ]

    def gpt3_predict_character(self, answers):
        """Pede ao GPT-3.5 para tentar adivinhar o personagem baseado nas respostas dadas."""
        prompt = f"""
        Eu tenho uma lista de personagens e suas características:
        {self.characters}

        Baseado nas seguintes respostas, tente adivinhar qual é o personagem:
        {answers}

        Responda apenas com o nome do personagem que você acredita que seja.
        """

        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=50,
            temperature=0.3,
            n=1
        )

        return response.choices[0].text.strip()

    def ask_question(self, question):
        """Faz uma pergunta ao usuário e coleta uma resposta."""
        while True:
            answer = input(f"{question} (sim/não): ").strip().lower()
            if answer in ["sim", "não"]:
                return answer
            else:
                print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

    def play(self):
        """Inicia o jogo usando GPT-3.5 para prever o personagem."""
        print("Bem-vindo ao Mini-Akinator com GPT-3.5!")

        answers = {}
        for question in self.questions:
            answers[question] = self.ask_question(question)

        character = self.gpt3_predict_character(answers)
        if character != "Desconhecido":
            print(f"Você está pensando em {character}!")
        else:
            print("Não consegui adivinhar o personagem.")

if __name__ == "__main__":
    akinator = MiniAkinatorGPT()
    akinator.play()
