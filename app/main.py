import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes

from app.chain import build_chain

load_dotenv()

USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"

if USE_OPENAI:
    from providers.openai import get_model
else:
    from providers.ollama import get_model

model = get_model()
chain = build_chain(model)

app = FastAPI(
    title="LangServe Translator",
    version="1.0.0",
    description="Prompt-driven translation API using LangChain and LangServe"
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)