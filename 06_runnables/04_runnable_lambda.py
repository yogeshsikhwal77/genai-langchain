from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough

load_dotenv()

def word_count(text):
    return len(text.split())
prompt = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word-count': RunnableLambda(word_count)
})

final_chain = joke_gen_chain | parallel_chain

result = final_chain.invoke({'topic':'iits'})

print(result)