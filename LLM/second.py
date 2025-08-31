from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",temperature=1)

result = llm.invoke("What is the capital of Pakistan? Answer should be brief.")

print(result.content)