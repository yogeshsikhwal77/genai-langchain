from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,ToolMessage

load_dotenv()
@tool
def multiply(a: int,b: int) -> int:
    """we need to return product of two numbers a and b"""
    return a*b

llm = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
llm_with_tool = llm.bind_tools([multiply])

query = HumanMessage('you multiply 3 and 2894')

messages = [query]

result = llm_with_tool.invoke(messages)
messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

print(llm_with_tool.invoke(messages).content)