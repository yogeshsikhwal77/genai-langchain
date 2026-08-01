
import wikipedia
from langchain_community.retrievers import WikipediaRetriever

# 1. Set a custom User-Agent (replace with your app name and contact email)
wikipedia.set_user_agent("MyLangchainApp/1.0 (your-email@example.com)")

# 2. Initialize and use your retriever normally
retriever = WikipediaRetriever()
query = "mahatma gandhi"
result = retriever.invoke(query)

print(result)