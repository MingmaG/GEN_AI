# 🚀  Generative AI & LangChain Learning 

Welcome to my **Gen AI Learning Repository**!  
This repo documents my personal journey in exploring **Generative AI**, **LangChain**, and **LLM application development** — from the basics to building real-world projects.

---

## 🌱 About This Repository

This repository serves as my **learning log** and **code practice space** as I explore:
- 🧠 **LangChain** – framework for developing LLM-powered applications  
- 🤖 **Prompt Engineering** – designing and structuring effective prompts  
- 🔗 **Runnables & Chains** – understanding data flow and model composition  
- 📄 **Document Loaders & Text Splitters** – for building context-aware systems  
- 💬 **Chat Models** – connecting LLMs with conversational interfaces  
- 🧩 **Parsers & Output Structuring** – making model outputs usable and reliable  

---

## 📚 Folder Structure

genai-learning/
├── chatmodels/
├── runnables/
├── document_loaders/
├── chains/
├── prompts/
└── README.md

---

## 🧩 Key Concepts I’m Learning

| Concept | Description |
|----------|--------------|
| **PromptTemplate** | How to define reusable prompt structures |
| **Runnable** | Standardized execution interface for any component |
| **DocumentLoader** | Load and preprocess text for retrieval or summarization |
| **Parser** | Convert raw LLM output into structured data |
| **Chains** | Combine multiple components to create workflows |
| **Agents (future)** | Automating decisions with LLM reasoning |

---

## 🧠 Example Code Snippet

```python
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

prompt = PromptTemplate(
    template="Write a short poem about {topic}.",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

result = parser.invoke(
    model.invoke(
        prompt.invoke({"topic": "sunrise"})
    )
)

print(result)
