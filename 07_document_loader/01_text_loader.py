from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('text.txt',encoding='utf-8')

docs = loader.load()

prompt = PromptTemplate(
    template='give me 5 line summary of this text \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

# print(docs)
# print("-"*50)
# print(type(docs))
# print("-"*50)
# print(len(docs))
# print("-"*50)
# print(docs[0].metadata)

chain = prompt | model | parser

result = chain.invoke({'text':docs[0].page_content})

print(result)
