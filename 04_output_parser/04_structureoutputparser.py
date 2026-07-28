
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser # deprsiate not used now




llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1',description='Fact  1 abour topic'),
    ResponseSchema(name='fact_2',description='Fact  2 abour topic'),
    ResponseSchema(name='fact_3',description='Fact  3 abour topic')
]

parser =  StructuredOutputParser.from_responce_schemas(schema)

templete  = PromptTemplate(
    template='Give 3 facts abour that {topic} \n {format_instuction}',
    input_variables=['topic'],
    partial_variables={'format_instuction': parser.get_format_instructions()}
)

prompt = templete.format({'topic':'john cena'})
result = model.invoke(prompt)
result = parser.parse(result.content)

print(result)