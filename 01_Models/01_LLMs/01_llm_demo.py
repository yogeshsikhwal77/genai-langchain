from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3.5-flash",temperature=0.3)

result = llm.invoke("Give location for IIt Jodhpur")
print(result)