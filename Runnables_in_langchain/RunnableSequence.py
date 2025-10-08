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
# actual code for runnable sequence begins here 

from langchain.schema.runnable import RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt1 = PromptTemplate(
  template='write short story about {topic}',
  input_variables=['topic']
)
prompt2 = PromptTemplate(
  template='write summary about {text}',
  input_variables=['text']
)

parser = StrOutputParser()
chain = RunnableSequence(prompt1, model, parser, prompt2, model , parser)

print(chain.invoke({'topic':'Snow'}))