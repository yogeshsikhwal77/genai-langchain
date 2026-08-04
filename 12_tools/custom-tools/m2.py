from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field

class Additon(BaseModel):
    a: int = Field(required=True,description="first number for addition")
    b: int = Field(required=True,description="second number for addition")

def additon(a: int,b: int) -> int:
    return a + b

additon_tool = StructuredTool.from_function(
    func=additon,
    name="addition",
    description="add two numbers",
    args_schema=Additon
)

result =additon_tool.invoke({"a":10,"b":20})

print(result)
print(additon_tool.name)
print(additon_tool.description)
print(additon_tool.args)