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

