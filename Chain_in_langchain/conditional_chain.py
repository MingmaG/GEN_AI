from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_base = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
  openai_api_key = openrouter_api_key,
  openai_api_base= openrouter_api_base,
  model ="qwen/qwen3-coder:free, google",
  default_headers = {'HTTPS-Referer':'https://your-app-url.com'}

)


from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

class Feedback(BaseModel):
  sentiment: Literal['positive','negative'] = Field(description='give the sentiment enther positive or negative or neutral')

parser1 = PydanticOutputParser(pydantic_object=Feedback)

parser = StrOutputParser()

prompt1 = PromptTemplate(
  template = ' Classify the sentiment of the following feedback text into positive and negative\n on ,{feedback} \n {format_instruction}',
  input_variables=['feedback'],
  partial_variables={'format_instruction':parser1.get_format_instructions()}
)

prompt2 = PromptTemplate(
  template='Write an appropriate response to this positive feedback on \n {feedback}',
  input_variables=['feedback']
)
prompt3 = PromptTemplate(
  template='Write an appropriate response to this Negative feedback on \n {feedback}',
  input_variables=['feedback']
)
classifier_chain = prompt1 | model | parser1

branch_chain = RunnableBranch(
  (lambda x:x.sentiment =='positive', prompt2 | model | parser),
  (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
  RunnableLambda(lambda x:'couldn not find the sentiment')

)
chain = classifier_chain | branch_chain

print(chain.invoke({'topic':'Hiking','feedback':'bad day'}))

chain.get_graph().print_ascii()