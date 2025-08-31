from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-4o-mini")

result = llm.invoke("What is the capital of Pakistan? Answer should be brief.")

print(result)