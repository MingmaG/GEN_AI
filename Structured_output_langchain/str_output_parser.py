from llm_client import model
from langchain_core.prompts import PromptTemplate


template1 = PromptTemplate(
  template = "write a detail report on {topic}",
  input_variables = ['topic']
)


template2 = PromptTemplate(
  template = "write 3 line summery on the following topic./n {text}",
  input_variables = ['text']
)

prompt1 = template1.invoke({'topic':'apple tree'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result1 = model.invoke(prompt2)

print(result1.content)