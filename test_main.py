import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from agent import calculadora

client = TestClient(app)

def test_calculadora_soma():
    """Testa se a função de calculo resolve contas básicas corretamente."""
    resultado = calculadora("2 + 2")
    assert resultado == "4"

def test_calculadora_complexa():
    """Testa se a função de calculo resolve contas mais complexas corretamente."""
    resultado = calculadora("sqrt(144)")
    assert resultado == "12.0"

def test_calculadora_seguranca():
    """Testa se a calculadora bloqueia comandos perigosos.(ex: import os)"""
    comando_perigoso = "__import__('os').system('ls')"
    resultado = calculadora(comando_perigoso)
    assert "Erro" in resultado or "não permitido" in resultado

@patch("main.meu_agente")
def test_api_chat_responde_200(mock_agente):
    """Testa se o endpoint /chat recebe a mensagem e devolve JSON, fingindo que a IA respondeu 'Olá!'."""
    
    mock_agente.return_value = "Resposta de teste"

    response = client.post("/chat", json={"mensagem": "Olá, IA!"})
    assert response.status_code == 200

    json_response = response.json()
    assert json_response["resposta"] == "Resposta de teste"
