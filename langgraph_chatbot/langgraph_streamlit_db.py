import streamlit as st
from langgraph_backend_db import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage
import uuid
from dotenv import load_dotenv
load_dotenv()

#********* utility functions ****

def generate_thread():
    thread_id = uuid.uuid4()
    return str(thread_id)

#******** reset ui **************

def reset_chat():
    thread_id = generate_thread()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id, title = 'New Chat'):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'][thread_id] = title


def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable':{'thread_id': thread_id}})
    return state.values.get("messages",[])
    
def generate_thread_title(text, max_len=30):
    text = text.strip()
    return text[:max_len] if text else "New Chat"



    
# st.session_state -> dict -> 

#*********session setup *********

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()
    
add_thread(st.session_state['thread_id'])



#********* Sidebar UI ***********
 
st.sidebar.title('Langgraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My conversations')

for thread_id, title in reversed(list(st.session_state['chat_threads'].items())):
    if st.sidebar.button(title, key=f"thread_btn_{thread_id}"):
        st.session_state['thread_id'] = thread_id

        messages = load_conversation(thread_id)
        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content':msg.content})
        st.session_state['message_history'] = temp_messages
      
           
#********* Main UI **************

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=ello'}

user_input = st.chat_input("Type here")

if user_input:
    # Current thread
    current_thread = st.session_state['thread_id']
    inputs = {"messages": [HumanMessage(content=user_input)]}

    # Add user message
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})

    with st.chat_message('user'):
        st.text(user_input)

    #CONFIG = {'configurable': {'thread_id': current_thread}}

    CONFIG = {
        "configurable": {"thread_id": current_thread},
        "metadata":{
            "thread_id": current_thread},
        "run_name":"chat_turn",
    }

    if st.session_state["chat_threads"][current_thread] == "New Chat":
        title = generate_thread_title(user_input)
        inputs["title"] = title
        st.session_state["chat_threads"][current_thread] = title

        # Stream AI response
    ai_chunks = []
    with st.chat_message("assistant"):
        placeholder = st.empty()
        for message_chunk, metadata in chatbot.stream(
            inputs,
            config=CONFIG,
            stream_mode='messages'
        ):
            ai_chunks.append(message_chunk.content)
            placeholder.markdown("".join(ai_chunks))  # live update

    ai_message = "".join(ai_chunks).strip()
    st.session_state['message_history'].append(
        {'role':'assistant', 'content':ai_message}
        )
    
# Update local session with latest titles from DBst.session_state['chat_threads'] = retrieve_all_threads()


   
        

 



