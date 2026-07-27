from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expert'),
    ('human','explain {topic} in your {domain}')
])

prompt = chat_template.invoke({'domain':'labour','topic':'problems'})

print(prompt.content)