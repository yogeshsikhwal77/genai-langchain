from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnableLambda,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import sys
from dotenv import load_dotenv

load_dotenv()

video_id = "lVylRtlPOIE"
try:
    # 1. Create an instance of the API
    yt_api = YouTubeTranscriptApi()
    
    # 2. Use fetch() and append .to_raw_data() to match the old format
    transcript_list = yt_api.fetch(video_id, languages=["en"]).to_raw_data()
    
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print("Transcripts loaded succesfully")

except TranscriptsDisabled:
    print("no caption is availble for that video")
    sys.exit()

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap=200)
chunks = splitter.create_documents([transcript])
embeddings = GoogleGenerativeAIEmbeddings(model='gemini-embedding-2')
vector_store = Chroma.from_documents(chunks,embeddings)
retriever = vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4})

def format_docs(retrived_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrived_docs)
    return context_text
parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)
llm = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite',temperature=0.3)

parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

print(main_chain.invoke("summarize the video"))
