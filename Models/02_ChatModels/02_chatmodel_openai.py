from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-0.6',temperature=0.6)

result = model.invoke("Which model i use")

print(result.content)