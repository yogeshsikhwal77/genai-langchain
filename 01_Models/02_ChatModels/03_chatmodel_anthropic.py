from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='gpt-0.6',temperature=0.6)

result = model.invoke("Which model i use")

print(result.content)