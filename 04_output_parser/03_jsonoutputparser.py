
# -----------------imp--------------------#

# no schma enforce
# we cannot decide the format which come through it decide by ai automatic
# Solution --> structue output parser

#------------------------------------------#


from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from langchain_core.output_parsers import JsonOutputParser
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

parser = JsonOutputParser()
templete  = PromptTemplate(
    template='Give me the name date of birth age and nature in one word of mahatma gandi \n {format_instuction}',
    input_variables=[],
    partial_variables={'format_instuction': parser.get_format_instructions()}
)

prompt = templete.format()
result = model.invoke(prompt)
result = parser.parse(result.content)

print(result)