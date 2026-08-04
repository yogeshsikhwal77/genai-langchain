from langchain_core.tools import tool

@tool
def addition(a: int,b: int) -> int:
    """addition of two numbers"""
    return a + b

result = addition.invoke({"a":10,"b":20})

print(result)

print(addition.name)
print(addition.description)
print(addition.args)

print(addition.args_schema.model_json_schema())