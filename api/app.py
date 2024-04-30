from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="langchain-server", version="1.0", description="API Server")

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} in around 100 words."
)

add_routes(app, prompt | model, path="/essay")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
