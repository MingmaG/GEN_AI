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

template1 = PromptTemplate(
  template = 'Give me review on the {topic}',
  input_variables=['topic']
)


template2 = PromptTemplate(
  template = 'give 2 line about the {text}',
  input_variables=['text']
)
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic': 'Mera Peak'})


print(result)

# code of simple chain 
"""

chain = template | model | parser
result = chain.invoke({'topic':'Langtang Trek'})

"""
chain.get_graph().print_ascii()