from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableParallel
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)

model1 = ChatHuggingFace(llm=llm)
model2 = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short questions from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='merege the provided notes and quiz to a single documet \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

prallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merged_chain = prompt3 | model2 | parser

chain = prallel_chain | merged_chain

text = """
I started for school very late that morning and was in great
dread of a scolding, especially because M. Hamel had said
that he would question us on participles, and I did not
know the first word about them. For a moment I thought of
running away and spending the day out of doors. It was so
warm, so bright! The birds were chirping at the edge of the
woods; and in the open field back of the sawmill the
Prussian soldiers were drilling. It was all much more
tempting than the rule for participles, but I had the
strength to resist, and hurried off to school.
"""

result = chain.invoke({'text':text})

print(result)
