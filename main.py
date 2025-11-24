from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import meu_agente
import uvicorn
import os

class PedidoChat(BaseModel):
    mensagem: str

class RespostaChat(BaseModel):
    resposta: str

app = FastAPI(title="Minha API de Chat com IA")

@app.post("/chat", response_model=RespostaChat)
async def conversar(pedido: PedidoChat):
    try:
        resposta_ia = str(meu_agente(pedido.mensagem))

        return RespostaChat(resposta=resposta_ia)
    except Exception as e:
        print(f"Erro: {e}")
        raise HTTPException(status_code=500, detail="Erro ao processar a solicitação.")
    

if __name__ == "__main__":
        uvicorn.run(
            "main:app",
            host=os.getenv("API_HOST", "127.0.0.1"),
            port=int(os.getenv("API_PORT", 8000)),
            reload=True
        )