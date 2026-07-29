from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='expalin the following joke \n {joke}',
    input_variables=['joke']
)

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>40,prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = report_gen_chain | branch_chain

result = final_chain.invoke({'topic':'iits'})

print(result)