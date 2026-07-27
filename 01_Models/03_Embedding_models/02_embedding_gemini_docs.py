from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2',dimensions=32)

documents = [
    "my name is jonn doe",
    "my college is iit ",
    "my school is raj"
]

result = embedding.embed_documents(documents)

print(str(result))

