from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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
  SystemMessage(content='Your are a helpful AI assistant')
]

while True:
  user_input = input('User : ')
  chat_history.append(HumanMessage(content=user_input))
  if user_input == 'exit':
    break
  result = model.invoke(chat_history)
  chat_history.append(AIMessage(content=result.content))
  print('AI : ',result.content)

print(chat_history)