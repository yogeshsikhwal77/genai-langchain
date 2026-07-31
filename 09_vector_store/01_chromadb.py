from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_chroma import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()

doc1 = Document(
    page_content="Jaipur, known as the Pink City, is the capital of Rajasthan. It is famous for its stunning royal architecture, including the Hawa Mahal, City Palace, and Amber Fort.",
    metadata={"city": "Jaipur", "state": "Rajasthan", "source": "travel_guide"}
)

doc2 = Document(
    page_content="Mumbai is the financial capital of India and the heart of the Bollywood film industry. The iconic Gateway of India monument overlooks the Arabian Sea.",
    metadata={"city": "Mumbai", "state": "Maharashtra", "source": "travel_guide"}
)

doc3 = Document(
    page_content="Varanasi is one of the oldest continuously inhabited cities in the world. Millions of pilgrims gather on its famous ghats leading down to the sacred River Ganges.",
    metadata={"city": "Varanasi", "state": "Uttar Pradesh", "source": "history_archive"}
)

doc4 = Document(
    page_content="Bengaluru, often referred to as the Silicon Valley of India, is the nation's leading information technology exporter. It is also famous for its green parks and pleasant year-round weather.",
    metadata={"city": "Bengaluru", "state": "Karnataka", "source": "business_directory"}
)

doc5 = Document(
    page_content="Kolkata, affectionately called the City of Joy, is renowned for its grand colonial-era architecture, vibrant literary and art scenes, and massive Durga Puja celebrations.",
    metadata={"city": "Kolkata", "state": "West Bengal", "source": "culture_magazine"}
)

cities = [doc1,doc2,doc3,doc4,doc5]

vector_store = Chroma(

    embedding_function=GoogleGenerativeAIEmbeddings(model='gemini-embedding-2'),
    persist_directory='my-db',
    collection_name='sample'
)

document_ids = vector_store.add_documents(cities)
doc5_id = document_ids[4]

print(vector_store.get(include=['embeddings','documents','metadatas']))

print(vector_store.similarity_search(query='which city have nerest himaliyas',k=2))
print(vector_store.similarity_search_with_score(query='which city have nerest himaliyas',k=2))

print(vector_store.similarity_search_with_score(query="tell me about this place",filter={"city": "Kolkata"}))

updated_doc5 = Document(
    page_content="Formerly the capital of British India, Kolkata is famous for the iconic Howrah Bridge, the majestic Victoria Memorial, and being the only Indian city to still operate a tram network. Its street food culture, especially the mouth-watering kathi rolls and roshogolla, is legendary.",
    metadata={"city": "Kolkata", "state": "West Bengal", "source": "culture_magazine"}
)

vector_store.update_document(document_id=doc5_id,document=updated_doc5)

# view document
vector_store.get(include=['embeddings','documents','metadatas'])

# delete document
vector_store.delete(ids=[doc5_id])
