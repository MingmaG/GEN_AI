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
# actual code for runnable parallel begins here 

from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt1 = PromptTemplate(
  template='write few line about {topic}',
  input_variables=['topic']
)
prompt2 = PromptTemplate(
  template='write few line about {topic}',
  input_variables=['topic']
)
parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt1, model, parser),
    'Linkdin': RunnableSequence(prompt2, model, parser)}

)
result = parallel_chain.invoke({'topic':'ai'})
print(result['tweet'])
print(result['Linkdin'])