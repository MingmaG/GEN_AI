from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv
import os
load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_base = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
  openai_api_key = openrouter_api_key,
  openai_api_base= openrouter_api_base,
  model ="meta-llama/llama-3.3-8b-instruct:free",
  default_headers = {'HTTPS-Referer':'https://your-app-url.com'}

)

chat_history = [
  SystemMessage(content='your are helpful ai ')
]
# chatprompttemplet for multiple message .
chat_template = ChatPromptTemplate(
  [('system','Your are a {domain} expert'),
   ('human', 'Explain in simple term what is {topic}')
  ]
)

prompt = chat_template.invoke({'domain':'football', 'topic':'Messi'})

result = model.invoke(prompt)
print(result.content)