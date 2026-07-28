from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate


llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

templete1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

templete2 = PromptTemplate(
    template='Write a summary 3 line report on {topic}',
    input_variables=['topic']
)

prompt1 = templete1.invoke({'topic':'iit jodhpur'})

result1 = model.invoke(prompt1)

prompt2 = templete2.invoke({'topic':'iit jodhpur'})

result2 = model.invoke(prompt2)

print(result1.content)
print(result2.content)





