from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2',dimensions=32)

documents = [
    "Mumbai is the financial capital of India, famous for the Gateway of India and the bustling Bollywood film industry.",
    "New Delhi is the political heart of the nation, home to the Parliament of India and historic Mughal monuments.",
    "Bengaluru is known as the Silicon Valley of India, serving as the country's main hub for IT companies and tech startups.",
    "Chennai is the cultural and industrial hub of South India, renowned for its automobile industry and classical music.",
    "Kolkata, situated on the Hooghly River, is celebrated as the cultural capital of India with rich literary and architectural heritage.",
    "Hyderabad is famous for its historic Charminar, rich Nizam heritage, and booming biotechnology sector.",
    "Jaipur, the capital of Rajasthan, is known worldwide as the Pink City due to its royal palaces and historic forts.",
    "Varanasi, located along the banks of the sacred Ganges River, is one of the world's oldest continuously inhabited spiritual cities."
]

query = 'what is jaipur'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)[0]

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("simarility_score" ,score)