from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

messages = [
    SystemMessage(content='you are a housewife'),
    HumanMessage(content='what work you done')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)