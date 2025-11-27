from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import meu_agente
import uvicorn
import os

class PedidoChat(BaseModel):
    message: str

class RespostaChat(BaseModel):
    response: str

app = FastAPI(title="Dreamsquad AI Chat")

@app.post("/chat", response_model=RespostaChat)
async def conversar(pedido: PedidoChat):
    try:
        resposta_ia = str(meu_agente(pedido.message))

        return RespostaChat(response=resposta_ia)
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