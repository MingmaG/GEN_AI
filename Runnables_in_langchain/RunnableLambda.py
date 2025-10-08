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


from langchain.schema.runnable import RunnableParallel, RunnableSequence, RunnableLambda, RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def word_counter(text):
  return len(text.split())

prompt = PromptTemplate(
  template='write a joke about {topic}',
  input_variables=['topic']
)
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)
parallel_chain = RunnableParallel({
  'joke':RunnablePassthrough(),
  'word_count': RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'ai'})
print(result)