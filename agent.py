import os
import math
from dotenv import load_dotenv
from strands import Agent, tool
from strands.models.ollama import OllamaModel

load_dotenv()

@tool
def calculadora(expressao: str) -> str:
    """
    Calcula o resultado matemático de uma expressão.
    Útil para resolver contas de somar, subtrair, multiplicar, dividir e raiz quadrada.

    Args:
        expressao: A conta matemática para resolver (ex: '123*456' ou 'sqrt(144)').
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
        temperature=0.1
    )

    agente = Agent(
        model=modelo,
        tools=[calculadora],
        system_prompt="Você é um assistente útil. Se o usuário pedir uma conta matemática, use a ferramenta calculadora para resolver."
    )

    return agente

meu_agente = criar_agente()