from llm_client import model # custom made for using model.
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


schema = [
  ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
  ResponseSchema(name='fact_2', description='Fact 2  about the topic'),
  ResponseSchema(name='fact_3', description='Fact 3 about the topic'),

]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
  template='Give 3 facts about {topic}\n {format_instruction}',
  input_variables=['topic'],
  partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'topic':'EBC Trek'})
result = model.invoke(prompt)
final_result = parser.parse(result.content)

print(final_result)
#pros : enforce to give structure.
#cons : no data validation therefure need pydantic output parser
