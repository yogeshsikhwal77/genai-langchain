from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel,Field

class AdditonInput(BaseModel):
    a: int = Field(required=True,description="first number to add ")
    b: int = Field(required=True,description="second number to add ")

class AdditionTool(BaseTool):
    name: str = "addition"
    description: str = "addition two numbers"

    args_schema: Type[BaseModel] = AdditonInput

    def _run(self,a:int,b:int) -> int:
        return a + b

addition_tool = AdditionTool()

result = addition_tool.invoke({'a':10,'b':20})

print(result)
print(addition_tool.name)
print(addition_tool.description)
print(addition_tool.args)