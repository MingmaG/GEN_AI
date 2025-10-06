from llm_client import model # custom made for using model.
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field


class Person(BaseModel):
  name:str= Field(description='name of the person')
  age: int= Field(description='age of the person')
  city: str= Field(descripton='name of the city ')

parser = PydanticOutputParser(pydantic_object= Person)

template = PromptTemplate(
  template='Generate the name , age  and city of the fictional {place} person \n {format_instruction}',
  input_variables=['place'],
  partial_variables={'format_instruction':parser.get_format_instructions()}
)
prompt = template.format(place='nepal')
result =model.invoke(prompt)
final_result = parser.parse(result.content)

print(final_result)