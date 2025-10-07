import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
openrouter_api_base = os.getenv("OPENROUTER_API_BASE")

model = ChatOpenAI(
    openai_api_key=openrouter_api_key,
    openai_api_base=openrouter_api_base,
    model_name="deepseek/deepseek-chat-v3.1:free",  # deepseek/deepseek-chat-v3.1:free, openai/gpt-oss-20b:free, qwen/qwen3-coder:free, google/gemma-3n-e2b-it:free, meta-llama/llama-3.3-8b-instruct:free
    default_headers={"HTTP-Referer": "http://your-app-url.com"}
)

st.header('Research Tool')
paper_input = st.selectbox("Select Research Paper Name",['Attention is all you Need','BERT: Pre-training of Deep Bidirectional Transofrmer', 'GPT-3 : Language Model are Few-Shot Learner'])
style_input = st.selectbox("Select Explanation Style", ["Begineer Friendly",'Technical ', 'Code Oriented'])
length_input = st.selectbox("Select Explanation Length",['Short (1-2 paragraphs)','Long(detailed explanation)'])


template = load_prompt('template.json')
"""
# without using chain  

   prompt =template.invoke({
  'paper_input': paper_input,
  'style_input':style_input,
  'length_input':length_input
})

if st.button('Summarize'): 
  result = model.invoke(prompt)
  st.write(result.content)

"""
# with using chain 
if st.button('Summerize'):
  chain = template | model
  result = chain.invoke({
    'paper_input': paper_input,
    'style_input':style_input,
    'length_input': length_input
  })
  st.write(result.content)
