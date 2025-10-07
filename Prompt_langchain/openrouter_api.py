import os
"""from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()


openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_base = os.getenv("OPENROUTER_API_BASE")

llm = ChatOpenAI(
    openai_api_key=openrouter_api_key,
    openai_api_base=openrouter_api_base,
    model_name="qwen/qwen3-coder:free",  # deepseek/deepseek-chat-v3.1:free, openai/gpt-oss-20b:free, qwen/qwen3-coder:free, google/gemma-3n-e2b-it:free, meta-llama/llama-3.3-8b-instruct:free
    default_headers={"HTTP-Referer": "http://your-app-url.com"}
)

messages = [HumanMessage(content="what is the capital of nepal")]
response = llm.invoke(messages)
print(response.content)
"""
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
openrouter_api_base = os.getenv('OPENROUTER_API_BASE')

llm = ChatOpenAI(
  openai_api_key = openrouter_api_key,
  openai_api_base = openrouter_api_base,
  model = "qwen/qwen3-coder:free",
  default_headers={"HTTP-Referer":"http://your-app-url.com"}
  
)

message = [HumanMessage(content='what you said earlier?')]
result = llm.invoke(message)
print(result.content)