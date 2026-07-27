from langchain_core.prompts import PromptTemplate

# Set up the prompt template with placeholders
template = PromptTemplate(
    template=
    "Give me the {data} for the city of {city}. Limit the length of your response to: {length}.",
    input_variables=["data", "city", "length"],
    validate_template=True
)

template.save('templete.json')