from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "my name is jonn doe",
    "my college is iit ",
    "my school is raj"
]

result = embedding.embed_documents(documents)

print(str(result))

