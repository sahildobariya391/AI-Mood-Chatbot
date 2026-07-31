from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2506",
    api_key=os.getenv("MISTRAL_API_KEY")
)

response = model.invoke("Hello")
print(response.content)