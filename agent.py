import math
from dotenv import load_dotenv
from strands import tool

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
    