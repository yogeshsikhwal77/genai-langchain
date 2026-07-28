from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel,Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite')

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description='give the sentiment of the feedback')

parser = StrOutputParser()
parser1 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='classify the sentiment of the following feedback test either postive or negative \n {format_instructions} \n Feedback: {feedback}',
    input_variables=['feedback'],
    partial_variables={'format_instructions' : parser1.get_format_instructions()}
)

classification_chain = prompt1 | model | parser1

prompt2 = PromptTemplate(
    template='write an appropriate responce to the positive feedback \n {feedback}' ,
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='write an appropriate responce to the negative feedback \n {feedback}' ,
    input_variables=['feedback']
)

prep_chain = RunnablePassthrough.assign(
    sentiment=lambda x: classification_chain.invoke(x).sentiment
)

branch_chain = RunnableBranch(
    (lambda x:x['sentiment'] == 'positive',prompt2 | model | parser),
    (lambda x:x['sentiment'] == 'negative',prompt3 | model | parser),
    RunnableLambda(lambda x: "not able to find sentiment")

)

chain = prep_chain | branch_chain

result = chain.invoke({'feedback':"this is good "})

print(result)

chain.get_graph().print_ascii()

