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
from langchain.schema.runnable import RunnableParallel
parser = StrOutputParser()

prompt1 = PromptTemplate(
  template='Generate short and simple notes from the following text \n {text}',
  input_variables=['text']
)
prompt2 = PromptTemplate(
  template='Generate short questions answers from the following text \n {text}',
  input_variables=['text']
)
prompt3 = PromptTemplate(
  template='Merge the provided notes and quiz into a single document \n ->{notes} , quiz-> \n {quiz}',
  input_variables=['notes','quiz']
)

parallel_chain = RunnableParallel({
  'notes': prompt1 | model | parser,
  'quiz': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain
text = """Gradient descent is one of the most fundamental optimization algorithms in machine learning and deep learning. It provides a systematic way to minimize a function by iteratively moving in the direction of the steepest descent, that is, opposite to the gradient. In simple terms, it helps models learn by adjusting their parameters to reduce errors during training.

Concept and Intuition

Imagine standing on the top of a hill and trying to reach the lowest point in the valley. You cannot see the entire terrain, but you can feel the slope beneath your feet. If you take small steps downhill, you’ll eventually reach the bottom. This is the essence of gradient descent — it uses the slope (the gradient) of the loss function to guide the model’s parameters toward the minimum error."""

result = chain.invoke({'text':text})
print(result)

chain.get_graph().print_ascii()