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
# actual code for runnable branch begins here
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableSequence, RunnablePassthrough

prompt1 = PromptTemplate(
  template='Write a detail report on {topic}',
  input_variables=['topic']
)


prompt2 = PromptTemplate(
  template='Summarize the following {ttext}',
  input_variables=['text']
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser # using LCEL ( langchain expression language)

branch_chain = RunnableBranch(
  (lambda x: len(x.split())>200, RunnableSequence(prompt2, model, parser)),
  RunnablePassthrough()
  
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'AI for travel'}))