from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFacePipeline.from_model_id(
#     model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         temperature = 0.5,
#         max_new_tokens = 100
#     )
# )

# model = ChatHuggingFace(llm=llm)
model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age: int = Field(gt=18,description='age of the person')
    city: str = Field(description='city of the person where he belong')

parser = PydanticOutputParser(pydantic_object=Person)

templete = PromptTemplate(
    template='Generate name,age,city of this {identity} person \n {format_instruction}',
    input_variables=['identity'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = templete | model | parser

result = chain.invoke({'identity':'trump'})

print(result)