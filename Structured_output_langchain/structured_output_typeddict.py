
from typing import TypedDict, Annotated, Optional, Literal
from llm_client import model



class Review(TypedDict):
  key_themes : Annotated[list[str], 'write down all the key themes discussed in a review in a list']
  summery: Annotated[str,'brief summary of the review']
  sentiment: Annotated[Literal['pos','neg'],'return sentiment of the review either positive or negative or neutral']
  pros:Annotated[Optional[list[str]],'write all the pros inside a list']
  const:Annotated[Optional[list[str]],'write all the cons inside the list']
  name: Annotated[Optional[str], 'write the name of the reviewer']

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Artificial Intelligence (AI) is one of the most powerful and fast-growing technologies in the modern world. It refers to the ability of machines to think, learn, and make decisions like humans. Today, AI is present in almost every aspect of our lives—from using voice assistants like Siri and Alexa to self-driving cars, chatbots, and even medical diagnosis systems. The impact of AI is huge and continues to shape how we live, work, and communicate.

One of the biggest advantages of AI is its ability to increase efficiency and productivity. Machines can perform repetitive tasks faster and more accurately than humans. For example, in factories, robots controlled by AI can work continuously without getting tired. In offices, AI tools can help process large amounts of data quickly, allowing people to focus on creative and meaningful work. In healthcare, AI is helping doctors detect diseases earlier and suggest better treatments, which can save lives. Another benefit is that AI systems can make decisions based on data, reducing human error and improving accuracy in various fields.

""")

print(result)