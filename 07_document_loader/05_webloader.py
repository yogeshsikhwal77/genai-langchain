from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

url ='https://github.com/yogeshsikhwal77/genai-langchain/blob/main/05_chain/sequential_chain.py'
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template='give me answer of this question \n {question} from the following text {text}',
    input_variables=['question','text']
)

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

chain = prompt | model | parser

question = 'tell me about summary of this'

result = chain.invoke({'question':question ,'text':docs})

print(result)