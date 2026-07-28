from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFacePipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
# api
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)

# local 
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

# model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')
model = ChatHuggingFace(llm=llm)

templete1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

templete2 = PromptTemplate(
    template='Write a summary 3 line report on {topic}',
    input_variables=['topic']
)

# prompt1 = templete1.invoke({'topic':'iit jodhpur'})

# result1 = model.invoke(prompt1)

# prompt2 = templete2.invoke({'topic':'iit jodhpur'})

# result2 = model.invoke(prompt2)

# print(result1.content)
# print(result2.content)

parser = StrOutputParser()

chain = templete1 | model| parser | templete2 | model | parser

result = chain.invoke({'topic':'IIT Jodhur'})

print(result)





