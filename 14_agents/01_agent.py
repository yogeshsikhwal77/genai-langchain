from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor,create_react_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate
load_dotenv()

search_tool = DuckDuckGoSearchRun()

template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}'''

llm = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

prompt = PromptTemplate.from_template(template)

agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt

)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

responce = agent_executor.invoke({"input":"3 ways to reach delhi from jodhpur"})

print(responce)

print(responce['output'])