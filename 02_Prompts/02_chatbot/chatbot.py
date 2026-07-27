from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

chat_history = [
    SystemMessage(content="you are a engineer")
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break

    result = model.invoke(chat_history)

    if isinstance(result.content, list):
        # Extract the 'text' key from the first block in the list
        ai_response = result.content[0].get('text', '')
    else:
        ai_response = result.content
    
    chat_history.append(AIMessage(content=ai_response))
    print("AI: ",ai_response)

print(chat_history)