from llm_client import model 
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

parser = JsonOutputParser()

template = PromptTemplate(
  template='Give me best time, cost , duriation of going to {topic} \n {format_instruction}',
  input_variables=['topic'],
  partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'EBC trek'})

print(result)
print(type(result))