import os
import math
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.ollama import OllamaModel

load_dotenv()

@tool
def calculadora(expressao: str) -> str:
    """
    Avalia uma expressão matemática simples e retorna o resultado.
    Útil para realizar cálculos de adição, subtração, multiplicação, divisão e potências.
    O agente deve usar esta ferramenta sempre que uma pergunta envolver matemática.

    Args:
        expressao: A conta matemática para resolver (ex: '123*456' ou 'sqrt(144)').

    Returns:
        str: O resultado do cálculo ou uma mensagem de erro.
    """
    funcoes_permitidas = {
        'sqrt': math.sqrt,
        'pow': math.pow,
        'pi': math.pi,
        'round': round
    }

    try:
        resultado = eval(expressao, {"__builtins__":{}}, funcoes_permitidas)
        return str(resultado)
    except Exception as erro:
        return f"Erro ao calcular: {str(erro)}"
    
def criar_agente():
    modelo = OllamaModel(
        host=os.getenv("OLLAMA_HOST"),
        model_id=os.getenv("OLLAMA_MODEL"),
        temperature=0.1,
        keep_alive="5m"
    )

    agente = Agent(
        model=modelo,
        tools=[calculadora],
        system_prompt="Você é um assistente de IA útil e preciso. "
                "Para qualquer pergunta que envolva cálculos matemáticos, "
                "você DEVE utilizar a ferramenta 'calculadora' disponível. "
                "Não tente adivinhar o resultado."
    )
    print("Agente inicializado com sucesso.")
    return agente

meu_agente = criar_agente()