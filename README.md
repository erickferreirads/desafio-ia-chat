# Desafio Dreamsquad - AI Chat API

Este projeto é uma API de Chat desenvolvida como parte do teste técnico para a vaga de estágio. A aplicação utiliza um Agente de IA rodando localmente (via Ollama) que consegue conversar naturalmente e também realizar cálculos matemáticos precisos utilizando uma ferramenta dedicada.

## 🛠️ Tecnologias

  * **Python 3.10+**
  * **FastAPI:** Para criar a API web.
  * **Strands Agents SDK:** Para gerenciar o agente de IA e as ferramentas.
  * **Ollama:** Para rodar o modelo de linguagem localmente.
  * **Pytest:** Para testes automatizados.

-----

## ⚙️ Configuração e Instalação

### 1\. Pré-requisitos

Você precisa ter instalado no seu computador:

  * [Python](https://www.python.org/downloads/)
  * [Ollama](https://ollama.com/)

### 2\. Configurar o Modelo de IA

Este projeto usa o modelo **Llama 3.1** (ou Qwen 2.5) pois versões anteriores (como o Llama 3 padrão) não suportam bem o uso de ferramentas.

Abra seu terminal e execute:bash
ollama pull llama3.1



### 3. Instalar o Projeto
Clone o repositório e instale as dependências:

````bash
# 1. Crie um ambiente virtual (recomendado)
python -m venv.venv

# 2. Ative o ambiente
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source.venv/bin/activate

# 3. Instale as bibliotecas
pip install -r requirements.txt
````

### 4\. Configurar Variáveis (.env)

Duplique o arquivo chamado `.env.example` na raiz do projeto e renomeie-o para `.env`:

```bash
# Comando rápido para criar o.env (Linux/Mac/Git Bash)
cp.env.example.env
```

-----

## ▶️ Como Rodar

Com o Ollama aberto e o ambiente virtual ativado, execute:

```bash
python main.py
```

A API estará rodando em `http://127.0.0.1:8000`.

-----

## 🧪 Como Testar

### Teste Manual

1.  Acesse `http://127.0.0.1:8000/docs` no seu navegador.
2.  Vá no endpoint `POST /chat` e clique em **Try it out**.
3.  Envie um JSON de teste:
    ```json
    {
      "message": "Quanto é a raiz quadrada de 144?"
    }
    ```
4.  O agente deve usar a calculadora e responder `12.0`.

### Testes Automatizados

Para verificar se a lógica e a segurança da calculadora estão funcionando, rode no terminal:

```bash
pytest
```

-----

## 📂 Estrutura de Arquivos

  * `main.py`: Código principal da API e rotas.
  * `agent.py`: Configuração do agente e da ferramenta de cálculo.
  * `test_main.py`: Testes unitários e de integração.
  * `requirements.txt`: Lista de dependências do projeto.
