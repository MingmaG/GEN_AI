from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
import os
load_dotenv()

openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
openrouter_api_base = os.getenv('OPENROUTER_API_BASE')


llm = ChatOpenAI(
  openai_api_key = openrouter_api_key,
  openai_api_base = openrouter_api_base,
  model='meta-llama/llama-3.3-8b-instruct:free',
  default_headers={'HTTPS-Referer':'https://your-app-url.com'}
)

prompt = ChatPromptTemplate.from_messages([
  ('system','your are a helpful AI assistant that writes clean and well commented python code'),
  ('human','{question}')


])

message = prompt.format_messages(question = 'write python code to check prime')

response = llm.invoke(message)

print(response.content)
