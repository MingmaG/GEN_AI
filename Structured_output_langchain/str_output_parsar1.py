from llm_client import model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


template1 = PromptTemplate(
  template= "give me full review of {topic}",
  input_variables=['topic']
)

template2 = PromptTemplate(
  template = "give 5 line summary of \n {text}",
  input_variables=['text']

)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result =chain.invoke({'topic':'EBC trek'})

print(result)
